import sys


def main():
    while True:
        command = input("$ ")
        if command == "exit" or command == "type" or command == "echo":
            print(f"{command} is a shell builtin")
        else:
            print(f"{command}: not found")


if __name__ == "__main__":
    main()
