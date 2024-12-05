inputText = open('04-input.txt', 'r').read()

xmasCount = 0
lineCount = 0
currentLine = 0

for i in inputText:
    if(i == '\n'): lineCount += 1

for i in range(len(inputText)):
    if(inputText[i] == '\n'): currentLine += 1
    if(inputText[i] != 'A'): continue
    
    if(inputText[i + 1] == '\n' or inputText[i - 1] == '\n'): continue
    
    if(currentLine >= lineCount): continue
    if(currentLine == 0): continue

    if(inputText[i + 140] == 'M' and inputText[i - 142] == 'M' and inputText[i + 142] == 'S' and inputText[i - 140] == 'S'): xmasCount += 1
    if(inputText[i + 140] == 'S' and inputText[i - 142] == 'S' and inputText[i + 142] == 'M' and inputText[i - 140] == 'M'): xmasCount += 1
    if(inputText[i + 140] == 'M' and inputText[i - 142] == 'S' and inputText[i + 142] == 'M' and inputText[i - 140] == 'S'): xmasCount += 1
    if(inputText[i + 140] == 'S' and inputText[i - 142] == 'M' and inputText[i + 142] == 'S' and inputText[i - 140] == 'M'): xmasCount += 1

print(xmasCount)