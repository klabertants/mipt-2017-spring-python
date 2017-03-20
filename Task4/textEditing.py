# Error codes:
# 1 - Not enough arguments.
# 2 - Can't format correctly.

import argparse
from sys import stdin, stdout

punctuation_marks = [',', '.', '?', '!', '-', ':', '’']


# Dividing text into paragraphs.

def parse_paragraphs(text):
    paragraphs = []
    current_paragraph = ''
    prev_line = ''
    for line in text:
        if line == '' and not prev_line == '':
            paragraphs.append(current_paragraph)
            current_paragraph = ''
        elif line == '' and prev_line == '':
            pass
        prev_line = line
        if not line == '':
            current_paragraph += line + '\n'
    if current_paragraph != '':
        paragraphs.append(current_paragraph)
    return paragraphs


# Forming right words from the text

def my_parser(text):
    words = []
    current_word = ""
    size = len(text)
    index = 0

    while (index < size):
        char = text[index]

        if (char.isalpha() or char.isdigit()) and index < size:
            current_word += char
            index += 1

        elif char == ' ':
            while char == ' ' and index < size:
                index += 1
                char = text[index % size]
            if (index == size):
                if current_word != "":
                    words.append(current_word)
                    current_word = ""
            elif punctuation_marks.count(char) > 0:
                while not (char.isalpha() or char.isdigit()) and index < size:
                    if punctuation_marks.count(char) > 0:
                        current_word += char
                    index += 1
                    char = text[index % size]
                if current_word != "":
                    words.append(current_word)
                    current_word = ""
            elif char.isalpha() or char.isdigit():
                if current_word != "":
                    words.append(current_word)
                    current_word = ""

        elif punctuation_marks.count(char) > 0:
            if current_word == "":
                exit(2)
                index += 1
            else:
                while not (char.isalpha() or char.isdigit()) and index < size:
                    if punctuation_marks.count(char) > 0:
                        current_word += char
                    index += 1
                    char = text[index % size]
                words.append(current_word)
                current_word = ""

        elif char == '\n':
            index += 1
            if current_word != "":
                words.append(current_word)
                current_word = ""

    if current_word != "":
        words.append(current_word)

    return words


# Format paragraph as task required.

def make_paragraph_great_again(paragraph, b, w):
    words = my_parser(paragraph)
    new_paragraph = []
    if b + len(words[0]) > w:
        exit(2)
    current_line = ''
    for i in range(b):
        current_line += ' '
    for word in words:
        if len(word) > w:
            exit(2)
        if len(current_line) + len(word) + int(len(current_line) > 0) \
                * 1 > w:
            new_paragraph.append(current_line)
            current_line = word
        elif len(current_line) + len(word) + int(len(current_line) > 0) \
                * 1 <= w:
            if current_line == b * " ":
                current_line += word
            else:
                current_line += ' ' + word
    if current_line != '':
        new_paragraph.append(current_line)
    return '\n'.join(new_paragraph)


# Parse arguments.

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default=stdin,
                    help='Input source')
parser.add_argument('-o', '--output', type=str, default=stdout,
                    help='Output source')
parser.add_argument('-l', '--line-length', type=int, default=None,
                    help='Length of the line')
parser.add_argument('-p', '--paragraph-spaces', type=int, default=None,
                    help='Paragraph spaces number')
args = parser.parse_args()

# Checking arguments.

if args.line_length is None or args.paragraph_spaces is None:
    exit(1)

b = args.paragraph_spaces
w = args.line_length

# Open sources.

if args.input != stdin:
    fin = open(args.input)
else:
    fin = stdin

if args.output != stdout:
    fout = open(args.output, 'w')
else:
    fout = stdout

# Writing to output.

paragraphs = parse_paragraphs([line.strip() for line in fin])
for (index, paragraph) in enumerate(paragraphs):
    fout.write(make_paragraph_great_again(paragraph, b=b, w=w))
    if index < len(paragraphs) - 1:
        fout.write("\n")

fout.close()
