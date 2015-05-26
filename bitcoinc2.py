
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:24:10 2015

@author: timothy.burchfield
http://www.computerhope.com/issues/ch000549.htm
get zbar
https://code.google.com/p/qrdecoder/wiki/zbarInstallation
https://github.com/jacobvalenta/zbar-py27-msi/blob/master/zbar-0.10.win32-py2.7_2.msi

for raspi
https://github.com/rmurray2/Install-OpenCV-on-Raspi/blob/master/README.md
http://stackoverflow.com/questions/23538522/scanning-qr-code-via-zbar-and-raspicam-modul

"""

"""
lower and upper limits!
maybe check size!
"""
import time
import socket
import sys
from qrtools import QR
import os
import datetime
import shutil
import cv2

host = "localhost" # Get local machine name
port = 1234
secret = "PLACEHOLDERCHANGEMELAYTAH"
protect = "PLLLLLLACEHOLDER"
transactor = "HEYGUESSWHATIMAPLACEHOLDERTOO"
pricecheck = "IAMAPLACEHOLDER"

def AESencrypt(password, plaintext, base64=False):
    import hashlib
    import os
    from Crypto.Cipher import AES
    SALT_LENGTH = 32
    DERIVATION_ROUNDS = 1337
    BLOCK_SIZE = 16
    KEY_SIZE = 32
    MODE = AES.MODE_CBC

    salt = os.urandom(SALT_LENGTH)
    iv = os.urandom(BLOCK_SIZE)

    paddingLength = 16 - (len(plaintext) % 16)
    paddedPlaintext = plaintext+chr(paddingLength)*paddingLength
    derivedKey = password
    for i in range(0, DERIVATION_ROUNDS):
        derivedKey = hashlib.sha256(derivedKey+salt).digest()
    derivedKey = derivedKey[:KEY_SIZE]
    cipherSpec = AES.new(derivedKey, MODE, iv)
    ciphertext = cipherSpec.encrypt(paddedPlaintext)
    ciphertext = ciphertext + iv + salt
    if base64:
        import base64
        return base64.b64encode(ciphertext)
    else:
        return ciphertext.encode("hex")


def AESdecrypt(password, ciphertext, base64=False):
    import hashlib
    from Crypto.Cipher import AES
    SALT_LENGTH = 32
    DERIVATION_ROUNDS = 1337
    BLOCK_SIZE = 16
    KEY_SIZE = 32
    MODE = AES.MODE_CBC

    if base64:
        import base64
        decodedCiphertext = base64.b64decode(ciphertext)
    else:
        decodedCiphertext = ciphertext.decode("hex")
    startIv = len(decodedCiphertext)-BLOCK_SIZE-SALT_LENGTH
    startSalt = len(decodedCiphertext)-SALT_LENGTH
    data, iv, salt = decodedCiphertext[:startIv], decodedCiphertext[startIv:startSalt], decodedCiphertext[startSalt:]
    derivedKey = password
    for i in range(0, DERIVATION_ROUNDS):
        derivedKey = hashlib.sha256(derivedKey+salt).digest()
    derivedKey = derivedKey[:KEY_SIZE]
    cipherSpec = AES.new(derivedKey, MODE, iv)
    plaintextWithPadding = cipherSpec.decrypt(data)
    paddingLength = ord(plaintextWithPadding[-1])
    plaintext = plaintextWithPadding[:-paddingLength]
    return plaintext


#also need to check address for bein good n stuff
def sendt(address, amount):
    print"sendt called"
    data = AESencrypt(secret, protect+"|"+transactor+"|"+address+"|"+str(amount)+"|"+protect)   

    s = socket.socket()
    s.connect((host, port))
    s.send(data)
    q = s.recv(2048)
    
    s.close
    x=parse(q)
    print x, 'from client sendt'
    return x
    
    
def parse(rawdata):
    plaintextlist = AESdecrypt(secret, rawdata)
    plaintextlist = plaintextlist.split("|")
    if plaintextlist[0]==plaintextlist[-1] and protect==plaintextlist[-1]:
        if plaintextlist[1]==pricecheck:
            return (plaintextlist[2],plaintextlist[3],plaintextlist[4],plaintextlist[5])

        elif plaintextlist[1]==transactor:
            print "we got transaction data, hash:", plaintextlist[2]
            return plaintextlist[2]
        else:
            print "Ok what the heck he sent the protected phrases but without the correct protocol..."
    else:
        print "The stuff decrypted didn't have the protected phrase......."
        


def scanadd(name):

    myCode = QR(filename=name)
    if myCode.decode():
        if myCode.data_type == "text":
            print "worked"
            retval=""
            add = False
            start = True
            for x in myCode.data:
                if x in "13" and start:
                    add = True
                    start = False
                    retval+=x
                elif add and x in "123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ":
                    retval+=x
                else:
                    add=False
            print "raw",myCode.data
            return retval
            #aystit(retval, amt)
        else:
            print "That isn't text you tricky trickster"
    else:
        print "I can't decode that.  Sorry."
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        
        
def takepic(): #return filename from current file
    ramp_frames = 30
    print "starting up camera"
    camera = cv2.VideoCapture(0)
    def get_image(c):
        retval, im = c.read()
        return im
    for i in xrange(ramp_frames):
        temp = get_image(camera)
    print "Taking image..."
    camera_capture_1 = get_image(camera)
    time.sleep(.1)
    camera_capture_2 = get_image(camera)
    time.sleep(.1)
    camera_capture_3 = get_image(camera)
    time.sleep(.1)
    camera_capture_4 = get_image(camera)
    time.sleep(.1)
    camera_capture_5 = get_image(camera)
    time.sleep(.1)
    cv2.imwrite("current0.png", camera_capture_1)
    cv2.imwrite("current1.png", camera_capture_2)
    cv2.imwrite("current2.png", camera_capture_3)
    cv2.imwrite("current3.png", camera_capture_4)
    cv2.imwrite("current4.png", camera_capture_5)
    del(camera)

        
def getp(): #return price limit and time
    print "about to send p/l"
    data = AESencrypt(secret, protect+"|"+pricecheck+"|"+protect)   

    s = socket.socket()
    s.connect((host, port))
    s.sendall(data)
    q = s.recv(2048)
    print "q=",q
    print "dec q=",AESdecrypt(secret,q)
    s.close
    return parse(q)




