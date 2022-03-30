print("This is a Calculator\n "
      "Choice :\n"
      "1. Add two numbers\n"
      "2. Subtract a number from number\n"
      "3. Multiply two numbers\n"
      "4. Divide two numbers\n"
      "5. To find percentage\n"
      "6. To  finish calculating")
condn = True
while condn:

    choice = int(input("Enter your choice:"))
    if choice == 1:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        print(a, "+", b, "=", a + b)

    elif choice == 2:
        a1 = int(input("Enter A: "))
        b1 = int(input("Enter B: "))
        print(a1, "-", b1, "=", a1 - b1)

    elif choice == 3:
        a2 = int(input("Enter A: "))
        b2 = int(input("Enter B: "))
        print(a2, '*', b2, '=', a2 * b2)

    elif choice == 4:
        a3 = int(input("Enter A: "))
        b3 = int(input("Enter B: "))
        print(a3, '/', b3, '=', a3 / b3)

    elif choice == 5:
        m = int(input("Enter maximum number: "))
        o = int(input("Enter obtained number:"))
        print("Percentage of above input: ", (o / m) * 100)
    elif choice == 6:
        condn = False
    else:
        print("Please input appropriate choice")
