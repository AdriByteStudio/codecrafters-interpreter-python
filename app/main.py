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
        ",": "COMMA",
        ".": "DOT",
        "-": "MINUS",
        "+": "PLUS",
        ";": "SEMICOLON",
        "*": "STAR",
        "(": "LEFT_PAREN",
        ")": "RIGHT_PAREN",
        "{": "LEFT_BRACE",
        "}": "RIGHT_BRACE",
    }
    had_errors = False
    i = 0
    line = 1

    while i < len(file_contents):
        character = file_contents[i]

        if character in token_types:
            print(f"{token_types[character]} {character} null")
        elif character == "=":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("EQUAL_EQUAL == null")
                i += 2
                continue
            else:
                print("EQUAL = null")
        elif character == "!":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("BANG_EQUAL != null")
                i += 2
                continue
            else:
                print("BANG ! null")
        elif character == "<":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("LESS_EQUAL <= null")
                i += 2
                continue
            else:
                print("LESS < null")
        elif character == ">":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "=":
                print("GREATER_EQUAL >= null")
                i += 2
                continue
            else:
                print("GREATER > null")
        elif character == "/":
            if i + 1 < len(file_contents) and file_contents[i + 1] == "/":
                # A comment goes until the end of the line.
                while i < len(file_contents) and file_contents[i] != "\n":
                    i += 1
                continue
            else:
                print("SLASH / null")
        elif character == "\n":
            line += 1
        elif character not in " \r\t":
            print(
                f"[line {line}] Error: Unexpected character: {character}",
                file=sys.stderr,
            )
            had_errors = True

        i += 1

    print("EOF  null")

    if had_errors:
        exit(65)


if __name__ == "__main__":
    main()
