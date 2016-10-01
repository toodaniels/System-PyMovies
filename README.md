# System-PyMovies
Postgres BD

create table pelicula (
  id serial,
  titulo text,
  director text,
  genero text,
  compra integer,
  venta integer,
  stock integer,
  primary key(id)
);

Modulos de Python 

Servidor 
  flask
  postgresql
Cliente 
  pyqt5

Primero abrir y revisar la dirección en el navegador http://localhost:3000/
