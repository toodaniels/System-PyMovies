from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests
import socket
from PyQt5 import uic
from delete import Delete
from new import Add
from search import Search
from update import Update 

import  sys
import time

class Menu(QMainWindow):
	"""docstring for tipo"""
	def __init__(self,delete,search,add,update,ip,name):
		
		QMainWindow.__init__(self)
		uic.loadUi("Menu.ui",self)
		self.setObjectName("window")
		self.delete=delete
		self.search=search
		self.add=add
		self.update=update
		self.labelip.setText(name+" estas conectado en "+ip)
		self.botonbuscar.clicked.connect(self.opensearch)
		self.botonnuevo.clicked.connect(self.openadd)
		self.botonactual.clicked.connect(self.openupdate)
		self.botoneliminar.clicked.connect(self.opendelete)
		
		with open("style.css") as f:
			self.setStyleSheet(f.read())
	
	def opensearch(self):
		self.search.show()
	def openadd(self):
		self.add.show()
	def openupdate(self):
		self.update.show()
	def opendelete(self):
		self.delete.show()
		


name = socket.gethostname()
r = requests.get('http://127.0.0.1:3000/get_my_ip', params={'hostname':str(name) })
app=QApplication(sys.argv)
_delete=Delete()
_search=Search()
_new=Add()
_update=Update()
_menu=Menu(_delete,_search,_new,_update,str(r.json()['ip']),name)
_menu.show()
app.exec_()