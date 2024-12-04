inputText = open('01-input.txt', 'r')

list1 = []
list2 = []

similarityScore = 0

for i in range(1000):
    currentNumber = str.split(inputText.readline())
    list1.append(currentNumber[0])
    list2.append(currentNumber[1])

for i in list1:
    similarityScore += int(i) * int(list2.count(i))

print(similarityScore)