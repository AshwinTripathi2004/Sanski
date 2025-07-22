# sanski_interpreter.py

import sys

variables = {}

def vad(statement):
    print(eval(statement, {}, variables))

def execute(line):
    line = line.strip()
    
    if line.startswith("vad("):
        content = line[4:-1]  # Get inside vad()
        vad(content)

    elif line.startswith("rachay"):
        parts = line.split()
        var_name = parts[1]
        value = eval(' '.join(parts[3:]), {}, variables)
        variables[var_name] = value

def run_sanski(filename):
    with open(filename, 'r') as file:
        code = file.read()
        lines = code.split('..')  # split by Sanski statement end
        for line in lines:
            if line.strip():
                execute(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sanski_interpreter.py <filename.sns>")
    else:
        run_sanski(sys.argv[1])
