class Reader():
    def __init__(self, filename:str = "", content=""):
        super(Reader, self).__init__()
        self.content = content
        self.filename= filename
        self.size = 0
        self.pos = 0
        self.lines = []
        self.countlines = 0
        self.loadFile()
    
    def loadFile(self):
        if self.filename != "":
            try:
                with open(self.filename,'r') as file:
                    self.content = file.read()
                    i = 0;
                    lines = self.content.splitlines()
                    posi = 0
                    for line in lines:
                        self.countlines+=1
                        self.lines.append(posi)
                        posi += len(line)
                        i+=1
                    self.content+='\0'
                    self.size = len(self.content)
            except FileNotFoundError:
                print("Archivo", self.filename, "no encontrado")
                exit(1)
        else:
            i = 0;
            lines = self.content.splitlines()
            posi = 0
            for line in lines:
                self.countlines+=1
                self.lines.append(posi)
                posi += len(line)
                i+=1
            self.content+='\0'
            self.size = len(self.content)

    def getCC(self):
        return self.content[self.pos]

    def getLine(self, line:int):
        return self.content.splitlines()[line-1]

    def avanzar(self):
        self.pos=self.pos+1
