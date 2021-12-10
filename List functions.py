lucky_numbers = [4, 8, 15, 16,23, 42]
friends = ["Ken", "Ken", "Summer", "Bonnie", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed") # Add a string at the end of the list
friends.insert(3, "Kelly")  # Add Kelly at position 1
friends.remove("Toby") # remove Toby in the list
# friends.clear()                     # clear all elements
# friends.pop()                       # remove the last element
print(friends)
print (friends.index("Ken")) # index tells me if Bonnie in the list
print (friends.count("Ken")) # count how many Ken in the list



Games = ["A", "Q", "A", "C"]
Games.sort() # sort by letters, also work for numbers
Games.reverse() # reverse the order
Games1 = Games.copy() # copy list from Games
print(Games)
print (Games1)