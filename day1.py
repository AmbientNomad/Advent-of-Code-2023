with open("Advent 2023\day 1 - input.txt") as file:
    inputLines = [eachEntry.rstrip() for eachEntry in file]

numFinder = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

numConverts = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


#def first(thisList):
#    return thisList[0]

#def last(thisList):
#    return thisList[len(thisList) - 1]

def getDigits(thisString):
    return [x for x in thisString if x.isdigit()]

def calVal(thisString):
    return getFirstNum(thisString) + getLastNum(thisString)

def calibrationValues(thisInput):
    return [int(calVal(getDigits(x))) for x in thisInput]

def getFirstNum(thisList):
    tempList = []

    for eachChar in thisList:
        tempList.append(eachChar)
        tempString = "".join(tempList)

        for eachNum in numFinder:

            if eachNum in tempString and eachNum.isdigit():
                return eachNum
            
            elif eachNum in tempString and eachNum.isalpha():
                return numConverts[eachNum]
            
            else:
                pass

def getLastNum(thisList):
    tempList = []

    for eachChar in reversed(thisList):
        tempList.insert(0, eachChar)
        tempString = "".join(tempList)

        for eachNum in numFinder:

            if eachNum in tempString and eachNum.isdigit():
                return eachNum
            
            elif eachNum in tempString and eachNum.isalpha():
                return numConverts[eachNum]
            
            else:
                pass

def convertInputLines(thisString):
    return getFirstNum(thisString) + getLastNum(thisString)


print("Part 1 answer: ")
print(sum(calibrationValues(inputLines)))

part2Input = [convertInputLines(x) for x in inputLines]

print("Part 2 answer: ")
print(sum(calibrationValues(part2Input)))
