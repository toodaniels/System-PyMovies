from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import requests
import  sys
import time

class Update(QMainWindow):
	"""docstring for tipo"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("update.ui",self)
		self.setObjectName("window")
		self.pushButton.clicked.connect(self.up)
		self.pushButton_2.clicked.connect(self.search)
		with open("style.css") as f:
			self.setStyleSheet(f.read())

	def search(self):
		datos ={
			'id':self.lineEdit_7.text(),
			'titulo':"",
			'director':"",
			'genero':""
		}
		r = requests.post('http://127.0.0.1:3000/select', params=datos)	
		self.lineEdit.setText(str(r.json()[0][1]))
		self.lineEdit_2.setText(str(r.json()[0][2]))
		self.lineEdit_3.setText(str(r.json()[0][3]))
		self.lineEdit_4.setText(str(r.json()[0][4]))
		self.lineEdit_5.setText(str(r.json()[0][5]))
		self.lineEdit_6.setText(str(r.json()[0][6]))
				
					

	def up(self):
		datos ={
			'id':self.lineEdit_7.text(),
			'titulo' : self.lineEdit.text(),
			'director' : self.lineEdit_2.text(),
			'genero' : self.lineEdit_3.text(),
			'compra' : self.lineEdit_4.text(),
			'venta' : self.lineEdit_5.text(),
			'stock' : self.lineEdit_6.text()			
		}
		r = requests.post('http://127.0.0.1:3000/update_movie', params=datos)
		if (r.json()['status']):
			pass
		else:
			QMessageBox.information(self, 'Error',"Ocurrio un error")
		

