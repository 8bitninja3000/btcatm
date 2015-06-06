# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:27:55 2015

@author: Tim
"""
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread
from PyQt4.QtGui import QMainWindow, QApplication
from atratumgui import Ui_MainWindow
import time


legalagr="LegalesePlaceholder Legalese Legalese Legalese Legalese Legalese Legalese LegalesePlaceholder Legalese Legalese Legalese Legalese Legalese Legalese LegalesePlaceholder Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese LegalesePlaceholder Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Legalese Do you agree?"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

import bitcoinc2

class ImageDialog(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.state = 0
        self.curad = ""
        self.enough = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.no.clicked.connect(self.no)
        self.ui.yes.clicked.connect(self.yes)#build fxn
        self.ui.Message.setWordWrap(True)
        self.thread=Worker()
        self.connect(self.thread, QtCore.SIGNAL("PL Call"), self.pl)
        self.lights=LWorker()
        print "Successfully connected fxn"
    def yes(self):
        if True:#self.enough:
            
            print "Yes, state " +str(self.state)
            if self.state == 0:
                self.scansom()
                return
            if self.state == 1:
                self.changestate(2) #################### THIS NEEDS TO GO TO DISCLAIMER
                return
            if self.state == 2:
                self.changestate(3)
                return #Allow bills and start up a transaction! B)
            if self.state == 3:
                try:
                    HM=float(self.ui.BV.text())
                    b=True
                except:
                    self.mess("Please give me a number. (: ")
                    b=False
                if b:
                    print "we got our number",HM
                    print "first",HM <= float(self.ullim)
                    print "second",HM >= float(self.llim)
                    if HM <= float(self.ullim) and HM >= float(self.llim):
                        print "conditions satisfied"
                        self.changestate(4)
                        print "this should be four:",self.state
                        self.mess("Sending transaction...")
                        app.processEvents()
                        self.txid=bitcoinc2.sendt(self.curad, HM)
                        self.mess("Transaction complete.  ID: %s" % self.txid)
                        app.processEvents()
                        time.sleep(10)
                        self.changestate(0)
                        return
                        
                self.mess("Invalid number...")
                return
                
    def mess(self, mess):
        print "Setting message to",mess
        self.ui.Message.setText(mess)
        
    def no(self):
        print "No, state " +str(self.state)
        if True:#self.enough:
            if self.state == 0:
                self.scansom()
                return
            if self.state == 1:
                self.changestate(0)
                return
            if self.state == 2:
                self.changestate(0)
                return
            if self.state == 3:
                try:
                    HM=float(self.ui.BV.text())
                    b=True
                except:
                    self.mess("Please give me a number. (: ")
                    b=False
                if b:
                    print "we got our number",HM
                    print "first",HM <= float(self.ullim)
                    print "second",HM >= float(self.llim)
                    if HM <= float(self.ullim) and HM >= float(self.llim):
                        print "conditions satisfied"
                        self.changestate(4)
                        print "this should be four:",self.state
                        self.mess("Sending transaction...")
                        app.processEvents()
                        self.txid=bitcoinc2.sendt(self.curad, HM)
                        self.mess("Transaction complete.  ID: %s" % self.txid)
                        app.processEvents()
                        time.sleep(10)
                        self.changestate(0)
                        return
                        
                self.mess("Invalid number...")
                return
                
    def scansom(self):#take more pictures
        bitcoinc2.takepic()
        got=False
        for x in range(5):
            a=bitcoinc2.scanadd("current%s.png" % x)
            if a:
                self.curad=a
                got=True
        if not got:
            self.mess("Please scan again")
        else:
            self.mess("Are you sure it's "+self.curad+"?")
            self.changestate(1)
    def pl(self):
        plt=bitcoinc2.getp()
        self.llim=float(plt[1])
        self.ullim=float(plt[2])
        if self.ullim-self.llim > 0:
            self.enough = True
        else:
            self.enough = False
        self.stamp=plt[3]
        if self.enough:
            self.ui.price.setText("Price: %.2f USD/BTC" % float(plt[0]))
            self.ui.usdlim.setText("Limit: %.2f - %.2f USD" % (self.llim, self.ullim))
            self.ui.timestamp.setText("Prices and limits true as of %s" % self.stamp)
        else:
            self.ui.price.setText("Price: %.2f USD/BTC--OUT OF STOCK" % float(plt[0]))
            self.ui.timestamp.setText("OUT OF STOCK as of %s" % self.stamp)
            self.mess("Sorry, we are out of stock, but we should be back soon.")

    
    def changestate(self,state):
        self.state=state
        self.lights.lstate=state
        if state==0:
            font= QtGui.QFont()
            font.setPointSize(14)
            font.setFamily(_fromUtf8("Garamond"))
            self.ui.Message.setFont(font)
            self.mess("Press any button to scan the qr code.")
        if state == 2:
            font = QtGui.QFont()
            font.setFamily(_fromUtf8("Garamond"))
            font.setPointSize(10)
            self.ui.Message.setFont(font)
            self.mess(legalagr)
        if state == 3:
            self.mess("Insert $1 or $5 bills, then press either button to initiate the transaction.")
            #Here some of the code here is rather psuedo considering the lack of bill validator...
        ######## Maybe add stuff to mess with lights ############
    
class Worker(QThread):
    def __init__(self, parent = None):
        print "We made a worker."
        QThread.__init__(self, parent)
        self.exiting = False
        time.sleep(.1)
        self.start()
        print "About to call the caller."
    def run(self):
        print "Got called."
        self.emit(QtCore.SIGNAL("PL Call"))
        time.sleep(600)
        self.run()
        
    
    def __del__(self):
    
        self.exiting = True
        self.wait()
        
class LWorker(QThread):
    def __init__(self, parent = None):
        print "We made an *L*worker."
        QThread.__init__(self, parent)
        self.lstate=0
        self.exiting = False
        self.start()
        print "L------About to call the caller."
    def run(self):
        #0s #1d #2d #3s
        if self.lstate==0 or self.lstate==3: #s
            time.sleep(.5)
            #both off#
            time.sleep(.5)
            #both on#
        else:
            time.sleep(.5)
            #one off#
            time.sleep(.5)
            #other off#
        self.run()
        
    
    def __del__(self):
    
        self.exiting = True
        self.wait()

if __name__=="__main__":
    
    app = QApplication(sys.argv)
    x=ImageDialog()


    x.showFullScreen()
    
    sys.exit(app.exec_())
