inputText = open('1-input.txt', 'r')

list1 = []
list2 = []

difference = 0

for i in range(1000):
    currentNumber = str.split(inputText.readline())
    list1.append(currentNumber[0])
    list2.append(currentNumber[1])

list1.sort()
list2.sort()

for i in range(1000):
    difference += abs(int(list1[i]) - int(list2[i]))

print(difference)