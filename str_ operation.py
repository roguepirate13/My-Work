str1 = input("Please Enter the main string = ")


def substr():
    
    index1 = int(input("Enter Index 1 = "))
    index2 = int(input("Enter Index 2 = "))
    substring = str1[index1:index2]
    
    print("Substring extracted from", index1, "to", index2, " = ", substring)


substr()c
s = input("What is your favourite color\n")
print("So your favourite color is", s.upper())
a = input("Where are you from?")
print("Elements of your string:", a.split())