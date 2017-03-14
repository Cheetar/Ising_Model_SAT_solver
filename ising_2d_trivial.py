import pycosat

from utils import xnor_to_cnf_edge, xor_to_cnf_edge


class IsingTrivial():
    """ We try to calculate the number of states that have exactly maximum energy
    """

    def __init__(self):
        n = 4
        d = 2
        self.n = n
        self.d = d

        self.all_points = range(1, n**d+1)
        self.all_clauses = []

        # For each point
        # For each row
        for k in range(0, n):
            i = k * n
            line = self.all_points[i:i + n]
            for j in range(len(line)):
                self.add_clause(line[j], line[(j + 1) % len(line)], self.map_edge_coord_to_number(j,k,False))
                #print line[j]
                #print line[(j + 1) % len(line)]
                #print self.map_edge_coord_to_number(j,k,False)
                #print "\n"
        # For each column
        for k in range(0, n):
            line = self.all_points[k:n**d:n]
            for j in range(len(line)):
                self.add_clause(line[j], line[(j + 1) % len(line)], self.map_edge_coord_to_number(k,(line[j]-k)/self.n,True))
                #print line[j]
                #print line[(j + 1) % len(line)]
                #print self.map_edge_coord_to_number(k,(line[j]-k)/self.n,True)
                #print "\n"

    def add_clause(self, a, b, c):
        self.all_clauses += xnor_to_cnf_edge(a, b, c)

    def add_clause_end(self):
        for a in range(17,49):
            self.all_clauses += [[a]]

    def map_point_coord_to_number(self, x, y):
        """ y - rzad
            x - columna
        """
        return self.n * y + x

    def map_edge_coord_to_number(self, x, y, dir):
        """ y - rzad
            x - columna
        """
        return self.n * y + x + (dir + 1) * (len(self.all_points)) + 1

    def printout_clauses(self):
        for clause in self.all_clauses:
            print clause

    def solve(self):
        return pycosat.solve(self.all_clauses)

    def itersolve(self):
        return pycosat.itersolve(self.all_clauses)
    
ising = IsingTrivial()
ising.add_clause_end()
# print ising.map_edge_coord_to_number(1, 5, True)


for i in list(ising.itersolve()):
   print i

#ising.printout_clauses()

