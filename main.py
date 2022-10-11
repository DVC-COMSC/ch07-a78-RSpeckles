
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []
printList = []

#First loop runs through each of the words in the list
#second loop looks for the index of the letters a, r, and e in the word being currently evaluated and adds them to a list
for i in range(len(words)):
    for j in range(len(are)):
        #prevIdx is used to determine the starting index of the find command
        #This makes sure that only letters after the last found letter are evaluated
        #letters in "are" that come out of order should not be counted, eg. the first e in "assertive"
        if j == 0:
            prevIdx = 0
        else:
            prevIdx = idxlst[j-1]
        idxlst.append(words[i].find(are[j], prevIdx))
    #This if statement checks that all of the values in "are" have been found and they come in order
    if -1 not in idxlst and sorted(idxlst) == idxlst:
        printList.append(words[i])
    idxlst = []

print(printList)
        


# print the words that has 'a', 'r', 'e' in sequence

