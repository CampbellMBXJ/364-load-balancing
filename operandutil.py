"""
Module of functions for generating var names
"""
MIN_VAR = "r"
FLOW_VAR = "x"
FLAG_VAR = "u"
CAP_SOURCE_VAR = "c"
CAP_DEST_VAR = "d"

def create_flow(sn, tn, dn):
    """Creates a operand name for given flow"""
    return f"{FLOW_VAR}{sn}{tn}{dn}"

def create_min():
    """Creates operand to be minimized"""
    return MIN_VAR

def create_capacity(xn, yn, is_source):
    """Creates operand for capacity"""
    if is_source:
        return f"{CAP_SOURCE_VAR}{xn}{yn}"
    else:
        return f"{CAP_DEST_VAR}{xn}{yn}"

def create_flag(sn, tn, dn):
    """Creates a operand name for given flow"""
    return f"{FLAG_VAR}{sn}{tn}{dn}"