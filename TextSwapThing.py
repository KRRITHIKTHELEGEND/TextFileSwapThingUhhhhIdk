
def swapText():
    text1 = input("Enter First File Name Here: ")
    print(" ")
    text2 = input("Enter Second File Name Here: ")

    with open(text1, 'r') as one:
        dataOne = one.read()

    with open(text2, 'r') as two:
        dataTwo = two.read()

    with open(text1, 'w') as one:
        one.write(dataTwo)

    with open(text2, 'w') as two:
        two.write(dataOne)
print(" ")
something = input("Start or Stop? : ")

if(something == 'start'):
    print(" ")
    swapText()

elif(something == 'stop'):
    print(" ")
    print("OK..")

else:
    print(" ")
    print("That's not a valid input DUMB")
