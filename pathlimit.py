"""
PathLimit class for constructin individual path limit constraints
"""

from linebuilder import *

class PathLimit(LineBuilder):
    PL = "pl"
    PATH_LIMIT = 2
    def __init__(self, n_transit_nodes):
        """Constructer"""
        super(PathLimit, self).__init__()
        self.n_transit_nodes = n_transit_nodes

    def create_constraint(self, sn, dn):
        """Builds constraint for given nodes"""
        self.tab().label(f"{self.PL}{sn}{dn}")
        
        for tn in range(1, self.n_transit_nodes+1):
            flag_op = create_flag(sn,tn,dn)
            self.add(flag_op)

        self.equals(self.PATH_LIMIT)