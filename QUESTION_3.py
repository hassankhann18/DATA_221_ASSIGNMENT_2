# NAME: HASSAN ADNAN
# UCID: 30217418
# QUESTION 3
from string import punctuation

def normalize_line(line):
    line = line.lower()              # Lower case the line

    line = "".join(line.split())    # removing all the whitespaces

    cleaned = ""
    for char in line:
        if char not in punctuation:
            cleaned += char

    return cleaned

def main():
    filename = "sample-file.txt"

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    group = {}

    for i in range (len(lines)):
        original = lines[i].rstrip("\n")
        norm = normalize_line(original)

        if norm in group:
            group[norm].append((i+1, original))
        else:
            group[norm] = [(i+1, original)]

    duplicate_sets = []

    for norm_key in group:
        if len(group[norm_key]) >= 2:
            duplicate_sets.append(group[norm_key])


    print("Duplicate sets:", len(duplicate_sets))

    for s in duplicate_sets:
        print(s)

if __name__ == "__main__":
    main()



