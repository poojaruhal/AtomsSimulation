import numpy as np
from Atom import Atom
from Atoms import Atoms

barium = Atom('Barium', [0.1, 0.0, 0.0])
titanium = Atom('Titanium', [0.0, 0.0, 0.3])
print(barium)
print(titanium)

d = 1.10
molecule = Atoms('2B', positions=[(0., 0., 0.), (0., 0., d)])
print(molecule)

titaniumMolecule = Atoms('Bati', atoms=[barium, titanium])
print(titaniumMolecule)

