userStartNum = int(input("give me starting num "))
userEndNum = int(input("give me end num "))

while userStartNum <= userEndNum:
        userStartNum += 1
        print(userStartNum)

number_range = range(1, 21, 2)  

print("Choose a number from the following range:")
for number in number_range:
    print(number)

user_choice = int(input("Enter your choice: "))


if user_choice in number_range:
    print(f"You chose {user_choice}.")
else:
    print("Invalid choice. Please choose a number from the specified range.")







