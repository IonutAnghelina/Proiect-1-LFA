fin = open("text.in", "r")
fout = open("text.out", "w")


def readDFA(inputFile):
    alphabet, states = set(), set()  # Both the alphabet and the number of states will be build based on the information in the input.
    # That's why we won't be limited to some states names or a set of letter in the alphabet

    l = inputFile.readline().split()

    noStates, noTransitions = int(l[0]), int(l[1])

    inputLines = []

    # print(alphabet)

    for i in range(noTransitions):
        currentLine = [x.strip() for x in inputFile.readline().split()]
        inputLines.append(currentLine)

        states.add(currentLine[0])
        states.add(currentLine[1])
        alphabet.add(currentLine[2])

    transitions = dict()

    for state in states:
        transitions[state] = dict()

    for line in inputLines:
        transitions[line[0]][line[2]] = line[1]

    initialState = inputFile.readline().split()[0].strip()
    finalStates = [x.strip() for x in inputFile.readline().split()][1:]

    return (sorted(list(states)), sorted(list(alphabet)), transitions, initialState, finalStates)


def process(DFAutomaton, word, currentState, currentStack, outputFile):
    if currentState == "ImpossibleState":
        print("NU", file=outputFile)
        return
    currentStack.append(currentState)
    if word == "":
        if currentState in DFAutomaton[4]:
            print("DA", file=outputFile)
            print(*currentStack, file=fout)
        else:
            print("NU", file=outputFile)
    else:
        process(DFAutomaton, word[1:], DFAutomaton[2][currentState].get(word[0], "ImpossibleState"), currentStack,
                outputFile)


DFAutomaton = readDFA(fin)

# print(DFAutomaton)

noWords = int(fin.readline().split()[0])
for i in range(noWords):
    currentWord = fin.readline().strip()
    process(DFAutomaton, currentWord, DFAutomaton[3], [], fout)
