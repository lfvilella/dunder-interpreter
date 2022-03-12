import antlr4
import click

from .antlr.CLexer import CLexer
from .antlr.CParser import CParser


def run(filepath: str):
    input_stream = antlr4.FileStream(filepath)
    lexer = CLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.primaryExpression()
    # printer = MyGrammarListener()
    # walker = ParseTreeWalker()
    # walker.walk(printer, tree)


@click.command()
@click.option('--filepath', type=str, required=True)
def main(filepath):
    run(filepath=filepath)


if __name__ == '__main__':
    main()
