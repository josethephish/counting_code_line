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
