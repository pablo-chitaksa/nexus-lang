import time
import sys

print("00     0   000000    0   0     0     0    000000")
print("0 0    0   0          0 0      0     0    0     ")
print("0  0   0   000000      0       0     0    000000")
print("0   0  0   0          0 0      0     0         0")
print("0    000   000000    0   0     0000000    000000")
print("Welcome to Nexus client!")
while True:
    cmd = input("cmd>")
    parts = cmd.split()
    # Stop command
    if cmd.lower() == "stop":
        sys.exit()
    # Help command
    elif cmd.lower() == "help":
        print("print [text] - Prints a [text].")
        print("stop - Stop the client.")
        print("wait [num] - Waits a [num]")
        print("input [text] - Input command.")
        print("let [varname] = [variable] - Add a variable (NOT WORKING IN CLIENT!)")
    # Print command
    elif len(parts) >= 2 and parts[0].lower() == "print":
        printtxt = " ".join(parts[1:])
        print(printtxt)
    # Wait command
    elif len(parts) >= 2 and parts[0].lower() == "wait":
        try:
            wait_time = float(parts[1])  # Преобразуем время ожидания в число
            time.sleep(wait_time)
            if len(parts) > 2:
                text_to_print = " ".join(parts[2:])
                print(text_to_print)
        # ValueError
        except ValueError:
            print("ERROR: Enter a NUMBER")
            sys.exit()
        # Exception as e
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit()
    # Input command
    elif len(parts) >= 2 and parts[0].lower() == "input":
        inputable = " ".join(parts[1:])
        input(inputable)
    elif cmd == "let":
        print("This command not working in client. Try make a .nxs file with adding this command and launch it with nexus.exe.")
    # Command not found error 
    else:
        print("ERROR: Command not found.")
        sys.exit()
