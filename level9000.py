def make_change(total_charge, payment):
   diff = round(payment - total_charge, 2)
   diffFormat = "{:.2f}".format(diff)


   return print("Your change is %s" % diffFormat)


def count_bills(payment_in_bills):
    payment_in_bills = int(payment_in_bills)
    hundreds = payment_in_bills // 100
    payment_in_bills %= 100
    fifties = payment_in_bills // 50
    payment_in_bills %= 50
    twenties = payment_in_bills // 20
    payment_in_bills %= 20
    tens = payment_in_bills // 10
    payment_in_bills %= 10
    fives = payment_in_bills // 5
    payment_in_bills %= 5
    ones = payment_in_bills // 1
    payment_in_bills %= 1
    return print("Hundreds: %s, Fifties: %s, Twenties: %s, Tens: %s, Fives: %s, Ones: %s" % (hundreds, fifties, twenties, tens, fives, ones))




def count_coins(payment_in_coins):
    payment_in_coins = int(payment_in_coins)
    quarters = payment_in_coins // 25
    payment_in_coins %= 25
    dimes = payment_in_coins // 10
    payment_in_coins %= 10
    nickels = payment_in_coins // 5
    payment_in_coins %= 5
    pennies = payment_in_coins // 1
    payment_in_coins %= 1
    return print("Quarters: %s, Dimes: %s, Nickels: %s, Pennies: %s" % (quarters, dimes, nickels, pennies))


def value_of_change():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    return print("The total value of your change is $%s" % total)


make_change(148.50, 200)
count_bills(51)
count_coins(51.51)
value_of_change()