a = input("What is your fav color?\n")
print(a.upper(), "is a great color")
print("="*25)
b = str("I am Manoj, I am a sport enthusiast")
print(b.split())
print("="*25)
c = []
d = b.split()
for a in d:
    c.append(a)
print(c)
print("="*25)
for a in c:
    for i in a:
        print(i)
print("="*25)
print(len(b))
print("="*25)
print(b.upper())
print("="*25)
print(b.lower())
if "sport" in b:
    print("We have a match for 'sport'")

print("sports" in b)
print(b[:11], "\n", b[12:], "\nIn reverse:\n", b[::-1], "\n", b[1::1])
print(b.replace(" ", "-"))
print(b.startswith("I"))
print(b.endswith("."))
b = str("I am Manoj, I am a sport enthusiast")
print("I: ", b.count("I" or "i"), "\nA:", b.count("a"))
