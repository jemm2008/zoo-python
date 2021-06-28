from .animmal import Animmal
################################################################
class Elephant(Animmal):
    def __init__(self, namein, agein, healthin = 120, happinessin = 65, weightin = 4500, iqqin = "Very Smart_!!"):
        super().__init__(namein, agein, healthin, happinessin)
        self.weight = weightin
        self.iqq = iqqin

    def __str__(self):
        return (f"""Peso:      {self.weight} Kg.
inteligencia:  {self.iqq}.
=======================================E.N.D.\n""")