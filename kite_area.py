#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: September 2019
# This is program calculates  the area of a kite
#   with user input


def main():
    # this function calculates the area of a kite

    # input
    print("Dr.Bob wants to know the area of your kite for",
          "scientific research.")
    print("")
    length = int(input("Enter length of the kite (cm): "))
    width = int(input("Enter width of the kite (cm): "))

    # process
    area = (length*width)/2

    # output
    print("")
    print("Area is {}mm^2".format(area))


if __name__ == "__main__":
    main()
