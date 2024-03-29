import sys
import csv


def main():
    file_in = get_input_file()
    file_out = get_output_file()
    repertoire = read_file(file_in)
    create_file(repertoire, file_out)


# Get input file
def get_input_file():
    if len(sys.argv) < 2:
        sys.exit("Usage <input file.csv> <output file.txt")
    return sys.argv[1]


# Get output file
def get_output_file():
    if len(sys.argv) < 3:
        sys.exit("Usage <input file.csv> <output file.txt")
    return sys.argv[2]


# Read the file
def read_file(file_in):
    repertoire = []
    with open(file_in) as file:
        reader = csv.DictReader(file)
        for row in reader:
            repertoire.append(
                {"Name": row["Name"], "Surname": row["Surname"], "Piece": row["Piece"]})
    return repertoire


# Create sorted file
def create_file(repertoire, file_out):
    with open(file_out, "w") as file:
        for author in sorted(repertoire, key=lambda author: author["Surname"]):
            file.write("{0} {1}, {2}\n".format(author["Surname"], author["Name"], author["Piece"]))
        return True


if __name__ == "__main__":
    main()