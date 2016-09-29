from flask import render_template,Flask,request,jsonify
from conectdb import pelicula 
app = Flask(__name__ , static_url_path='/static')

pel = pelicula()

@app.route("/")
def index(list=None):
		return render_template('index.html')

@app.route("/search")
def search(list=None):
		return render_template('search.html')
@app.route("/update")
def update(list=None):
		return render_template('update.html')
@app.route("/add")
def add(list=None):
		return render_template('add.html')
@app.route("/delete")
def delete(list=None):
		return render_template('delete.html')

@app.route("/select" , methods=["GET","POST"])
def selectpel():
	id =str(request.args.get('id'))
	titulo= str(request.args.get('titulo'))
	director = str(request.args.get('director'))
	genero = str(request.args.get('genero'))
	where =""
	if (id =="" and titulo=="" and director =="" and genero==""):
		pel.selectall()
	else:
		if (id!=""):
			if where=="":
				where+=" id = %s "%(id)
			else:
				where+=" and id = %s "%(id)
		if (titulo!=""):
			if where=="":
				where+=" titulo like '" +titulo+ "%'"
			else:
				where+=" and titulo like '" +titulo+ "%'"
		if (director!=""):
			if where=="":
				where+=" director like '" +director+ "%'"
			else:
				where+=" and director like '" +director+ "%'"
		if (genero!=""):
			if where=="":
				where+=" genero like '" +genero+ "%'"
			else:
				where+=" and genero like '" +genero+ "%'"
		where = "select * from pelicula where "+where
		pel.select(where)
	resp = []
	for tupla in pel.lista:
		resp.append(tupla)
	return jsonify(resp), 200

@app.route("/insert_movie", methods=["GET","POST"])
def insert_movie():
	status = True
	try:
		titulo= str(request.args.get('titulo'))
		director = str(request.args.get('director'))
		genero = str(request.args.get('genero'))
		compra= int(request.args.get('compra'))
		venta = int(request.args.get('venta'))
		stock = int(request.args.get('stock'))
		pel.insert(titulo,director,genero,compra,venta,stock)
	except Exception as e:
		status = False
	return jsonify({'status': status}), 200
	
@app.route("/update_movie", methods=["GET","POST"])
def update_movie():
	status = True
	try:
		id= int(request.args.get('id'))
		titulo= str(request.args.get('titulo'))
		director = str(request.args.get('director'))
		genero = str(request.args.get('genero'))
		compra= int(request.args.get('compra'))
		venta = int(request.args.get('venta'))
		stock = int(request.args.get('stock'))
		pel.update(id,titulo,director,genero,compra,venta,stock)
	except Exception as e:
		status = False
		raise e
	return jsonify({'status': status}), 200

@app.route("/delete_movie", methods=["GET","POST"])
def delete_movie():
	status = True
	try:
		id= int(request.args.get('id'))
		pel.delete(id)
	except Exception as e:
		status = False
		raise e
	return jsonify({'status': status}), 200

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
	print (str(request.args.get('hostname'))+" Se conectó "+request.remote_addr)
	return jsonify({'ip': request.remote_addr}), 200


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(debug = True,host='localhost', port=3000)