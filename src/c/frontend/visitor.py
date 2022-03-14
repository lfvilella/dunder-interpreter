import antlr4
from antlr4.error.ErrorListener import ErrorListener
import click

from .antlr.CVisitor import CVisitor
from .antlr.CParser import CParser


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol.text in ['int']:  # Xunxo
            pass
        else:
            raise SyntaxError(f"line {line}:{column} {msg}")


class Visitor(CVisitor):
    pass


def run(filepath: str):
    input_stream = antlr4.FileStream(filepath)
    lexer = CLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)

    parser = CParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(listener=MyErrorListener())

    tree = parser.primaryExpression()

    # breakpoint()
    # print('tree.exception', tree.exception)
    # printer = MyGrammarListener()
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


@click.command()
@click.option('--filepath', type=str, required=True)
def main(filepath):
    run(filepath=filepath)


if __name__ == '__main__':
    main()
