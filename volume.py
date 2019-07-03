"""
volume class for constructin individual volume constraints
"""

from linebuilder import *

class Volume(LineBuilder):
    DV = "dv"
    def __init__(self, n_transit_nodes):
        """Constructer"""
        super(Volume, self).__init__()
        self.n_transit_nodes = n_transit_nodes

    def create_constraint(self, sn, dn):
        """Builds constraint for given nodes"""
        self.tab().label(f"{self.DV}{sn}{dn}")

        for tn in range(1, self.n_transit_nodes+1):
            flow_op = create_flow(sn,tn,dn)
            self.add(flow_op)

        demand_volume = self.calc_df(sn,dn)
        self.equals(demand_volume)

    def calc_df(self, sn, dn):
        """Calculates demand volume"""
        return 2 * sn + dn