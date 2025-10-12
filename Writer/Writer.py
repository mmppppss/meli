class Writer:
    def __init__(self, fileOut, parser):
        self.out = fileOut
        self.parser = parser

    def write(self):
        with open(self.out, "w") as fileOut:
            fileOut.write(self.parser.getResult())
            fileOut.close()
