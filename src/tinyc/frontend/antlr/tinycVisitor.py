# Generated from /Users/felipe/projects/della-compiler/src/tinyc/frontend/tinyc.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tinycParser import tinycParser
else:
    from tinycParser import tinycParser

# This class defines a complete generic visitor for a parse tree produced by tinycParser.

class tinycVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tinycParser#program.
    def visitProgram(self, ctx:tinycParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#statement.
    def visitStatement(self, ctx:tinycParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#paren_expr.
    def visitParen_expr(self, ctx:tinycParser.Paren_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#expr.
    def visitExpr(self, ctx:tinycParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#test.
    def visitTest(self, ctx:tinycParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#sum_.
    def visitSum_(self, ctx:tinycParser.Sum_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#term.
    def visitTerm(self, ctx:tinycParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#id_.
    def visitId_(self, ctx:tinycParser.Id_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tinycParser#integer.
    def visitInteger(self, ctx:tinycParser.IntegerContext):
        return self.visitChildren(ctx)



del tinycParser