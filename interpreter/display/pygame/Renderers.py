from typing import List

import pygame

from interpreter.runtime.Model import Line, Turtle, Environment

WHITE = pygame.Color(255, 255, 255)


class LineRenderer:
    def __init__(self, lines: List[Line]):
        self.lines = lines

    def draw(self, surface):
        for line in self.lines:
            self.draw_line(line, surface)

    def draw_line(self, line: Line, surface):
        if len(line.points) <= 1:
            return
        pygame.draw.lines(surface, WHITE, False, line.points)


class RobotRenderer:
    def __init__(self, robot: Turtle):
        self.robot = robot
        self.lines = LineRenderer(robot.lines)

    def draw(self, surface):
        self.lines.draw(surface)
        if not self.robot.visible:
            return
        pygame.draw.circle(surface, WHITE, (round(self.robot.pos[0]), round(self.robot.pos[1])), 10)


class EnvironmentRenderer:
    def __init__(self, environment: Environment):
        self.robot = RobotRenderer(environment.turtle)

    def draw(self, surface):
        self.robot.draw(surface)
