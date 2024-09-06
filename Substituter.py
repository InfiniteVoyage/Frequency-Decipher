text = "Jgnnq Yqtnf!"
text = text.lower()



def replaceLetters(repText:str):
    splitText = list(repText)
    ExcLetters = []
    UndoTexts = []

    print("input letter to replace with what letter example: a c (Will replace a's with c's) \n" )
    print(repText)
    print("\n")

    

    while True:
        excLetter = input().lower()
        excLetter = excLetter.split()

        

        if excLetter[0].lower() == "exit":
            break

        elif excLetter[0].lower() == "undo":
            if len(ExcLetters) > 0:
                ExcLetters.pop()
                if len(UndoTexts) > 0:
                    splitText = list(UndoTexts.pop())
                    print("\n")
                    print("".join(splitText))
                    print("\n")
            else:
                print("\n")
                print("".join(splitText))
                print("\n")
        else:
            tempTable = []
            UndoTexts.append("".join(splitText))
        
            for index, letter in enumerate(splitText):
                if excLetter[0] == letter:
                    

                    alrPlaced = any(index in table for table in ExcLetters)

                    if not alrPlaced:
                        splitText[index] = excLetter[1]
                        tempTable.append(index)
        

            
            ExcLetters.append(tempTable)


            print("\n")
            print("".join(splitText))
            print("\n")


replaceLetters(text)


