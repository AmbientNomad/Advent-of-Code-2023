import re

with open("Advent 2023\day 2 - input.txt") as file:
    inputLines = [eachEntry.rstrip() for eachEntry in file]


"""
This lil' bunch of code at the start is going to take our input, and turn
it into a usable dictionary that will probably be completely invailidated
by part 2. Whatever.

Spoiler: It wasn't invalidated! In fact it made part 2 a breeze.
"""

gameDict = {}

for eachGame in inputLines:
    gameNumber = re.search(r'(Game \d+)', eachGame)
    currentGame = gameNumber.group()
    gameDict.update({currentGame: {"red": "", "green": "", "blue": ""}})

    for eachColor in ["red", "green", "blue"]: 
        cubeQuant = re.findall(r'(\d|\d\d) {}'.format(eachColor), eachGame)
        x = max([int(x) for x in cubeQuant]) #Find the highest number from
                                             #a specific color.
        gameDict[currentGame].update({eachColor: x})


def part1ColorCheck(red, green, blue):
    """
    Part 1 uses hard coded values for the maximum of any given color, so I
    decided to keep it simple and return true or false based on
    whether or not those values could be met.
    """

    if red <= 12 and green <= 13 and blue <= 14:
        return True
    
    else: return False

    
def part1GameCheck(gameID):
    """
    First set the values of red, green and blue to match their quantities
    from the dictionary. Then, check to see if those quantities match the
    values for part 1. Then, return only the numeric value from the game
    id, or return 0.
    """

    red = gameDict[gameID]["red"]
    green = gameDict[gameID]["green"]
    blue = gameDict[gameID]["blue"]

    IDNum = re.search(r'\d+', gameID)

    if part1ColorCheck(red, green, blue):
        return int(IDNum.group())
    
    else: return 0


def part2Power(gameID):
    """
    First set the values of red, green and blue to match their quantities
    from the dictionary. Multiply each together, and return that value.
    """

    red = gameDict[gameID]["red"]
    green = gameDict[gameID]["green"]
    blue = gameDict[gameID]["blue"]

    return red * green * blue


part1 = str(sum([part1GameCheck(x) for (x) in gameDict]))
part2 = str(sum(part2Power(x) for x in gameDict))

print("Part 1 Answer: " + part1)
print("Part 2 Answer: " + part2)
