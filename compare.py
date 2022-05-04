def main():
    x = int(input("What is X: "))
    y = int(input("What is Y: "))
    compare(x, y)


def compare(x, y):
    if x < y:
        print("X is less than Y")
    elif x > y:
        print("X is greater than Y")
    else:
        print("X is equal to Y")


main()
