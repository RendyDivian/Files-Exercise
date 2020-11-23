import string

#auxiliary function
def replacePunc(stringValue):
    dPunc = string.punctuation

    for i in dPunc:
        stringValue = stringValue.replace(i,"")

    return stringValue

def hapax(filename):
    filename = filename.lower()

    readFile = open(filename,"r")
    data = readFile.read().lower()
    data = data.split()

    listOccurs = {}
    for i in data:
        current = replacePunc(i)
        listOccurs.setdefault(current,0)
        listOccurs[current] = listOccurs[current] + 1
        
    print("Total words : " + str(len(listOccurs)))
    print("Hapax words : ")
    for i in listOccurs.keys():
        nOccurs = listOccurs.get(i)
        if nOccurs == 1:
            print(i,end=",")

#most common word
    print("Most commond word")
    maximum = max(listOccurs,key = listOccurs.get)
    print(maximum,listOccurs[maximum])
            


hapax("gamlenorge")

