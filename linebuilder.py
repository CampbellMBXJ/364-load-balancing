"""
LineBuilder class for generating line outputs
"""

from operandutil import *

class LineBuilder:
    def __init__(self):
        """Initilisies an empty string"""
        self.line = ""

    def __str__(self):
        """returns line ot print"""
        return self.line

    def label(self, label):
        """Adds label to line string"""
        self.white_space()
        self.line += f"{label}:"
        return self

    def operand(self, operand):
        """Adds an operand without any operator"""
        self.white_space()
        self.line += str(operand)
        return self

    def add(self, operand):
        """Adds a plus operator and an operand"""
        self.white_space()
        #if there is no operands yet, add  just the operand
        if self.line == "" or self.line[-2:] == ": ":
            self.line += f"{str(operand)}"
            return self

        self.line += f"+ {str(operand)}"
        return self

    def sub(self, operand):
        """Adds a subtraction operator and an operand"""
        self.white_space()
        #if there is no operands yet, add  just the operand
        if self.line == "" or self.line[-2:] == ": ":
            self.line += f"{str(operand)}"
            return self
        self.line += f"- {str(operand)}"
        return self
    
    def equals(self, operand):
        """Adds a equals operator and an operand"""
        self.white_space()
        self.line += f"= {str(operand)}"
        return self

    def less_equals(self, operand):
        """Adds a less then or equals operator and an operand"""
        self.white_space()
        self.line += f"<= {str(operand)}"
        return self

    def tab(self):
        """Adds a tab (four spaces)"""
        self.line += "    "
        return self

    def header(self, header):
        """Sets line to a header string"""
        self.line = header
        return self

    def white_space(self):
        """Adds white space if it is not the begining of the line"""
        if self.line == "" or self.line[-1] == " ":
            #start of line or already whitespace, no white space needed
            return
        self.line += " "