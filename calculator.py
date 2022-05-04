while True:
    try:
        x = float(input("What is X: "))
        y = float(input("What is Y: "))

    except ValueError:
        print("Float Number Required")
    else:
        break
z = x + y
print(f"{z:,.2f}")
