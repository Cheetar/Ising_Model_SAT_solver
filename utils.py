def old_xnor_to_cnf(a, b):
    # Returns list of cnf clauses
    clauses = []
    clauses.append([-a, b])
    clauses.append([a, -b])
    return clauses


def old_xor_to_cnf(a, b):
    # Returns list of cnf clauses
    clauses = []
    clauses.append([-a, -b])
    clauses.append([a, b])
    return clauses


def xnor_to_cnf(a, b):
    # Returns list of cnf clauses
    clauses = []
    clauses.append([-a, b])
    clauses.append([a, -b])
    return clauses


def xor_to_cnf(a, b):
    # Returns list of cnf clauses
    clauses = []
    clauses.append([-a, -b])
    clauses.append([a, b])
    return clauses


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


def half_add_to_cnf(a, b, c, s):
    clauses = []
    clauses.append([a, -b, s])
    clauses.append([-a, -b, c])
    clauses.append([-a, b, s])
    return clauses


def add_to_cnf(a, b, cin, s, cout):
    clauses = []
    clauses.append([a, b, -cin, s])
    clauses.append([a, -b, cin, s])
    clauses.append([-a, b, cin, s])
    clauses.append([-a, -b, -cin, s])
    clauses.append([-a, -b, cout])
    clauses.append([-a, -cin, cout])
    clauses.append([-b, -cin, cout])
    return clauses
