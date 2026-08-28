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
    keywords = {
        "and": "AND",
        "class": "CLASS",
        "else": "ELSE",
        "false": "FALSE",
        "for": "FOR",
        "fun": "FUN",
        "if": "IF",
        "nil": "NIL",
        "or": "OR",
        "print": "PRINT",
        "return": "RETURN",
        "super": "SUPER",
        "this": "THIS",
        "true": "TRUE",
        "var": "VAR",
        "while": "WHILE",
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
        elif character == '"':
            start = i
            i += 1
            while i < len(file_contents) and file_contents[i] != '"':
                if file_contents[i] == "\n":
                    line += 1
                i += 1

            if i >= len(file_contents):
                print(
                    f"[line {line}] Error: Unterminated string.",
                    file=sys.stderr,
                )
                had_errors = True
            else:
                lexeme = file_contents[start : i + 1]
                literal = file_contents[start + 1 : i]
                print(f"STRING {lexeme} {literal}")
        elif character.isdigit():
            start = i
            while i < len(file_contents) and file_contents[i].isdigit():
                i += 1

            # Look for a fractional part.
            if (
                i + 1 < len(file_contents)
                and file_contents[i] == "."
                and file_contents[i + 1].isdigit()
            ):
                # Consume the ".".
                i += 1
                while i < len(file_contents) and file_contents[i].isdigit():
                    i += 1

            lexeme = file_contents[start:i]
            literal = str(float(lexeme))
            print(f"NUMBER {lexeme} {literal}")
            continue
        elif character.isalpha() or character == "_":
            start = i
            while i < len(file_contents) and (
                file_contents[i].isalnum() or file_contents[i] == "_"
            ):
                i += 1

            lexeme = file_contents[start:i]
            token_type = keywords.get(lexeme, "IDENTIFIER")
            print(f"{token_type} {lexeme} null")
            continue
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
