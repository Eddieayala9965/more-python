numbers = [1, 2, 3, 4, 5, 99, 2600, 300]
sorted(numbers)
print(numbers)

word = "Hello"
emptyList = []

for letter in word:
    emptyList.append(letter)

emptyList.reverse()
print(emptyList)

emptyList2 = ""

for letter in emptyList:
    emptyList2 += letter

print(emptyList2)


names = ["Luffy", "Zoro", "Sanji", "Usopp", "Nami"]

if "Luffy" in names:
    names.remove("Luffy")
else:
    names.append("Luffy")   


print(names)
