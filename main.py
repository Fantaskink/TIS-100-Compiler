import sys
from antlr4 import *
from pretty_printer.pretty_printer import PrettyPrinter
from code_generation.code_generator import CodeGenerator
from generated.tis100Lexer import tis100Lexer
from generated.tis100Parser import tis100Parser


def get_code():
    with open('code/program.txt') as f:
        loaded_code = f.read()
        return loaded_code


if __name__ == '__main__':
    code = get_code()
    input_stream = InputStream(code)
    lexer = tis100Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = tis100Parser(token_stream)

    ast = parser.program()
    pretty_printer = PrettyPrinter()
    pretty_printer.visitProgram(ast)

    code_generator = CodeGenerator()
    code_generator.generate_code(ast)
