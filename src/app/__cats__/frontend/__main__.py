import antlr4
import click

from .output.py3.dunderCatsLexer import dunderCatsLexer
from .output.py3.dunderCatsParser import dunderCatsParser
from backend.visitor import CustomTinycVisitor


def run(filepath: str):
    input_stream = antlr4.FileStream(filepath)
    lexer = dunderCatsLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)

    parser = dunderCatsParser(stream)
    tree = parser.program()
    CustomTinycVisitor().visit(tree)


@click.command()
@click.option('--filepath', type=str, required=True)
def main(filepath):
    run(filepath=filepath)


if __name__ == '__main__':
    main()
