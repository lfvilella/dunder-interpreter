import antlr4
from antlr4.error.ErrorListener import ErrorListener
import click

from .antlr.tinycLexer import tinycLexer
from .antlr.tinycParser import tinycParser
from .antlr.tinycListener import tinycListener


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(
            f'Coé, erro na linha {line}:{column}. Simbolo nada ve esse: {offendingSymbol.text}'
        )
        # super().syntaxError(self, recognizer, offendingSymbol, line, column, msg, e)


def run(filepath: str):
    input_stream = antlr4.FileStream(filepath)
    lexer = tinycLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)

    parser = tinycParser(stream)
    # parser.removeErrorListeners()
    # parser.addErrorListener(listener=MyErrorListener())

    tree = parser.program()

    # breakpoint()
    # print('tree.exception', tree.exception)
    listener = tinycListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)


@click.command()
@click.option('--filepath', type=str, required=True)
def main(filepath):
    run(filepath=filepath)


if __name__ == '__main__':
    main()
