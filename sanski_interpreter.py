# sanski_interpreter.py

import sys

variables = {}

def vad(statement):
    print(eval(statement, {}, variables))

def execute(line):
    line = line.strip()

    if not line or line.startswith("#"):
        return None

    # Handle print
    if line.startswith("vad("):
        content = line[4:-1]
        vad(content)

    # Variable declaration
    elif line.startswith("rachay"):
        parts = line.split()
        var_name = parts[1]
        value = eval(' '.join(parts[3:]), {}, variables)
        variables[var_name] = value

    # Handle conditional logic - replace with Python-style
    elif line.startswith("yadi") or line.startswith("yadi_anya") or line.startswith("anyatha"):
        converted = (
            line.replace("yadi", "if")
                .replace("yadi_anya", "elif")
                .replace("anyatha", "else")
        )
        return "CONTROL:" + converted
    
    return None

def run_sanski(filename):
    with open(filename, 'r') as file:
        code = file.read()
        lines = code.split('..')  # End of statement = double dots

        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            result = execute(line)

            # Handle control blocks (if, elif, else)
            if result and result.startswith("CONTROL:"):
                block = result[len("CONTROL:"):]
                block_code = block + "\n"

                i += 1
                # Collect the body of the block (next indented lines)
                while i < len(lines):
                    inner_line = lines[i].strip()
                    if inner_line.startswith("    ") or inner_line.startswith("\t") or inner_line == "":
                        if inner_line:
                            block_code += "    " + inner_line + "\n"
                        i += 1
                    else:
                        break

                try:
                    exec(block_code, {}, variables)
                except Exception as e:
                    print("Truti (Error):", e)
            else:
                i += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sanski_interpreter.py <filename.sns>")
    else:
        run_sanski(sys.argv[1])
