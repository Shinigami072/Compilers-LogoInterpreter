from enum import Enum
from typing import List


class Statement:

    def accept(self, visitor):
        cls = self.__class__
        func_name = "visit" + cls.__name__

        while not hasattr(visitor, func_name):
            cls = cls.__base__

            if cls == type(Statement) or cls is None:
                raise NotImplementedError("No Handler registered for %s" % self)

            func_name = "visit" + cls.__name__

        method = visitor.__getattribute__(func_name)

        if callable(method):
            return method(self)

        raise NotImplementedError("No Handler registered")

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return self.__class__.__name__


class Type(Enum):
    NUMBER = float,
    STRING = str,
    BOOLEAN = bool


class Expression(Statement):
    def __init__(self, expr_type: Type):
        self.type = expr_type

    def __str__(self):
        return "E(%s)" % self.type

    def __repr__(self):
        return self.__str__()


class Constant(Expression):
    def __init__(self, expr_type: Type, value):
        super().__init__(expr_type)
        self.value = value

    def __str__(self):
        return "C(%s,%s)" % (self.type, self.value)

    def __repr__(self):
        return self.__str__()


class UnaryOperator(Expression):
    def __init__(self, expr_type: Type, operator: str, expression: Expression):
        super().__init__(expr_type)
        self.operator = operator
        self.expression = expression

    def __str__(self):
        return "O[%s](%s,%s)" % (self.operator, self.type, self.expression)


class BinaryOperator(Expression):
    def __init__(self, expr_type: Type, operator: str, left: Expression, right: Expression):
        super().__init__(expr_type)
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        return "O(%s,%s %s %s)" % (self.type, self.left, self.operator, self.right)


class Variable(Expression):
    def __init__(self, expr_type: Type, name: str):
        super().__init__(expr_type)
        self.name = name

    def __str__(self):
        return "V(%s,%s)" % (self.type, self.name)


class FunctionCall(Expression):
    def __init__(self, expr_type: Type, name: str, arguments: List[Expression]):
        super().__init__(expr_type)
        self.name = name
        self.arguments = arguments

    def __str__(self):
        return "F(%s,%s,[%s])" % (self.type, self.name, self.arguments)


class BooleanConstant(Constant):
    def __init__(self, value: bool):
        super().__init__(Type.BOOLEAN, value)
        self.value: bool


class StringConstant(Constant):
    def __init__(self, value: str):
        super().__init__(Type.STRING, value)
        self.value: str


class NumberConstant(Constant):
    def __init__(self, value: float):
        super().__init__(Type.NUMBER, value)
        self.value: float


class NumberUnaryOperator(UnaryOperator):
    class Operator(Enum):
        Neg = "-"

    def __init__(self, operator: Operator, expression: Expression):
        if expression.type != Type.NUMBER:
            raise ValueError(expression, "Expected a number Expression")
        super().__init__(Type.NUMBER, operator.value, expression)


class NumberBinaryOperator(BinaryOperator):
    class Operator(Enum):
        Mul = "*",
        Div = "/",
        Sub = "-",
        Add = "+"

    def __init__(self, operator: Operator, left: Expression, right: Expression):
        if left.type != Type.NUMBER:
            raise ValueError(left, "Expected a number expression")

        if right.type != Type.NUMBER:
            raise ValueError(right, "Expected a number expression")

        super().__init__(Type.NUMBER, operator.value, left, right)


class Comparison(BinaryOperator):
    class Operator(Enum):
        Less = "<",
        More = ">",
        Equal = "=",

    def __init__(self, operator: Operator, left: Expression, right: Expression):
        if left.type != Type.NUMBER:
            raise ValueError(left, "Expected a number expression")

        if right.type != Type.NUMBER:
            raise ValueError(right, "Expected a number expression")

        super().__init__(Type.BOOLEAN, operator.value, left, right)


class COMMAND(Enum):
    CUSTOM = 1,
    TURTLE_MOVE = 2,
    TURTLE_ROTATE = 4,
    TURTLE_VISIBILITY = 8,
    TURTLE_XY = 9,
    CLEAR_SCREEN = 16,
    HOME = 32
    PEN = 64


class CMD(Statement):
    def __init__(self, cmd: COMMAND, arguments: List[Expression]):
        self.cmd = cmd
        self.argument_count = len(arguments)
        self.arguments = arguments

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
    def __init__(self, cmd, arg: Expression):
        super().__init__(cmd, [arg])
        self.first = arg


class TwoArg(CMD):
    def __init__(self, cmd, arg1: Expression, arg2: Expression):
        super().__init__(cmd, [arg1, arg2])
        self.first = arg1
        self.second = arg2


class PRINT(Statement):
    def __init__(self, value: Expression):
        self.value = value


class Block(Statement):
    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def __str__(self):
        return "[\n" + "\n".join([str(s) for s in self.statements]) + "\n]"

    def __repr__(self):
        return self.__str__()


class Repeat(Statement):
    def __init__(self, n: int, block: Block):
        super().__init__()
        self.n = n
        self.block = block

    def __str__(self):
        return "REPEAT(%d)\n%s" % (self.n, self.block)

    def __repr__(self):
        return self.__str__()


class If(Statement):
    def __init__(self, condition: Expression, block: Block):
        super().__init__()

        if condition.type != Type.BOOLEAN:
            raise ValueError("Boolean expresion expected")

        self.condition = condition
        self.block = block

    def __str__(self):
        return "IF(%s)\n%s" % (self.condition, self.block)

    def __repr__(self):
        return self.__str__()
