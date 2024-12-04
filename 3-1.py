import re
inputText = open('03-input.txt', 'r').read()

finalMuliplication = 0

mulList = re.findall(r'mul\(\d+,\d+\)', inputText)

for i in mulList:
    currentMultiplicaton = (i[4:-1].split(','))
    finalMuliplication += int(currentMultiplicaton[0]) * int(currentMultiplicaton[1])

print(finalMuliplication)