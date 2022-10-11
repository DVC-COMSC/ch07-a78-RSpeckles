
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []
printList = []


for i in range(len(words)):
    for j in range(len(are)):
        if j == 0:
            prevIdx = 0
        else:
            prevIdx = idxlst[j-1]
        idxlst.append(words[i].find(are[j], prevIdx))
    if -1 not in idxlst and sorted(idxlst) == idxlst:
        printList.append(words[i])
    idxlst = []

print(printList)
        


# print the words that has 'a', 'r', 'e' in sequence

