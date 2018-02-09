import re
import sys
from babel.dates import format_date
from datetime import date


def interactively_substitute_fields(inputPath, outputPath):
    content = ""
    with open(inputPath, 'r') as texInput:
        content = texInput.read()

    match = re.search("<([^>]+)>", content)
    while match:
        if match.groups()[0] == "WRITING DATE":
            value = ("Le "
                     + format_date(date.today(), format='long', locale='fr'))
        else:
            value = input("{}: ".format(match.groups()[0]))

        content = (content[:match.start()]
                   + value
                   + content[match.end():])
        match = re.search("<([^>]+)>", content)

    with open(outputPath, 'w') as texOutput:
        texOutput.write(content)


if __name__ == '__main__':
    try:
        inputPath = sys.argv[1]
        outputPath = sys.argv[2]
    except IndexError:
        print("Usage:\n\t{} <input_path> <output_path>".format(__file__))
        exit()

    interactively_substitute_fields(inputPath, outputPath)
