"""Binary class for constructin individual binaries
"""

from linebuilder import *

class Binary(LineBuilder):
    EQUALS = 0
    def __init__(self):
        """Constructer"""
        super(Binary, self).__init__()

    def create_constraint_flow(self, sn, tn, dn):
        """Builds Binaries for given nodes"""
        flow_op = create_flag(sn, tn, dn)
        self.tab().operand(flow_op)
    