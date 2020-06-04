import math
import typing


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


class Environment:
    def __init__(self, width: float, height: float, turtle=None):
        self.width = width
        self.height = height
        if turtle is None:
            turtle = Turtle(width / 2, height / 2)
        self.turtle = turtle
