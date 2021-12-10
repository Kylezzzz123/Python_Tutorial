monthConversions = {
    "Jan": "January",  # Jan is a key, January is a value
    "Feb": "February", # the key must be unique 
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}



print(monthConversions["Dec"])   # give a value associates to the key
print(monthConversions.get("Dec")) # get function can specify a default value that I want to use if the key was not found
print(monthConversions.get("Luv", "Not a valid Key")) #set a default value "Not a valid Key"