from mysql import connector

class Model:
    """
    *******************************************
    * A data model with MySQL for a cinema DB *
    *******************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key,val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor(buffered=True)
    
    def close_db(self):
        self.cnx.close()

    """
    *********************
    * peliculas methods *
    *********************
    """

    def create_pelicula(self,nombre,clasificacion,genero,sinopsis,director,duracion):
        try:
            sql = 'INSERT INTO peliculas (`p_nombre`, `p_clasificacion`,`p_genero`,`p_sinopsis`,`p_director`,`p_duracion`) VALUES (%s,%s,%s,%s,%s,%s)'
            vals = (nombre,clasificacion,genero,sinopsis,director,duracion)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_pelicula(self,id_pelicula):
        try:
            sql = "SELECT * FROM peliculas WHERE peliculas.id_pelicula =  %s"
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err
    
    def read_all_peliculas(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def update_pelicula(self,fields,vals):
        try:
            sql = 'UPDATE peliculas SET '+','.join(fields) + 'WHERE id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_pelicula(self,id_pelicula):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *****************
    * salas methods *
    *****************
    """

    def create_sala(self,id_sala,asientos):
        try:
            sql = 'INSERT INTO salas (`id_sala`,`s_asientos`) VALUES (%s,%s)'
            vals = (id_sala,asientos)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_sala(self,id_sala):
        try:
            sql = "SELECT * FROM salas WHERE salas.id_sala =  %s"
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err
    
    def read_all_salas(self):
        try:
            sql = 'SELECT * FROM salas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def update_sala(self,fields,vals):
        try:
            sql = 'UPDATE salas SET '+','.join(fields) + 'WHERE id_sala = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_sala(self,id_sala):
        try:
            sql = 'DELETE FROM salas WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * usuarios methods *
    ********************
    """

    def create_usuario(self,id_usuario,clave,tipo,nombre,app,apm,telefono):
        try:
            sql = 'INSERT INTO usuarios (`id_usuario`,`u_clave`,`u_tipo`,`u_nombre`,`u_app`,`u_apm`,`u_telefono`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            vals = (id_usuario,clave,tipo,nombre,app,apm,telefono)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_usuario(self,id_usuario):
        try:
            sql = "SELECT * FROM usuarios WHERE usuarios.id_usuario =  %s"
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err
    
    def read_all_usuarios(self):
        try:
            sql = 'SELECT * FROM usuarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def update_usuario(self,fields,vals):
        try:
            sql = 'UPDATE usuarios SET '+','.join(fields) + 'WHERE id_usuario = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_usuario(self,id_usuario):
        try:
            sql = 'DELETE FROM usuarios WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    *********************
    * funciones methods *
    *********************
    """

    def create_funcion(self,pelicula,sala,inicio):
        try:
            sql = 'INSERT INTO funciones (`f_pelicula`,`f_sala`,`f_inicio`) VALUES (%s,%s,%s)'
            vals = (pelicula,sala,inicio)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_funcion(self,id_funcion):
        try:
            sql = "SELECT * FROM funciones WHERE funciones.id_funcion =  %s"
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def read_all_funciones(self):
        try:
            sql = 'SELECT * FROM funciones'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def update_funcion(self,fields,vals):
        try:
            sql = 'UPDATE funciones SET '+','.join(fields) + 'WHERE id_funcion = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_funcion(self,id_funcion):
        try:
            sql = 'DELETE FROM funciones WHERE id_funcion = %s'
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * asientos methods *
    ********************
    """

    def create_asiento(self,sala,nombre):
        try:
            sql = 'INSERT INTO asientos (`a_sala`,`a_nombre`) VALUES (%s,%s)'
            vals = (sala,nombre)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_asiento(self,id_asiento):
        try:
            sql = "SELECT * FROM asientos WHERE asientos.id_asiento =  %s"
            vals = (id_asiento,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err


    def read_all_asientos(self):
        try:
            sql = 'SELECT * FROM asientos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    def update_asiento(self,fields,vals):
        try:
            sql = 'UPDATE asientos SET '+','.join(fields) + 'WHERE id_asiento= %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_asiento(self,id_asiento):
        try:
            sql = 'DELETE FROM asientos WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *******************
    * boletos methods *
    *******************
    """

    def create_boleto(self,funcion,asiento,disponible,precio):
        try:
            sql = 'INSERT INTO boletos (`b_funcion`,`b_asiento`,`b_disponible`,`b_precio`) VALUES (%s,%s,%s,%s)'
            vals = (funcion,asiento,disponible,precio)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_boleto(self,id_boleto):
        try:
            sql = "SELECT * FROM boletos WHERE boletos.id_boleto =  %s"
            vals = (id_boleto,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def read_all_boletos(self):
        try:
            sql = 'SELECT * FROM boletos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def update_boleto(self,fields,vals):
        try:
            sql = 'UPDATE boletos SET '+','.join(fields) + 'WHERE id_boleto= %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_boleto(self,id_boleto):
        try:
            sql = 'DELETE FROM boletos WHERE id_boleto = %s'
            vals = (id_boleto,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *******************
    * compras methods *
    *******************
    """

    def create_compra(self,usuario,cantidad,fecha,total):
        try:
            sql = 'INSERT INTO compras (`c_usuario`,`c_cantidad`,`c_fecha`,`c_total`) VALUES (%s,%s,%s,%s)'
            vals = (usuario,cantidad,fecha,total)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_compra(self,id_compra):
        try:
            sql = "SELECT * FROM compras WHERE compras.id_compra =  %s"
            vals = (id_compra,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def read_all_compras(self):
        try:
            sql = 'SELECT * FROM compras'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    def update_compra(self,id_compra,total):
        try:
            sql = 'UPDATE compras SET c_cantidad = c_cantidad + 1, c_total = c_total + %s WHERE id_compra = %s'
            #sql = 'UPDATE compras SET '+','.join(fields) + 'WHERE id_compra= %s'
            vals=(total,id_compra)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_compra(self,id_compra):
        try:
            sql = 'DELETE FROM compras WHERE id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***************************
    * detalles compra methods *
    ***************************
    """

    def create_compra_detalle(self,id_compra,id_boleto):
        try:
            sql = 'INSERT INTO detalles_compras (`id_compra`,`id_boleto`) VALUES (%s,%s)'
            vals = (id_compra,id_boleto)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_compra_detalle(self,id_compra):
        try:
            sql = "SELECT * FROM detalles_compras WHERE detalles_compras.id_compra =  %s"
            vals = (id_compra,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record

        except connector.Error as err:
            return err

    def read_all_compras_detalles(self):
        try:
            sql = 'SELECT * FROM detalles_compras'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    def update_compra_detalles(self,fields,vals):
        try:
            sql = 'UPDATE detalles_compras SET '+','.join(fields) + 'WHERE id_compra= %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_compra_detalle(self,id_compra):
        try:
            sql = 'DELETE FROM detalles_compras WHERE id_compra = %s'
            vals = (id_compra,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *****************
    * Login methods *
    *****************
    """

    def login_a_usuario(self,id_usuario,clave):
        try:
            sql = 'SELECT * FROM usuarios WHERE id_usuario = %s and u_clave = %s'
            vals = (id_usuario,clave)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return True,records

        except connector.Error as err:
            return False,err
    
    """
    *****************
    * Other methods *
    *****************
    """
    def no_asientos_sala(self,id_sala):
        try:
            sql = 'SELECT salas.s_asientos FROM salas WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchone()
            return True,records

        except connector.Error as err:
            return False,err
    
    def get_last_funcion(self):
        try:
            sql = 'SELECT MAX(id_funcion) FROM funciones'
            self.cursor.execute(sql)
            records = self.cursor.fetchone()
            return records

        except connector.Error as err:
            return err
    
    def get_idasientos_from_sala(self,id_sala):
        try:
            sql = 'SELECT asientos.id_asiento FROM asientos WHERE asientos.a_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    def read_all_funciones_cartelera(self):
        try:
            sql = 'SELECT funciones.id_funcion,peliculas.p_nombre,f_sala,f_inicio FROM funciones,peliculas WHERE f_inicio BETWEEN now() AND ADDDATE(now(),7) AND funciones.f_pelicula = peliculas.id_pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def read_all_boletos_funcion(self,id_funcion):
        try:
            sql = 'SELECT * FROM boletos WHERE b_funcion = %s AND b_disponible = 1'
            vals = (id_funcion,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    
    def fechahora_hoy(self):
        try:
            sql = 'select now()'
            self.cursor.execute(sql)
            records = self.cursor.fetchone()
            return records

        except connector.Error as err:
            return err

    def get_last_compra(self):
        try:
            sql = 'SELECT MAX(id_compra) FROM compras'
            self.cursor.execute(sql)
            records = self.cursor.fetchone()
            return records

        except connector.Error as err:
            return err
    
    
    def update_boleto_comprado(self,id_boleto):
        try:
            sql = 'UPDATE boletos SET b_disponible = 0 WHERE id_boleto= %s'
            vals = (id_boleto,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_all_compras_where_usuario(self,id_usuario):
        try:
            sql = 'SELECT compras.* FROM compras WHERE compras.c_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err

    def read_all_boletos_where_usuario(self,id_usuario):
        try:
            sql = 'SELECT boletos.id_boleto,peliculas.p_nombre,funciones.f_sala,funciones.f_inicio,asientos.a_nombre,boletos.b_precio,dc.id_compra FROM boletos,detalles_compras dc,compras,funciones,asientos,peliculas WHERE boletos.id_boleto = dc.id_boleto AND dc.id_compra = compras.id_compra AND compras.c_usuario = %s AND funciones.id_funcion = boletos.b_funcion AND peliculas.id_pelicula = funciones.f_pelicula AND asientos.id_asiento = boletos.b_asiento'
            vals = (id_usuario,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records

        except connector.Error as err:
            return err
    


