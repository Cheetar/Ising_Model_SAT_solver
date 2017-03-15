def xor_to_cnf_edge(a, b, c):
    # Returns list of cnf clauses with result
    clauses = []
    clauses.append([-a, -b, -c])
    clauses.append([a, b, -c])
    clauses.append([a, -b, c])
    clauses.append([-a, b, c])
    return clauses


def xnor_to_cnf_edge(a, b, c):
    # Returns list of cnf clauses with result
    clauses = []
    clauses.append([-a, -b, c])
    clauses.append([a, b, c])
    clauses.append([a, -b, -c])
    clauses.append([-a, b, -c])
    return clauses


def one_to_cnf(x, r):
    return [[-x, r]]


def two_to_cnf(r):
    return [[-r]]


def three_to_cnf(r1, r2):
    return [[-r1, r2]]


def four_to_cnf(x, r1, r2):
    return [[-x, -r1, r2]]


def five_to_cnf(x, r):
    return [[-x, -r]]
