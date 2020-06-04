from typing import Optional

from interpreter.logo.logoVisitor import *
from interpreter.logo.logoParser import *
from interpreter.runtime.logo_ast import *


class LogoASTMakingParseTreeVisitor(logoVisitor):

    def visitProg(self, ctx: logoParser.ProgContext) -> Block:
        return Block([cmd for line in ctx.line() for cmd in self.visit(line).statements])

    def visitComparison(self, ctx: logoParser.ComparisonContext):
        t = ctx.comparisonOperator().start.type
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if t == logoParser.MORE_:
            return Comparison(Comparison.Operator.More, left, right)
        elif t == logoParser.LESS_:
            return Comparison(Comparison.Operator.Less, left, right)
        elif t == logoParser.EQUAL_:
            return Comparison(Comparison.Operator.Equal, left, right)
        else:
            raise ValueError("Unsupported Comparison")

    def visitIfe(self, ctx: logoParser.IfeContext) -> If:
        block = self.visit(ctx.block())
        condition = self.visit(ctx.comparison())
        return If(condition, block)

    def visitBlock(self, ctx: logoParser.BlockContext) -> Block:
        return Block([self.visit(cmd) for cmd in ctx.cmd()])

    def visitRepeat(self, ctx: logoParser.RepeatContext):
        return Repeat(n=int(ctx.number().getText()), block=self.visit(ctx.block()))

    def visitLine_print(self, ctx: logoParser.Line_printContext) -> PRINT:

        if ctx.value() is not None:
            return PRINT(self.visit(ctx.value()))
        elif ctx.quotedstring() is not None:
            return PRINT(self.visit(ctx.quotedstring()))
        else:
            raise IllegalStateException("This should not have happened")

    def visitLine(self, ctx: logoParser.LineContext) -> Block:
        cmds = ctx.cmd()
        if len(cmds) > 0:
            return Block([self.visitCmd(cmd) for cmd in cmds])
        elif ctx.line_print() is not None:
            return Block([self.visit(ctx.line_print())])
        else:
            raise NotImplementedError("This line handling was not implemented")

    def visitRt(self, ctx: logoParser.RtContext):
        return OneArg(COMMAND.TURTLE_ROTATE, self.visitExpression(ctx.expression()))

    def visitLt(self, ctx: logoParser.BkContext):
        return OneArg(COMMAND.TURTLE_ROTATE,
                      NumberUnaryOperator(NumberUnaryOperator.Operator.Neg, self.visitExpression(ctx.expression())))

    def visitFd(self, ctx: logoParser.FdContext) -> Statement:
        return OneArg(COMMAND.TURTLE_MOVE, self.visitExpression(ctx.expression()))

    def visitBk(self, ctx: logoParser.BkContext):

        return OneArg(COMMAND.TURTLE_MOVE,
                      NumberUnaryOperator(NumberUnaryOperator.Operator.Neg, self.visitExpression(ctx.expression())))

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

    def visitExpression(self, ctx: logoParser.ExpressionContext) -> Expression:
        if ctx.getChildCount() == 1:
            return self.visitMultiplyingExpression(ctx.left)
        else:
            left = self.visitMultiplyingExpression(ctx.children[0])

            for i in range(1, len(ctx.children[1:]), 2):
                op = ctx.children[i]
                right = ctx.children[i + 1]
                if op.getText() == '+':
                    operator = NumberBinaryOperator.Operator.Add
                else:
                    operator = NumberBinaryOperator.Operator.Sub
                left = NumberBinaryOperator(operator, left, self.visitMultiplyingExpression(right))

            return left

    def visitSetxy(self, ctx: logoParser.SetxyContext):
        return TwoArg(COMMAND.TURTLE_XY, self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

    def visitMultiplyingExpression(self, ctx: logoParser.MultiplyingExpressionContext) -> Expression:
        if ctx.getChildCount() == 1:
            return self.visitSignExpression(ctx.left)
        else:
            left = self.visitSignExpression(ctx.children[0])

            for i in range(1, len(ctx.children[1:]), 2):
                op = ctx.children[i]
                right = ctx.children[i + 1]

                if op.getText() == '*':
                    operator = NumberBinaryOperator.Operator.Mul
                else:
                    operator = NumberBinaryOperator.Operator.Div

                left = NumberBinaryOperator(operator, left, self.visitSignExpression(right))

            return left

    def visitSignExpression(self, ctx: logoParser.SignExpressionContext) -> Expression:
        sign = len([x for x in ctx.getChildren(lambda x: x.getText() == "-")]) % 2 == 0
        number = ctx.number()
        if number is not None:
            num = self.visitNumber(number)
            if not sign:
                num = NumberUnaryOperator(NumberUnaryOperator.Operator.Neg, num)

            return num
        else:
            raise NotImplementedError("Func and deref unimplemented")

    def visitValue(self, ctx: logoParser.ValueContext):
        expression = ctx.expression()
        str_literal = ctx.STRINGLITERAL()

        if expression is not None:
            return self.visit(expression)
        elif str_literal is not None:
            return StringConstant(str_literal.getText()[1:])
        else:
            raise NotImplementedError("deref unimplemented")

    def visitQuotedstring(self, ctx: logoParser.QuotedstringContext) -> StringConstant:
        return StringConstant(ctx.getText()[1:-1])

    def visitNumber(self, ctx: logoParser.NumberContext) -> NumberConstant:
        return NumberConstant(float(ctx.NUMBER().getText()))

    def defaultResult(self) -> Optional[Statement]:
        return None
