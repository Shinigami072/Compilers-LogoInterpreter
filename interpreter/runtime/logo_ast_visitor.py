from abc import ABC

from interpreter.runtime.logo_ast import PROGRAM, EXPRESION, CMD, BINOP, Sub, Add, Mul, Div, NUMBER, NoArg, OneArg


class ASTVisitor:
    def visit(self, ast):
        if ast is None:
            return None
        return ast.accept(self)

    def visitProgram(self, program: PROGRAM):
        pass

    def visitExpression(self, expression: EXPRESION):
        pass

    def visitCMD(self, cmd: CMD):
        pass

    def visitBINOP(self, binop: BINOP):
        pass

    def visitSub(self, sub: Sub):
        pass

    def visitAdd(self, add: Add):
        pass

    def visitMul(self, mul: Mul):
        pass

    def visitDiv(self, div: Div):
        pass

    def visitNumber(self, number: NUMBER):
        pass
