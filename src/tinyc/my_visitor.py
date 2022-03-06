from antlr4 import *
from output.py3.tinycLexer import tinycLexer
from output.py3.tinycVisitor import tinycVisitor
from output.py3.tinycParser import tinycParser


class MyVisitor(tinycVisitor):

    def visitProgram(self, ctx):
        print("visitProgram",ctx.getText())
        return self.visitChildren(ctx)

    def visitProgram(self, ctx):
        print('visitProgram', ctx.getText())
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        print('visitStatement', ctx.getText())
        return self.visitChildren(ctx)

    def visitParen_expr(self, ctx):
        print('visitParen_expr', ctx.getText())
        return self.visitChildren(ctx)

    def visitExpr(self, ctx):
        print('visitExpr', ctx.getText())
        return self.visitChildren(ctx)

    def visitTest(self, ctx):
        print('visitTest', ctx.getText())
        return self.visitChildren(ctx)

    def visitSum_(self, ctx):
        print('visitSum_', ctx.getText())
        return self.visitChildren(ctx)

    def visitTerm(self, ctx):
        print('visitTerm', ctx.getText())
        return self.visitChildren(ctx)

    def visitId_(self, ctx):
        print('visitId_', ctx.getText())
        return self.visitChildren(ctx)

    def visitInteger(self, ctx):
        print('visitInteger', ctx.getText())
        return self.visitChildren(ctx)

    def visitAtomExpr(self, ctx):
        print("visitAtomExpr",int(ctx.getText()))
        return int(ctx.getText())

    def visitParenExpr(self, ctx):
        print("visitParenExpr",ctx.getText())
        return self.visit(ctx.expr())


def main():
    #lexer = arithmeticLexer(StdinStream())
    breakpoint()
    expression = "{ i=1; while (i<100) i=i+i; }"
    lexer = tinycLexer(InputStream(expression))
    stream = CommonTokenStream(lexer)
    parser = tinycParser(stream)
    tree = parser.program()
    answer = MyVisitor().visit(tree)
    print(answer)


if __name__ == '__main__':
    main()
