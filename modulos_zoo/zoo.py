from .animmal import Animmal
from .guepardo import Guepardo
from .gacela import Gacela
from .elefante import Elephant
################################################################
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animales = []

    #def  add_animal(self):
    #    pass

    def add_guepardo(self, nombre, edad):
        self.animales.append(Guepardo(nombre, edad))
        return self

    def add_gacela(self, name, edad):
        self.animales.append( Gacela(name, edad) )
        return self

    def add_elefante(self, name, edad):
        self.animales.append(Elephant(name, edad))
        return self

    def print_all_info(self):
        print("-"*30, self.zoo_name, "-"*30)
        for animal in self.animales:
            Animmal.animmal_info(animal)

    def feed_allzoo(self):
        print("Todo el SERENGUETI Comiendooo!!")
        for animal in self.animales:
            Animmal.hora_de_comer(animal)