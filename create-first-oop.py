# nstantiate an instance object of Person with name of 'Sonny', email of sonny@hotmail.com, and phone of '483-485-4948', store it in the variable sonny.
# Instantiate another person with the name of 'Jordan', email of jordan@aol.com, and phone of '495-586-3456', store it in the variable jordan.
# Have sonny greet jordan using the greet method.
# Have jordan greet sonny using the greet method.
# Write a print statement to print the contact info (email and phone) of Sonny.
# Write another print statement to print the contact info of Jordan.

class Person:
  

    def __init__(self, name, email, phone):
      self.name = name
      self.email = email
      self.phone = phone
      self.friends = []  

    def greet(self, other_person):
      print('Hello %s, I am %s!' % (other_person.name, self.name))
    
    def print_contact_info(self, contactInfo):
       print("email: %s and phone number: %s " % (contactInfo.email, contactInfo.phone))
    
    def add_friend(self, friends):
       self.friends.append(friends)
    
    def num_friends(self):
       return print(len(self.friends))



sonny = Person("Sonny", "sonny@hotmail.com", 4834854948)
jordan = Person("Jordan", "jordan@aol.com", 495586345)

jordan.add_friend(sonny)
sonny.add_friend(jordan)

jordan.num_friends()
sonny.num_friends()




sonny.greet(jordan)
jordan.greet(sonny)

print(sonny.email)
print(jordan.email)
sonny.print_contact_info(sonny)




class Vehicle:
    def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year
    def print_info(self, carInfo):
        print("Check out my %s %s %s" % (carInfo.year, carInfo.make, carInfo.model))


eddiesCar = Vehicle("Honda", "Civic", 2016)

print(eddiesCar.make, eddiesCar.model, eddiesCar.year)

eddiesCar.print_info(eddiesCar)