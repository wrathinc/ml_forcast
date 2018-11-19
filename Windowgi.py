import sys 
from PyQt4 import QtGui, QtCore

class Winodow(QtGui.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50,50,500,300)
		self.setWindowTitle("Reddit Reads")
		self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))



app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec__())