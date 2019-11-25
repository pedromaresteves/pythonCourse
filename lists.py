demo_list = [1, "hello", 1.34, True, [1,2,3]]
colors = ['red', "green", "blue"]

numbersList = list((1,2,3,4))

print(numbersList)

rangepoo = list(range(1, 10))

poops = range(1, 5)
print(poops)
print(rangepoo)
print(dir(colors))
print(len(colors))
print(colors.index("green"))
print("green" in colors)
colors[1] = "yellow"
print(colors)
print("green" in colors)
colors.append("hello")
colors.extend(["bye", "poop"])
colors.extend(list(("bye", "poop")))

colors.insert(1, "RED")
colors.pop()
colors.remove("bye")
colors.sort(reverse=True)
print(colors)