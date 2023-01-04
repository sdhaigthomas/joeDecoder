from os import system
import platform
#**************************************************************************
class Assets:
    def __init__(self):
        self.toDecode = "011101000110100001101001011100110010000001101001011100110010000001101110011011110111010000100000011000100110100101101110011000010111001001111001001000000010100000110010001101000111100000110010001101000010100100000000000000000000000000000000111110111110100010111110100000100010100010100010100000100010100010100010100000100010100010100010100000100010100010100010100000100010100010100010111100100010100010111110100000100010100010101000100000100010100010101100100000100010100010100100100000100010100010100110100000100010100010100010100000100010100010100010100000111110111110100010"
        self.lineCounter = 0
        self.result = ""
        self.num = 0
        self.rows = 0
        self.run()
    def run(self):
        self.clear()
        self.settings()
        self.decripter()
#**************************************************************************
    def clear(self):
        if platform.system() == 'Windows':
            system("cls")
        else:
            system("clear")
#**************************************************************************
    def settings(self):
        self.toDecode = input("Paste in Joe-code here!\n")
        self.clear()
        while True:
            num = input("How wide is the Joe-code?\n")
            try:
                num = int(num)
                if num > 0:
                    self.rows = num 
                    return
                else:
                    print("Please enter a valid number above 1.")
            except:
                print("Please enter a number.")
            self.clear()
#**************************************************************************
    def decripter(self):
        lineCounter = 0
        for i in range(len(self.toDecode)):
            if lineCounter == self.rows:
                lineCounter = 0
                self.result += "\n"
            if int(self.toDecode[i]) == 1:
                self.result += "█"
            elif int(self.toDecode[i]) == 0:
                self.result += " "
            else:
                pass
            lineCounter += 1
            print(lineCounter)
        print(self.result)
#**************************************************************************
assets = Assets()
