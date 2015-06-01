# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:24:10 2015

@author: timothy.burchfield
http://stackoverflow.com/questions/23538522/scanning-qr-code-via-zbar-and-raspicam-modul
http://www.tutorialspoint.com/python/python_networking.htm

"""

import socket
import time
from blockchain.wallet import Wallet
from blockchain import exchangerates
import random

try:
    import notifytext
    text=True
    print "texting module import successfully"
except:
    text=False
    print "texting module not present"
    
wanttext=False

host = "localhost"
port = 1234
secret = "PLACEHOLDERCHANGEMELAYTAH"     #encryption key
protect = "PLLLLLLACEHOLDER"              #key at the start to signify successful decryption
pricecheck = "IAMAPLACEHOLDER"               #key to signify price/limits
transactor = "HEYGUESSWHATIMAPLACEHOLDERTOO"        #key to signify transaction

bcid=""        ### blockchain.info credentials identification #
bcpw=""      ### ^^^^^^^^^^^^^^^^^^^^^^ password

if bcid == "" or bcpw == "":
    print "You forgot to add the password and stuff"

fee=.05 #fee - how much extra charged to the user.  If they want $10 of xtc, they'll have to put 10$+10$*fee
jic=.90 #jic - just in case the price changes enough that I wouldn't have enough.  Sets limit lower than reality.  low jic means low limit.  0=<jic=<1  

wallet=Wallet(bcid,bcpw)   #Initialize blockchain wallet

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

#sometimes this still runs
def gotstuff(parsed):
    if parsed[0]==protect and parsed[-1]==protect:
        if parsed[1]==transactor:
            print "we are going to try and make a transaction."
            try:
                
                txhash=transact(parsed[2],float(parsed[3]))
                print "gotstuff got txhash"
            except Exception,e:
                print str(e)
                print "TROUBLE WIT A CAPTIDUL T"
                txhash=";)"
            #send a confirmation??  ILL SEND THE HASH
            return (AESencrypt(secret, protect+"|"+transactor+"|"+txhash+"|"+protect))
        elif parsed[1]==pricecheck:
            print "gonna send a price check"
            #send timestamped price
            #DEFINE PRICED AND TIMESTAMP
            formtime=time.strftime("%Y-%m-%d, %H:%M:%S") #good
            print "got timestamp"
            onextc=1/(exchangerates.to_btc("USD",1)) #good
            print "got one xtc"
            xtcs=float(wallet.get_balance())/100000000 #btcs in wallet
            print 
            limitinusd=xtcs*onextc/(1-fee)
            llimit=".01"#str(.01/exchangerates.to_btc("USD",1)) #Do i even need this????? I thought I did this to avoid fees but bc makes me anyways???
            ulimit=str(limitinusd*jic)
            priced=(1+fee)*onextc
            print "math worked fine"
            print "gonna return stuff"
            return (AESencrypt(secret, protect+"|"+pricecheck+"|"+str(priced)+"|"+llimit+"|"+ulimit+"|"+formtime+"|"+protect))

            
        else:
            #????????????????????
            print "Dumb client sent something with protect but without a key"
            return None
    else:
        print "Hey either it didn't decrypt right or it's decrypted wit the wrong key or the client didn't use the protected words"
        return None
def transact(adr,amt):
    print adr
    print amt, "is the usd"
    actualsat=exchangerates.to_btc("USD",float(amt))*100000000
    print actualsat, "is before fee"
    amtinsatoshi=int((1-fee)*actualsat)
    print amtinsatoshi, "is the amount in satoshi"
    bal=wallet.get_balance()
    print bal, "bal"
    a= wallet.list_addresses()
    change=""
    for x in a:
        print x.address, type(x.address)
        if x.balance == 0 and x.total_received == 0:
            print "conditions are trueeeeeeeeeee"
            change = x.address
    if not change:
        change = wallet.new_address("change "+str(int(random.uniform(10,999)))).address
    recipients = {adr:amtinsatoshi,str(change):(wallet.get_balance()-amtinsatoshi)-10000}
    print recipients
    if bal>amtinsatoshi:
        print "about to send"
        payment = wallet.send_many(recipients)
    else:
        print "about to send all"
        payment=wallet.send(adr,wallet.get_balance())
    print "hash: ", payment.tx_hash
    a=wallet.list_addresses()
    for x in a:
        if x.balance == 0 and x.total_received != 0:
            wallet.archive_address(x.address)
    if text and wanttext:
        nb=float(wallet.get_balance())/(100000000*exchangerates.to_btc("USD",1))
        notifytext.trans(adr, amt, nb)
        urg=0
        if nb<5:
            urg=5
        elif nb<10:
            urg=4
        elif nb<20:
            urg=3
        elif nb<50:
            urg=2
        elif nb<100:
            urg=1
        if urg:
            notifytext.low(nb, urg)
    return payment.tx_hash
    


s = socket.socket()

s.bind((host, port))
s.listen(5)

while 1:
    client, address = s.accept()
    data = client.recv(2048)
    if data:
        try:
            plain = AESdecrypt(secret, data).split("|")
            print "Got some good data B-)", plain
            x=gotstuff(plain)
            print "got to gettin message, it's",x
            if x:
                client.sendall(x)
        except:
            print "Got some bad data :( "
    client.close() 






