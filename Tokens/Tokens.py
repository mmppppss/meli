class Tokens:
    BOX = "BOX"
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
    NAM = "NAM"
    THM = "THM"

    CAD = "CAD"
    PCI = "PCI"
    PAP = "PAP"

    COM = "COM"
    NAT = "NAT"

    NLN = "NLN"#new line
    BLD = "BLD"#bold
    ITL = "ITL"#italic

    NUM = "NUM"
    ID_ = "ID_"
    CLS = "CLS"

    reservados = ["text", "image", "link", "title", "list",
                  "form", "input", "row", "table", "button", "box", "name", "theme", "n", "b", "i"]
    tkns = [TXT, IMG, LNK, TLE, LST, FRM, INP, ROW, TBL, BTN, BOX, NAM, THM,  NLN, BLD, ITL, BSL]
def reserved(id):
    if id in Tokens.reservados:
        return Tokens.tkns[Tokens.reservados.index(id)]
    else:
        return Tokens.NAT

class Token:
    def __init__(self) -> None:
        self.tokenType = Tokens.NAT
        self.value:str = ""
    def createToken(self, type, content):
        self.tokenType = type
        self.value = content
    def printTK(self):
        print("<", self.tokenType, ",", self.value, ">", sep="")

