#Definition of the schema of the DB
#This is a DB for managing information about a cinema, clients, movies, etc.

#Create the DB
CREATE DATABASE IF NOT EXISTS cinema_db;

#Select the database to work with
USE cinema_db;

CREATE TABLE IF NOT EXISTS peliculas(
	id_pelicula INT NOT NULL AUTO_INCREMENT,
    p_nombre VARCHAR(30),
    p_clasificacion VARCHAR(3),
    p_genero VARCHAR(20),
    p_sinopsis VARCHAR(100),
    p_director VARCHAR(30),
    p_duracion TIME,
    PRIMARY KEY(id_pelicula)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS salas(
	id_sala VARCHAR(10) NOT NULL,
    s_asientos INT NOT NULL,
    PRIMARY KEY(id_sala)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS usuarios(
	id_usuario VARCHAR(30) NOT NULL,
    u_clave VARCHAR(30) NOT NULL,
    u_tipo VARCHAR(10) NOT NULL,
    u_nombre VARCHAR(30),
    u_app VARCHAR(30),
    u_apm VARCHAR(30),
    u_telefono VARCHAR(10),
    PRIMARY KEY(id_usuario)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS funciones(
	id_funcion INT NOT NULL AUTO_INCREMENT,
    f_pelicula INT,
    f_sala varchar(10),
    f_inicio DATETIME NOT NULL,
    PRIMARY KEY(id_funcion),
    CONSTRAINT fkpelicula_funciones FOREIGN KEY(f_pelicula)
		REFERENCES peliculas(id_pelicula)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
	CONSTRAINT fksala_funciones FOREIGN KEY(f_sala)
		REFERENCES salas(id_sala)
		ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB; 

CREATE TABLE IF NOT EXISTS asientos(
	id_asiento INT NOT NULL AUTO_INCREMENT,
    a_sala varchar(10),
    a_nombre VARCHAR(10),
    PRIMARY KEY(id_asiento),
    CONSTRAINT fksala_asientos FOREIGN KEY(a_sala)
		REFERENCES salas(id_sala)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS boletos(
	id_boleto INT NOT NULL AUTO_INCREMENT,
    b_funcion INT,
    b_asiento INT,
    b_disponible boolean NOT NULL,
    b_precio FLOAT,
    PRIMARY KEY(id_boleto),
    CONSTRAINT fkfuncion_boletos FOREIGN KEY(b_funcion)
		REFERENCES funciones(id_funcion)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
	CONSTRAINT fkasiento_boletos FOREIGN KEY(b_asiento)
		REFERENCES asientos(id_asiento)
        ON DELETE SET NULL
        ON UPDATE CASCADE		
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS compras(
	id_compra INT NOT NULL AUTO_INCREMENT,
    c_usuario VARCHAR(30),
    c_cantidad INT,
    c_fecha DATETIME,
    c_total FLOAT,
    PRIMARY KEY(id_compra),
	CONSTRAINT fkusuario_compras FOREIGN KEY(c_usuario)
		REFERENCES usuarios(id_usuario)
		ON DELETE SET NULL
		ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS detalles_compras(
	id_compra INT NOT NULL,
    id_boleto INT NOT NULL,
    PRIMARY KEY(id_compra,id_boleto),
	CONSTRAINT fkcompra_dc FOREIGN KEY(id_compra)
		REFERENCES compras(id_compra),
	CONSTRAINT fkboleto_dc FOREIGN KEY(id_boleto)
		REFERENCES boletos(id_boleto)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;


#Sentencia para crear primer admin
INSERT INTO usuarios (`id_usuario`,`u_clave`,`u_tipo`,`u_nombre`,`u_app`,`u_apm`,`u_telefono`) VALUES ('luissoriano@outlook.com','1234','admin','Luis','Soriano','Crespo','4641145785');















