from __future__ import annotations
import math
import typing

from interpreter.runtime.logo_ast import Type


class Line:
    def __init__(self):
        self.points = list()

    def add_point(self, point: typing.Tuple[float, float]):
        self.points.append(point)


class Turtle:
    def __init__(self, x: float, y: float, rot: float = 0, pencil_down=False, draw=True):
        self.pos = (x, y)
        self.rot = rot
        self.lines = [Line()]
        self.pencil_down = pencil_down
        self.draw_Robot = draw
        self.visible = True
        if pencil_down:
            self._extendLine()

    def _extendLine(self):
        self.lines[-1].add_point(self.pos)

    def clear(self):
        self.lines.clear()

        if self.pencil_down:
            self.lines.append(Line())

    def move_to(self, new_pos: typing.Tuple[float, float]):
        self.pos = new_pos

        if self.pencil_down:
            self._extendLine()

    def move(self, dist: float):
        dx = dist * math.cos(math.radians(self.rot))
        dy = dist * math.sin(math.radians(self.rot))

        x, y = self.pos
        new_pos = (x + dx, y + dy)
        self.move_to(new_pos)

    def move_pencil_down(self):
        if not self.pencil_down:
            self._extendLine()
            self.pencil_down = True

    def move_pencil_up(self):
        if self.pencil_down:
            self.pencil_down = False
            self.lines.append(Line())

    def rotate(self, deg):
        self.rot += deg
        if self.rot < 0:
            self.rot += 360

        if self.rot > 360:
            self.rot -= 360

    def __str__(self):
        return "Turtle(x=%s,y=%s,rot=%s,pen=%s)" % (
            str(round(self.pos[0])),
            str(round(self.pos[1])),
            str(round(self.rot)),
            str(self.pencil_down)
        )


class Var:
    def __init__(self, name: str, var_type: Type, value):
        self.name = name
        self.type = var_type
        self.value = value

    def __str__(self):
        return "Variable(%s,%s,%s)" % (self.name, self.type, self.value)

    def __repr__(self):
        return self.__str__()


class Function(Var):
    def __init__(self, name: str, returnType: Type, arguments: typing.List[typing.Tuple[str, Type]], value):
        super().__init__(name, Type.FUNCTION, value)
        self.returnType = returnType
        self.arguments = arguments

    def check_arguments(self, *arguments: Var):
        if len(arguments) != len(self.arguments):
            raise ValueError("Expected %d arguments got %d" % (len(self.arguments), len(arguments)))

        for i, a in enumerate(arguments):
            if self.arguments[i][1] != a.type:
                raise ValueError("Argument %s is %s not %s" % (self.arguments[i][0], self.arguments[i][1], a.type))

    def __str__(self):
        return "Function(%s,%s)" % (self.name, self.arguments)

    def __repr__(self):
        return self.__str__()


class Scope:
    def __init__(self, name: str, parent: typing.Optional["Scope"] = None):
        self.parent = parent
        self.name = name
        self.current: typing.Dict[str, Var] = {}

    def lookup(self, name: str) -> typing.Optional[Var]:
        value = self.current.get(name)
        if value is not None:
            return value
        elif self.parent is not None:
            return self.parent.lookup(name)
        else:
            return None

    def insert(self, variable: Var):
        self.current[variable.name] = variable

    def __str__(self):
        return "Scope(%s,%s)={%s}" % (self.name, self.parent, self.current)

    def __repr__(self):
        return self.__str__()


class Environment:
    def __init__(self, width: float, height: float, turtle=None, current_scope: Scope = Scope("BuiltIn")):
        self.width = width
        self.height = height
        if turtle is None:
            turtle = Turtle(width / 2, height / 2)
        self.turtle: Turtle = turtle
        self.current_scope: Scope = current_scope
        self.build_in_scope: Scope = current_scope

    def push_scope(self, name: str):
        name = name \
            if self.current_scope is None or self.current_scope is self.build_in_scope \
            else self.current_scope.name + "-" + name

        self.current_scope = Scope(
            name,
            parent=self.current_scope)

    def pop_scope(self):
        if self.current_scope is not None:
            self.current_scope = self.current_scope.parent

    def lookup(self, name):
        self.current_scope.lookup(name)

    def insert(self, var: Var):
        self.current_scope.insert(var)
