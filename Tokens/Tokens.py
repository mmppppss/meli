class Tokens:
    TXT = "TXT"
    IMG = "IMG"
    LNK = "LNK"
    TLE = "TLE"
    LST = "LST"
    FRM = "FRM"
    INP = "INP"
    ROW = "ROW"
    TBL = "TBL"
    BTN = "BTN"

    BSL = "BSL"

    CAD = "CAD"
    PCI = "PCI"
    PAP = "PAP"

    COM = "COM"
    NAT = "NAT"

    reservados = ["text", "img", "link", "title", "list",
                  "form", "input", "row", "table", "button"]
    tkns = [TXT, IMG, LNK, TLE, LST, FRM, INP, ROW, TBL, BTN]
def reserved(id):
    if id in Tokens.reservados:
        return Tokens.tkns[Tokens.reservados.index(id)]
    else:
        return Tokens.NAT

class Token:
    def __init__(self) -> None:
        self.tokenType = Tokens.NAT
        self.value = None
    def createToken(self, type, content):
        self.tokenType = type
        self.value = content
    def printTK(self):
        print("<", self.tokenType, ",", self.value, ">", sep="")

