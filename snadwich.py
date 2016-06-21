import sys

def performOp(a, b, op):
    if "ps" == op: # +
        c = a + b
    elif "ms" == op: # -
        c = a - b
    elif "mx" == op: # *
        c = a * b
    elif "dx" == op: # /
        c = a / b
    elif "md" == op: # %
        c = a % b
    elif "ex" == op: # **
        c = a ** b
    else:
        raise ValueError("invalid expression")

def parseTokens(currLine):
    firstInt = True
    tokens = currLine.split( )
    for i in tokens:
        if i.isdigit():
            if firstInt:
                firstInt = False
                j = int(i)
            else:
                k = int(i)
        else:
            operation = i

    print(performOp(j, k, operation))


def parseLine(currLine):
    i = 0

    for i in currLine:
        print(i)

def main():
    currFile = None
    try:
        #parseLine(sys.argv[1])
        #parseTokens()
        currFile = open(sys.argv[1])
    except IndexError:
        print("Note enough arguments.")
        return

    line = currFile.readline()
    while line:
        try:
            parseTokens(line)
        except ValueError:
            print("Invalid operand")
        line = currFile.readline()
    currFile.close()

if __name__ == "__main__": main()
