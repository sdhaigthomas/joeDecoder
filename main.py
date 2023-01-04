from os import system
import platform
#**************************************
def clear():
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")

def integerValidator(minimum, maximum, message):
        while True:
            num = input(message + "\n")
            try:
                num = int(num)
                if num < maximum or num < minimum:
                    return num
                else:
                    print("Please enter a valid number within 1 and " + str(maximum) + ".")
            except:
                print("Please enter a number.")
            clear()
#**************************************
toDecode = input("Paste in joe code here!\n")
clear()
rows = integerValidator(1,1000000000, "Please enter code's width(in charicters).")
#**************************************
toDecode = "011101000110100001101001011100110010000001101001011100110010000001101110011011110111010000100000011000100110100101101110011000010111001001111001001000000010100000110010001101000111100000110010001101000010100100000000000000000000000000000000111110111110100010111110100000100010100010100010100000100010100010100010100000100010100010100010100000100010100010100010100000100010100010100010111100100010100010111110100000100010100010101000100000100010100010101100100000100010100010100100100000100010100010100110100000100010100010100010100000100010100010100010100000111110111110100010"
lineCounter = 0
result = ""
#**************************************
for i in range(len(toDecode)):
    if lineCounter == rows:
        lineCounter = 0
        result += "\n"
    if int(toDecode[i]) == 1:
        result += "█"
    else:
        result += " "
    lineCounter += 1
    print(lineCounter)
#**************************************
print(result)