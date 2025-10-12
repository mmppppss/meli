from Reader.reader import Reader
from Parser.Parser import Parser
from Writer.Writer import Writer
import argparse, time, threading

from http.server import HTTPServer, SimpleHTTPRequestHandler

def server(file_out):
    PORT = 8000
    handler = SimpleHTTPRequestHandler
    httpd = HTTPServer(('localhost', PORT),handler)
    print(f"Server Running in: http://localhost:{PORT}/{file_out}")
    httpd.serve_forever()

def live(args):
    read = Reader(args.input)
    cache = read.content
    proccess(args)
    while True:
        time.sleep(2)
        f = open(args.input,'r')
        content = f.read()
        if content != cache :
            print("RELOAD FILE")
            cache = content
            proccess(args)


def proccess(args):
    read = Reader(args.input)
    parser = Parser(read)
    write = Writer(args.output, parser)
    write.write()


def main():
    parser = argparse.ArgumentParser(description='Transpilador a HTML')

    parser.add_argument('-i', '--input', help='Archivo de entrada', required=True)
    parser.add_argument('-o', '--output', help='Archivo de salida', required=True)
    parser.add_argument('-l', '--live', help='Servidor en Vivo', action='store_true', required=False)

    args = parser.parse_args()
    print(args)

    thr = threading.Thread(target=server, args=(args.output, )).start()
    
    if(args.live):
        print("LIVE MODE")
        live(args)
    else:
        proccess(args)

if __name__ == '__main__':
    main()
