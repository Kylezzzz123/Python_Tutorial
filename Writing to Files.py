test_file = open("fileTest.txt", 'a')   # read is r, write is w, append is a, read and write is r+


test_file.write("haha")   # write new thing into the file
test_file.write("\nBonnie")   #\n is new line



test_file = open("fileTest.txt", "w")   # overwite the whole file
 
test_file = open("CreateNewFile.txt", "w")    # create a new file if you don't have it

html_file = open("index.html", "w")   # create html file
html_file.write("<p>This is HTML</p>")

html_file.close()
test_file.close()