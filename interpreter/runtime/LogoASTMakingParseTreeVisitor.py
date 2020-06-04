from typing import Optional

from interpreter.logo.logoVisitor import *
from interpreter.logo.logoParser import *
from interpreter.runtime.logo_ast import *


class LogoASTMakingParseTreeVisitor(logoVisitor):

    def visitProg(self, ctx: logoParser.ProgContext) -> PROGRAM:
        return PROGRAM([cmd for line in ctx.line() for cmd in self.visitLine(line).cmds])

    def visitLine(self, ctx: logoParser.LineContext) -> PROGRAM:
        cmds = ctx.cmd()
        if len(cmds) > 0:
            return PROGRAM([self.visitCmd(cmd) for cmd in cmds])

    def visitRt(self, ctx: logoParser.RtContext):
        return OneArg(COMMAND.TURTLE_ROTATE, self.visitExpression(ctx.expression()))

    def visitLt(self, ctx: logoParser.BkContext):
        return OneArg(COMMAND.TURTLE_ROTATE, NEG(self.visitExpression(ctx.expression())))

    def visitFd(self, ctx: logoParser.FdContext) -> AST:
        return OneArg(COMMAND.TURTLE_MOVE, self.visitExpression(ctx.expression()))

    def visitBk(self, ctx: logoParser.BkContext):
        return OneArg(COMMAND.TURTLE_MOVE, NEG(self.visitExpression(ctx.expression())))

    def visitCs(self, ctx: logoParser.CsContext):
        return NoArg(COMMAND.CLEAR_SCREEN)

    def visitHome(self, ctx: logoParser.HomeContext):
        return NoArg(COMMAND.HOME)

    def visitPu(self, ctx: logoParser.PdContext):
        return PEN(False)

    def visitPd(self, ctx: logoParser.PdContext):
        return PEN(True)

    def visitSt(self, ctx: logoParser.StContext):
        return Visibility(True)

    def visitHt(self, ctx: logoParser.HtContext):
        return Visibility(False)

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

    def visitSetxy(self, ctx: logoParser.SetxyContext):
        return TwoArg(COMMAND.TURTLE_XY, self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

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
