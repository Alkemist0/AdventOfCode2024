inputText = open('02-input.txt', 'r')

safeReports = 0

for i in range(1000):
    currentReport = str.split(inputText.readline())
    
    for j in range(len(currentReport)):
        currentReport[j] = int(currentReport[j])
    
    if(currentReport[1] > currentReport[0]):
        levelIncreasing = True
    else:
        levelIncreasing = False
    
    skipped = False
    
    for j in range(2, len(currentReport)):
        if(levelIncreasing and currentReport[j] > currentReport[j-1] and abs(currentReport[j] - currentReport[j-1]) <= 3):
            if(j == len(currentReport) - 1):
                safeReports += 1
            continue
        elif(levelIncreasing and currentReport[j] > currentReport[j-2] and abs(currentReport[j] - currentReport[j-2]) <= 3 and not skipped):
            if(j == len(currentReport) - 1):
                safeReports += 1
            skipped = True
            continue
        elif(currentReport[j] < currentReport[j-1] and not levelIncreasing and abs(currentReport[j] - currentReport[j-1]) <= 3):
            if(j == len(currentReport) - 1):
                safeReports += 1
            continue
        elif(currentReport[j] < currentReport[j-2] and not levelIncreasing and abs(currentReport[j] - currentReport[j-2]) <= 3 and not skipped):
            if(j == len(currentReport) - 1):
                safeReports += 1
            skipped = True
            continue
        else:
            break

print(safeReports)