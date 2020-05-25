from interpreter.runtime.logo_ast import *
from interpreter.runtime.logo_ast_visitor import ASTVisitor


class Interpreter(ASTVisitor):
    def __init__(self, environment):
        self.environment = environment

    def execute(self, program: PROGRAM):
        program.accept(self)

    def visitProgram(self, program: PROGRAM):
        for cmd in program.cmds:
            self.visit(cmd)

    def visitFD(self, fd: FD):
        self.environment.turtle.move(self.visit(fd.amount))

    def visitRT(self, rt: RT):
        self.environment.turtle.rotate(self.visit(rt.amount))

    def visitAdd(self, add: Add):
        return self.visit(add.left) + self.visit(add.right)

    def visitSub(self, sub: Sub):
        return self.visit(sub.left) - self.visit(sub.right)

    def visitMul(self, mul: Mul):
        return self.visit(mul.left) * self.visit(mul.right)

    def visitDiv(self, div: Div):
        return self.visit(div.left) / self.visit(div.right)

    def visitNumber(self, number: NUMBER):
        return number.value
