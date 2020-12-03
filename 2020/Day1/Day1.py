# Read input file
file1 = open('2020/Day1/input.txt', 'r') 
Lines = file1.readlines() 

myList = []
for line in Lines:
    
    myList.append(int(line))

for idx, val in enumerate(myList):
    print(idx, val)

def theCheck(inputList):
    
    for idx, val in enumerate(inputList):
        for idx2, val2 in enumerate(inputList):
            for idx3, val3 in enumerate(inputList):
                if idx == idx2:
                    continue
                elif idx2 == idx3:
                    continue

                else:
                    if (val + val2 + val3) == 2020:
                        print("Found 2020! " + str(val) + ", " + str(val2) + ", " + str(val3))
                '''
                    else:
                        print("Not 2020! " + str(val) + ", " + str(val2))
'''

theCheck(myList)