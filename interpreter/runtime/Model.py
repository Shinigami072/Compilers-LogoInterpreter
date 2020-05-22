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

    def move(self, dist: float):
        dx = dist * math.cos(math.radians(self.rot))
        dy = dist * math.sin(math.radians(self.rot))

        x, y = self.pos

        self.pos = (x + dx, y + dy)

        if self.pencil_down:
            self.lines[-1].add_point(self.pos)

    def move_pencil_down(self):
        if not self.pencil_down:
            self.lines[-1].add_point(self.pos)
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
