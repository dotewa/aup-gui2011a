#!/usr/bin/python
# -*- coding: utf-8 -*-

# messagebox.py

import sys
from PyQt4 import QtGui


class MessageBox(QtGui.QWidget):
    quitbox = None
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(600, 600, 500, 500)
        self.setWindowTitle('message box')
        self.quitbox = QtGui.QPushButton('Close', self) 
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.quitbox.geometry()
        self.quitbox.move((self.width()/2)-(self.quitbox.width()/2),(self.height()/2)-(self.quitbox.height()/2))
        
       
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())
