def shout(name): #def is defining a function def functionname(parameter):
    name=name.upper()
    return "Hello " + name + "!" # return is whatever we get back 
print (shout("Jacob"))
print (shout("Mary"))
print (shout("Herm")) 

def whisper(name):
    name=name.lower()
    return "hello " + name + "."
    
print (whisper("MARY"))

def pi_reminder():
    return 3.14159265
    
print (pi_reminder())

def add(x,y):
    return "adding your numbers" #code will only do first return line
    return x+y
    return "your numbers add up to" + str(x+y)
print (add(2,3))