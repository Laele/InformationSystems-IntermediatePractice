class View:
    """
    ***************************
    * A view  for a cinema DB *
    ***************************
    """
    def start(self):
        print('==================================')
        print('= ¡Bienvenido a  cine Salamanca! =')
        print('==================================')
    
    def end(self):
        print('===============')
        print('= ¡Nos vemos! =')
        print('===============')

    def back(self):
        print('==================================')
        print('= Regresando a menú anterior ... =')
        print('==================================')
    
    def main_menu(self):
        print("************************")
        print("* -- Menu Principal -- *")
        print("************************")
        print("1. Acceder")
        print("2. Crear Cuenta")
        print("3. Salir")
    
    def option(self,last):
        print("Selecciona una opcion (1 - "+last+"'): ", end = "")
    
    def not_valid_option(self):
        print("¡Opcion no valida!\nIntenta de nuevo")
    
    def ask(self,output):
        print(output, end = "")
    
    def msg(self, output):
        print(output)
    
    def ok(self,id,op):
        print("+"*(len(str(id))+len(op)+24))
        print("+ ¡"+str(id)+" se "+op+" correctamente! +")
        print("+"*(len(str(id))+len(op)+24))
    
    def error(self,err):
        print(" ¡ERROR! ".center(len(err)+4, "-"))
        print("- "+err+" -")
        print("-"*(len(err)+4))

