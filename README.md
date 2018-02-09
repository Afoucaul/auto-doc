#Autodoc

This piece of software lets you generate a `.pdf` document from a `.tex` template, by interactively filling fields defined in the template.


##How to use it

Create your `.tex` template and leave tags enclosed in a pair of `<>`, such as `<FIELD1>`.
Then, run `make`.
You will be prompted to input the textual value of each field.
Then, a `.pdf` document will be generated from your `.text` template, each field having been replaced by the corresponding value.


##How it works

This piece of software relies on three files: `generate.py`, `Makefile`, and `template.tex`.

When the `make` command is run, the `generate.py` script is executed.
This script reads the input file, that is `template.tex`, and performs a regex lookup with the pattern `<[^>]+>` on this input.
For each result, the user is prompted to input the text they would like the field to be replaced with.
Then, the processed text is written to a temporary `.tex` file.

The temporary `.tex` file is then passed to `pdflatex`, and a document named `output.pdf` is produced.


##What it requires

- Python 3
    - The `babel` package
- pdfLaTeX
- GNU Make
