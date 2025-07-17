import sys
import os
import time
import re
# Parser

# List of all commands:
# print [text]
# wait [num]
# stop
# input [text]
# let [name] = [variable]

variables = {}  # Словарь для хранения переменных

def execute_command(command):
    parts = command.split()
    cmd = parts[0].lower()

    if cmd == "print":
        output = command[6:]  # Обрезаем "print "
        # Используем регулярные выражения для более точной замены
        for var_name, var_value in variables.items():
            output = re.sub(r'\b' + var_name + r'\b', str(var_value), output) # \b - граница слова
        try:
            result = eval(output, {}, variables)
            print(result)
        except (SyntaxError, NameError, TypeError):
            print(f"ERROR: Invalid expression: {output}")



    elif cmd == "wait":
        try:
            wait_time = float(parts[1])
            time.sleep(wait_time)
            if len(parts) > 2:
                print(" ".join(parts[2:]))
        except (ValueError, IndexError):
            print("ERROR: Invalid wait command. Use: wait <number> [text]")
    elif cmd == "stop":
        sys.exit()
    elif cmd == "input":
        print(input(" ".join(parts[1:])))
    elif cmd == "let":
        if len(parts) < 4 or parts[1] == '=' or parts[2] != '=':
            print("ERROR: Invalid let command. Use: let <variable_name> = <value>")
            return
        variable_name = parts[1]
        value_str = parts[3]

        try:
            value = int(value_str)
        except ValueError:
            try:
                value = float(value_str)
            except ValueError:
                if value_str.lower() in ["true", "false"]:
                    value = value_str.lower() == "true"
                else:
                    value = value_str.strip('"').strip("'")

        variables[variable_name] = value
    else:
        print(f"ERROR: Command '{cmd}' not found.")


def parse_and_execute_file(filename):
    if not filename.lower().endswith(".nxs"):
        print(f"Error: File ‘{filename}’ must have the ‘.nxs’ extension.")
        return

    if not os.path.exists(filename):
        print(f"Error: File ‘{filename}’ not found.")
        return

    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    execute_command(line)
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]  # Получаем имя файла из аргументов командной строки
        parse_and_execute_file(filename)
    else:
        print("Error: Please specify an .nxs file as an argument.")
