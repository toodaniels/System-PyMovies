import postgresql #importo el modulo postgresql


class pelicula(object): #creo clase pelicula
		"""Clase de pelicula en la BD"""
		def __init__(self):#Constructor creo la conexion a la base de datos
			query = ('pq://%s:%d@%s:%i/%s'%("user",pass,"host",port,"Database"))
			print(query)
			self.db =postgresql.open(query) #Conexión

		def selectall(self): # Funcion para mostrar todos los registros
			# el resutado lo guarda en una variable lista de la clase
			self.lista = self.db.prepare("select * from pelicula ORDER BY id ASC")

		def select(self, query): # Funcion ejecuta la busqueda que se le asigna por el servidor 
			# el resutado lo guarda en una variable lista de la clase
			self.lista = self.db.prepare(query + " ORDER BY id ASC")

		def insert(self,titulo,director,genero,compra,venta,stock): #Inserta en la base de datos 
			mkpeli=self.db.prepare("insert into pelicula(titulo,director,genero,compra,venta,stock) values ($1,$2,$3,$4,$5,$6)")
			#noimporta si retorna por que no requerimos ver resultados 
			mk = mkpeli(titulo,director,genero,compra,venta,stock)

		def update(self,id,titulo,director,genero,compra,venta,stock): #Actualiza el regustro segun el id 
			uppeli = self.db.prepare("update pelicula set titulo=$2,director=$3,genero=$4,compra=$5,venta=$6,stock=$7 where id = $1 or titulo = $2")
			#noimporta si retorna por que no requerimos ver resultados 
			up = uppeli(id,titulo,director,genero,compra,venta,stock)

		def delete(self,id): #Elimina un registro segun su id  
			rmpeli =self.db.prepare("delete from pelicula where id = $1 ")
			#noimporta si retorna por que no requerimos ver resultados 
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
