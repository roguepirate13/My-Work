l1 = ["laptop", "screen", "mouse", "pod", "camera"]
print(l1)
l1[3] = "Earpods"

l1.sort()
print(l1)
l1.sort(reverse=True)
print("\n",l1)

list1 = [1, 2, 3, 4, "a"]
list1.remove("a")
print("\n",list1)

l2 = [1, 2, 3, 4, "a"]
l1.append(l2)
print(l1, "\n")
list1.extend(l1)
print(list1, "\n")
for a in list1:
    print(a)
for i in range(len(list1)):
    print(list1[i])
print("\n", list1)
list1[1:3] = ["b"]
print(list1)
