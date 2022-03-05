import antlr4
import click

from output.py3.tinycLexer import tinycLexer
from output.py3.tinycParser import tinycParser


def run(filepath: str):
    input_stream = antlr4.FileStream(filepath)
    lexer = tinycLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = tinycParser(stream)
    tree = parser.program()
    # printer = MyGrammarListener()
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


@click.command()
@click.option('--filepath', type=str, required=True)
def main(filepath):
    run(filepath=filepath)


if __name__ == '__main__':
    main()
