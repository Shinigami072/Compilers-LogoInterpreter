from antlr4 import *
import sys

from antlr4.tree.Tree import TerminalNodeImpl

from .logo.logoLexer import logoLexer
from .logo.logoListener import logoListener
from .logo.logoParser import logoParser


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
    lexer = logoLexer(input_text)
    stream = CommonTokenStream(lexer)
    parser = logoParser(stream)
    printer = LogoPrintListener()
    tree = parser.prog()
    print(tree.children)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
