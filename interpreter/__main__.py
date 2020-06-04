import argparse
import sys

from antlr4 import *

from interpreter.display.pygame.PygameDisplay import PygameDisplay
from interpreter.display.windowed.WindowedDisplay import WindowedDisplay
from interpreter.logo.logoLexer import logoLexer
from interpreter.runtime.Interpreter import Interpreter
from interpreter.runtime.LogoASTMakingParseTreeVisitor import LogoASTMakingParseTreeVisitor
from interpreter.runtime.Model import Environment, Turtle
from interpreter.runtime.logo_ast import PROGRAM

if __name__ is not None and "." in __name__:
    from .logo.logoParser import logoParser
else:
    from interpreter.logo.logoParser import logoParser


def create_AST(input_text: InputStream) -> PROGRAM:
    lexer = logoLexer(input_text)
    stream = CommonTokenStream(lexer)
    parser = logoParser(stream)
    visitor = LogoASTMakingParseTreeVisitor()

    tree = parser.prog()
    return visitor.visit(tree)


def create_interpreter(environment: Environment, program: PROGRAM):
    interpreter = Interpreter(environment)
    interpreter.execute(program)


def main(argv):
    arguments = argparse.ArgumentParser(prog="Logo interpreter written using python")
    arguments.add_argument("--inputFile", help="File to load program from", default=None, required=False)
    arguments.add_argument("--display-backend", help="Backed to use for display", default="windowed",
                           choices=["windowed", "pygame"])
    arguments.add_argument("--width", help="Environment width", default=1000.0)
    arguments.add_argument("--height", help="Environment width", default=1000.0)

    args = arguments.parse_args(argv[1:])

    # input_text = InputStream(data="fd 60 rt 120 fd 60 rt 120 fd 60 rt 120\n")

    environment = Environment(args.width, args.height, turtle=Turtle(args.width / 2, args.height / 2))

    backend = args.display_backend
    if backend == "pygame":
        PygameDisplay(environment)
    else:
        WindowedDisplay(environment)

    infile = args.inputFile
    repeat = True
    while (repeat):
        if infile is None:
            input_text = InputStream(input(">"))  # InputStream(data="fd 60 rt 120 fd 60 rt 120 fd 60 rt 120\n")
        else:
            repeat = False
            print(">", infile)
            input_text = FileStream(infile)

        ast = create_AST(input_text)
        print(ast)
        create_interpreter(environment, ast)

    # TODO CREATE AST representing the whole program
    # Current support for rotating right - moving forward and basic expressions
    # TODO Implement all builtin commands
    # TODO Implement print_line
    # TODO Procedure Declaration
    # TODO Procedure Invocation
    # TODO Extend expressions to use functions
    # TODO CREATE INTERPRETER using the environment and AST
    input("Exit")


if __name__ == '__main__':
    main(sys.argv)
