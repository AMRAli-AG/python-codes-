def tokenize(code):
    keywords = []
    identifiers = []
    numbers = []
    operators = []
    delimiters = []

    keyword_set = {'if', 'else', 'while'}
    operator_set = {'+', '-', '*', '/'}
    delimiter_set = {';', '(', ')', ','}

    current_token = ''
    i = 0
    while i < len(code):
        char = code[i]

        if char.isspace():
            i += 1
            continue

        if char.isalpha() or char == '_':
            while i < len(code) and (code[i].isalnum() or code[i] == '_'):
                current_token += code[i]
                i += 1
            
            if current_token in keyword_set:
                keywords.append(current_token)
            else:
                identifiers.append(current_token)
            current_token = ''
            continue

        if char.isdigit():
            while i < len(code) and code[i].isdigit():
                current_token += code[i]
                i += 1
            numbers.append(current_token)
            current_token = ''
            continue

        if char in operator_set:
            operators.append(char)
            i += 1
            continue

        if char in delimiter_set:
            delimiters.append(char)
            i += 1
            continue

        i += 1

    return keywords, identifiers, numbers, operators, delimiters

code = """if x > 10
while y < 20;"""

keywords, identifiers, numbers, operators, delimiters = tokenize(code)

print("Keywords:", keywords)
print("Identifiers:", identifiers)
print("Numbers:", numbers)
print("Operators:", operators)
print("Delimiters:", delimiters)
