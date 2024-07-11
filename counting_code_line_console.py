import sys

class LineCounter:
    def count_lines(self, code):
        in_block_comment = False
        code_lines = 0

        for line in code:
            stripped_line = line.strip()

            if in_block_comment:
                if stripped_line.endswith("'''") or stripped_line.endswith('"""'):
                    in_block_comment = False
                continue

            if stripped_line.startswith("'''") or stripped_line.startswith('"""'):
                in_block_comment = True
                continue

            if stripped_line == "" or stripped_line.startswith("#"):
                continue

            code_lines += 1

        return code_lines

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m counter.line_counter <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as file:
            code = file.readlines()

        counter = LineCounter()
        num_lines = counter.count_lines(code)
        print(f"Number of lines of code: {num_lines}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

if __name__ == '__main__':
    main()
