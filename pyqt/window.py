#!/usr/bin/python

# quitbutton.py

import sys
from PyQt4 import QtGui, QtCore


class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('Icons/img.png'))
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')

        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(84, 50, 60, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))
       
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        


app = QtGui.QApplication(sys.argv)

icon = Icon()
icon.show()
sys.exit(app.exec_())


