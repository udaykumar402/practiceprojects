
"""python code to match the string which is given by teacher,that student need to guess in 6 attempts"""


def Task(Text):  # user defined function

    flag = True  # flag is a variable

    for x in range(6):  # range for max 6 attempts
        student = input("enter the 5 character word, which is selected by the student:")  # taking string for comparison

        if student.isupper() and student.isalpha():   # checking the give string is in uppercase or not

            if len(Text) == len(student):  # comparing length of strings

                for i in Text:  # Loop for checking each character

                    if i in student:  # checking presents

                        if student.index(i) == Text.index(i):  # comparing the index of characters
                            print(i, "is present in teacher's word in right position")

                        else:
                            print(i, "is present in teacher's word, but in different position")
                            flag = False  #
                        """if any one of the character index is not matched then flag become False else  flag remain as 
                        True """

                    else:
                        print(i, "does not exist in teacher's word")
                        flag = False
                        """if character does not exist in teacher's word then flag become False else flag remain True"""

                if flag:  # if flag True this block will be executed
                    print("congratulations! string successfully matched....")
                    print("..........you won the game............")
                    break

                else:  # if flag False this block will be executed
                    print("sorry string doesn't matched..., please try again with new string")
                    continue  # to take input again if given string not matched

            else:
                print("invalid string entered...please try again!")
            continue  # to take input again if given string is invalid

        else:
            print("you have entered invalid string please enter the string in capital letters only..")
            continue

    else:   # if there is no chance to give input then only this block will be executed
        print("------you loose the game-------")


Task("TREND")  # Function calling to run the function
