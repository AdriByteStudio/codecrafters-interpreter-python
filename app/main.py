import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    token_types = {
        "(": "LEFT_PAREN",
        ")": "RIGHT_PAREN",
    }

    for character in file_contents:
        if character in token_types:
            print(f"{token_types[character]} {character} null")
        elif character not in " \r\t\n":
            raise NotImplementedError("Scanner not implemented")

    print("EOF  null")


if __name__ == "__main__":
    main()
