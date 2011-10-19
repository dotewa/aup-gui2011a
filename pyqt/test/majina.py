
from PyQt4 import QtGui , QtCore
from pymongo import Connection

connection = Connection()
db = connection.gui
class Example ( QtGui.QWidget ):
	row = 0
	def __init__ ( self ):
		super ( Example , self ). __init__ ()
		self.resize(500,300)
		self.setWindowTitle ( " scores " )
		self.initData ()
		self.initUI ()
		row=0;
		col=0;
	def initData ( self ):
		data = []
		for names in db.david_nameslist.find():
			data.append(names['name'])

		self.model = QtGui.QStandardItemModel (12 , 3)
		col = 0
		for i in data :
			item = QtGui.QStandardItem(str((i)))
			self.model.setItem(self.row,col,item )
			self.row = self.row + 1
	def initUI ( self ):
		self.tv=QtGui.QTableView(self)
		self.tv.setModel(self.model)
		#lv = QtGui . QListView( self )
		#lv.setModel(self.model )
		self.tv.move(70,100)
		self.tv.resize(250,150)
		vbox=QtGui.QVBoxLayout()
		vbox.addWidget(self.tv)
		#layout=QtGui.QVBoxLayout()
		#layout.addWidget(lv)
		col=0
		row=0
		add=QtGui.QPushButton("Add",self)
		add.move(245,270)
		
		self.connect(add, QtCore.SIGNAL('clicked()'), self.showDialog)
				
        
		
		delete=QtGui.QPushButton("Delete",self)
		delete.move(50,270)
		
		edit=QtGui.QPushButton("Edit",self )
		edit.move(140,270)
		
		majina=QtGui.QLabel("Name:David Otewa", self)
		majina.move(15,10)
		
		year=QtGui.QLabel("Year :1st semester 2011-2012", self)
		year.move(15,25)
		
		subject=QtGui.QLabel("Subject : Graphical user interface", self)
		subject.move(15,40)
		
		teacher=QtGui.QLabel("Teacher : Israel Canasa", self)
		teacher.move(15,55)
		#majina=QtGui.QLabel("Teacher : Israel Canasa", self)
        #majina.move(265,100)
        
        #year = QtGui.QLabel("Year :1st semester 2011-2012", self)
        #year.move(265,105)

        #subject= QtGui.QLabel("Subject : Graphical user interface", self)
        #subject.move(265,120)
        
        #teacher=QtGui.QLabel("Teacher : Israel Canasa", self)
        #teacher.move(265,135)
		
	def showDialog(self):
		
		text, ok = QtGui.QInputDialog.getText(self, 'Names', 
				'Enter your name:')
			
		if ok:
			name=str(text)
			data = {"name":name}
			db.david_nameslist.insert(data);
			

			self.add(name)
			
	def add(self,name):
		data=str(name)
		col=0
		if data != ("  ") :
			item = QtGui.QStandardItem(str((data)))
			self.model.setItem(self.row,col,item )
			self.row = self.row + 1
		
		
	
app=QtGui.QApplication([])
ex=Example()
ex.show()
app.exec_()
