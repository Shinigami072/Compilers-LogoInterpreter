from typing import Optional

from interpreter.logo.logoVisitor import *
from interpreter.logo.logoParser import *
from interpreter.runtime.logo_ast import *


class LINE(AST):
    def __init__(self, cmds: List[CMD]):
        self.cmds = cmds


class LogoASTMakingParseTreeVisitor(logoVisitor):

    def visitProg(self, ctx: logoParser.ProgContext) -> PROGRAM:
        return PROGRAM([cmd for line in ctx.line() for cmd in self.visitLine(line).cmds])

    def visitLine(self, ctx: logoParser.LineContext) -> LINE:
        cmds = ctx.cmd()
        if len(cmds) > 0:
            return LINE([self.visitCmd(cmd) for cmd in cmds])

    def visitRt(self, ctx: logoParser.RtContext):
        return RT(self.visitExpression(ctx.expression()))

    def visitFd(self, ctx: logoParser.FdContext) -> AST:
        return FD(self.visitExpression(ctx.expression()))

    def visitExpression(self, ctx: logoParser.ExpressionContext) -> EXPRESION:
        if ctx.getChildCount() == 1:
            return self.visitMultiplyingExpression(ctx.left)
        else:
            left = self.visitMultiplyingExpression(ctx.children[0])

            for i in range(1, len(ctx.children[1:]), 2):
                op = ctx.children[i]
                right = ctx.children[i + 1]
                if op.getText() == '+':
                    left = Add(left, self.visitMultiplyingExpression(right))
                else:
                    left = Sub(left, self.visitMultiplyingExpression(right))

            return left

    def visitMultiplyingExpression(self, ctx: logoParser.MultiplyingExpressionContext) -> EXPRESION:
        if ctx.getChildCount() == 1:
            return self.visitSignExpression(ctx.left)
        else:
            left = self.visitSignExpression(ctx.children[0])

            for i in range(1, len(ctx.children[1:]), 2):
                op = ctx.children[i]
                right = ctx.children[i + 1]
                if op.getText() == '*':
                    left = Mul(left, self.visitSignExpression(right))
                else:
                    left = Div(left, self.visitSignExpression(right))

            return left

    def visitSignExpression(self, ctx: logoParser.SignExpressionContext) -> EXPRESION:
        sign = len([x for x in ctx.getChildren(lambda x: x.getText() == "-")]) % 2 == 0
        number = ctx.number()
        if number is not None:
            num = self.visitNumber(number)
            if not sign:
                num = NUMBER(-num.value)
            return num
        else:
            return self.visitChildren(ctx)

    def visitNumber(self, ctx: logoParser.NumberContext) -> NUMBER:
        return NUMBER(float(ctx.NUMBER().__str__()))

    def defaultResult(self) -> Optional[AST]:
        return None

    def aggregateResult(self, aggregate, nextResult) -> Optional[AST]:
        if aggregate is None:
            return nextResult
        else:
            return aggregate
