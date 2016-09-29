from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import requests
import  sys
import time

class Delete(QMainWindow):
	"""docstring for tipo"""
	def __init__(self):
		QMainWindow.__init__(self)

		uic.loadUi("delete.ui",self)
		self.setObjectName("window")
		self.pushButton.clicked.connect(self.up)
		with open("style.css") as f:
			self.setStyleSheet(f.read())
	def up(self):
		datos ={
			'id':self.lineEdit.text()			
		}
		r = requests.post('http://127.0.0.1:3000/delete_movie', params=datos)
		if (r.json()['status']):
			pass
		else:
			QMessageBox.information(self, 'Error',"Ocurrio un error")
		

