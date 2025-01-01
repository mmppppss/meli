from Analex.Analex import Analex
from Reader.reader import Reader
from Tokens.Tokens import Tokens, Token

class Parser:

    def __init__(self, Reader):
        self.analex= Analex(Reader)
        self.analex.analex()
        self.result = "" 
        self.codigo()

    def getResult(self):
        return f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Hola</title>
    </head>
    <body>
        {self.result}
        <br>
        <span>powered by M.E.L.I. preAlpha 0.0.1 </span>
    </body>
</html>"""
    def isValid(self):
        return self.analex.TK.tokenType in Tokens.tkns

    def codigo(self):
        #self.analex.TK.printTK()
        if self.isValid():
            self.sentencia()
            self.codigo()
    
    def sentencia(self):
        if self.analex.TK.tokenType == Tokens.TXT :
            self.text()

    def text(self):
        self.analex.analex()
        if self.analex.TK.tokenType == Tokens.PAP:
            self.analex.analex()
            if self.analex.TK.tokenType == Tokens.CAD:
                temp=f"<span>{self.analex.TK.value}</span>"
                self.analex.analex()
                if self.analex.TK.tokenType == Tokens.PCI:
                    self.result+=temp+" "
                    self.analex.analex()
                    #self.analex.TK.printTK()
                else:
                    print("ERROR: Se esperaba )")
            else:
                print("ERROR: Se esperaba una cadena")
        else:
            print("ERROR: Se esperaba (")
