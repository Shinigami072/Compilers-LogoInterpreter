from typing import List

class AST:
    def accept(self, visitor):
        pass


class PROGRAM(AST):
    def __init__(self, cmds):
        self.cmds = cmds

    def __str__(self):
        return "Program( %s )" % self.cmds

    def __repr__(self):
        return self.__str__()

    def accept(self, visitor):
        return visitor.visitProgram(self)


class EXPRESION(AST):
    def accept(self, visitor):
        return visitor.visitExpression(self)


class CMD(AST):
    def __init__(self, cmd, arguments: List[EXPRESION]):
        self.cmd = cmd
        self.token = cmd
        self.arguments = arguments

    def accept(self, visitor):
        return visitor.visitCMD(self)

    def __str__(self):
        return "CMD %s %s %s" % (self.cmd, self.token, self.arguments)

    def __repr__(self):
        return self.__str__()


class FD(CMD):
    def __init__(self, ammount: EXPRESION):
        super().__init__("FD", [ammount])
        self.amount = ammount

    def __str__(self):
        return "FD %s" % self.amount

    def __repr__(self):
        return self.__str__()

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitFD(self)


class RT(CMD):
    def __init__(self, ammount: EXPRESION):
        super().__init__("RT", [ammount])
        self.amount = ammount

    def __str__(self):
        return "RT %s" % self.amount

    def __repr__(self):
        return self.__str__()

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitRT(self)


class BINOP(EXPRESION):
    def __init__(self, left: EXPRESION, op, right: EXPRESION):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return "[<%s> %s <%s>]" % (self.left, self.op, self.right)

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitBINOP(self)


class Sub(BINOP):
    def __init__(self, left: EXPRESION, right: EXPRESION):
        super().__init__(left, '-', right)

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitSub(self)


class Add(BINOP):
    def __init__(self, left: EXPRESION, right: EXPRESION):
        super().__init__(left, '+', right)

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitAdd(self)


class Mul(BINOP):
    def __init__(self, left: EXPRESION, right: EXPRESION):
        super().__init__(left, '*', right)

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitMul(self)


class Div(BINOP):
    def __init__(self, left: EXPRESION, right: EXPRESION):
        super().__init__(left, '/', right)

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitDiv(self)


class NUMBER(EXPRESION):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "NUMBER(%s)" % self.value

    def __repr__(self):
        return self.__str__()

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitNumber(self)
