import sys
import signal

from antlr4 import *

from interpreter.display.pygame.PygameDisplay import PygameDisplay
from interpreter.display.windowed.WindowedDisplay import WindowedDisplay
from interpreter.runtime.Model import Environment

if __name__ is not None and "." in __name__:
    from .logo.logoListener import logoListener
    from .logo.logoParser import logoParser
else:
    from logo.logoListener import logoListener
    from logo.logoParser import logoParser

import random
import time


class LogoPrintListener(logoListener):
    def explore(self, ctx: RuleContext):
        ruleName = logoParser.ruleNames[ctx.getRuleIndex()];
        print(ruleName, end=" ")
        for child in ctx.children:
            if child is RuleContext:
                self.explore(child)
            else:
                print(child, end=" ")

    def enterCmd(self, ctx):
        print("CMD: %s" % ctx)

    def enterFd(self, ctx: logoParser.FdContext):
        ctx.expression()
        print("FD %s" % ctx.expression())

    def exitFd(self, ctx: logoParser.FdContext):
        print("_FD %s" % ctx.expression())
        self.explore(ctx.expression())

    def enterRt(self, ctx: logoParser.RtContext):
        print("RT %s" % ctx.expression())

    def exitRt(self, ctx: logoParser.RtContext):
        print("_RT %s" % ctx.expression())
        self.explore(ctx.expression())


def main(argv):
    if (len(argv) < 2):
        input_text = InputStream(data="fd 60 rt 120 fd 60 rt 120 fd 60 rt 120\n")
    else:
        input_text = FileStream(argv[1])

    environment = Environment(1000.0, 1000.0)
    display = PygameDisplay(environment)

    # TODO remove display Demonstration
    def robot_demo(robot):
        delay = 0.0001
        robot.move_pencil_down()
        for _ in range(6):
            for _ in range(6):
                for _ in range(6):
                    for y in range(6):
                        for i in range(6):
                            if random.random() < 0.05:
                                robot.move_pencil_down()
                            if random.random() < 0.6:
                                robot.move_pencil_up()
                            robot.move(60)
                            time.sleep(delay * 2)
                            robot.rotate(360 / 6)
                            time.sleep(delay)

                        robot.move(12)
                        time.sleep(delay)
                        robot.rotate(360 / 6)
                        time.sleep(delay)
                    robot.move(48)
                    time.sleep(delay)
                    robot.rotate(360 / 6)
                    time.sleep(delay)
                robot.move(96)
                time.sleep(delay)
                robot.rotate(360 / 6)
                time.sleep(delay)
            robot.move(192)
            time.sleep(delay)
            robot.rotate(360 / 6)
            time.sleep(delay)
            robot.draw_Robot = False

    robot_demo(environment.turtle)
    time.sleep(1)

    # lexer = logoLexer(input_text)
    # stream = CommonTokenStream(lexer)
    # parser = logoParser(stream)
    # printer = LogoPrintListener()
    #
    # tree = parser.prog()
    # print(tree.children)
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)
    display.close()


if __name__ == '__main__':
    main(sys.argv)
