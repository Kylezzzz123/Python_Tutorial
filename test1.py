company = ("Google", "Ebay")
choice=""
while choice != company:
     choice = input("Enter your dream company: ")
     if choice in company:
          print("You match")
          break
     else: 
          print("Try again")
