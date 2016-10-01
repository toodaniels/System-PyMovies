import postgresql


class pelicula(object):
		"""Clase de pelicula en la BD"""
		def __init__(self):
			query = ('pq://%s:%d@%s:%i/%s'%("user",pass,"host",port,"Database"))
			print(query)
			self.db =postgresql.open(query)

		def selectall(self):
			self.lista = self.db.prepare("select * from pelicula ORDER BY id ASC")

		def select(self, query):
			self.lista = self.db.prepare(query + " ORDER BY id ASC")

		def insert(self,titulo,director,genero,compra,venta,stock):
			mkpeli=self.db.prepare("insert into pelicula(titulo,director,genero,compra,venta,stock) values ($1,$2,$3,$4,$5,$6)")
			mk = mkpeli(titulo,director,genero,compra,venta,stock)

		def update(self,id,titulo,director,genero,compra,venta,stock):
			uppeli = self.db.prepare("update pelicula set titulo=$2,director=$3,genero=$4,compra=$5,venta=$6,stock=$7 where id = $1 or titulo = $2")
			up = uppeli(id,titulo,director,genero,compra,venta,stock)

		def delete(self,id):
			rmpeli =self.db.prepare("delete from pelicula where id = $1 ")
			rm = rmpeli(id)
			
"""
		def selectconexion(self):
			self.listcon = self.db.prepare("select * from conexion")
			
		def insertconexion(self,ip):
			mkcon=self.db.prepare("insert into conexion(ip,text(now())) values ($1)")
			mk = mkcon(ip)

		def insertmovi(self,ip,id,name):
			mkmov=self.db.prepare("insert into conexion(ip,id_movie,name_movie) values ($1,$2,$3)")
			mk = mkmov(ip,id,name)

		def selectmovi(self):
			self.listmov = self.db.prepare("select * from movimientos")

				
peli= pelicula()
peli.insert("Civil War","Hermanos Ruso","Ciencia Ficción", 400,500,200)
peli.update(22,"Civil War 2","Hermanos Ruso","Ciencia Ficción", 400,501,200)
peli.delete(23)
peli.selectall()
"""




"""
llenado multiple
mkpeli.load_rows([
	("Avengers 2", "Marvel","Ciencia Ficción",500,600,5),
	("Avengers 2", "Marvel","Ciencia Ficción",500,600,5),
	("Avengers 2", "Marvel","Ciencia Ficción",500,600,5),
])
"""
