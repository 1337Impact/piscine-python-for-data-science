import sys

if len(sys.argv) == 1:
    exit()
elif len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
    exit()

try:
    argument = int(sys.argv[1])
    print("I'm Odd" if int(argument) % 2 else "I'm Even.")
except Exception:
    print("AssertionError: argument is not an integer")
