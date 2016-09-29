from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import requests
import  sys
import time

class Add(QMainWindow):
	"""docstring for tipo"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("new.ui",self)
		self.setObjectName("window")
		self.pushButton.clicked.connect(self.mk)
		with open("style.css") as f:
			self.setStyleSheet(f.read())
		
	def mk(self):
		datos ={
			'titulo' : self.lineEdit.text(),
			'director' : self.lineEdit_2.text(),
			'genero' : self.lineEdit_3.text(),
			'compra' : self.lineEdit_4.text(),
			'venta' : self.lineEdit_5.text(),
			'stock' : self.lineEdit_6.text()			
		}
		r = requests.post('http://127.0.0.1:3000/insert_movie', params=datos)
		if (r.json()['status']):
			pass
		else:
			QMessageBox.information(self, 'Error',"Ocurrio un error")
