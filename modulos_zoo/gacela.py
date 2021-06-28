from .animmal import Animmal
################################################################
class Gacela(Animmal):
    def __init__(self, namein, agein, healthin = 80, happinessin = 77 , speed = 65):
        super().__init__(namein, agein, healthin,happinessin)
        self.speed = speed

    def __str__(self):
        return (f"""Velocidad: {self.speed} Km/h.
=======================================E.N.D.\n""")