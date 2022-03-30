def uni():
    for i in s2:
        if i in s1:
            pass
    else:
        s1.add(i)
        print("Union of S1 and S2:", s1)


def inter():
    s3 = set()
    for i in s2:
        if i in s1:
            s3.add(i)
    else:
        pass
    print("Intersection of S1 and S2:", s3)


s1 = set()
s2 = set()


def operation():

    n1 = int(input("Enter length of set1:"))
    for i in range(n1):
        s1.add(int(input(">>>")))
    n2 = int(input("Enter length of set2:"))
    for i in range(n2):
        s2.add(int(input(">>>")))
    print("S1:", s1)
    print("S2:", s2)




condn = True
while condn:
    ch1 = input("Do you wish to operate on Set?[Yes/No]: ")
    if ch1 == "Yes" or "yes":
        operation()
    ch = int(input("ENTER YOUR CHOICE: 1. UNION 2. INTERSECTION 3. EXIT"))
    if ch == 1:
        uni()
        print("If you want to continue to operate enter your choice")
    elif ch == 2:
        inter()
        print("If you want to continue to operate enter your choice")
    elif ch == 3:
        condn = False

    else:
        print("INVALID CHOICE")
