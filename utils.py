def old_xnor_to_cnf(a, b):
    # Retuens list of cnf clauses
    clauses = []
    clauses.append([-a, b])
    clauses.append([a, -b])
    return clauses


def old_xor_to_cnf(a, b):
    # Retuens list of cnf clauses
    clauses = []
    clauses.append([-a, -b])
    clauses.append([a, b])
    return clauses


def xnor_to_cnf(a, b):
    # Retuens list of cnf clauses
    clauses = []
    clauses.append([-a, b])
    clauses.append([a, -b])
    return clauses


def xor_to_cnf(a, b):
    # Retuens list of cnf clauses
    clauses = []
    clauses.append([-a, -b])
    clauses.append([a, b])
    return clauses
