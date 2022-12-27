name_validation = True

#found this on https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
#this chceks if the 'name' contains an integer or not


#i wanted to use a do until loop here however, there isn't one in python
#https://www.daniweb.com/programming/software-development/threads/39804/do-while-loop-in-python

#keep looping until there is no numbers in the name

while name_validation : 
   
    name = input("What is your name?")

    def has_numbers(name):
        #this chceks if the 'name' contains an integer or not
        return any(char.isdigit() for char in name)

    
    name_validation = has_numbers(name)   
    #checks if the name has a number, if it does, display message, and go back to name validation.
    if name_validation:
        print("You can't have numbers in your name")
    
    else:
        break
   
    
print("Hello there " + name)


