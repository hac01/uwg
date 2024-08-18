import argparse
import os

def generate_wordlist(names, domain=None):
    wordlist = []
    for name in names:
        name = name.strip()
        if len(name.split()) != 2:
            continue
        
        first, last = name.split()
        first_initial = first[0]
        last_initial = last[0]

        formats = [
            f"{first}.{last}",
            f"{first_initial}.{last}",
            f"{first}_{last}",
            f"{first}.{last_initial}",
            f"{first_initial}{last}",
            f"{first}{last_initial}",
            f"{first_initial}.{last_initial}",
            f"{last}.{first}",
            f"{first}-{last}",
            f"{last}.{first_initial}"
        ]

        if domain:
            formats = [f"{entry}@{domain}" for entry in formats]
        
        wordlist.extend(formats)

    return wordlist

def write_to_file(wordlist, output_file):
    with open(output_file, 'w') as f:
        for username in wordlist:
            f.write(f"{username}\n")

def main():
    parser = argparse.ArgumentParser(description="Generate a wordlist from names.")
    parser.add_argument('-n', '--name', type=str, help="A single name to process (format: 'First Last')")
    parser.add_argument('-f', '--file', type=str, help="A file containing multiple names (each on a new line)")
    parser.add_argument('-d', '--domain', type=str, help="Optional domain to append for email format")
    parser.add_argument('-o', '--output', type=str, default='wordlist.txt', help="Output file name (default: wordlist.txt)")

    args = parser.parse_args()

    if args.name:
        names = [args.name]
    elif args.file:
        if not os.path.isfile(args.file):
            print(f"File {args.file} not found!")
            return
        with open(args.file, 'r') as f:
            names = f.readlines()
    else:
        print("Please provide a name or a file with names.")
        return

    wordlist = generate_wordlist(names, args.domain)
    write_to_file(wordlist, args.output)
    print(f"Wordlist generated successfully and saved to {args.output}!")

if __name__ == "__main__":
    main()
