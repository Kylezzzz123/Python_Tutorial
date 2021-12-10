test_file = open("fileTest.txt", 'r')   # read is r, write is w, append is a, read and write is r+
print(test_file.read())
print(test_file.readline())   # read first line
print(test_file.readlines())   # read all lines


for tests in test_file.readlines():
    print(tests)
    
test_file.close()
