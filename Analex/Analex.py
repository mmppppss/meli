from Reader.reader import Reader
from Tokens.Tokens import Tokens, Token, reserved
class Analex:
    def __init__(self, src:Reader) -> None:
        self.reader = src
        self.TK = Token()
    
    def test(self):
            c = self.reader.getCC()
            print(self.reader.pos, self.reader.getCC(), c, self.reader.content[self.reader.pos])
            self.reader.avanzar()
    def analex(self):
        c = ""
        ac = ""
        estado = 0
        #print("analex")
        #while True:
        while self.reader.pos <= len(self.reader.content)-1:
            c = self.reader.getCC()
            if estado == 0: 
                if c == " " or c == "\n":
                    self.reader.avanzar()
                elif c == "\"":
                    estado = 1
                    self.reader.avanzar()
                elif c.isalpha():
                    estado = 4
                    ac=ac+c
                    self.reader.avanzar()
                elif c == "(":
                    estado = 6
                    self.reader.avanzar()
                elif c == ")":
                    estado = 7
                    self.reader.avanzar()
                elif c == ",":
                    estado = 8
                    self.reader.avanzar()
                elif c == "\\":
                    estado = 9
                    self.reader.avanzar()
                else:
                    print("ERROR",c)
                    return
            elif estado == 1:
                if c == "\\":
                    #ac?
                    estado = 2
                    self.reader.avanzar()
                elif c == "\"":
                    estado = 3
                    self.reader.avanzar()
                else:
                    ac=ac+c
                    self.reader.avanzar()
                    estado = 1
            elif estado == 2:
                ac=ac+c
                estado = 1
                self.reader.avanzar()
            elif estado == 3:
                self.TK.createToken(Tokens.CAD, ac)
                return
            elif estado == 4:
                if c.isalpha():
                    ac += c
                    self.reader.avanzar()
                    estado = 4
                else:
                    estado = 5
            elif estado == 5:
                tkt = reserved(ac)
                if tkt != Tokens.NAT:
                    self.TK.createToken(tkt, "_")
                else:
                    print("ERROR id no identefied")
                return
            elif estado == 6:
                self.TK.createToken(Tokens.PAP, "_")
                return
            elif estado == 7:
                self.TK.createToken(Tokens.PCI, "_")
                return
            elif estado == 8:
                self.TK.createToken(Tokens.COM, "_")
                return
            elif estado == 9:
                self.TK.createToken(Tokens.BSL, "_")
                return


