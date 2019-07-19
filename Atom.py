import numpy as np
from ase import Atoms

class Atom(object):
    symbol = ""
    position = []

    def __init__(self,
                 symbol, positions):

        self.set_positions(positions)
        self.set_symbol(symbol)


    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        self.symbol

    def set_positions(self, newpositions):
        """Set positions"""
        self.position = np.array(newpositions, float)

    def get_positions(self):
        return self.position

    def __str__(self):
        return str(self.symbol) + ' : '+str(self.position)
