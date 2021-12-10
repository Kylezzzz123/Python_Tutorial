def translate (pharse):
    translation = ""
    for letter in pharse:
        if letter in "AEIOUaeiou":  # if letter has AEIOUaeiou
            if letter.upper(): 
                translation = translation + "G"  # initial traslation is "", then ""+ "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation 

print(translate(input("Enter a phrase: ")))