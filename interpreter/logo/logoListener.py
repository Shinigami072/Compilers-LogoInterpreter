# Generated from logo.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .logoParser import logoParser
else:
    from logoParser import logoParser

# This class defines a complete listener for a parse tree produced by logoParser.
class logoListener(ParseTreeListener):

    # Enter a parse tree produced by logoParser#prog.
    def enterProg(self, ctx:logoParser.ProgContext):
        pass

    # Exit a parse tree produced by logoParser#prog.
    def exitProg(self, ctx:logoParser.ProgContext):
        pass


    # Enter a parse tree produced by logoParser#line.
    def enterLine(self, ctx:logoParser.LineContext):
        pass

    # Exit a parse tree produced by logoParser#line.
    def exitLine(self, ctx:logoParser.LineContext):
        pass


    # Enter a parse tree produced by logoParser#cmd.
    def enterCmd(self, ctx:logoParser.CmdContext):
        pass

    # Exit a parse tree produced by logoParser#cmd.
    def exitCmd(self, ctx:logoParser.CmdContext):
        pass


    # Enter a parse tree produced by logoParser#procedureInvocation.
    def enterProcedureInvocation(self, ctx:logoParser.ProcedureInvocationContext):
        pass

    # Exit a parse tree produced by logoParser#procedureInvocation.
    def exitProcedureInvocation(self, ctx:logoParser.ProcedureInvocationContext):
        pass


    # Enter a parse tree produced by logoParser#procedureDeclaration.
    def enterProcedureDeclaration(self, ctx:logoParser.ProcedureDeclarationContext):
        pass

    # Exit a parse tree produced by logoParser#procedureDeclaration.
    def exitProcedureDeclaration(self, ctx:logoParser.ProcedureDeclarationContext):
        pass


    # Enter a parse tree produced by logoParser#parameterDeclarations.
    def enterParameterDeclarations(self, ctx:logoParser.ParameterDeclarationsContext):
        pass

    # Exit a parse tree produced by logoParser#parameterDeclarations.
    def exitParameterDeclarations(self, ctx:logoParser.ParameterDeclarationsContext):
        pass


    # Enter a parse tree produced by logoParser#func.
    def enterFunc(self, ctx:logoParser.FuncContext):
        pass

    # Exit a parse tree produced by logoParser#func.
    def exitFunc(self, ctx:logoParser.FuncContext):
        pass


    # Enter a parse tree produced by logoParser#repeat.
    def enterRepeat(self, ctx:logoParser.RepeatContext):
        pass

    # Exit a parse tree produced by logoParser#repeat.
    def exitRepeat(self, ctx:logoParser.RepeatContext):
        pass


    # Enter a parse tree produced by logoParser#block.
    def enterBlock(self, ctx:logoParser.BlockContext):
        pass

    # Exit a parse tree produced by logoParser#block.
    def exitBlock(self, ctx:logoParser.BlockContext):
        pass


    # Enter a parse tree produced by logoParser#ife.
    def enterIfe(self, ctx:logoParser.IfeContext):
        pass

    # Exit a parse tree produced by logoParser#ife.
    def exitIfe(self, ctx:logoParser.IfeContext):
        pass


    # Enter a parse tree produced by logoParser#comparison.
    def enterComparison(self, ctx:logoParser.ComparisonContext):
        pass

    # Exit a parse tree produced by logoParser#comparison.
    def exitComparison(self, ctx:logoParser.ComparisonContext):
        pass


    # Enter a parse tree produced by logoParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:logoParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by logoParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:logoParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by logoParser#make.
    def enterMake(self, ctx:logoParser.MakeContext):
        pass

    # Exit a parse tree produced by logoParser#make.
    def exitMake(self, ctx:logoParser.MakeContext):
        pass


    # Enter a parse tree produced by logoParser#line_print.
    def enterLine_print(self, ctx:logoParser.Line_printContext):
        pass

    # Exit a parse tree produced by logoParser#line_print.
    def exitLine_print(self, ctx:logoParser.Line_printContext):
        pass


    # Enter a parse tree produced by logoParser#quotedstring.
    def enterQuotedstring(self, ctx:logoParser.QuotedstringContext):
        pass

    # Exit a parse tree produced by logoParser#quotedstring.
    def exitQuotedstring(self, ctx:logoParser.QuotedstringContext):
        pass


    # Enter a parse tree produced by logoParser#name.
    def enterName(self, ctx:logoParser.NameContext):
        pass

    # Exit a parse tree produced by logoParser#name.
    def exitName(self, ctx:logoParser.NameContext):
        pass


    # Enter a parse tree produced by logoParser#value.
    def enterValue(self, ctx:logoParser.ValueContext):
        pass

    # Exit a parse tree produced by logoParser#value.
    def exitValue(self, ctx:logoParser.ValueContext):
        pass


    # Enter a parse tree produced by logoParser#signExpression.
    def enterSignExpression(self, ctx:logoParser.SignExpressionContext):
        pass

    # Exit a parse tree produced by logoParser#signExpression.
    def exitSignExpression(self, ctx:logoParser.SignExpressionContext):
        pass


    # Enter a parse tree produced by logoParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:logoParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by logoParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:logoParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by logoParser#expression.
    def enterExpression(self, ctx:logoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by logoParser#expression.
    def exitExpression(self, ctx:logoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by logoParser#deref.
    def enterDeref(self, ctx:logoParser.DerefContext):
        pass

    # Exit a parse tree produced by logoParser#deref.
    def exitDeref(self, ctx:logoParser.DerefContext):
        pass


    # Enter a parse tree produced by logoParser#fd.
    def enterFd(self, ctx:logoParser.FdContext):
        pass

    # Exit a parse tree produced by logoParser#fd.
    def exitFd(self, ctx:logoParser.FdContext):
        pass


    # Enter a parse tree produced by logoParser#bk.
    def enterBk(self, ctx:logoParser.BkContext):
        pass

    # Exit a parse tree produced by logoParser#bk.
    def exitBk(self, ctx:logoParser.BkContext):
        pass


    # Enter a parse tree produced by logoParser#rt.
    def enterRt(self, ctx:logoParser.RtContext):
        pass

    # Exit a parse tree produced by logoParser#rt.
    def exitRt(self, ctx:logoParser.RtContext):
        pass


    # Enter a parse tree produced by logoParser#lt.
    def enterLt(self, ctx:logoParser.LtContext):
        pass

    # Exit a parse tree produced by logoParser#lt.
    def exitLt(self, ctx:logoParser.LtContext):
        pass


    # Enter a parse tree produced by logoParser#cs.
    def enterCs(self, ctx:logoParser.CsContext):
        pass

    # Exit a parse tree produced by logoParser#cs.
    def exitCs(self, ctx:logoParser.CsContext):
        pass


    # Enter a parse tree produced by logoParser#pu.
    def enterPu(self, ctx:logoParser.PuContext):
        pass

    # Exit a parse tree produced by logoParser#pu.
    def exitPu(self, ctx:logoParser.PuContext):
        pass


    # Enter a parse tree produced by logoParser#pd.
    def enterPd(self, ctx:logoParser.PdContext):
        pass

    # Exit a parse tree produced by logoParser#pd.
    def exitPd(self, ctx:logoParser.PdContext):
        pass


    # Enter a parse tree produced by logoParser#ht.
    def enterHt(self, ctx:logoParser.HtContext):
        pass

    # Exit a parse tree produced by logoParser#ht.
    def exitHt(self, ctx:logoParser.HtContext):
        pass


    # Enter a parse tree produced by logoParser#st.
    def enterSt(self, ctx:logoParser.StContext):
        pass

    # Exit a parse tree produced by logoParser#st.
    def exitSt(self, ctx:logoParser.StContext):
        pass


    # Enter a parse tree produced by logoParser#home.
    def enterHome(self, ctx:logoParser.HomeContext):
        pass

    # Exit a parse tree produced by logoParser#home.
    def exitHome(self, ctx:logoParser.HomeContext):
        pass


    # Enter a parse tree produced by logoParser#stop.
    def enterStop(self, ctx:logoParser.StopContext):
        pass

    # Exit a parse tree produced by logoParser#stop.
    def exitStop(self, ctx:logoParser.StopContext):
        pass


    # Enter a parse tree produced by logoParser#label.
    def enterLabel(self, ctx:logoParser.LabelContext):
        pass

    # Exit a parse tree produced by logoParser#label.
    def exitLabel(self, ctx:logoParser.LabelContext):
        pass


    # Enter a parse tree produced by logoParser#setxy.
    def enterSetxy(self, ctx:logoParser.SetxyContext):
        pass

    # Exit a parse tree produced by logoParser#setxy.
    def exitSetxy(self, ctx:logoParser.SetxyContext):
        pass


    # Enter a parse tree produced by logoParser#random.
    def enterRandom(self, ctx:logoParser.RandomContext):
        pass

    # Exit a parse tree produced by logoParser#random.
    def exitRandom(self, ctx:logoParser.RandomContext):
        pass


    # Enter a parse tree produced by logoParser#fore.
    def enterFore(self, ctx:logoParser.ForeContext):
        pass

    # Exit a parse tree produced by logoParser#fore.
    def exitFore(self, ctx:logoParser.ForeContext):
        pass


    # Enter a parse tree produced by logoParser#number.
    def enterNumber(self, ctx:logoParser.NumberContext):
        pass

    # Exit a parse tree produced by logoParser#number.
    def exitNumber(self, ctx:logoParser.NumberContext):
        pass


    # Enter a parse tree produced by logoParser#comment.
    def enterComment(self, ctx:logoParser.CommentContext):
        pass

    # Exit a parse tree produced by logoParser#comment.
    def exitComment(self, ctx:logoParser.CommentContext):
        pass


