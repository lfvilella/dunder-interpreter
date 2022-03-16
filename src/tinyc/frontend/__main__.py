import antlr4
import click

from .antlr.tinycLexer import tinycLexer
from .antlr.tinycParser import tinycParser
from .visitor import CustomTinycVisitor


def run(filepath: str):
    input_stream = antlr4.FileStream(filepath)
    lexer = tinycLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)

    parser = tinycParser(stream)
    tree = parser.program()
    CustomTinycVisitor().visit(tree)


@click.command()
@click.option('--filepath', type=str, required=True)
def main(filepath):
    run(filepath=filepath)


if __name__ == '__main__':
    main()
