import headers
from linebuilder import *
from volume import Volume
from capacity import Capacity
from pathlimit import PathLimit
from load import Load
from flow import Flow
from bound import Bound
from binary import Binary

class FileBuilder:
    def __init__(self, n_source_nodes, n_transit_nodes, n_destination_nodes):
        """Constructor to set the number of each node type"""
        self.n_source_nodes = int(n_source_nodes)
        self.n_transit_nodes = int(n_transit_nodes)
        self.n_destination_nodes = int(n_destination_nodes)
        self.lines = []
    
    def __str__(self):
        """Returns line to print"""
        out = ""
        for i, line in enumerate(self.lines):
            line = line.__str__()
            if i+1 == len(self.lines):
                out += line
            else:
                out += f"{line}\n"
        return out
    
    def demand_volume(self):
        """Generates lines for demand volume constraints"""
        for sn in range(1, self.n_source_nodes+1):
            for dn in range(1, self.n_destination_nodes+1):
                volume = Volume(self.n_transit_nodes)
                volume.create_constraint(sn, dn)
                self.add_line(volume)

    def demand_flow(self):
        """Generates lines for demand volume constraints"""
        for sn in range(1, self.n_source_nodes+1):
            for tn in range(1, self.n_transit_nodes+1):
                for dn in range(1, self.n_destination_nodes+1):
                    flow = Flow()
                    flow.create_constraint(sn, tn, dn)
                    self.add_line(flow)
    
    def source_capicity(self):
        """Generates capacities for links from source to transit"""
        for sn in range(1, self.n_source_nodes+1):
            for tn in range(1, self.n_transit_nodes+1):
                capacity = Capacity(self.n_destination_nodes, True)
                capacity.create_constraint(sn, tn)
                self.add_line(capacity)
    
    def dest_capicity(self):
        """Generates capacities for links from transit to destination"""
        for tn in range(1, self.n_transit_nodes+1):
            for dn in range(1, self.n_destination_nodes+1):
                capacity = Capacity(self.n_source_nodes, False)
                capacity.create_constraint(tn, dn)
                self.add_line(capacity)

    def path_limit(self):
        """Generates path limit constraints"""
        for sn in range(1, self.n_source_nodes+1):
            for dn in range(1, self.n_destination_nodes+1):
                limit = PathLimit(self.n_transit_nodes)
                limit.create_constraint(sn, dn)
                self.add_line(limit)

    def transit_load(self):
        """Generates transit loads"""
        for tn in range(1, self.n_transit_nodes+1):
            load = Load(self.n_source_nodes, self.n_destination_nodes)
            load.create_constraint(tn)
            self.add_line(load)
    
    def bound(self):
        """Generates bounds"""
        for sn in range(1, self.n_source_nodes+1):
            for tn in range(1, self.n_transit_nodes+1):
                for dn in range(1, self.n_destination_nodes+1):
                    bound = Bound()
                    bound.create_constraint_flow(sn, tn, dn)
                    self.add_line(bound)
        bound = Bound()
        bound.create_constraint_min()
        self.add_line(bound)

    def binary(self):
        """Generates binaries"""
        for sn in range(1, self.n_source_nodes+1):
            for tn in range(1, self.n_transit_nodes+1):
                for dn in range(1, self.n_destination_nodes+1):
                    binary = Binary()
                    binary.create_constraint_flow(sn, tn, dn)
                    self.add_line(binary)

    def build_minimize(self):
        """Generates lines for minimize section"""
        header = LineBuilder().header(headers.MINIMIZE)
        self.add_line(header)

        min_equation = LineBuilder().tab().operand(create_min())
        self.add_line(min_equation)

    def build_subject_to(self):
        """Generates the subject section of the lp"""
        header = LineBuilder().header(headers.SUBJECT)
        self.lines.append(header)
        
        self.demand_volume()
        self.source_capicity()
        self.dest_capicity()
        self.path_limit()
        self.demand_flow()
        self.transit_load()

    def build_bounds(self):
        """Generates Bounds section of the LP"""
        header = LineBuilder().header(headers.BOUNDS)
        self.lines.append(header)

        self.bound()

    def build_binaries(self):
        """Generates Binaries section of the LP"""
        header = LineBuilder().header(headers.BINARIES)
        self.lines.append(header)

        self.binary()

    def build_end(self):
        """generates end header of the LP"""
        header = LineBuilder().header(headers.END)
        self.lines.append(header)


    def build_lp(self):
        """Builds entire LP file"""
        self.build_minimize()
        self.build_subject_to()
        self.build_bounds()
        self.build_binaries()
        self.build_end()
                

    def add_line(self, line):
        """adds line to line array"""
        self.lines.append(line)

                


    