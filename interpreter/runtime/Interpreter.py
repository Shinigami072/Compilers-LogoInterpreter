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

    def pen(self, pen: PEN):
        if pen.status:
            self.environment.turtle.move_pencil_down()
        else:
            self.environment.turtle.move_pencil_up()

    def visible(self, visibility: Visibility):
        self.environment.turtle.visible = visibility.status

    def visitCMD(self, cmd: CMD):
        if cmd.cmd == COMMAND.TURTLE_ROTATE:
            self.environment.turtle.rotate(self.visit(cmd.arguments[0]))
        elif cmd.cmd == COMMAND.TURTLE_MOVE:
            self.environment.turtle.move(self.visit(cmd.arguments[0]))
        elif cmd.cmd == COMMAND.PEN:
            self.pen(cmd)
        elif cmd.cmd == COMMAND.HOME:
            self.environment.turtle.pos = (self.environment.width / 2, self.environment.height / 2)
            self.environment.turtle.rot = 0
        elif cmd.cmd == COMMAND.CLEAR_SCREEN:
            self.environment.turtle.clear()
        elif cmd.cmd == COMMAND.TURTLE_VISIBILITY:
            self.visible(cmd)
        elif cmd.cmd == COMMAND.TURTLE_XY:
            self.environment.turtle.move_to((self.visit(cmd.arguments[0]), self.visit(cmd.arguments[1])))

    def visitAdd(self, add: Add):
        return self.visit(add.left) + self.visit(add.right)

    def visitSub(self, sub: Sub):
        return self.visit(sub.left) - self.visit(sub.right)

    def visitMul(self, mul: Mul):
        return self.visit(mul.left) * self.visit(mul.right)

    def visitDiv(self, div: Div):
        return self.visit(div.left) / self.visit(div.right)

    def visitNeg(self, neg: NEG):
        return -self.visit(neg.value)

    def visitNumber(self, number: NUMBER):
        return number.value
