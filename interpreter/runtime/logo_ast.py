from enum import Enum
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


class COMMAND(Enum):
    CUSTOM = 1,
    TURTLE_MOVE = 2,
    TURTLE_ROTATE = 4,
    TURTLE_VISIBILITY = 8,
    TURTLE_XY = 9,
    CLEAR_SCREEN = 16,
    HOME = 32
    PEN = 64


class CMD(AST):
    def __init__(self, cmd: COMMAND, arguments: List[EXPRESION]):
        self.cmd = cmd
        self.argument_count = len(arguments)
        self.arguments = arguments

    def accept(self, visitor):
        return visitor.visitCMD(self)

    def __str__(self):
        return "CMD %s %s" % (self.cmd, self.arguments)

    def __repr__(self):
        return self.__str__()


class NoArg(CMD):
    def __init__(self, cmd):
        super().__init__(cmd, [])


class PEN(NoArg):
    def __init__(self, status: bool):
        super().__init__(COMMAND.PEN)
        self.status = status


class Visibility(NoArg):
    def __init__(self, status: bool):
        super().__init__(COMMAND.TURTLE_VISIBILITY)
        self.status = status


class OneArg(CMD):
    def __init__(self, cmd, arg: EXPRESION):
        super().__init__(cmd, [arg])
        self.first = arg


class TwoArg(CMD):
    def __init__(self, cmd, arg1: EXPRESION, arg2: EXPRESION):
        super().__init__(cmd, [arg1, arg2])
        self.first = arg1
        self.second = arg2


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


class NEG(EXPRESION):
    def __init__(self, value: EXPRESION):
        self.value = value

    def accept(self, visitor):
        super().accept(visitor)
        return visitor.visitNeg(self)

    def __str__(self):
        return "-(%s)" % self.value


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
