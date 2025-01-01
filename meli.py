from Reader.reader import Reader
from Parser.Parser import Parser
from Writer.Writer import Writer
import argparse

def main():
    parser = argparse.ArgumentParser(description='Transpilador a HTML')

    parser.add_argument('-i', '--input', help='Archivo de entrada', required=True)
    parser.add_argument('-o', '--output', help='Archivo de salida', required=True)

    args = parser.parse_args()
    read = Reader(args.input)
    parser = Parser(read)
    write = Writer(args.output, parser)
    write.write()

if __name__ == '__main__':
    main()
