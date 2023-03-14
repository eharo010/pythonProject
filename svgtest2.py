from xml.etree import ElementTree
from xml.dom import minidom
import math
path1 = "C:/Users/Edward Haro/Downloads/scaled.svg"
file1 = open(path1, 'r')
print("Test File Open")

print("XML Tests")
namespace = {'svg': 'http://www.w3.org/2000/svg'}
file_path = path1;
svg = ElementTree.parse(file_path)
root1 = svg.getroot()
print("Printing Root")
print(root1)
print("Print SVG find all")
print(svg.findall(".//{http://www.w3.org/2000/svg}g"))
print("Printing Element Tree Parse")
print(svg)
#all above kind of not required
#######################################################
print("XML Mini Dom Tests\n")

doc = minidom.parse(file_path)  # parseString also exists
# attr = path.getAttribute('d')
path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]

only_cord = [] #list with all paths
# ghost = []
# cena = []
new_p = 0
element = 0
#u = 0
for path in doc.getElementsByTagName('path'):
    attr = path.getAttribute('d')
    for element in attr:
        if element == "M":
            new_p = new_p + 1
    remove = attr.strip('M')
    remove = remove.split()
    only_cord.append(remove)
    # ghost.append(cena)
print("# of Paths,", new_p, "\n")

print("Printing Path Coordinates Only\n", only_cord, "\n")

doc.unlink()
print("Printing MiniDom Parse:", doc, "\n")
print("Printing Path_Strings:\n", path_strings, "\n")

#array = []
#array_r = []

# print("Printing each path in Path_Strings")
# [print(i) for i in path_strings]
#
# copy_paths = path_strings
#
#
# print("Printing Copy Paths")
# print(copy_paths)
# rmv = copy_paths.strip("M")
#
# print("Printing Array")
#
# for j in path_strings:
#     array.append(j)
#
# print(array)

only_cordF = []
#only_cordN = []

k = 0
h = 0
for k in only_cord:
    for h in k:
        only_cordF.append(float(h))
#above code creates a new list of the path coordinates, however no way to identify paths

w = 0
#below code prints each individual coordinate in the list
for i in only_cord:
    for j in range(len(i)):
        print(only_cord[w][j])

    w = w + 1


print("Printing Floats No Path", only_cordF)
#Aprint(h)
p2mm = 0.2645833333
a = 0
a_val = []
t = 0

for i in only_cord: #for each list in only_cord
    for j in range(len(i)): #for parsing through the length of the list
        print(j)
        for a in i: #each value in each nested list path
            #print(only_cord[t][j])
            only_cord[t][j] = float(a) * p2mm   #this ouputs last value of 2nd path converted, then last value of first path converted
            a_val.append(float(a))
    t = t + 1

print("Printing Converted Values Test", only_cord)  #new issue is this prints same value over and over and it's wrong


p2mm = 0.2645833333
print("Converting from Pixels to MM")
cnt = 0
mm_cord = []
for cnt in only_cordF:
    convert = cnt * p2mm
    mm_cord.append(convert)

print(mm_cord)

#BELOW CODE FOR ADDING X Y (NOT WORKING)
# for i in mm_cord:
#     if i == 0:
#         mm_cord[i] = 'X' + mm_cord[i]
#     if ( i > 0 and i%2==0):
#         mm_cord[i] = 'Y' + mm_cord[i]
#     if (i > 0 and i%2==1):
#         mm_cord[i] = 'X' + mm_cord[i]
#
# print(mm_cord)



##############################################################################################################Test Code Tom
# print("Test Adding M Back to List")
myList = ['388 443 ', '387 418 ', '398 410 ', '409 409 ', '420 488 ', '219 385 220 386 223 386 224 387 ']

multiVal = 0.2645833333

newStr = ''
newerList = []
newList = []
cnt = 0

for i in range(len(myList)):
    listVal = ''
    for j in range(len(myList[i])):
        if (myList[i][j] == ' '):
            tmpA = round(multiVal * float(newStr), 6)
            listVal = listVal + str(tmpA) + ' '
            newStr = ''
        else:
            newStr = newStr + myList[i][j]
    # listVal = 'M' + listVal
    newList.append(listVal)

print(newList)


