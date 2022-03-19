import re
import random
import logging

from frontend.output.py3.dunderCatsParser import dunderCatsParser
from frontend.output.py3.dunderCatsVisitor import dunderCatsVisitor

from . import THUNDER_REFS


logger = logging.getLogger(__name__)


TABLE = {}


class CustomTinycVisitor(dunderCatsVisitor):
    # Visit a parse tree produced by dunderCatsParser#program.
    def visitProgram(self, ctx:dunderCatsParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dunderCatsParser#statement.
    def visitStatement(self, ctx:dunderCatsParser.StatementContext):
        logging.debug('visitStatement')
        start_text = ctx.start.text
        if start_text == 'if':
            paren_expr = self.visit(ctx.paren_expr().expr())
            statements = ctx.statement()
            if len(statements) == 1:
                if paren_expr:
                    return self.visit(statements[0])
            else:
                if paren_expr:
                    return self.visit(statements[0])
                else:
                    return self.visit(statements[1])

        elif start_text == 'while':
            paren_expr = self.visit(ctx.paren_expr().expr())
            while paren_expr:
                for statement in ctx.statement():
                    self.visit(statement)
                paren_expr = self.visit(ctx.paren_expr().expr())

        elif start_text == 'printf':
            expr = self.visit(ctx.paren_expr().expr())
            expr = TABLE.get(expr) or expr
            print(f"⚡⚡{random.choice(THUNDER_REFS)}⚡⚡:", expr)

        return self.visitChildren(ctx)

    # Visit a parse tree produced by dunderCatsParser#paren_expr.
    def visitParen_expr(self, ctx:dunderCatsParser.Paren_exprContext):
        logging.debug('visitParen_expr')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dunderCatsParser#expr.
    def visitExpr(self, ctx:dunderCatsParser.ExprContext):
        logging.debug('visitExpr')
        if '=' in ctx.getText():
            id = self.visit(ctx.id_())
            expr = self.visit(ctx.expr())
            TABLE[id] = expr
        return self.visitChildren(ctx)

        # return self.visit(ctx.test())

    # Visit a parse tree produced by dunderCatsParser#test.
    def visitTest(self, ctx:dunderCatsParser.TestContext):
        logging.debug('visitTest')
        ctx_text = ctx.getText()
        # is_conditional = re.search('[<|>]', ctx_text)
        if '<' not in ctx_text:
            return self.visitChildren(ctx)

        sum_ = ctx.sum_()
        param1 = self.visit(sum_[0])
        param1 = TABLE.get(param1) or param1
        param2 = self.visit(sum_[1])
        param2 = TABLE.get(param2) or param2
        return param1 < param2

    # Visit a parse tree produced by dunderCatsParser#sum_.
    def visitSum_(self, ctx:dunderCatsParser.Sum_Context):
        logging.debug('visitSum_')
        ctx_text = ctx.getText()
        is_math_expr = re.search('[+|-]', ctx_text)
        if not is_math_expr:
            return self.visitChildren(ctx)

        sum_ = self.visit(ctx.sum_())
        sum_ = TABLE.get(sum_) or sum_
        term = self.visit(ctx.term())
        term = TABLE.get(term) or term

        operator = is_math_expr.group()
        if operator == '+':
            return sum_ + term
        elif operator == '-':
            return sum_ - term
        else:
            raise SyntaxError(f"Invalid math expr '{operator}'")

    # Visit a parse tree produced by dunderCatsParser#term.
    def visitTerm(self, ctx:dunderCatsParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by dunderCatsParser#id_.
    def visitId_(self, ctx:dunderCatsParser.Id_Context):
        return ctx.STRING().symbol.text

    # Visit a parse tree produced by dunderCatsParser#integer.
    def visitInteger(self, ctx:dunderCatsParser.IntegerContext):
        return int(ctx.INT().symbol.text)
