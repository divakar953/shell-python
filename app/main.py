import sys


def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        else:
            print(command[5:])


if __name__ == "__main__":
    main()
