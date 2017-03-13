import pycosat

from utils import xnor_to_cnf, xor_to_cnf


class IsingTrivial():
    """ We try to calculate the number of states that have exactly maximum energy
    """

    def __init__(self):
        n = 4
        d = 2
        self.n = n
        self.d = d

        self.all_points = range(1, n**d + 1)
        self.all_clauses = []

        # For each point
        # For each row
        for k in range(0, n):
            i = k * n
            line = self.all_points[i:i + n]
            for j in range(len(line)):
                self.add_clause(line[j], line[(j + 1) % len(line)])
        # For each column
            for k in range(0, n):
                line = self.all_points[k:n**d:n]
                for j in range(len(line)):
                    self.add_clause(line[j], line[(j + 1) % len(line)])

    def add_clause(self, a, b):
        self.all_clauses += xnor_to_cnf(a, b)

    def map_point_coord_to_number(self, x, y):
        """ y - rzad
            x - columna
        """
        return self.n * y + x

    def map_edge_coord_to_number(self, x, y, dir):
        """ y - rzad
            x - columna
        """
        return self.n * y + x + (dir + 1) * (len(self.all_points))

    def printout_clauses(self):
        for clause in self.all_clauses:
            print clause

    def solve(self):
        return pycosat.solve(self.all_clauses)

    def itersolve(self):
        return pycosat.itersolve(self.all_clauses)

ising = IsingTrivial()
for i in list(ising.itersolve()):
    print i

print ising.map_edge_coord_to_number(0, 0, True)
