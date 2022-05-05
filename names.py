name = input("What is your name?").strip().title()


with open("names.txt", "a") as file:
    file.write(f"{name}\n")


