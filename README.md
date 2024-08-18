# Username and Email Wordlist Generator

This Python script generates a wordlist of potential usernames and email addresses based on provided names. You can input a single name or a file containing multiple names, and optionally specify a domain to format the output as email addresses.

## Features

- Generates various username formats:
  - `first.last`
  - `f.last`
  - `first_last`
  - `first.l`
  - `flast`
  - `firstl`
  - `f.l`
  - `last.first`
  - `first-last`
  - `last.f`
- Supports single name input or multiple names from a file.
- Optionally appends a domain to generate email addresses.


# Usage
## Single Name Input
Generate a wordlist for a single name and save it to a file:

```bash
python main.py --name "John Doe" --output mywordlist.txt
```
## Multiple Names from a File
Generate a wordlist for multiple names provided in a file:

```bash
python main.py --file names.txt --output mywordlist.txt
```
## Adding a Domain for Email Format
Generate email addresses by appending a domain to each username format:

```bash
python main.py --name "John Doe" --domain yoooh.com --output mywordlist.txt
```

## Command-Line Options
- `-n`, `--name`: A single name to process (format: "First Last").
- `-f`, `--file`: A file containing multiple names (each on a new line).
- `-d`, `--domain`: Optional domain to append for email format.
- `-o`, `--output`: Output file name (default: `wordlist.txt`).
