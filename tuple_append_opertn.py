tuple1 = ()
tuple2 = ()
l1 = list(tuple1)
l2 = list(tuple2)

count = int(input("Enter the total count of elements of tuple1: "))
print("enter elements of tuple1: ")
for i in range(0, count):
    l1.append(int(input(">>>")))
count1 = int(input("Enter the total count of elements of tuple2: "))
print("enter elements of tuple2 :")
for i in range(0, count1):
    l2.append(input(">>>"))
tuple1 = tuple(l1)
tuple2 = tuple(l2)
print("tuple1:", tuple1)
print("tuple2:", tuple2)
tuple3 = (max(tuple1), max(tuple2))
print("Max of tuple1 & tuple2", tuple3)
