from typing import List

import pyglet
from pyglet.gl import *

from interpreter.runtime.Model import Line, Turtle, Environment


class LineRenderer:
    def __init__(self, lines: List[Line]):
        self.lines = lines

    def draw(self):
        for line in self.lines:
            self.draw_line(line)

    def draw_line(self, line: Line):
        if len(line.points) <= 1:
            return
        (cnt, indices, lines) = self._get_line_data(line)
        pyglet.graphics.draw_indexed(cnt, pyglet.gl.GL_LINES,
                                     indices,
                                     lines,
                                     )

    @staticmethod
    def _get_line_data(line: Line):
        indices = []
        positions = []

        for i in range(0, len(line.points) - 1):
            indices.append(i)
            indices.append(i + 1)

        for x, y in line.points:
            positions.append(x)
            positions.append(y)

        positions = tuple(positions)
        return (len(positions) // 2), indices, ('v2f', positions)


class RobotRenderer:
    def __init__(self, robot: Turtle):
        self.robot = robot
        self.lines = LineRenderer(robot.lines)

    def draw(self):
        self.lines.draw()
        if not self.robot.visible:
            return

        glPushMatrix()
        glTranslatef(self.robot.pos[0], self.robot.pos[1], 0.0)
        glRotatef(self.robot.rot - 90.0, 0, 0, 1)
        glBegin(GL_TRIANGLES)
        glVertex2f(0, 10)
        glVertex2f(10, -5)
        glVertex2f(-10, -5)

        if self.robot.pencil_down:
            glVertex2f(0, -10)
            glVertex2f(5, -5)
            glVertex2f(-5, -5)

        glEnd()
        glPopMatrix()


class EnvironmentRenderer:
    def __init__(self, environment: Environment):
        self.robot = RobotRenderer(environment.turtle)

    def draw(self):
        self.robot.draw()
