import pycosat

from to_cnf import *


class IsingTrivial():
    """ We try to calculate the number of states that have exactly maximum energy
    """

    def __init__(self):
        n = 2
        d = 2
        k = 2
        self.n = n
        self.d = d
        self.k = k

        self.all_points = range(1, n**d + 1)
        self.all_edges = range(n**d + 1, 3 * (n**d) + 1)
        self.all_clauses = []

        self.add_edges_clauses()
        # self.set_all_edges_true()
        self.add_counter_clasues()

    def add_clause(self, a, b, c):
        self.all_clauses += xnor_to_cnf_edge(a, b, c)

    def add_edges_clauses(self):
        n = self.n
        # For each point
        for a in range(n):
            for b in range(n):
                self.add_clause(self.map_point_coord(a, b), self.map_point_coord((a + 1) % n, b),
                                self.map_edge_coord(a, b, False))
                self.add_clause(self.map_point_coord(a, b), self.map_point_coord(a, (b + 1) % n),
                                self.map_edge_coord(a, b, True))

    '''def set_all_edges_true(self):
        for edge in self.all_edges:
            self.all_clauses += [[edge]]'''

    def add_counter_clasues(self):
        # 1
        # For each edge
        for i in range(self.n**self.d + 1, 3 * self.n**self.d + 1):
            # i - absolute edge number
            self.all_clauses += one_to_cnf(i,
                                           self.map_register(i - self.n**self.d, 1))

        # 2
        for j in range(2, self.k + 1):
            self.all_clauses += two_to_cnf(self.map_register(1, j))

        # 3
        for i in range(2, 2 * self.n**self.d):
            for j in range(1, self.k + 1):
                self.all_clauses += three_to_cnf(
                    self.map_register(i - 1, j), self.map_register(i, j))

        # 4
        for i in range(2,  2 * self.n**self.d):
            for j in range(2, self.k + 1):
                edge_i = i + self.n**self.d
                self.all_clauses += four_to_cnf(edge_i,
                                                self.map_register(i - 1, j - 1), self.map_register(i, j))

        # 5
        for i in range(1,  2 * self.n**self.d + 1):
            edge_i = i + self.n**self.d
            self.all_clauses += five_to_cnf(edge_i,
                                            self.map_register(i - 1, self.k))

    # Mappers
    def map_point_coord(self, x, y):
        """ y - rzad
            x - columna
        """
        return self.n * y + x + 1

    def map_edge_coord(self, x, y, dir):
        """ y - rzad
            x - columna
        """
        return self.n * y + x + (dir + 1) * (len(self.all_points)) + 1

    def map_register(self, i, j):
        return 3 * self.n**self.d + (j - 1) * self.n + i + 1

    # for debugging pupuses

    def set_k(self, k):
        self.k = k

    def printout_clauses(self):
        for clause in self.all_clauses:
            print clause

    def solve(self):
        return pycosat.solve(self.all_clauses)

    def itersolve(self):
        return pycosat.itersolve(self.all_clauses)


ising = IsingTrivial()
ising.printout_clauses()

# ising.add_clause_end()
# print ising.map_edge_coord(1, 5, True)

print '\n'

for i in list(ising.itersolve()):
    print i

print len(list(ising.itersolve()))

# print ising.all_edges
