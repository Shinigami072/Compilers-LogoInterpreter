# Generated from logo.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logoParser import logoParser
else:
    from logoParser import logoParser

# This class defines a complete generic visitor for a parse tree produced by logoParser.

class logoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by logoParser#prog.
    def visitProg(self, ctx:logoParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#line.
    def visitLine(self, ctx:logoParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#cmd.
    def visitCmd(self, ctx:logoParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#procedureInvocation.
    def visitProcedureInvocation(self, ctx:logoParser.ProcedureInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#procedureDeclaration.
    def visitProcedureDeclaration(self, ctx:logoParser.ProcedureDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#parameterDeclarations.
    def visitParameterDeclarations(self, ctx:logoParser.ParameterDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#func.
    def visitFunc(self, ctx:logoParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#repeat.
    def visitRepeat(self, ctx:logoParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#block.
    def visitBlock(self, ctx:logoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#ife.
    def visitIfe(self, ctx:logoParser.IfeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#comparison.
    def visitComparison(self, ctx:logoParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:logoParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#make.
    def visitMake(self, ctx:logoParser.MakeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#print.
    def visitPrint(self, ctx:logoParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#quotedstring.
    def visitQuotedstring(self, ctx:logoParser.QuotedstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#name.
    def visitName(self, ctx:logoParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#value.
    def visitValue(self, ctx:logoParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#signExpression.
    def visitSignExpression(self, ctx:logoParser.SignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#multiplyingExpression.
    def visitMultiplyingExpression(self, ctx:logoParser.MultiplyingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#expression.
    def visitExpression(self, ctx:logoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#deref.
    def visitDeref(self, ctx:logoParser.DerefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#fd.
    def visitFd(self, ctx:logoParser.FdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#bk.
    def visitBk(self, ctx:logoParser.BkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#rt.
    def visitRt(self, ctx:logoParser.RtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#lt.
    def visitLt(self, ctx:logoParser.LtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#cs.
    def visitCs(self, ctx:logoParser.CsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#pu.
    def visitPu(self, ctx:logoParser.PuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#pd.
    def visitPd(self, ctx:logoParser.PdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#ht.
    def visitHt(self, ctx:logoParser.HtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#st.
    def visitSt(self, ctx:logoParser.StContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#home.
    def visitHome(self, ctx:logoParser.HomeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#stop.
    def visitStop(self, ctx:logoParser.StopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#label.
    def visitLabel(self, ctx:logoParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#setxy.
    def visitSetxy(self, ctx:logoParser.SetxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#random.
    def visitRandom(self, ctx:logoParser.RandomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#fore.
    def visitFore(self, ctx:logoParser.ForeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#number.
    def visitNumber(self, ctx:logoParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by logoParser#comment.
    def visitComment(self, ctx:logoParser.CommentContext):
        return self.visitChildren(ctx)



del logoParser