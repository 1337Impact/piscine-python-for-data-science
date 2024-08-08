import sys
from ft_filter import ft_filter


def main():
    """
Main function of the script.

This function processes command-line arguments to filter and print\
words from a given string based on their length.
    """
    try:
        if len(sys.argv) != 3:
            raise
        int(sys.argv[2])
    except Exception:
        print("AssertionError: the arguments are bad")
        return

    S = sys.argv[1]
    N = int(sys.argv[2])

    words = [w for w in ft_filter(lambda w: True if len(w) > N
                                  else False, S.split())]
    print(words)


if __name__ == "__main__":
    main()
