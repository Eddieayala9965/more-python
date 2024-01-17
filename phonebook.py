print("Electronic Phone Book")
print("=====================")
print("1. Look up an entry")
print("2. Set an entry")
print("3. Delete an entry")
print("4. List all entries")
print("5. Quit")

userInput = int(input("What do you want to do (1-5)? "))
phoneBook = {"name":"", "phone": ""}


if userInput == 2:
    usersName = input("Enter name: ")
    usersPhone = input("Enter Phone: ")
    if usersName == phoneBook["name"]:
        phoneBook["name"] = usersName
        if usersPhone == phoneBook["phone"]:
            phoneBook["phone"] = usersPhone
            print(f"name: {usersName}\nPhone: {usersPhone}")

if userInput == 1:
    usersName = input("What is the users name")
    if usersName != phoneBook["name"]:
        print("name is not found try again")
        userInput
    else:
        print(f"oh yes {usersName} is here!")
        print("Name " + phoneBook["name"])



            



