# Laura Burroughs
# CPSC 4970
# 3 April 2026
# Project 4

def fibonacci():
    a, b = 1, 1

    while True:
        yield a
        a, b = b, a+b
