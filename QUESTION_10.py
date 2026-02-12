# NAME: HASSAN ADNAN
# UCID: 30217418
# QUESTION 10


def find_lines_containing(filename, keyword):
    """
        Returns a list of (line_number, line_text) for lines that contain
        the keyword (case-insensitive). Line numbers start at 1.
        """
    results = []
    keywords = keyword.lower()

    with open(filename, 'r') as f:
        for i, line in enumerate(f, start=1):
            if keyword in line.lower():
                results.append((i, line.strip()))

    return results

def main():
    filename = "sample-file.txt"
    keyword = "lorem"

    matches = find_lines_containing(filename, keyword)

    print("Total Matching Lines:", len(matches))

    print("First 3 lines:")
    for line_number, line_text in matches[:3]:     # Printing first 3 lines
        print(line_number,":", line_text)

if __name__ == "__main__":
    main()


