list1 = []
# SRN = Student Register Number


def read():
    n = int(input("Enter Size of list: "))
    for i in range(0, n):
        ele = int(input("Enter SRN: "))
        list1.append(ele)
    print(list1)


read()
f = input("You want to add some more SRNs..? Yes/No:")
if f == "Yes" or "yes":
    pos = int(input("Enter the position:"))
    m = int(input("Enter SRN:"))
    list1.insert(pos, m)
else:
    pass