class ViewAdmin:
    """
    *********************************
    * A view Admins for a cinema DB *
    *********************************
    """

    def main_menu(self,usuario):
        print("************************************")
        print("* -- Hola Admin! "+usuario[3]+" -- *")
        print("* -- Menu Principal -- *")
        print("************************************")
        print("1. Funciones")
        print("2. Peliculas")
        print("3. Asientos")
        print("4. Salas")
        print("5. Usuarios")
        print("6. Boletos")
        print("7. Compras")
        print("8. Salir")

    """
    ***********************
    * Views for funciones *
    ***********************
    """

    def funciones_menu(self):
        print("***************************")
        print("* -- Submenu Funciones -- *")
        print("***************************")
        print("1. Crear Funcion")
        print("2. Mostrar Funcion")
        print("3. Mostrar todas las Funciones")
        print("4. Actualizar Funcion")
        print("5. Borrar Funcion")
        print("6. Mostrar Funciones de Cartelera")
        print("7. Regresar")
    
    def show_a_funcion(self,record):
        print(f'{record[0]:<6}|{record[1]:<6} |{record[2]:<10}|{record[3]}')

    def show_funcion_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(6)+"|"+"Pelicula".ljust(6)+"|"+"Sala".ljust(10)+"|"+"Inicio".ljust(20))
        print("-"*120)
    
    def show_funcion_midder(self):
        print("-"*120)
    
    def show_funcion_footer(self):
        print("*"*120)
    
    """
    ***********************
    * Views for Peliculas *
    ***********************
    """

    def peliculas_menu(self):
        print("***************************")
        print("* -- Submenu Peliculas -- *")
        print("***************************")
        print("1. Crear pelicula")
        print("2. Mostrar pelicula")
        print("3. Mostrar todas las peliculas")
        print("4. Actualizar pelicula")
        print("5. Borrar pelicula")
        print("6. Regresar")
    
    def show_a_pelicula(self,record):
        print(f'{record[0]:<6}|{record[1]:<30} |{record[2]:<13}|{record[3]:<13}|{record[4]:<70}|{record[5]:<20}|{record[6]}')

    def show_pelicula_header(self,header):
        print(header.center(160,"*"))
        print("Id".ljust(6)+"|"+"Nombre".ljust(30)+"|"+"Clasificacion "+"|"+"Genero".ljust(13)+"|"+"Sinopsis".ljust(70)+"|"+"Director".ljust(20)+"|"+"Duracion")
        print("-"*160)
    
    def show_pelicula_midder(self):
        print("-"*160)
    
    def show_pelicula_footer(self):
        print("*"*160)
    
    """
    ***********************
    * Views for Asientos *
    ***********************
    """

    def asientos_menu(self):
        print("***************************")
        print("* -- Submenu Asientos -- *")
        print("***************************")
        print("1. Crear asientos")
        print("2. Mostrar asientos")
        print("3. Mostrar todas los asientos")
        print("4. Actualizar asientos")
        print("5. Borrar asientos")
        print("6. Regresar")

    def show_a_asiento(self,record):
        print(f'{record[0]:<6}|{record[1]:<10} |{record[2]:<10}')

    def show_asiento_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(6)+"|"+"Sala".ljust(10)+"|"+"Nombre".ljust(10))
        print("-"*120)
    
    def show_asiento_midder(self):
        print("-"*120)
    
    def show_asiento_footer(self):
        print("*"*120)
    
    """
    *******************
    * Views for Salas *
    *******************
    """

    def salas_menu(self):
        print("***********************")
        print("* -- Submenu Salas -- *")
        print("***********************")
        print("1. Crear sala")
        print("2. Mostrar sala")
        print("3. Mostrar todas los salas")
        print("4. Actualizar sala")
        print("5. Borrar sala")
        print("6. Regresar")

    def show_a_sala(self,record):
        print(f'{record[0]:<10}|{record[1]:<6}')

    def show_sala_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(10)+"|"+"Asientos".ljust(6))
        print("-"*120)
    
    def show_sala_midder(self):
        print("-"*120)
    
    def show_sala_footer(self):
        print("*"*120)
    
    """
    *******************
    * Views for Usuarios *
    *******************
    """

    def usuario_menu(self):
        print("***************************")
        print("* -- Submenu Usuarios -- *")
        print("***************************")
        print("1. Crear usuario")
        print("2. Mostrar usuario")
        print("3. Mostrar todas los usuarios")
        print("4. Actualizar usuario")
        print("5. Borrar usuario")
        print("6. Regresar")

    def show_a_usuario(self,record):
        print(f'{record[0]:<30}|{record[1]:<20}|{record[2]:<10}|{record[3]:<20}|{record[4]:<20}|{record[5]:20}|{record[6]:<10}')

    def show_usuario_header(self,header):
        print(header.center(135,"*"))
        print("Id".ljust(30)+"|"+"Clave".ljust(20)+"|"+"Tipo".ljust(10)+"|"+"Nombre".ljust(20)+"|"+"A.Paterno".ljust(20)+"|"+"A.Materno".ljust(20)+"|"+"Telefono".ljust(10))
        print("-"*135)
    
    def show_usuario_midder(self):
        print("-"*135)
    
    def show_usuario_footer(self):
        print("*"*135)

    """
    *******************
    * Views for Boletos *
    *******************
    """

    def boleto_menu(self):
        print("***************************")
        print("* -- Submenu boletos -- *")
        print("***************************")
        print("1. ---------------")
        print("2. Mostrar boleto")
        print("3. Mostrar todas los boletos")
        print("4. ---------------")
        print("5. ---------------")
        print("6. Regresar")

    def show_a_boleto(self,record):
        print(f'{record[0]:<10}|{record[1]:<10}|{record[2]:<10}|{record[3]:<10}|{record[4]:<20}')

    def show_boleto_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(10)+"|"+"Funcion".ljust(10)+"|"+"Asiento".ljust(10)+"|"+"Disponible".ljust(10)+"|"+"Precio".ljust(10))
        print("-"*120)
    
    def show_boleto_midder(self):
        print("-"*120)
    
    def show_boleto_footer(self):
        print("*"*120)


    """
    *******************
    * Views for Compras *
    *******************
    """

    def compra_menu(self):
        print("***************************")
        print("* -- Submenu compras -- *")
        print("***************************")
        print("1. ---------------")
        print("2. Mostrar compra")
        print("3. Mostrar todas los compras")
        print("4. ---------------")
        print("5. ---------------")
        print("6. Regresar")

    def show_a_compra(self,record):
        print(f'{record[0]:<10}|{record[1]:<20}|{record[2]:<10}|{record[3]}|{record[4]:<10}')

    def show_compra_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(10)+"|"+"Usuario".ljust(20)+"|"+"Cantidad".ljust(10)+"|"+"Fecha".ljust(20)+"|"+"Total".ljust(10))
        print("-"*120)
    
    def show_compra_midder(self):
        print("-"*120)
    
    def show_compra_footer(self):
        print("*"*120)

