import sys


def main():
    """
    Main function of the script.

    This function counts various types of characters in a given input text.
    """
    inputValue = ""
    if (len(sys.argv) > 2):
        print("AssertionError")
        exit()
    elif (len(sys.argv) == 1):
        inputValue = input("What is the text to count?\n")
    else:
        inputValue = sys.argv[1]
    upperCase = 0
    lowerCase = 0
    punctuation = 0
    digits = 0
    spaces = 0
    for e in inputValue:
        if (e.isupper()):
            upperCase += 1
        elif (e.islower()):
            lowerCase += 1
        elif (e in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
            punctuation += 1
        elif (e.isdigit()):
            digits += 1
        elif (e.isspace() or e == '\r'):
            spaces += 1
    print(f"The text contains {len(inputValue)} characters:")
    print(upperCase, "upper letters")
    print(lowerCase, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


if __name__ == "__main__":
    main()
