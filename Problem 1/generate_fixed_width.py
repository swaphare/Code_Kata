class FixedWidthFileGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.data = [
            ("Hamdi", "Hamza", "30", "DC"),
            ("James", "John", "35", "New York"),
            ("Samson", "Jack", "55", "Los Angeles")
        ]

    def generate_file(self):
        with open(self.filename, "w", encoding='utf-8') as f:
            for record in self.data:
                line = f"{record[0]:<10}{record[1]:<10}{record[2]:<3}{record[3]:<15}\n"
                f.write(line)

if __name__ == "__main__":
    generator = FixedWidthFileGenerator("fixed_width.txt")
    generator.generate_file()
