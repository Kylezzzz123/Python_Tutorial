
try: 
    number = int(input("Enter a number: "))
    print(number)
except ValueError:           #except to avoid an erro from Python
    print("Invalid Input")

except ZeroDivisionError as err:   # divided by zero error , can add specific errors
    print(err)
