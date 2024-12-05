inputText = open('04-input.txt', 'r').read()

xmasCount = 0
lineCount = 0
currentLine = 0

for i in inputText:
    if(i == '\n'): lineCount += 1

for i in range(len(inputText)):
    if(inputText[i] == '\n'): currentLine += 1
    if(inputText[i] != 'X'): continue

    if(inputText[i + 1] == 'M' and inputText[i + 2] == 'A' and inputText[i + 3] == 'S'): xmasCount += 1
    if(inputText[i - 1] == 'M' and inputText[i - 2] == 'A' and inputText[i - 3] == 'S'): xmasCount += 1

    if(currentLine <= lineCount - 3):
        if(inputText[i + 141] == 'M' and inputText[i + 282] == 'A' and inputText[i + 423] == 'S'): xmasCount += 1
        if(inputText[i + 142] == 'M' and inputText[i + 284] == 'A' and inputText[i + 426] == 'S'): xmasCount += 1
        if(inputText[i + 140] == 'M' and inputText[i + 280] == 'A' and inputText[i + 420] == 'S'): xmasCount += 1
    
    if(currentLine >= 3):
        if(inputText[i - 141] == 'M' and inputText[i - 282] == 'A' and inputText[i - 423] == 'S'): xmasCount += 1
        if(inputText[i - 142] == 'M' and inputText[i - 284] == 'A' and inputText[i - 426] == 'S'): xmasCount += 1
        if(inputText[i - 140] == 'M' and inputText[i - 280] == 'A' and inputText[i - 420] == 'S'): xmasCount += 1

print(xmasCount)