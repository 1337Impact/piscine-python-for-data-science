import sys


def char_to_morse_code(c):
    """translate character to its coresponding in morese code

    Args:
        c (char): character to be translated

    Returns:
        string: translated character in morse code
    """
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    return (morse_code_dict[c.upper()])


def main():
    """main function responsable for taking argument and translating it
    to morse code.
    """
    if (len(sys.argv) != 2):
        print("AssertionError: the arguments are bad")
        return
    try:
        res = [char_to_morse_code(e) for e in sys.argv[1]]
        print(' '.join(res))
    except Exception:
        print("AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()
