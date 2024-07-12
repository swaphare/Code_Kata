import csv

class FixedWidthFileParser:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def parse_file(self):
        with open(self.input_file, "r", encoding='utf-8') as infile, open(self.output_file, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(["First Name", "Last Name", "Age", "City"])
            for line in infile:
                first_name = line[0:10].strip()
                last_name = line[10:20].strip()
                age = line[20:23].strip()
                city = line[23:38].strip()
                writer.writerow([first_name, last_name, age, city])

if __name__ == "__main__":
    parser = FixedWidthFileParser("fixed_width.txt", "output.csv")
    parser.parse_file()