class ViewUser:

    def main_menu(self,usuario):
        print("**************************************")
        print("* -- Hola Usuario! "+usuario[3]+" -- *")
        print("* -- Menu Principal -- *")
        print("**************************************")
        print("1. Ver Funciones de la Cartelera")
        print("2. Comprar Boletos")
        print("3. Mis Compras")
        print("4. Mis Datos")
        print("5. Mis Boletos")
        print("6. Salir")

    """
    ***************************
    * Views for Ver Funciones *
    ***************************
    """
    '''
    def funciones_menu(self):
        print("************************")
        print("* -- Ver  Funciones -- *")
        print("************************")
        print("1. Mostrar todas las Funciones de la cartelera")
        print("3. Mis Boletos")
        print("4. Regresar")
    '''
    def show_a_funcion(self,record):
        print(f'{record[0]:<6} |{record[1]:<15}|{record[2]:<10}|{record[3]}')

    def show_funcion_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(6)+"|"+"Pelicula".ljust(15)+"|"+"Sala".ljust(10)+"|"+"Inicio".ljust(20))
        print("-"*120)
    
    def show_funcion_midder(self):
        print("-"*120)
    
    def show_funcion_footer(self):
        print("*"*120)

    """
    *****************************
    * Views for Comprar Boletos *
    *****************************
    """
    def show_a_boleto(self,record):
        print(f'{record[0]:<10}|{record[1]:<20} |{record[2]:<10}|{record[3]}|{record[4]:<6}|{record[5]:<8}|{record[6]:<10}')

    def show_boleto_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(10)+"|"+"Pelicula".ljust(20)+"|"+"Sala".ljust(10)+"|"+"Inicio".ljust(20)+"|"+"Lugar".ljust(6)+"|"+"Precio".ljust(8)+"|"+"Id Compra".ljust(10))
        print("-"*120)
    
    def show_boleto_midder(self):
        print("-"*120)
    
    def show_boleto_footer(self):
        print("*"*120)

    """
    *******************
    * Views for Compras *
    *******************
    """
    '''
    def compra_menu(self):
        print("***************************")
        print("* -- Submenu compras -- *")
        print("***************************")
        print("1. ---------------")
        print("2. Mostrar compra")
        print("3. Mostrar todas los compras")
        print("4. ---------------")
        print("5. ---------------")
        print("6. Regresar")
    '''
    def show_a_compra(self,record):
        print(f'{record[0]:<10}|{record[2]:<10}|{record[3]}|{record[4]:<10}')

    def show_compra_header(self,header):
        print(header.center(120,"*"))
        print("Id".ljust(10)+"|""Cantidad".ljust(10)+"|"+"Fecha".ljust(20)+"|"+"Total".ljust(10))
        print("-"*120)
    
    def show_compra_midder(self):
        print("-"*120)
    
    def show_compra_footer(self):
        print("*"*120)

    """
    ******************************
    * Views for Compras-Detalles *
    ******************************
    """
    
    def show_a_compra_detalle(self,record):
        print(f'{record[0]:<10}|{record[2]:<10}')

    def show_compra_detalle_header(self,header):
        print(header.center(120,"*"))
        print("Id Compra".ljust(10)+"|""Id Boleto".ljust(10))
        print("-"*120)
    
    def show_compra_detalle_midder(self):
        print("-"*120)
    
    def show_compra_detalle_footer(self):
        print("*"*120)

