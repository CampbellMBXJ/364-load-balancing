"""
Load class for constructin individual transit load constraints
"""

from linebuilder import *

class Load(LineBuilder):
    TLOAD = "tload"
    EQUALS = 0
    def __init__(self, n_source_nodes, n_destination_nodes):
        """Constructer"""
        super(Load, self).__init__()
        self.n_source_nodes = n_source_nodes
        self.n_destination_nodes = n_destination_nodes

    def create_constraint(self, tn):
        """Builds constraint for given nodes"""
        self.tab().label(f"{self.TLOAD}{tn}")

        for sn in range(1, self.n_source_nodes+1):
            for dn in range(1, self.n_destination_nodes+1):
                flow_op = create_flow(sn,tn,dn)
                self.add(flow_op)

        self.sub(create_min()).less_equals(self.EQUALS)

    def calc_df(self, sn, dn):
        """Calculates demand volume"""
        return 2 * sn + dn