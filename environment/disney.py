# create function that determines how much a trip to disney is 
# adult tix=$100/day, child 90/day
#determine total cost of adults
#determine total cost of children
# add them to get daily cost 
# multiply by number of days to get total cost

def disneytrip(num_adults, num_kids, days):
    total = (num_adults*100)+(num_kids*90)*days
    return total
print (disneytrip(4,2,3))

def greet(player):
    if player == "mary":
        return "i love u"
    else:
        return "hi"
name1 = input("enter player 1's name:")
print(greet(name1))

def greetOptional(player = "user"):
    return "welcome to the game, " + player 
print (greetOptional("Mary"))
print (greetOptional())
#def createUser(name, email, password = "abcd1234"):
  # Some code to create the user
# createUser("John Smith", "Jsmith123@gmail.com")
# createUser("Marta Guzman", "MartaG789@gmail.com", "Puppies1")
# createUser("Artie Krausmann")
# Collapse



# Message Input
#scope
# hermaAge = 17
# def have_a_birthday():
#     hermaAge = 25
#     hermaAge += 1
#     print ("hbd you are now " +)