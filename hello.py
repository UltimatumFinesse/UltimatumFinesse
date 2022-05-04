# function
def main():
    # Ask user for their name
    # Remove whitespace from str and capitalise user's name
    name = input("What is your name? ").strip().title()
    # Call the hello function
    hello(name)


# Hello function
def hello(to):
    print(f"hello,", to)


main()
