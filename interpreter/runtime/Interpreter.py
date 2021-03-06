from interpreter.runtime.Model import Var
from interpreter.runtime.logo_ast import *
from interpreter.runtime.logo_ast_visitor import ASTVisitor

REPCOUNT = "REPCOUNT"


class Interpreter(ASTVisitor):
    def __init__(self, environment):
        self.environment = environment
        self.environment.insert(Var(REPCOUNT, Type.NUMBER, -1))

    def execute(self, program: Block):
        program.accept(self)

    def visitRepeat(self, repeat: Repeat):
        n = round(self.visit(repeat.n))
        self.environment.push_scope("Repeat")
        for i in range(n):
            self.environment.insert(Var(REPCOUNT, Type.NUMBER, i))
            self.visit(repeat.block)
        self.environment.pop_scope()

    def visitAssign(self, assign: Assign):
        self.environment.insert(
            Var(assign.name, assign.value.type, self.visit(assign.value))
        )

    def visitFor(self, for_e: For):
        from_v = self.visit(for_e.from_v)
        to_v = self.visit(for_e.to_v)
        step_v = self.visit(for_e.step_v)

        if from_v > to_v and step_v > 0:
            raise ValueError("From value greater than to value with positive step")

        if from_v < to_v and step_v < 0:
            raise ValueError("From value less than to value with negative step")

        if step_v == 0:
            raise ValueError("Step Equal to 0")

        self.environment.push_scope("For")
        for i in [from_v + x * step_v for x in range(round((to_v - from_v) / step_v))]:
            self.environment.insert(Var(for_e.name, Type.NUMBER, i))
            self.visit(for_e.block)
        self.environment.pop_scope()

    def visitIf(self, if_e: If):
        if self.visit(if_e.condition):
            self.environment.push_scope("If")
            self.visit(if_e.block)
            self.environment.pop_scope()

    def visitBlock(self, block: Block):
        for cmd in block.statements:
            self.visit(cmd)

    def pen(self, pen: PEN):
        if pen.status:
            self.environment.turtle.move_pencil_down()
        else:
            self.environment.turtle.move_pencil_up()

    def visitConstant(self, constant: Constant):
        return constant.value

    def visitVariable(self, var: Variable):
        got = self.environment.lookup(var.name)
        if got is None:
            raise ValueError("variable undefined")

        if var.type != Type.UNKNOWN and got.type != var.type:
            raise ValueError("variable %s is %s expected %s" % (var.name, got.type, var.type))

        return got.value

    def visitNumberUnaryOperator(self, number: NumberUnaryOperator):
        if number.operator == NumberUnaryOperator.Operator.Neg.value:
            return -self.visit(number.expression)
        else:
            raise ValueError("Unknown Operator")

    def visitComparison(self, comparison: Comparison):
        left = self.visit(comparison.left)
        right = self.visit(comparison.right)

        if comparison.operator == Comparison.Operator.Equal.value:
            return left == right
        elif comparison.operator == Comparison.Operator.Less.value:
            return left < right
        elif comparison.operator == Comparison.Operator.More.value:
            return left > right
        else:
            raise ValueError("Unknown Operator")

    def visitNumberBinaryOperator(self, number: NumberBinaryOperator):
        left = self.visit(number.left)
        right = self.visit(number.right)

        if number.operator == NumberBinaryOperator.Operator.Div.value:
            return left / right
        elif number.operator == NumberBinaryOperator.Operator.Mul.value:
            return left * right
        elif number.operator == NumberBinaryOperator.Operator.Add.value:
            return left + right
        elif number.operator == NumberBinaryOperator.Operator.Sub.value:
            return left - right
        else:
            raise ValueError("Unknown Operator")

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

    def visitPRINT(self, node: PRINT):
        print(str(self.visit(node.value)))
        return None
