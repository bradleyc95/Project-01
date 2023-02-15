# Bradley Cox, Project 1

import sys

filename = sys.argv[1]
file = open(filename, 'r')
sequenceArray = [None] * 100

def insert(pos, type, sequence):
    if type == 'DNA' and 'U' not in sequence:
        if pos < 100:
            sequenceArray[pos] = (type, sequence)
        else:
            print(f"{pos} is an invalid index")
    elif type == 'RNA' and 'T' not in sequence:
        if pos < 100:
            sequenceArray[pos] = (type, sequence)
        else:
            print(f"{pos} is an invalid index")
    else:
        print(f"{sequence} is not a valid {type} sequence")

def printArray():
    posCount = 0
    for each in sequenceArray:
        if each != None:
            print(f"[{posCount}]{each[0]}: {each[1]}")
        posCount += 1

def printArrayAtPos(pos):
    if pos > 99:
        print(f"{pos} is an invalid index")
    elif sequenceArray[pos] != None:
        print(f"[{pos}]{sequenceArray[pos][0]}: {sequenceArray[pos][1]}")
    else:
        print(f"No sequence exists at position {pos}, unable to print")

def remove(pos):
    if pos > 99:
        print(f"{pos} is an invalid index")
    elif sequenceArray[pos] != None:
        sequenceArray[pos] = None
    else:
        print(f"No sequence exists at position {pos}, unable to remove")

def copy(pos1, pos2):
    if pos1 > 99:
        print(f"{pos1} is an invalid index")
    elif pos2 > 99:
        print(f"{pos2} is an invalid index")
    elif sequenceArray[pos1] != None:
        sequenceArray[pos2] = sequenceArray[pos1]
    else:
        print(f"No sequence exists at position {pos1}, unable to copy")

def swap(pos1, start1, pos2, start2):
    if pos1 > 99:
        print(f"{pos1} is an invalid index")
    elif pos2 > 99:
        print(f"{pos2} is an invalid index")
    elif sequenceArray[pos1] == None or sequenceArray[pos2] == None:
        print("No sequence exists at one or more specified position, unable to swap")
    elif sequenceArray[pos1][0] != sequenceArray[pos2][0]:
        print("Error, unable to swap tails of non-matching sequence types")
    else:
        if start1 > len(sequenceArray[pos1][1]):
            print(f"Error, the value of start1 is greater than the length of the sequence, unable to swap")
        else:
            type = sequenceArray[pos1][0]
            seq1 = sequenceArray[pos1][1]
            seq2 = sequenceArray[pos2][1]

            tail1 = seq1[start1:]
            tail2 = seq2[start2:]
            seq1 = seq1[:start1] + tail2
            seq2 = seq2[:start2] + tail1

            insert(pos1, type, seq1)
            insert(pos2, type, seq2)

def transcribe(pos):
    if pos > 99:
        print(f"{pos} is an invalid index")
    elif sequenceArray[pos] == None:
        print(f"No sequence exists at position {pos}, unable to transcribe")
    elif sequenceArray[pos][0] == 'RNA':
        print(f"Sequence at position {pos} is RNA, unable to transcribe")
    else:
        seq = sequenceArray[pos][1]
        seq = seq.replace('T', 'U')

        insert(pos, 'RNA', seq)

for line in file:
    instruction = line.split()
    
    if instruction[0] == 'insert':
        insert(int(instruction[1]), instruction[2], instruction[3])
    elif instruction[0] == 'print':
        try:
            printArrayAtPos(int(instruction[1]))
        except IndexError:
            printArray()
    elif instruction[0] == 'remove':
        remove(int(instruction[1]))
    elif instruction[0] == 'copy':
        copy(int(instruction[1]), int(instruction[2]))
    elif instruction[0] == 'swap':
        swap(int(instruction[1]), int(instruction[2]), int(instruction[3]), int(instruction[4]))
    elif instruction[0] == 'transcribe':
        transcribe(int(instruction[1]))
