"""
Capacity class to generate cpacity constraints
"""
from linebuilder import *

class Capacity(LineBuilder):
    CAP_SOURCE = "capc"
    CAP_DEST = "capd"
    EQUALS = 0

    def  __init__(self, n_nodes, is_source = True):
        """Calls linebuilder constructer"""
        super(Capacity, self).__init__()
        self.n_nodes = n_nodes
        self.is_source = is_source


    def create_constraint(self, xn, yn):
        """Creates capacity constraint"""
        label = ""
        if self.is_source:
            label = f"{self.CAP_SOURCE}{xn}{yn}"
        else:
            label = f"{self.CAP_DEST}{xn}{yn}"
        self.tab().label(label)

        for zn in range(1, self.n_nodes+1):
            if self.is_source:
                flow_op = create_flow(xn, yn, zn)
            else:
                flow_op = create_flow(zn, xn, yn)
            self.add(flow_op)

        cap_op = create_capacity(xn, yn, self.is_source)
        self.sub(cap_op)
        self.equals(self.EQUALS)
        

        