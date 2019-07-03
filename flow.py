"""
Flow class for constructin individual flow constraints
"""

from linebuilder import *

class Flow(LineBuilder):
    DF = "df"
    PATH_LIMIT = 2
    EQUALS = 0
    def __init__(self):
        """Constructer"""
        super(Flow, self).__init__()

    def create_constraint(self, sn, tn, dn):
        """Builds constraint for given nodes"""
        self.tab().label(f"{self.DF}{sn}{tn}{dn}")
        flow_op = create_flow(sn, tn, dn)
        flag_op = create_flag(sn, tn, dn)
        demand_flow = self.calc_df(sn, dn)
        self.operand(self.PATH_LIMIT).operand(flow_op).sub(demand_flow).operand(flag_op).equals(self.EQUALS)

    def calc_df(self, sn, dn):
        """Calculates demand volume"""
        return 2 * sn + dn