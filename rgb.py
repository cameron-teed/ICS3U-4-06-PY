#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Oct 2019
# This is a program that finds the combinations of colors

import math


def main():

    counter = 0
    counter1 = 0
    counter2 = 0

    for counter in range(0, 255):
        for counter1 in range(0, 255):
            for counter2 in range(0, 255):
                print("{}, {}, {}".format(counter, counter1, counter2))


if __name__ == "__main__":
    main()
