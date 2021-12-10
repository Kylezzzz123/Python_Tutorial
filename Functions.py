def say_hi():         #give a function, to group a code together, we can combine the variable and it is easy to call the function
    print ("Hello User") # give an action for the function, but doing nothing if we don't call function

print("Top")
say_hi()   #call function
print("Bottom")


#------------------------------------------------------------------------------------------

def hey(name, age, game):   # we can give the hey information inside the ()
    print("Hello " + name + " You are " + age + " " + str(game))

hey("Ken", "33", 22)
hey("Summer", "22", 44)