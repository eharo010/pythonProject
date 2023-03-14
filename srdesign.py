#svg folders
path1 = "C:/Users/Edward Haro/Downloads/path.svg"
file1 = open(path1, 'r')
print("Test File Open")
#svg reading
#wholetext = []
#numbers = []
Lines = file1.readlines()

#gcode writing
#new_file = open("test_gcode.txt", "x")
#new_write = open('test_gocde.txt", "w")

#notes: line.rstrip() removes whitespace in back of string, line.lstrip() can edit to remove
# whatever you want at beginning of string
#notes: line.strip() removes whitespace from beginning/end of string


counter = 0
cnt = 0
for line in Lines:
    counter += 1
    #line = line.rstrip() #removes space at end of string (not needed)
    if counter == 35:
        #print(line.strip()) #removes spaces at beginning and end of string
        print("At Line 35")
        line = line.lstrip(' ')
        print(line)
        for letter in line.strip():
            if letter == 'd':
                print('remove d')
            if letter == '=':
                print('remove =')
                print(line.strip())
                if letter != '"':
                    print(line.strip())

       # for letter in line.strip():
        #    cnt += 1
         #   if cnt > 4:
          #      wholetext.append(line[cnt])
            #    if line[cnt].isdigit() == True:
             #       numbers.append(int(line[cnt]))
        #print(wholetext)  #literally ouputs ['d', '=', etc etc]
        #print(numbers) #prints just the numbers but as singular integers fook
        #print(cnt)