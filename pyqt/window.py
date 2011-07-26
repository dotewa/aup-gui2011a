#!/usr/bin/python

# icon.py

import sys
from PyQt4 import QtGui, QtCore




class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

   
			

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('test')
        self.setWindowIcon(QtGui.QIcon('Icons/img.png'))
        self.resize(250,150)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-self.width())/2, (screen.height()-self.height())/2)
        
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(0, 0, 60, 35)
        quitgeo = quit.geometry();
        quit.move((size.width()/2) - (quitgeo.width()/2), (size.height()/2) - (quitgeo.height()/2))
        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))
            
        self.exit = QtGui.QAction(QtGui.QIcon('Icons/img.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exit)


    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
            exit = QtGui.QAction(QtGui.QIcon('Icons/img.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        
        menubar = self.menuBar()
        file = menubar.addMenu('&Help')
        file.addAction(exit)





app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
