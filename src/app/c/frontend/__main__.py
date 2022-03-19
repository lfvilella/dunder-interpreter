import logging

import antlr4
from antlr4.error.ErrorListener import ErrorListener
import click

from .antlr.CLexer import CLexer
from .antlr.CParser import CParser


logger = logging.getLogger(__name__)


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol.text not in ['int']:  # Xunxo
            raise SyntaxError(f"line {line}:{column} {msg}")

        logger.info(f"Syntax Error skip: '{offendingSymbol.text}'. {e}")


def run(filepath: str):
    input_stream = antlr4.FileStream(filepath)
    lexer = CLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)

    parser = CParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(listener=MyErrorListener())

    parser.primaryExpression()  # tree


@click.command()
@click.option('--filepath', type=str, required=True)
def main(filepath):
    run(filepath=filepath)


if __name__ == '__main__':
    main()
