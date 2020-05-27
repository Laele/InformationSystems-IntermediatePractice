from model.model import Model
from view.view import View
from view.view import ViewAdmin
from view.view import ViewUser
from datetime import date

class Controller:
    """
    ********************************
    * A controller for a cinema DB *
    ********************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.viewAdmin = ViewAdmin()
        self.viewUser = ViewUser()
    
    def start(self):
        self.view.start()
        self.main_menu()
    
    """
    ***********************
    * General controllers *
    ***********************
    """

    def main_menu(self):
        o = '0'
        while o != '3':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.login()
            elif o == '2':
                self.create_usuario()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self,fs,vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if (v != ""):
                fields.append(f+" = %s")
                vals.append(v)
        return fields,vals

    """
    *************************
    * controllers for login *
    *************************
    """

    def ask_loginUsuario(self):
        self.view.ask('Id Usuario: ')
        id_usuario = input()
        self.view.ask('Clave: ')
        clave = input()
        return [id_usuario,clave]
    
    def ask_usuario(self):
        self.view.ask('Id Usuario: ')
        id_usuario = input()
        self.view.ask('Clave: ')
        clave = input()
        tipo = "usuario"
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        app = input()
        self.view.ask('Apellido Materno: ')
        apm = input()
        self.view.ask('Telefono: ')
        telefono = input()
        return [id_usuario,clave,tipo,nombre,app,apm,telefono]

    def login(self):
        id_contacto,clave = self.ask_loginUsuario()
        flag,out = self.model.login_a_usuario(id_contacto,clave)
        if flag == True and out:
            self.view.ok("Usuario" , "ah Logeado")
            #print(out)
            if out[2] == 'usuario':
                #print("hola usuario")
                self.main_menu_user(out)
            elif out[2] == 'admin':
                #print("hola admin")
                self.main_menu_admin(out)
        else:
            self.view.error("Los datos no coinciden :(")
        return

    """
    *************************
    * controllers for funciones *
    *************************
    """
    def askfuncion(self):
        self.view.ask('Pelicula: ')
        pelicula = input()
        self.view.ask('Sala: ')
        sala = input()
        self.view.ask('Inicio: ')
        inicio = input()
        return [pelicula,sala,inicio]
    
    
    """
    *************************
    * controllers for peliculas *
    *************************
    """
    def askpelicula(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Clasificación: ')
        clas = input()
        self.view.ask('Género: ')
        genero = input()
        self.view.ask('Sinópsis: ')
        sinopsis = input()
        self.view.ask('Director: ')
        director = input()
        self.view.ask('Duración: ')
        duracion = input()
        return [nombre,clas,genero,sinopsis,director,duracion]

    """
    *************************
    * controllers for salas *
    *************************
    """
    def asksala(self):
        self.view.ask('Id Sala: ')
        id_sala= input()
        self.view.ask('Asientos: ')
        asientos= input()
        return [id_sala,asientos]

    """
    ****************************
    * controllers for asientos *
    ****************************
    """
    def askasiento(self):
        self.view.ask('Sala: ')
        sala= input()
        self.view.ask('Nombre: ')
        nombre= input()
        return [sala,nombre]

    """
    ****************************
    * controllers for usuarios *
    ****************************
    """

    def askusuario(self):
        self.view.ask('Id Usuario: ')
        id_usuario = input()
        self.view.ask('Clave: ')
        clave = input()
        self.view.ask('tipo (admin o usuario): ')
        tipo = input()
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        app = input()
        self.view.ask('Apellido Materno: ')
        apm = input()
        self.view.ask('Telefono: ')
        telefono = input()
        return [id_usuario,clave,tipo,nombre,app,apm,telefono]

    """
    *****************************
    * General Users controllers *
    ****************************
    """

    def main_menu_user(self,usuario):
        o = '0'
        while o != '6':
            self.viewUser.main_menu(usuario)
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_all_funciones_user()
            elif o == '2':
                self.create_compra_user(usuario[0])
            elif o == '3':
                self.read_all_compras_user(usuario[0])
            elif o == '4':
                self.read_usuario_user(usuario[0])
            elif o == '5':
                self.read_all_boletos_user(usuario[0])
            elif o == '6':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    """
    ******************************
    * General Admins controllers *
    ******************************
    """

    def main_menu_admin(self,usuario):
        o = '0'
        while o != '8':
            self.viewAdmin.main_menu(usuario)
            self.view.option('8')
            o = input()
            if o == '1':
                self.funciones_menu_admin()
            elif o == '2':
                self.peliculas_menu_admin()
            elif o == '3':
                self.asientos_menu_admin()
            elif o == '4':
                self.salas_menu_admin()
            elif o == '5':
                self.usuarios_menu_admin()
            elif o == '6':
                self.boletos_menu_admin()
            elif o == '7':
                self.compras_menu_admin()
            elif o == '8':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def funciones_menu_admin(self):
        o = '0'
        while o != '7':
            self.viewAdmin.funciones_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_funcion_admin()
            elif o == '2':
                self.read_funcion_admin()
            elif o == '3':
                self.read_all_funciones_admin()
            elif o == '4':
                self.update_funcion_admin()
            elif o == '5':
                self.delete_funcion_admin()
            elif o == '6':
                self.read_all_funciones_user()
            elif o == '7':
                self.view.back()
            else:
                self.view.not_valid_option()
        return
    
    def peliculas_menu_admin(self):
        o = '0'
        while o != '6':
            self.viewAdmin.peliculas_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_pelicula_admin()
            elif o == '2':
                self.read_pelicula_admin()
            elif o == '3':
                self.read_all_peliculas_admin()
            elif o == '4':
                self.update_pelicula_admin()
            elif o == '5':
                self.delete_pelicula_admin()
            elif o == '6':
                self.view.back()
            else:
                self.view.not_valid_option()
        return
    
    def salas_menu_admin(self):
        o = '0'
        while o != '6':
            self.viewAdmin.salas_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_sala_admin()
            elif o == '2':
                self.read_sala_admin()
            elif o == '3':
                self.read_all_salas_admin()
            elif o == '4':
                self.update_sala_admin()
            elif o == '5':
                self.delete_sala_admin()
            elif o == '6':
                self.view.back()
            else:
                self.view.not_valid_option()
        return

    def asientos_menu_admin(self):
        o = '0'
        while o != '6':
            self.viewAdmin.asientos_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_asiento_admin()
            elif o == '2':
                self.read_asiento_admin()
            elif o == '3':
                self.read_all_asientos_admin()
            elif o == '4':
                self.update_asiento_admin()
            elif o == '5':
                self.delete_asiento_admin()
            elif o == '6':
                self.view.back()
            else:
                self.view.not_valid_option()
        return

    def usuarios_menu_admin(self):
        o = '0'
        while o != '6':
            self.viewAdmin.usuario_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_usuario_admin()
            elif o == '2':
                self.read_usuario_admin()
            elif o == '3':
                self.read_all_usuarios_admin()
            elif o == '4':
                self.update_usuario_admin()
            elif o == '5':
                self.delete_usuario_admin()
            elif o == '6':
                self.view.back()
            else:
                self.view.not_valid_option()
        return

    def boletos_menu_admin(self):
        o = '0'
        while o != '6':
            self.viewAdmin.boleto_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                pass
            elif o == '2':
                self.read_boleto_admin()
            elif o == '3':
                self.read_all_boletos_admin()
            elif o == '4':
                pass
            elif o == '5':
                pass
            elif o == '6':
                self.view.back()
            else:
                self.view.not_valid_option()
        return
    
    def compras_menu_admin(self):
        o = '0'
        while o != '6':
            self.viewAdmin.compra_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                pass
            elif o == '2':
                self.read_compra_admin()
            elif o == '3':
                self.read_all_compras_admin()
            elif o == '4':
                pass
            elif o == '5':
                pass
            elif o == '6':
                self.view.back()
            else:
                self.view.not_valid_option()
        return

    """
    *************************************
    * controllers for usuarios USER ONLY*
    *************************************
    """

    def create_usuario(self):
        id_contacto,clave,tipo,nombre,app,apm,telefono = self.ask_usuario()
        out = self.model.create_usuario(id_contacto,clave,tipo,nombre,app,apm,telefono)
        if out == True:
            self.view.ok("Usuario" , "Creado")
        else:
            if out.errno == 1062:
                self.view.error("El Id Usuario ya esta registrado")
                
            else:
                self.view.error("No se pudo agregar el Usuario Disculpe las molestias :(")
        return

    """
    **************************
    * controllers for admins *
    **************************
    """

    """
    *****************************
    * Funciones controllers *
    ****************************
    """
    def create_funcion_admin(self):
        pelicula,sala,inicio = self.askfuncion()
        out = self.model.create_funcion(pelicula,sala,inicio)
        if out == True:
            self.view.ok("Funcion" , "Creada")
            out,lugares = self.model.no_asientos_sala(sala)
            funcion = self.model.get_last_funcion()
            ids_asientos = self.model.get_idasientos_from_sala(sala)
            #print(str(lugares[0]))
            #print(ids_asientos)
            #print(ids_asientos[0][0],ids_asientos[1][0])
            for lugar in range(int(lugares[0])):
                self.create_boleto_admin(funcion[0],ids_asientos[lugar][0],45)
        else:                
            self.view.error("No se pudo agregar la Funcion :(")
        return

    def read_funcion_admin(self):    
        self.view.ask("Id Funcion: ")
        id_funcion = input()
        out = self.model.read_a_funcion(id_funcion)
        if type(out) == tuple:
            self.viewAdmin.show_funcion_header(" Datos de la Funcion " + id_funcion+" ")
            self.viewAdmin.show_a_funcion(out)
            self.viewAdmin.show_funcion_midder()
            self.viewAdmin.show_funcion_footer()
        else:
            if out == None:
                self.view.error("El Id de la Funcion no existe")
            else:
                self.view.error("Problema al leer el Id de la Funcion, Revisar datos")
        return
    
    def read_all_funciones_admin(self):    
        out = self.model.read_all_funciones()
        if type(out) == list:
            self.viewAdmin.show_funcion_header(" Todas las Funciones ")
            for funcion in out:
                self.viewAdmin.show_a_funcion(funcion)
            self.viewAdmin.show_funcion_midder()
            self.viewAdmin.show_funcion_footer()
        else:
            self.view.error("Problema al leer las Funciones, Revisar datos")
        return
    
    def update_funcion_admin(self):
        self.view.ask("Funcion a modificar: ")
        id_funcion = input()
        funcion = self.model.read_a_funcion(id_funcion)
        if type(funcion) == tuple:
            self.viewAdmin.show_funcion_header(" Datos de la Funcion "+id_funcion+" ")
            self.viewAdmin.show_a_funcion(funcion)
            self.viewAdmin.show_funcion_midder()
            self.viewAdmin.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error("La Funcion no exite en la bd")
            else:
                self.view.error("Problema al leer la Funcion, Revisa")
            return
        self.view.msg("Ingresa los valores a modificar (vacio para dejarlo igual):")
        whole_vals = self.askfuncion()
        fields, vals = self.update_lists(["f_pelicula","f_sala","f_inicio"],whole_vals)
        vals.append(id_funcion)
        vals = tuple(vals)
        out = self.model.update_funcion(fields,vals)
        if out == True:
            self.view.ok(id_funcion, "Actualizada...")
        else:
            self.view.error("No se pudo actualizar la Funcion, Revisa")
        return

    def delete_funcion_admin(self):
        self.view.ask("Funcion a borrar: ")
        id_funcion = input()
        count = self.model.delete_funcion(id_funcion)
        if count != 0:
            self.view.ok(id_funcion,"Borro")
        else:
            if count == 0:
                self.view.error("La Funcion no exite")
            else:
                self.view.error("Problema al borrar la Funcion. Revisa")
        return


        

    """
    *************************
    * Peliculas controllers *
    *************************
    """
    def create_pelicula_admin(self):
        nombre,clas,genero,sinopsis,director,duracion = self.askpelicula()
        out = self.model.create_pelicula(nombre,clas,genero,sinopsis,director,duracion)
        if out == True:
            self.view.ok("Pelicula" , "Creada")
        else:                
            self.view.error("No se pudo agregar la Pelicula :(")
        return

    def read_pelicula_admin(self):    
        self.view.ask("Id Pelicula: ")
        id_pelicula = input()
        out = self.model.read_a_pelicula(id_pelicula)
        if type(out) == tuple:
            self.viewAdmin.show_pelicula_header(" Datos de la pelicula " + id_pelicula+" ")
            self.viewAdmin.show_a_pelicula(out)
            self.viewAdmin.show_pelicula_midder()
            self.viewAdmin.show_pelicula_footer()
        else:
            if out == None:
                self.view.error("El Id de la Pelicula no existe")
            else:
                self.view.error("Problema al leer el Id de la Pelicula, Revisar datos")
        return

    def read_all_peliculas_admin(self):    
        out = self.model.read_all_peliculas()
        if type(out) == list:
            self.viewAdmin.show_pelicula_header(" Todas las Peliculas ")
            for pelicula in out:
                self.viewAdmin.show_a_pelicula(pelicula)
            self.viewAdmin.show_pelicula_midder()
            self.viewAdmin.show_pelicula_footer()
        else:
            self.view.error("Problema al leer las Peliculas, Revisar datos")
        return
    
    def update_pelicula_admin(self):
        self.view.ask("Pelicula a modificar: ")
        id_pelicula = input()
        pelicula = self.model.read_a_pelicula(id_pelicula)
        if type(pelicula) == tuple:
            self.viewAdmin.show_pelicula_header(" Datos de la Pelicula "+id_pelicula+" ")
            self.viewAdmin.show_a_pelicula(pelicula)
            self.viewAdmin.show_pelicula_midder()
            self.viewAdmin.show_pelicula_footer()
        else:
            if pelicula == None:
                self.view.error("La Pelicula no exite en la bd")
            else:
                self.view.error("Problema al leer la Pelicula, Revisa")
            return
        self.view.msg("Ingresa los valores a modificar (vacio para dejarlo igual):")
        whole_vals = self.askpelicula()
        fields, vals = self.update_lists(["p_nombre","p_clasificacion","p_genero","p_sinopsis","p_director","p_duracion"],whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_pelicula(fields,vals)
        if out == True:
            self.view.ok(id_pelicula, "Actualizada...")
        else:
            self.view.error("No se pudo actualizar la Pelicula, Revisa")
        return
    
    def delete_pelicula_admin(self):
        self.view.ask("Pelicula a borrar: ")
        id_pelicula = input()
        count = self.model.delete_pelicula(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula,"Borro")
        else:
            if count == 0:
                self.view.error("La Pelicula no exite")
            else:
                self.view.error("Problema al borrar la Pelicula. Revisa")
        return

    """
    *********************
    * Salas controllers *
    *********************
    """

    def create_sala_admin(self):
        id_sala,asientos= self.asksala()
        out = self.model.create_sala(id_sala,asientos)
        if out == True:
            self.view.ok("Sala" , "Creada")
            for asiento in range(int(asientos)):
                self.view.ask("Nombre/Lugar del asiento "+(str(asiento+1)+": "))
                nombre = input()
                out = self.model.create_asiento(id_sala,nombre)
                if out == True:
                    self.view.ok("Asiento" , "Creado")
                else:                
                    self.view.error("No se pudo agregar el Asiento :(")
        else:                
            self.view.error("No se pudo agregar la Sala :(")
        return
    
    def read_sala_admin(self):    
        self.view.ask("Id Sala: ")
        id_sala = input()
        out = self.model.read_a_sala(id_sala)
        if type(out) == tuple:
            self.viewAdmin.show_sala_header(" Datos de la Sala " + id_sala+" ")
            self.viewAdmin.show_a_sala(out)
            self.viewAdmin.show_sala_midder()
            self.viewAdmin.show_sala_footer()
        else:
            if out == None:
                self.view.error("El Id de la Sala no existe")
            else:
                self.view.error("Problema al leer el Id de la Sala, Revisar datos")
        return
    
    def read_all_salas_admin(self):    
        out = self.model.read_all_salas()
        if type(out) == list:
            self.viewAdmin.show_sala_header(" Todas las Sala ")
            for sala in out:
                self.viewAdmin.show_a_sala(sala)
            self.viewAdmin.show_sala_midder()
            self.viewAdmin.show_sala_footer()
        else:
            self.view.error("Problema al leer las Sala, Revisar datos")
        return

    def update_sala_admin(self):
        self.view.ask("Sala a modificar: ")
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)
        if type(sala) == tuple:
            self.viewAdmin.show_sala_header(" Datos de la Sala "+id_sala+" ")
            self.viewAdmin.show_a_sala(sala)
            self.viewAdmin.show_sala_midder()
            self.viewAdmin.show_sala_footer()
        else:
            if sala == None:
                self.view.error("La Sala no exite en la bd")
            else:
                self.view.error("Problema al leer la Sala, Revisa")
            return
        self.view.msg("Ingresa los valores a modificar (vacio para dejarlo igual):")
        whole_vals = self.asksala()
        fields, vals = self.update_lists(["id_sala","s_asientos"],whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields,vals)
        if out == True:
            self.view.ok(id_sala, "Actualizada...")
        else:
            self.view.error("No se pudo actualizar la Sala, Revisa")
        return

    def delete_sala_admin(self):
        self.view.ask("Sala a borrar: ")
        id_sala = input()
        count = self.model.delete_sala(id_sala)
        if count != 0:
            self.view.ok(id_sala,"Borro")
        else:
            if count == 0:
                self.view.error("La Sala no exite")
            else:
                self.view.error("Problema al borrar la Sala. Revisa")
        return

    """
    ************************
    * asientos controllers *
    ************************
    """
    def create_asiento_admin(self):
        sala,nombre = self.askasiento()
        out = self.model.create_asiento(sala,nombre)
        if out == True:
            self.view.ok("Asiento" , "Creada")
        else:                
            self.view.error("No se pudo agregar el Asiento :(")
        return
    
    def read_asiento_admin(self):    
        self.view.ask("Id Asiento: ")
        id_asiento = input()
        out = self.model.read_a_asiento(id_asiento)
        if type(out) == tuple:
            self.viewAdmin.show_asiento_header(" Datos del Asiento " + id_asiento+" ")
            self.viewAdmin.show_a_asiento(out)
            self.viewAdmin.show_asiento_midder()
            self.viewAdmin.show_asiento_footer()
        else:
            if out == None:
                self.view.error("El Id del Asiento no existe")
            else:
                self.view.error("Problema al leer el Id del Asiento, Revisar datos")
        return
    
    def read_all_asientos_admin(self):    
        out = self.model.read_all_asientos()
        if type(out) == list:
            self.viewAdmin.show_asiento_header(" Todas los Asientos ")
            for sala in out:
                self.viewAdmin.show_a_asiento(sala)
            self.viewAdmin.show_asiento_midder()
            self.viewAdmin.show_asiento_footer()
        else:
            self.view.error("Problema al leer los Asiento, Revisar datos")
        return

    def update_asiento_admin(self):
        self.view.ask("Asiento a modificar: ")
        id_asiento = input()
        asiento = self.model.read_a_asiento(id_asiento)
        if type(asiento) == tuple:
            self.viewAdmin.show_asiento_header(" Datos del Asiento "+id_asiento+" ")
            self.viewAdmin.show_a_asiento(asiento)
            self.viewAdmin.show_asiento_midder()
            self.viewAdmin.show_asiento_footer()
        else:
            if asiento == None:
                self.view.error("El Asiento no exite en la bd")
            else:
                self.view.error("Problema al leer el Id del Asiento, Revisa")
            return
        self.view.msg("Ingresa los valores a modificar (vacio para dejarlo igual):")
        whole_vals = self.askasiento()
        fields, vals = self.update_lists(["a_sala","a_nombre"],whole_vals)
        vals.append(id_asiento)
        vals = tuple(vals)
        out = self.model.update_asiento(fields,vals)
        if out == True:
            self.view.ok(id_asiento, "Actualizada...")
        else:
            self.view.error("No se pudo actualizar el Asiento, Revisa")
        return

    def delete_asiento_admin(self):
        self.view.ask("Asiento a borrar: ")
        id_asiento = input()
        count = self.model.delete_asiento(id_asiento)
        if count != 0:
            self.view.ok(id_asiento,"Borro")
        else:
            if count == 0:
                self.view.error("El Asiento no exite")
            else:
                self.view.error("Problema al borrar el Asiento. Revisa")
        return

    """
    ************************
    * Usuarios controllers *
    ************************
    """
    def create_usuario_admin(self):
        id_contacto,clave,tipo,nombre,app,apm,telefono = self.askusuario()
        out = self.model.create_usuario(id_contacto,clave,tipo,nombre,app,apm,telefono)
        if out == True:
            self.view.ok("Usuario" , "Creado")
        else:
            if out.errno == 1062:
                self.view.error("El Id Usuario ya esta registrado")
                
            else:
                self.view.error("No se pudo agregar el Usuario Disculpe las molestias :(")
        return

    def read_usuario_admin(self):    
        self.view.ask("Id Usuario: ")
        id_usuario = input()
        out = self.model.read_a_usuario(id_usuario)
        if type(out) == tuple:
            self.viewAdmin.show_usuario_header(" Datos del usuario " + id_usuario+" ")
            self.viewAdmin.show_a_usuario(out)
            self.viewAdmin.show_usuario_midder()
            self.viewAdmin.show_usuario_footer()
        else:
            if out == None:
                self.view.error("El Id del usuario no existe")
            else:
                self.view.error("Problema al leer el Id del usuario, Revisar datos")
        return

    def read_all_usuarios_admin(self):    
        out = self.model.read_all_usuarios()
        if type(out) == list:
            self.viewAdmin.show_usuario_header(" Todas los usuarios ")
            for usuario in out:
                self.viewAdmin.show_a_usuario(usuario)
            self.viewAdmin.show_usuario_midder()
            self.viewAdmin.show_usuario_footer()
        else:
            self.view.error("Problema al leer los Usuario, Revisar datos")
        return
    
    def update_usuario_admin(self):
        self.view.ask("Usuario a modificar: ")
        id_usuario = input()
        usuario = self.model.read_a_usuario(id_usuario)
        if type(usuario) == tuple:
            self.viewAdmin.show_usuario_header(" Datos de la usuario "+id_usuario+" ")
            self.viewAdmin.show_a_usuario(usuario)
            self.viewAdmin.show_usuario_midder()
            self.viewAdmin.show_usuario_footer()
        else:
            if usuario == None:
                self.view.error("La usuario no exite en la bd")
            else:
                self.view.error("Problema al leer la usuario, Revisa")
            return
        self.view.msg("Ingresa los valores a modificar (vacio para dejarlo igual):")
        whole_vals = self.askusuario()
        fields, vals = self.update_lists(["id_usuario","u_clave","u_tipo","u_nombre","u_app","u_apm","u_telefono"],whole_vals)
        vals.append(id_usuario)
        vals = tuple(vals)
        out = self.model.update_usuario(fields,vals)
        if out == True:
            self.view.ok(id_usuario, "Actualizado...")
        else:
            self.view.error("No se pudo actualizar el usuario, Revisa")
        return
    
    def delete_usuario_admin(self):
        self.view.ask("usuario a borrar: ")
        id_usuario = input()
        count = self.model.delete_usuario(id_usuario)
        if count != 0:
            self.view.ok(id_usuario,"Borro")
        else:
            if count == 0:
                self.view.error("La usuario no exite")
            else:
                self.view.error("Problema al borrar el usuario. Revisa")
        return
    
    """
    ************************
    * boletos controllers *
    ************************
    """
    def create_boleto_admin(self,idFuncion,idAsiento,precio):
        #print(idFuncion,idAsiento,1,precio)
        out = self.model.create_boleto(idFuncion,idAsiento,1,precio)
        if out == True:
            self.view.ok("boleto" , "Creado")
        else:
            if out.errno == 1062:
                self.view.error("El Id boleto ya esta registrado")
                
            else:
                self.view.error("No se pudo agregar el boleto Disculpe las molestias :(")
        return

    def read_boleto_admin(self):    
        self.view.ask("Id boleto: ")
        id_boleto = input()
        out = self.model.read_a_boleto(id_boleto)
        if type(out) == tuple:
            self.viewAdmin.show_boleto_header(" Datos del boleto " + id_boleto+" ")
            self.viewAdmin.show_a_boleto(out)
            self.viewAdmin.show_boleto_midder()
            self.viewAdmin.show_boleto_footer()
        else:
            if out == None:
                self.view.error("El Id del boleto no existe")
            else:
                self.view.error("Problema al leer el Id del boleto, Revisar datos")
        return

    def read_all_boletos_admin(self):    
        out = self.model.read_all_boletos()
        if type(out) == list:
            self.viewAdmin.show_boleto_header(" Todas los boletos ")
            for boleto in out:
                self.viewAdmin.show_a_boleto(boleto)
            self.viewAdmin.show_boleto_midder()
            self.viewAdmin.show_boleto_footer()
        else:
            self.view.error("Problema al leer los boleto, Revisar datos")
        return

    def delete_boleto_admin(self):
        self.view.ask("boleto a borrar: ")
        id_boleto = input()
        count = self.model.delete_boleto(id_boleto)
        if count != 0:
            self.view.ok(id_boleto,"Borro")
        else:
            if count == 0:
                self.view.error("La boleto no exite")
            else:
                self.view.error("Problema al borrar el boleto. Revisa")
        return

    """
    ************************
    * compras controllers *
    ************************
    """
    '''
    def create_compra_admin(self,idFuncion,idAsiento,precio):
        #print(idFuncion,idAsiento,1,precio)
        out = self.model.create_compra(idFuncion,idAsiento,1,precio)
        if out == True:
            self.view.ok("compra" , "Creado")
        else:
            if out.errno == 1062:
                self.view.error("El Id compra ya esta registrado")
                
            else:
                self.view.error("No se pudo agregar el compra Disculpe las molestias :(")
        return
    '''

    def read_compra_admin(self):    
        self.view.ask("Id compra: ")
        id_compra = input()
        out = self.model.read_a_compra(id_compra)
        if type(out) == tuple:
            self.viewAdmin.show_compra_header(" Datos del compra " + id_compra+" ")
            self.viewAdmin.show_a_compra(out)
            self.viewAdmin.show_compra_midder()
            self.viewAdmin.show_compra_footer()
        else:
            if out == None:
                self.view.error("El Id del compra no existe")
            else:
                self.view.error("Problema al leer el Id del compra, Revisar datos")
        return

    def read_all_compras_admin(self):    
        out = self.model.read_all_compras()
        if type(out) == list:
            self.viewAdmin.show_compra_header(" Todas los compras ")
            for compra in out:
                self.viewAdmin.show_a_compra(compra)
            self.viewAdmin.show_compra_midder()
            self.viewAdmin.show_compra_footer()
        else:
            self.view.error("Problema al leer los compra, Revisar datos")
        return

    '''
    def delete_compra_admin(self):
        self.view.ask("compra a borrar: ")
        id_compra = input()
        count = self.model.delete_compra(id_compra)
        if count != 0:
            self.view.ok(id_compra,"Borro")
        else:
            if count == 0:
                self.view.error("La compra no exite")
            else:
                self.view.error("Problema al borrar el compra. Revisa")
        return
    '''

    """
    *************************
    * controllers for users *
    *************************
    """
    """
    ************************
    * compras controllers *
    ************************
    """
    
    def create_compra_user(self,id_usuario):
        flag = 1
        cartelera = self.model.read_all_funciones_cartelera()
        self.viewAdmin.show_funcion_header(" Funciones de Cartelera ")
        for funcion in cartelera:
            self.viewAdmin.show_a_funcion(funcion)
        self.viewAdmin.show_funcion_midder()
        self.viewAdmin.show_funcion_footer()
        self.view.ask("Introduce el Id de la funcion: ")
        id_funcion = input()
        out = self.model.read_a_funcion(id_funcion)
        if type(out) == tuple:
            r = '1'
            while (r == '1'):
                boletos = self.model.read_all_boletos_funcion(int(id_funcion))
                self.viewAdmin.show_boleto_header(" Todas los boletos para la funcion seleccionada ")
                for boleto in boletos:
                    self.viewAdmin.show_a_boleto(boleto)
                self.viewAdmin.show_boleto_midder()
                self.viewAdmin.show_boleto_footer()
                self.view.ask("Introduce el Id del boleto para comprar: ")
                id_boleto = input()
                boleto = self.model.read_a_boleto(id_boleto)
                if type(boleto) == tuple:
                    hoy = self.model.fechahora_hoy()
                    #print(id_usuario)
                    #print(hoy[0])
                    if flag == 1:
                        self.model.create_compra(id_usuario,0,hoy[0],0)
                        flag = 0
                    lastcompra = self.model.get_last_compra()
                    #print(lastcompra[0])
                    #print(boleto[0])
                    self.create_compraDetalle_user(lastcompra[0],boleto[0])
                    self.update_boleto(boleto[0])
                    self.update_compra_user(lastcompra[0],boleto[4])
                    r2 = ''
                    while (r2 != '0' and r2 != '1'):
                        self.view.ask("¿Quieres comprar otro boleto para la misma función?: (1 para: SÍ, 0 para: No) ")
                        r2 = input()
                    r = r2
                else:
                    if boleto == None:
                        self.view.error("El Id del boleto no existe")
                    else:
                        self.view.error("Problema al leer el Id del boleto, Revisar datos")
        else:
            if out == None:
                self.view.error("El Id de la Funcion no existe")
            else:
                self.view.error("Problema al leer el Id de la Funcion, Revisar datos")       
        return
    
    def read_all_compras_user(self,id_usuario):    
        out = self.model.read_all_compras_where_usuario(id_usuario)
        if type(out) == list:
            self.viewUser.show_compra_header(" Todas mis compras ")
            for compra in out:
                self.viewUser.show_a_compra(compra)
            self.viewUser.show_compra_midder()
            self.viewUser.show_compra_footer()
        else:
            self.view.error("Problema al leer las compras, Revisar datos")
        return

    def update_compra_user(self,id_compra,total):
        compra = self.model.read_a_compra(id_compra)
        if type(compra) == tuple:
            pass
        else:
            if compra == None:
                self.view.error("La compra no exite en la bd")
            else:
                self.view.error("Problema al leer la compra, Revisa")
            return
        '''
        whole_vals = ['','',cantidad,'',total]
        fields, vals = self.update_lists(["id_compra","c_usuario","c_cantidad","c_fecha","c_total"],whole_vals)
        vals.append(id_compra)
        vals = tuple(vals)
        '''
        out = self.model.update_compra(id_compra,total)
        if out == True:
            self.view.ok(id_compra, "Actualizado...")
        else:
            self.view.error("No se pudo actualizar la compra, Revisa")
        return
    
    """
    *****************************
    * Funciones controllers *
    ****************************
    """
    
    def read_all_funciones_user(self):    
        out = self.model.read_all_funciones_cartelera()
        if type(out) == list:
            self.viewUser.show_funcion_header(" Funciones de Cartelera ")
            for funcion in out:
                self.viewUser.show_a_funcion(funcion)
            self.viewUser.show_funcion_midder()
            self.viewUser.show_funcion_footer()
        else:
            self.view.error("Problema al leer las Funciones, Revisar datos")
        return
    
    """
    *******************************
    * compras detalle controllers *
    *******************************
    """

    def create_compraDetalle_user(self,id_compra,id_boleto):
        out = self.model.create_compra_detalle(id_compra,id_boleto)
        if out == True:
            self.view.ok("Compra-Detalle" , "Creada")
        else:                
            self.view.error("No se pudo agregar Compra-Detalle Disculpe las molestias :(")
        return
    
    

    def read_compraDetalle_user(self,id_compra):    
        out = self.model.read_a_compra_detalle(id_compra)
        if type(out) == tuple:
            self.viewUser.show_compra_header(" Datos del compra-Detalle " + id_compra+" ")
            self.viewUser.show_a_compra(out)
            self.viewUser.show_compra_midder()
            self.viewUser.show_compra_footer()
        else:
            if out == None:
                self.view.error("El Id del compra no existe")
            else:
                self.view.error("Problema al leer el Id del compra, Revisar datos")
        return

    '''
    *******************
    *** Boleto Update *
    *******************
    '''
    def update_boleto(self,id_boleto):
        boleto = self.model.read_a_boleto(id_boleto)
        if type(boleto) == tuple:
            pass
        else:
            if boleto == None:
                self.view.error("El boleto no exite en la bd")
            else:
                self.view.error("Problema al leer la boleto, Revisa")
            return
        #print(fields,vals)
        out = self.model.update_boleto_comprado(id_boleto)
        if out == True:
            self.view.ok(id_boleto, "Actualizado...")
        else:
            self.view.error("No se pudo actualizar el boleto, Revisa")
        return

    def read_all_boletos_user(self,id_usuario):    
        out = self.model.read_all_boletos_where_usuario(id_usuario)
        if type(out) == list:
            self.viewUser.show_boleto_header(" Boletos Adquiridos ")
            for boleto in out:
                self.viewUser.show_a_boleto(boleto)
            self.viewUser.show_boleto_midder()
            self.viewUser.show_boleto_footer()
        else:
            self.view.error("Problema al leer los boletos, Revisar datos")
        return

    '''
    ************************
    *** read usuario datos *
    ************************
    '''
    def read_usuario_user(self,id_usuario):    
        out = self.model.read_a_usuario(id_usuario)
        if type(out) == tuple:
            self.viewAdmin.show_usuario_header(" Mis Datos " + id_usuario+" ")
            self.viewAdmin.show_a_usuario(out)
            self.viewAdmin.show_usuario_midder()
            self.viewAdmin.show_usuario_footer()
        else:
            if out == None:
                self.view.error("El Id del usuario no existe")
            else:
                self.view.error("Problema al leer el Id del usuario, Revisar datos")
        return