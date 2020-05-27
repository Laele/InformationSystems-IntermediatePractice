#from model.model import Model

#m = Model()
#print('Ahuevo wey')

#m.create_pelicula("Avengers End-Game","B","Acción","Super Heroes Marvel luchan contra Thanos.","Luis Soriano","2:10:02")

#data = m.real_all_peliculas()
#print(data)

from controller.controller import Controller

c = Controller()
c.start()

#m.close_db()