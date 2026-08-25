import sys


def main():
    while True:
        command = input("$ ")
        if command.startswith("echo"):
            print(command[5:])
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
