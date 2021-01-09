#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a Nested Loops program.


def area():

    userinput = input("Enter your grade: ")
    print("")

    if userinput == "4+":
        print("Your mark is 97%")
    elif userinput == "4":
        print("Your mark is 90%")
    elif userinput == "4-":
        print("Your mark is 83%")
    elif userinput == "3+":
        print("Your mark is 78%")
    elif userinput == "3":
        print("Your mark is 75%")
    elif userinput == "3-":
        print("Your mark is 71%")
    elif userinput == "2+":
        print("Your mark is 68%")
    elif userinput == "2":
        print("Your mark is 65%")
    elif userinput == "2-":
        print("Your mark is 61%")
    elif userinput == "1+":
        print("Your mark is 58%")
    elif userinput == "1":
        print("Your mark is 55%")
    elif userinput == "1-":
        print("Your mark is 51%")
    elif userinput == "R":
        print("Your mark is 30%")
    else:
        print("You are not enter your grade collectly. ")


def main():
    area()


if __name__ == "__main__":
    main()
