import sys

def printStr(string):
   quoteFound = False
    toPrint = ""

    for i in string:
       if quoteFound and i != "\"":
          toPrint += i
        if "\"" == i:
           quoteFound = True
    print toPrint

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

   return c

def parseTokens(currLine):
   firstInt = True
    toPrint = False
    operation = j = k = stringToPrint = None

    if currLine[0] == "#": # Comment in code
       return 0

    tokens = currLine.split( )
    for i in tokens:
       if i.isdigit():
          if firstInt:
             firstInt = False
                j = int(i)
            else:
               k = int(i)
        elif i == "pt":
           toPrint = True
        elif i == "is":
           continue
        elif '\"' in i:
           if toPrint:
              break
           else:
              raise SyntaxError("Syntax issue")
        elif firstInt: # condition for var
           continue
        else:
           operation = i


    # Handle printing
    if toPrint:
       if j and k:
          print performOp(j, k, operation)
       else:
          printStr(currLine)
            return 0
    a = performOp(j, k, operation)
    return a


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
       print("Not enough arguments.")
        return
    except IOError:
       print("Invalid filename")
        return

    line = currFile.readline()
    while line:
       try:
          var = parseTokens(line)
       except ValueError:
          print("Invalid operand")
        line = currFile.readline()
    currFile.close()

if __name__ == "__main__": main()
