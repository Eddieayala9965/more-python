def madlib(name, subject):
    return f"{name} fav subject is {subject}"

name = "eddie"
subject = "math"


print(madlib(name, subject))

def Fahrenheit(C):
    return (C * 9/5) + 32

def Celsius(F):
    return (F - 32) * 5/9


print(Fahrenheit(25))
print(Celsius(40))


def isEven(num):
    if num % 2 == 0:
        return True
    else: 
        return False
    

def isOdd(num):
    if num % 3 == 0:
        return True
    else:
        return False 
    

print(isEven(2))
print(isOdd(3))

mixNumList = [1, 3, 5, 7,7,8, 20, 22, 24, 33, 55, 30, 44 , 46]

def get_even_numbers(input_list):
    even_numbers = []
    for number in input_list:  
        if number % 2 == 0:  
            even_numbers.append(number)  
    return even_numbers  


def get_odd_numbers(input_list):
    odd_numbers = []
    for number in input_list:  
        if number % 3 == 0:  
            odd_numbers.append(number)  
    return odd_numbers  


def smallestNum(smallList):
    smallNum = []
    for small in smallList:
        if small <= 1:
            smallNum.append(small)
    return smallNum


def largestNum(longList):
    longNum = []
    for long in longList:
        if long > 40:
            longList.append(long)
    return longNum
    


print(get_even_numbers(mixNumList))
print(get_odd_numbers(mixNumList))
print(smallestNum(mixNumList))
print(largestNum(mixNumList))
