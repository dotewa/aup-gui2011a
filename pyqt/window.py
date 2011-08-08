#!/usr/bin/python
# -*- coding: utf-8 -*-

# gridlayout1.py

import sys
from PyQt4 import QtGui,QtCore


class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('test')
		self.setWindowIcon(QtGui.QIcon('Icons/img.png'))
		self.resize(300,150)
		#self.center()
		#self.setWindowTitle('grid layout')

		names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
            '4', '5', '6', '*', '1', '2', '3', '-',
            '0', '.', '=', '+']

		grid = QtGui.QGridLayout()

		j = 0
		pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3)]

		for i in names:
			button = QtGui.QPushButton(i)
			if j == 2:
				grid.addWidget(QtGui.QLabel(''), 0, 2)
			else: grid.addWidget(button, pos[j][0], pos[j][1])
			j = j + 1

		self.setLayout(grid)
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
ex = Example()
ex.show()
sys.exit(app.exec_())
