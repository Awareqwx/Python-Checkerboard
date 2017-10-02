import sys

def checkerboard():
    for i in range(0, 9):
        for j in range(0, 9):
            if bool((i + j) % 2):
                sys.stdout.write("█")
            else:
                sys.stdout.write(" ")
        print

def scalableCheckerboard(a, b):
    for i in range(0, a):
        for j in range(0, b):
            if bool((i + j) % 2):
                sys.stdout.write("█")
            else:
                sys.stdout.write(" ")
        print

checkerboard()
print
scalableCheckerboard(3, 3)
print
scalableCheckerboard(12, 25)
print
scalableCheckerboard(50, 5)
print
scalableCheckerboard(2, 100)