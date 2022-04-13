import pandas

d = {
  "Company": "RR",
  "Model": "Phantom",
  "Make": 2018
}
print(d)
print("*"*20)
l1 = [d["Company"], d["Model"], d["Make"]]
for x in d.keys():
    print(x)
for a in d.values():
    print(a)
print(l1)
print("*"*20)
for x, y in d.items():
    print(x, y)
print("*"*20)
d.pop("Make")
print(d)
print("*"*20)
d1 = d.copy()
l2 = ["Lamborghini", "Huracan", 2016]
d1[l2[0]], d1[l2[1]], d1[l2[2]] = "RR", "Phantom", 2018
print(pandas.Series(d1))
print("*"*20)


car1 = {
  "company": "Lamborghini",
  "model": "Avatendor"
}
car2 = {
  "company": "Tata",
  "model": "Curvv"
}
car3 = {
  "company": "Mahindra",
  "model" : "XUV700"
}

mycollection = {
  "Car1" : pandas.Series(car1),
  "Car2" : pandas.Series(car2),
  "Car3" : pandas.Series(car3)
}

print(pandas.Series(mycollection))
