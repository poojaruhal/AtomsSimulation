import numpy as np


class Atoms(object):
    celldisp = 0
    positions = []
    symbol = ''
    atoms = []

    def __init__(self,
                 symbol=None, atoms=None, positions: object = None, celldisp: object = None):

        if symbol is None:
            self.get_symbol()
        else:
            self.set_symbol(symbol)

        if atoms is None:
            self.get_atoms()
        else:
            self.set_atoms(atoms)

        if celldisp is None:
            self.celldisp = self.get_celldisp()
        else:
            self.set_celldisp(celldisp)

        if positions is None:
            self.positions = self.get_positions()
        else:
            self.set_positions(positions)

    def set_atoms(self, atoms):
        """Set atoms in the structure"""
        self.atoms = atoms

    def get_atoms(self):
        """get the list of atoms."""
        return self.atoms

    def set_symbol(self, symbol):
        """Set symbol"""
        self.symbol = symbol

    def get_symbol(self):
        """get the symbol of atoms."""
        return self.symbol

    def set_celldisp(self, celldisp):
        """Set the unit cell displacement vectors."""
        self.celldisp = np.array(celldisp, float)

    def get_celldisp(self):
        """Get the unit cell displacement vectors."""
        return self.celldisp

    def set_positions(self, newpositions):
        """Set positions"""
        self.positions = np.array(newpositions, float)

    def get_positions(self):
        return self.positions

    def __str__(self):
        tokens = []

        if self.atoms:
            for atom in self.atoms:
                tokens.append(atom.symbol)

        if self.positions is None:
            tokens.append()
        else:
            for position in self.positions:
                tokens.append(position)

        return str(self.get_symbol()) + ': ' + str(tokens)
