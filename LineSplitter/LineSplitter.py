"""
Tammas Hicks
CIS315
Assignment 6

This is a program for determining whether sentences in a file can be split such
that each word is a valid word. The first part in running the program will be
to construct a dictionary from the passed dictionary text file, which can be
used to verify the existence of tested 'words'.
"""
import sys

word_dict = {}


def filler():
    with open('diction10k.txt', 'r') as mydoc:
        line = mydoc.readline()

        while line:
            word_dict[line.strip("\n")] = line.strip("\n")
            line = mydoc.readline()

# using the with command closes it when it goes out of scope

def split(line: str):
    n = len(line) + 1
    phraseArray = [0] * n
    for x in range(n):
        if line[:x] in word_dict:
            phraseArray[x] = line[:x]

    for i in range(n):
        for j in range(i,n):
            if line[i:j] in word_dict:
                if phraseArray[i] != 0:
                    phraseArray[j] = phraseArray[i] + " " + line[i:j]
    if phraseArray[n - 1] != 0:
        sys.stdout.write("YES, can split.\n")
        sys.stdout.write(f"{phraseArray[n - 1]}\n\n")

    else:
        sys.stdout.write("No, cannot split.\n\n")



def dictsplit(line: str):
    """
    This method will print out every possible way a line can be split into a legal sentence
    """
    phraseDict = {}
    n = len(line) + 1
    for x in range(n):
        if line[:x] in word_dict:
            phraseDict[x] = [line[:x]]

    for i in range(n):
        for j in range(i,n):
            if line[i:j] in word_dict:
                if i in phraseDict:
                    if j in phraseDict:
                        phraseDict[j] = phraseDict[j] + [word + " " + line[i:j] for word in phraseDict[i]]
                    else:
                        phraseDict[j] = [word + " " + line[i:j] for word in phraseDict[i]]
    if (n - 1) in phraseDict:
        sys.stdout.write("YES, can be split.\n")
        for word in phraseDict[n - 1]:
            print(word)
    else:
        print("No, cannot be split")




def recursive_split(line):
    n = len(line) + 1
    if (n == 1):
        return True, ""
    else:
        for i in range(n):
            if line[0:i] in word_dict:
                rightSplit = recursive_split(line[i:])
                if rightSplit[0] is True:
                    return True, line[0:i] + " " + rightSplit[1]

    return False, ""



def dyn_prog():
    count = int(sys.stdin.readline())

    for i in range(count):
        line = sys.stdin.readline().strip("\n")
        sys.stdout.write(f"Phrase {i + 1}:\n{line}\n\n")
        sys.stdout.write(f"Output {i+1}:\n")
        dictsplit(line)


if __name__ == '__main__':
    filler()
    dyn_prog()