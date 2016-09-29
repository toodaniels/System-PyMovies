from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import requests
import  sys
import time

class Search(QMainWindow):
	"""docstring for tipo"""
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("search.ui",self)
		self.setObjectName("window")
		self.pushButton.clicked.connect(self.mkwhere)
		self.lineEditid.textChanged.connect(self.mkwhere)
		self.lineEdittitile.textChanged.connect(self.mkwhere)
		self.lineEditdirector.textChanged.connect(self.mkwhere)
		self.lineEditgenero.textChanged.connect(self.mkwhere)
		with open("style.css") as f:
			self.setStyleSheet(f.read())

	def mkwhere (self):
		self.tableWidget.setRowCount(0)
		datos ={
			'id':self.lineEditid.text(),
			'titulo':self.lineEdittitile.text(),
			'director':self.lineEditdirector.text(),
			'genero':self.lineEditgenero.text()
		}
		r = requests.post('http://127.0.0.1:3000/select', params=datos)
		self.tableWidget.setColumnCount(7)
		self.tableWidget.setHorizontalHeaderLabels(["ID","Titulo","Director","Genero","Compra","Venta","Stock"])
		row=0
		for tupla in r.json():
				self.tableWidget.insertRow(row)	
				for it in range(len(tupla)):
					item=QTableWidgetItem(str(tupla[it]))
					self.tableWidget.setItem(row,it,item)
				row=row+1
		

		

