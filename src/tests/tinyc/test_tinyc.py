import time
from pathlib import Path
import sys
import unittest

from entrypoint import run


PATH = Path(__file__).parent

class TestTinyC(unittest.TestCase):
    # TODO use pytest.mark.parametrize
    def teste_example1(self):
        tmp = sys.stdout
        fname = 'test_scenario_1.log'
        sys.stdout = open(fname, 'w')

        run(filepath=PATH / 'examples/example1.c')

        sys.stdout.close()
        sys.stdout = tmp
        content = None
        with open(fname) as file:
            content = file.read()

        expected_content = (
            "ANTLR runtime and generated code versions disagree: 4.9.2!=4.8\n"
            "ANTLR runtime and generated code versions disagree: 4.9.2!=4.8\n")
        assert content == expected_content

    # def teste_missing_end_bracket(self):
    #     tmp = sys.stdout
    #     fname = 'test_scenario_2.log'
    #     sys.stdout = open(fname, 'w')

    #     run(filepath=PATH / 'examples/missing_end_bracket.c')

    #     sys.stdout.close()
    #     sys.stdout = tmp
    #     content = None
    #     with open(fname) as file:
    #         content = file.read()

    #     expected_content = (
    #         "ANTLR runtime and generated code versions disagree: 4.9.2!=4.8\n"
    #         "ANTLR runtime and generated code versions disagree: 4.9.2!=4.8\n"
    #         ".line 2:0 extraneous input '<EOF>' expecting {'if', 'while', 'do', ';', '{', '}', '(', STRING, INT}")
    #     assert content == expected_content


if __name__ == '__main__':
    unittest.main()
