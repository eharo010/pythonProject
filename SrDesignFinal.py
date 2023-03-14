# Description: How to detect and draw contours around objects in
# an image using OpenCV.

import cv2  # Computer vision library
import svgutils.transform as sg  # svg utility library
import sys  # System parameter and functions library
import numpy as np
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("400x100")
root.title("Selection")
Display = Button(root, height=7,
                 width=50,
                 text="Please select an image/file, click to close.",
                 command=root.destroy)
Display.pack()

mainloop()

from tkinter.filedialog import askopenfilename  # tkinter GUI used to select file

path = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

# Read the color image
image = cv2.imread(path)

if image is None:
    #    sys.exit("Could not read the image or file.")
    cv2.namedWindow("Error, Re-run program", cv2.WINDOW_NORMAL)
    cv2.waitKey(0)  # Wait for keypress to continue
    cv2.destroyAllWindows()  # Close windows

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Gray image', gray)
cv2.waitKey(0)  # Wait for keypress to continue
cv2.destroyAllWindows()  # Close windows

# ----------------------------------------
blurred = cv2.GaussianBlur(gray, (3, 3), 0)  # gaussian blur
median = cv2.medianBlur(blurred, 1)  # median blur
bilateral = cv2.bilateralFilter(median, 3, 50, 50)  # bilateral filter
# ----------------------------------------

# Convert the grayscale image to binary
ret, binary = cv2.threshold(bilateral, 150, 255,  # threshold of 150
                            cv2.THRESH_OTSU)

# Display the binary image
cv2.imshow('Binary image', binary)
cv2.waitKey(0)  # Wait for keypress to continue
cv2.destroyAllWindows()  # Close windows

# To detect object contours, we want a black background and a white
# foreground, so we invert the image (i.e. 255 - pixel value)
inverted_binary = ~binary
cv2.imshow('Inverted binary image', inverted_binary)
cv2.waitKey(0)  # Wait for keypress to continue
cv2.destroyAllWindows()  # Close windows

# use morphology to close figure
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35, 35))
morph = cv2.morphologyEx(inverted_binary, cv2.MORPH_CLOSE, kernel, )

# Find the contours on the inverted binary image, and store them in a list
# Contours are drawn around white blobs.
# hierarchy variable contains info on the relationship between the contours
contours, hierarchy = cv2.findContours(inverted_binary,  # inverted_binary
                                       cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

# mask = np.full(inverted_binary.shape, 255, "uint8")
# contours, hierarchies = cv2.findContours(inverted_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
#    cv2.drawContours(mask, [cnt], -1, 0, -1)

# Find contours, obtain bounding rect, and draw width
for c in contours:  # revert all back to image
    x, y, w, h = cv2.boundingRect(c)
    cv2.putText(image, str(w), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 1)

cv2.imshow('Result with bounding rectangles (green) and detected contour lines (pink)', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Fills in the inside of contours
cv2.drawContours(image, contours, -1, (1), thickness=-1)
# cv2.drawContours(image, contours, -1, color=(255, 255, 255), thickness=cv2.FILLED)
# cv2.fillPoly(image, contours, -1, (255,0,255))

mask = np.zeros(image.shape, np.uint8)
cv2.drawContours(mask, contours, 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))

# Contours list converted to svg
with open("path_test.svg", "w+") as f:
    f.write(f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">')

    for c in contours:
        f.write('<path d="M')
        for i in range(len(c)):
            x, y = c[i][0]
            f.write(f"{x} {y} ")
        f.write('" style="stroke:pink"/>')
    f.write("</svg>")

fig = sg.fromfile('path_test.svg')
fig.set_size(('3508', '2480'))  # '2480','3508'
fig.save('scaled_test.svg')

# Draw the contours (in red) on the original image and display the result
# Input color code is in BGR (blue, green, red) format
# -1 means to draw all contours
with_contours = cv2.drawContours(image, contours, -1, (255, 0, 255), 3)
cv2.imshow('Detected contours', with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show the total number of contours that were detected
root = Tk()
root.geometry("400x100")
root.title("Points")
var = StringVar()
label = Message(root, textvariable=var, relief=RAISED)

var.set("Total number of points: " + str(len(c)))
label.pack()
root.mainloop()

root = Tk()
root.geometry("400x100")
root.title("Contours")
var = StringVar()
label = Message(root, textvariable=var, relief=RAISED)

var.set("Total number of contours detected: " + str(len(contours)))
label.pack()
root.mainloop()

print('Total number of contours detected: ' + str(len(contours)))

# -------------------------------------------------------------------------

from xml.dom import minidom
import math

path1 = "C:\\Users\\mavbr\\OneDrive - email.ucr.edu\\Documents\\GitHub\\OpenCV\\scaled_test.svg"
file1 = open(path1, 'r')
file_path = path1;
print("Test File Open")

print("XML Mini Dom Tests\n")

doc = minidom.parse(file_path)  # parseString also exists
# attr = path.getAttribute('d')
path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]

only_cord = [] #list with all paths
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
print("# of Paths,", new_p, "\n")

print("Printing Path Coordinates Only\n", only_cord, "\n")

doc.unlink()
print("Printing MiniDom Parse:", doc, "\n")
print("Printing Path_Strings:\n", path_strings, "\n")

only_cordF = []
#only_cordN = []

k = 0
h = 0
for k in only_cord:
    for h in k:
        only_cordF.append(float(h))

print("Printing Floats No Path", only_cordF)
#Aprint(h)
p2mm = 0.2645833333
a = 0
a_val = []
t = 0

def AddTrailingZeros(myStr):
    tmpA = myStr[myStr.find('.') + len('.'):]
    cnt = 0

    while not (len(tmpA) >= 6):
        tmpA = tmpA + '0'
        cnt = cnt + 1
    for i in range(cnt):
        myStr = myStr + '0'

    return myStr


f = open("svg.gcode", "w")
f.write("G90; ")
f.write("G91; G1 Z2.000000 G90; ")
for i in range(len(only_cord)):
    f.write("G1 ")
    for j in range(len(only_cord[i])):
        only_cord[i][j] = round(p2mm * float(only_cord[i][j]), 6)
        if ((j + 1) % 2 == 1):
            if (j >= 2):
                f.write("G1 ")
            only_cord[i][j] = 'X' + str(only_cord[i][j])
            f.write(AddTrailingZeros(only_cord[i][j]) + " ")
        else:
            only_cord[i][j] = 'Y' + str(only_cord[i][j])
            f.write(AddTrailingZeros(only_cord[i][j]) + "; ")
            if (i == 0 and j == 1):
                f.write("G91; G1 Z3.000000 G90; ")
            elif (j == 1):
                f.write("G91; G1 Z3.000000 G90; ")

    # if (((i + 1) % 2 == 1) and i != 0):
    #     f.write("G91;\nG1 Z-5.000000\nG90;\n")
    # else:
    f.write("G91; G1 Z2.000000 G90; ")
        # if(i == 0):
        #     f.write("G91;\nG1 Z-5.000000\nG90;\n")

if (len(only_cord) % 2 == 1):
    f.write("G91; G1 Z2.000000 G90; ")
f.close()
print("Priting Converted Coordinates with XY\n", only_cord)

print("Printing Converted Values Test", only_cord)  #new issue is this prints same value over and over and it's wrong