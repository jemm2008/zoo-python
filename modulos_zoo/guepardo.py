from .animmal import Animmal
################################################################
class Guepardo(Animmal):
    def __init__(self, namein, agein, healthin = 83, happinessin = 75, hungryin = 60):
        super().__init__(namein, agein, healthin,happinessin)
        self.hungry = hungryin

    def __str__(self):
        return (f"""Hambre:    {self.hungry}. (si es menor a 45,   !!! _ ESTA MUY HAMBRIENTO _ !!!
========================================E.N.D.\n""")