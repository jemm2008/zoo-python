class Animmal: 
    def __init__(self, namein, agein, healthin, happinessin):
        self.name = namein
        self.age = agein
        self.health = healthin
        self.happiness = happinessin

    def animmal_info(self):
        print(f"""
=============================================
Nombre:    {self.name}.
Edad:      {self.age}.
Salud:     {self.health}.
Felicidad: {self.happiness}.""")
        print(self.__str__())
        return self

    def hora_de_comer(self):
        if self.health > 79: self.health += 10
        if self.health < 80 and type(self).__name__ == "Guepardo": self.health += 17
        if self.health < 80 and type(self).__name__ == "Gacela": self.health += 23
        if self.health < 80 and type(self).__name__ == "Elephant": self.health += 19
        if self.happiness > 79: self.happiness += 10
        if self.happiness < 80 and type(self).__name__ == "Guepardo": self.happiness += 17
        if self.happiness < 80 and type(self).__name__ == "Gacela": self.happiness -= 11
        if self.happiness < 80 and type(self).__name__ == "Elephant": self.happiness += 31
        return self