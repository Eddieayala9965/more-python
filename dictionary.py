hotel = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}


menu = input("Would you like to check in or check out? ")
floor1 = range(100, 199)
floor2 = range(200, 299)
floor3 = range(300, 399)
floor4 = range(400, 499)
floor5 = range(500, 599)



if menu == "check in":
    numOfPeople = int(input("how many poeple are in you party "))

    nameofPeople = str(input("What are the names? "))

    roomFloor = int(input("what floor would you like? (1-5) "))

    if roomFloor == 1:
       roomNum = int(input("What room number would you like "))
       if roomNum in floor1:
           print(f"you are all checked in on floor {roomFloor} room {roomNum}")
           hotel.setdefault(numOfPeople, {})[roomNum] = nameofPeople
    if roomFloor == 2:
        roomNum = int(input("What room number would you like "))
        if roomNum in floor2:
           print(f"you are all checked in on floor {roomFloor} room {roomNum}")
           hotel.setdefault(numOfPeople, {})[roomNum] = nameofPeople
    if roomFloor == 3:
        roomNum = int(input("What room number would you like "))
        if roomNum in floor3:
           print(f"you are all checked in on floor {roomFloor} room {roomNum}")
           hotel.setdefault(numOfPeople, {})[roomNum] = nameofPeople
    if roomFloor == 4:
        roomNum = int(input("What room number would you like "))
        if roomNum in floor4:
           print(f"you are all checked in on floor {roomFloor} room {roomNum}")
           hotel.setdefault(numOfPeople, {})[roomNum] = nameofPeople
    if roomFloor == 5:
        roomNum = int(input("What room number would you like "))
        if roomNum in floor5:
           print(f"you are all checked in on floor {roomFloor} room {roomNum}")
           hotel.setdefault(str(numOfPeople), {})[str(roomNum)] = nameofPeople.split()
    



print(hotel)







hotel = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}

menu = input("Would you like to check in or check out? ")
floor_ranges = {
    1: range(100, 199),
    2: range(200, 299),
    3: range(300, 399),
    4: range(400, 499),
    5: range(500, 599),
}

if menu == "check in":
    numOfPeople = int(input("How many people are in your party? "))
    nameofPeople = input("What are the names? ")
    roomFloor = int(input("What floor would you like? (1-5) "))
    roomNum = int(input("What room number would you like? "))
    if roomNum in floor_ranges.get(roomFloor, []):
        print(f"You are all checked in on floor {roomFloor} room {roomNum}")
        hotel.setdefault(str(numOfPeople), {})[str(roomNum)] = nameofPeople.split()
    else:
        print("Invalid room number for the chosen floor.")


print(hotel)
