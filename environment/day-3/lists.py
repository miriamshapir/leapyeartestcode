first_favorite_food="chocolate"
second_favorite_food="cookies"
third_favorite_food="salad"
forth_favorite_food="cherries"
fifth_favorite_food="chicken"

fav_foods = ["chocolate" , "cookies" , "salad" , "cherries" , "chicken"]
# search the list, add to it, categorize it, move them around, get length of list, change/remove an item 
# CRUD = create, read, update, delete

print(fav_foods[4]) 

#updatesmth in the list
print(fav_foods[2])
fav_foods[2]="chicken"
print(fav_foods[2])

#include smth in the list
fav_foods.append("brownies")
print(fav_foods)

for food in fav_foods:
    print("I sure do love " + food + "!")
    
# dstamp1=["Derek","Stampone",30,"Brown","Brown",5.7,185,8,True]
# dstamp1_firstname=dstamp[0] 

  ##key:value. called a dictionary (dict)
# dstamp1 = {"firstname": "Derek",
#   "lastname": "Stampone"
#   "age": 30,
#   "eyecolor": "Brown",
#   "haircolor": "Brown",
#   "height": 5.8,
#   "weight": 185,
#   "lucky_number": 8,
#   "registed_to_vote?": True
# }

# print(dstamp1["lucky_number"])
# dstamp1["lucky_number"]=7
# dstamp1["ethnicity"]="white" #updates/adds to the key
# print(dstamp1)

superheroes = {
 "jeff": "Rogue",
 "deanna": "Jessica Jones",
 "danny": "Static Shock",
 "ash": "Supergirl",
 "derek": "The Hulk"
}

superheroes["Mary"]="wonder woman"

for person in superheroes:
    print(person)
    
for person in superheroes:
    print(superheroes[person])
    
for x in range(1,101):
    print(x)
    
for x in range(1,101):
    if x%2==0:
        print(x)
        
for x in range(1,1000000): 
    if x**2 < 1000000:
        print(x**2)
 ### below is a LIST of dictionaries not a dictionary       
actors  = [
  {"name": "Molly Ringwald", "role": "Claire Standish", "grade": 10},
  {"name": "Judd Nelson", "role": "John Bender", "grade": 12},
  {"name": "Ally Sheedy", "role": "Allison Reynolds", "grade": 11},
  {"name": "Anthony Michael Hall", "role": "Brian Johnson", "grade": 10}
]

print(actors[2]["name"])
print(actors[3]["role"])
print(len(actors))

for people in actors:
  print("The role of " + people["role"] + " was played by " + people["name"])
