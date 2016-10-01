# -*- coding: utf-8 -*-
from flask import render_template,Flask,request,jsonify #mando a llamar lo que necesito de flask
from conectdb import pelicula # importo la clase pelicula del archivo conectdb 
app = Flask(__name__ , static_url_path='/static') # Agrego la dirección que sera estatica 

pel = pelicula() #Creo un objeto tipo pelicula

@app.route("/") # Si desde el navegador acceden a la dirección "/" es decir http://localhost:3000/ 
def index(list=None): #se ejecuta esta funcion
		return render_template('index.html') #muesta el archivo 'index.html' de la carpeta templates

@app.route("/search") # Si desde el navegador acceden a la dirección "/search" es decir http://localhost:3000/search 
def search(list=None): #Se ejecuta esta función
		return render_template('search.html')
	
@app.route("/update")# Si desde el navegador acceden a la dirección "/update" es decir http://localhost:3000/update 
def update(list=None):# se ejecuta esta función
		return render_template('update.html')
	
@app.route("/add")# Si desde el navegador acceden a la dirección "/add" es decir http://localhost:3000/add 
def add(list=None):# se ejecuta esta función
		return render_template('add.html')
	
@app.route("/delete")# Si desde el navegador acceden a la dirección "/delete" es decir http://localhost:3000/delete 
def delete(list=None):#se ejecuta esta función
		return render_template('delete.html')

@app.route("/select" , methods=["GET","POST"]) # Puede acceder con ambos metods GET y POST
def selectpel(): #se ejecutaesta funcion 
	id =str(request.args.get('id')) # Guardo los argumentos o parametro que llegan por medio de esos metodos 
	titulo= str(request.args.get('titulo'))
	director = str(request.args.get('director'))
	genero = str(request.args.get('genero'))
	where =""
	if (id =="" and titulo=="" and director =="" and genero==""): #si no hay nada en esos parametros ejecuta la funcion
		pel.selectall() # Seleccionar todas las tuplas de la tabla Pelicula
	else: #Si se encuentra alguna creo el Where que me daria las tuplas que necesito
		if (id!=""): #Si id es diferente de vacio
			if where=="": #Agrego a la cadena where id = (id del parametro)
				where+=" id = %s "%(id)
			else:
				where+=" and id = %s "%(id)
		if (titulo!=""): #Igual que con id pero con titulo
			if where=="":
				where+=" titulo like '" +titulo+ "%'" #Like  sirve para que busque en la columna titulo 
			else: # Tuplas que en ese campo comienzan con el titulo 
				where+=" and titulo like '" +titulo+ "%'"
		if (director!=""):#Igual que con titulo pero con director
			if where=="":
				where+=" director like '" +director+ "%'"
			else:
				where+=" and director like '" +director+ "%'"
		if (genero!=""):#Igual que con director pero con genero
			if where=="":
				where+=" genero like '" +genero+ "%'"
			else:
				where+=" and genero like '" +genero+ "%'"
		where = "select * from pelicula where "+where #Agrego de una vez lo que falta en la sentencia SQL para que busque
		# lo que es requerido ejemplo : select * from pelicula where id = 5 and genero like una
		pel.select(where)#ejecuta la funcion select del objeto de pelicula 
		#buscará si existen tuplas con id = 5 y que en su campo genero comience con la palabra una
	resp = [] #inicializo un diccionario vacio para guardar las tuplas
	for tupla in pel.lista: # una vez ejecutada la sentencia recorre la lista del objeto pel dondese almacenan
		resp.append(tupla)#las tuplas encontradas 
	return jsonify(resp), 200 # envio el diccionario como tipo json con elcodigo 200 que es el cdigo para respuestas correctas

@app.route("/insert_movie", methods=["GET","POST"]) #Pueden acceder con ambos metodos GET y POST
def insert_movie(): #Se ejecuta esta función
	status = True # Variable booleana que utilizo para saber si ocurrio un error
	try: #Trata de ejecutar
		titulo= str(request.args.get('titulo')) # ALmaceno los parametros o argumentos que envian por los dos metodos 
		director = str(request.args.get('director'))
		genero = str(request.args.get('genero'))
		compra= int(request.args.get('compra'))
		venta = int(request.args.get('venta'))
		stock = int(request.args.get('stock'))
		pel.insert(titulo,director,genero,compra,venta,stock) #ejecuta la funcion insert del objeto pelicula
	except Exception as e:
		status = False
	return jsonify({'status': status}), 200
	
@app.route("/update_movie", methods=["GET","POST"])  #Pueden acceder con ambos metodos GET y POST
def update_movie(): #ejecuta esta funcion
	status = True # Me sirve para saber si en el transcurso de la ejecucion ocurre agun erro
	try:
		id= int(request.args.get('id')) #obtiene los parametros que se envian por ambos metodos
		titulo= str(request.args.get('titulo'))
		director = str(request.args.get('director'))
		genero = str(request.args.get('genero'))
		compra= int(request.args.get('compra'))
		venta = int(request.args.get('venta'))
		stock = int(request.args.get('stock'))
		pel.update(id,titulo,director,genero,compra,venta,stock) #ejecuta la funcion update del objeto pel
	except Exception as e:
		status = False #cambia el status
		raise e
	return jsonify({'status': status}), 200 # envia en forma de json para que el clientesepa si la accion se realizo correctamente

@app.route("/delete_movie", methods=["GET","POST"])  #Pueden acceder con ambos metodos GET y POST
def delete_movie():#se ejecuta esta funcion
	status = True #para saber si ocurre algun error
	try:
		id= int(request.args.get('id')) #recibe el parametro id que se envia por alguno de los metodos 
		pel.delete(id)  #ejecuta la funcion delete del objeto pel
	except Exception as e:
		status = False # si ocurre algun error con lo que esta dentro del try cambia el valor de status 
		raise e
	return jsonify({'status': status}), 200 #envia el status en un tipo json para que el cliente lo interprete 

@app.route("/get_my_ip", methods=["GET"]) #solo sirve para conocer la ip de quien accede al sitio
def get_my_ip(): # se ejecuta esta funcion 
	print (str(request.args.get('hostname'))+" Se conectó "+request.remote_addr)
	return jsonify({'ip': request.remote_addr}), 200


@app.errorhandler(404) #en caso de tratar de acceder a una direccion que no existe se envia el codigo 404 
def page_not_found(error):
    return render_template('page_not_found.html'), 404 #retorno un html mencionando el erro

if __name__ == "__main__": #se ejecuta en elmetodo main o principal hilo
    app.run(debug = True,host='localhost', port=3000) #corre el servidor pero lo tengo en modo prueba debug si es necesario 
#acceder a este se puede eliminar ese parametro 
