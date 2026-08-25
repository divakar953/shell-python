import sys


def main():
    while True:
        command = input("$ ")
        if command.startswith("echo"):
            print(command[5:])
        else:
            break


if __name__ == "__main__":
    main()
