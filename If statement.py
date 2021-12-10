is_male = True
is_tall = False

if is_male or is_tall:   # or statment 
    print("You are a male or tall or both")
if is_male and is_tall:
    print("You are both")
elif is_male and not is_tall:  #  not statement
    print("You are a short male")
elif not is_male and is_tall:    # not statement
    print("You are not male but tall")
else:
    print("You are neither male nor tall")


