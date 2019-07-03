"""
Bound class for constructin individual bounds
"""

from linebuilder import *

class Bound(LineBuilder):
    EQUALS = 0
    def __init__(self):
        """Constructer"""
        super(Bound, self).__init__()

    def create_constraint_flow(self, sn, tn, dn):
        """Builds Bound for given nodes"""
        flow_op = create_flow(sn, tn, dn)
        self.tab().operand(self.EQUALS).less_equals(flow_op)
    
    def create_constraint_min(self):
        """Builds bound for min equation"""
        min_op = create_min()
        self.tab().operand(self.EQUALS).less_equals(min_op)