while True:
    print("\n=== Calc ===")

    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))

    print("Ops: +  -  *  /")
    op = input("Enter op: ")

    if op == '+':
        r = a + b
        print(f"{a} + {b} = {r}")
    elif op == '-':
        r = a - b
        print(f"{a} - {b} = {r}")
    elif op == '*':
        r = a * b
        print(f"{a} * {b} = {r}")
    elif op == '/':
        if b != 0:
            r = a / b
            print(f"{a} / {b} = {r}")
        else:
            print("Err: div by 0")
    else:
        print("Invalid op")

    c = input("Do you want to calc again? (y/n): ")
    if c.lower() != 'y':
        print("Bye!")
        break
