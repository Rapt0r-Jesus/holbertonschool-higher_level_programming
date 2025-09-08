#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        index = 0
        for val in row:
            if index != 0:
                print(" ", end="")
            print("{:d}".format(val), end="")
            index += 1
        print()
