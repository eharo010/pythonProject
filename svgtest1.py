from xml.etree import ElementTree
import math
#from lxml import etree
from copy import deepcopy
path1 = "C:/Users/Edward Haro/Downloads/scaled.svg"
file1 = open(path1, 'r')
print("Test File Open")
#new_file = open("test_gcode.txt", "x")
#new_write = open('test_gcode.txt", "w")
Lines = file1.readlines()

counter = 0
cnt = 0
for line in Lines:
    counter += 1
    #line = line.rstrip() #removes space at end of string (not needed)
    if counter == 35:
        print("At Line 35")
        test = line.strip()
        print("Initial Line")
        print(test)


john = test.strip('d=')
cena = john.strip('"M119 ')
print("Remove d=")
print(john)
print("Remove M119" )
print(cena)

#####################################################
print("XML Tests")
namespace = {'svg': 'http://www.w3.org/2000/svg'}
file_path = path1;
svg = ElementTree.parse(file_path)
root1 = svg.getroot()
print(root1)
print(svg.findall(".//{http://www.w3.org/2000/svg}g"))
print(svg)


#######################################################
print("XML Mini Dom Tests")
from xml.dom import minidom
doc = minidom.parse(file_path)  # parseString also exists
path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
doc.unlink()
print(doc)
print(path_strings)

i = 0
array = []
[print(i) for i in path_strings]
for i in path_strings:
    array.append(i)

print(array)
print("Converting to Pixels to MM")
x = 0;
y = 1/5;
while x < len(array):
    #convert = array(x) * 0.2
    array[x] = array[x] * y
    array.append(array[x])


#svg_parse = ElementTree.parse(file_path)
#
#for letters in cena:
    

#new1 = open("test_gcode.txt", "w")
                 #new_write.write(john)
                # Lines1 = new_write.readlines()
                # new1.close()
#print(Lines1)