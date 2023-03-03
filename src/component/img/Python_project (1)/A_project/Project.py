import cv2
import pywt
import math
import numpy as np
import pandas as pd

# 3DWT -( Discrete wavelet transform for Cover Image)

img = cv2.imread('satellite.jpg')
img = cv2.resize(img, dsize=(512, 512))
Img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imwrite("3DWT_Satellite.jpg", Img)

[LL1, (HL1, LH1, HH1)] = pywt.dwt2(Img, 'db2')
[LL2, (HL2, LH2, HH2)] = pywt.dwt2(LL1, 'db2')
[LL3, (HL3, LH3, HH3)] = pywt.dwt2(LL2, 'db2')

# Watermark logo (Hilbert Curve)

import turtle


sc=turtle.Screen()
sc.setup(200,200)
spiral=turtle.Turtle()
spiral.speed(1000)
sc.bgcolor("black")

col = ("gray", "gray", "gray", "gray")
c=0
for i in range(250):
    spiral.pensize(1)
    spiral.forward(i*6)
    spiral.right(144)
    spiral.color(col[c])
    if c==3:
       c=0
    else:
       c+=1
       
spiral.hideturtle()


### This will create .eps file ####
from tkinter import *
from turtle import *
from PIL import Image
import os
import time

# keeping eps file name as image
eps_file = "temp.eps"

# generating eps file
ts = turtle.getscreen()
turtle.hideturtle()
ts.getcanvas().postscript(file=eps_file)

# get current python file name as string without ".py"
fname = os.path.basename(__file__)
filename = fname.replace('.py','.png')

# Converting eps file to jpg | with filename 
#im.save(str(filename)+".jpg", "JPEG")

# Convert eps to transparent png using ghost script
os.popen("gswin64c -dSAFER -dBATCH -dNOPAUSE -r300 -sDEVICE=pngalpha -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sOutputFile="+filename+" -dEPSCrop temp.eps")

# Merge transparent png on top of given background png
time.sleep(2)

# Get transparent image file height / width
img = Image.open(filename)
h, w = img.size
print(h,w)

# Get background image file height / width
background = Image.open('logo.png')
hh, ww = background.size
print(hh,ww)      

#resize the transparent png image
yoff = round((h)/2)
xoff = round((w)/2)
size = yoff,xoff
print(size)
img = img.resize(size ,Image.ANTIALIAS)
background.paste(img, (round(yoff-h/2),round(xoff-w/2)), img)

#Save file as New Image file
background.save("_"+filename,"PNG")
print("DONE")
ts.exitonclick()

# 3DWT -( Discrete wavelet transform for Watermark Image)

img = cv2.imread('_Project.png')
img = cv2.resize(img, dsize=(512, 512))
Img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imwrite("3DWT_logo.png", Img)

[LL1, (HL1, LH1, HH1)] = pywt.dwt2(Img, 'db2')
[LL2, (HL2, LH2, HH2)] = pywt.dwt2(LL1, 'db2')
[LL3, (HL3, LH3, HH3)] = pywt.dwt2(LL2, 'db2')

# Embedding

import cv2
img = cv2.imread('satellite.jpg')
watermark = cv2.imread("_Project.png")
percent_of_scaling = 20
new_width = int(img.shape[1] * percent_of_scaling/100)
new_height = int(img.shape[0] * percent_of_scaling/100)
new_dim = (new_width, new_height)
resized_img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)

wm_scale = 40
wm_width = int(watermark.shape[1] * wm_scale/100)
wm_height = int(watermark.shape[0] * wm_scale/100)
wm_dim = (wm_width, wm_height)
resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)
h_img, w_img, _ = resized_img.shape
center_y = int(h_img/2)
center_x = int(w_img/2)
h_wm, w_wm, _ = resized_wm.shape
top_y = center_y - int(h_wm/2)
left_x = center_x - int(w_wm/2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

roi = resized_img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)
resized_img[top_y:bottom_y, left_x:right_x] = result

filename = 'Image.jpg'
cv2.imwrite(filename, resized_img)
cv2.imshow("Resized Input Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Emcryption And Decryption

from PIL import Image
import numpy as np
import os
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import cv2 
import random
from math import log
from tqdm import tqdm

def getImageMatrix_gray(imageName):
    im = Image.open(imageName).convert('LA')
    pix = im.load()
    image_size = im.size 
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
                row.append((pix[width,height]))
        image_matrix.append(row)
    return image_matrix, image_size[0], image_size[1],color

def getImageMatrix(imageName):
    im = Image.open(imageName) 
    pix = im.load()
    color = 1
    if type(pix[0,0]) == int:
      color = 0
    image_size = im.size 
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
                row.append((pix[width,height]))
        image_matrix.append(row)
    return image_matrix, image_size[0], image_size[1],color

def multiplicative_cipher_technique(imagename):
    im = Image.open(imagename).convert('LA')
    pix = im.load()
    image_size = im.size 
    image_matrix = []
    for width in range(int(image_size[0])):
        WI=Image.jpg(200,200)+0.0001*W(200,200)
        EWI=[WI*26]*0.0001*32
        row = []
        for height in range(int(image_size[1])):
                row.append((pix[width,height]))
        image_matrix.append(row)
    return image_matrix, image_size[0], image_size[1],color

def multiplicative_cipher_Encryption(imageName, key):
    N = 256
    key_list = [ord(x) for x in key]
    G = [key_list[0:4] ,key_list[4:8], key_list[8:12]]
    g = []
    R = 1
    for i in range(1,4):
        s = 0
        for j in range(1,5):
            s += G[i-1][j-1] * (10**(-j))
        g.append(s)
        R = (R*s) % 1

    L = (R + key_list[12]/256) % 1
    S_x = round(((g[0]+g[1]+g[2])*(10**4) + L *(10**4)) % 256)
    V1 = sum(key_list)
    V2 = key_list[0]
    for i in range(1,13):
        V2 = V2 ^ key_list[i]
    V = V2/V1

    L_y = (V+key_list[12]/256) % 1
    S_y = round((V+V2+L_y*10**4) % 256)
    C1_0 = S_x
    C2_0 = S_y
    C = round((L*L_y*10**4) % 256)
    C_r = round((L*L_y*10**4) % 256)
    C_g = round((L*L_y*10**4) % 256)
    C_b = round((L*L_y*10**4) % 256)
    x = 4*(S_x)*(1-S_x)
    y = 4*(S_y)*(1-S_y)
    
    imageMatrix,dimensionX, dimensionY, color = getImageMatrix(imageName)
    multiplacitive_cipher_EncryptionIm = []
    for i in range(dimensionX):
        row = []
        for j in range(dimensionY):
            row = []
        for j in range(dimensionY):
            while x <0.8 and x > 0.2 :
                x = 4*x*(1-x)
            while y <0.8 and y > 0.2 :
                y = 4*y*(1-y)
            x_round = round((x*(10**4))%256)
            y_round = round((y*(10**4))%256)
            C1 = x_round ^ ((key_list[0]+x_round) % N) ^ ((C1_0 + key_list[1])%N)
            C2 = x_round ^ ((key_list[2]+y_round) % N) ^ ((C2_0 + key_list[3])%N) 
            if color:
              C_r =((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((key_list[6]+imageMatrix[i][j][0]) % N) ^ ((C_r + key_list[7]) % N)
              C_g =((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((key_list[6]+imageMatrix[i][j][1]) % N) ^ ((C_g + key_list[7]) % N)
              C_b =((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((key_list[6]+imageMatrix[i][j][2]) % N) ^ ((C_b + key_list[7]) % N)
              row.append((C_r,C_g,C_b))
              C = C_r

            else:
              C = ((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((key_list[6]+imageMatrix[i][j]) % N) ^ ((C + key_list[7]) % N)
              row.append(C)
              
            x = (x + C/256 + key_list[8]/256 + key_list[9]/256) % 1
            y = (x + C/256 + key_list[8]/256 + key_list[9]/256) % 1
            for ki in range(12):
                key_list[ki] = (key_list[ki] + key_list[12]) % 256
                key_list[12] = key_list[12] ^ key_list[ki]
        multiplacitive_cipher_EncryptionIm.append(row)

    im = Image.new("L", (dimensionX, dimensionY))
    if color:
        im = Image.new("RGB", (dimensionX, dimensionY))
    else: 
        im = Image.new("L", (dimensionX, dimensionY)) 
      
    pix = im.load()
    for x in range(dimensionX):
        for y in range(dimensionY):
            pix[x, y] = multiplacitive_cipher_EncryptionIm[x][y]
    im.save(imageName.split('.')[0] + "_Encrypted.png", "PNG")

def multiplicative_cipher_Decryption(imageName, key):
    N = 256
    key_list = [ord(x) for x in key]

    G = [key_list[0:4] ,key_list[4:8], key_list[8:12]]
    g = []
    R = 1
    for i in range(1,4):
        s = 0
        for j in range(1,5):
            s += G[i-1][j-1] * (10**(-j))
        g.append(s)
        R = (R*s) % 1
    
    L_x = (R + key_list[12]/256) % 1
    S_x = round(((g[0]+g[1]+g[2])*(10**4) + L_x *(10**4)) % 256)
    V1 = sum(key_list)
    V2 = key_list[0]
    for i in range(1,13):
        V2 = V2 ^ key_list[i]
    V = V2/V1

    L_y = (V+key_list[12]/256) % 1
    S_y = round((V+V2+L_y*10**4) % 256)
    C1_0 = S_x
    C2_0 = S_y
    
    C = round((L_x*L_y*10**4) % 256)
    I_prev = C
    I_prev_r = C
    I_prev_g = C
    I_prev_b = C
    I = C
    I_r = C
    I_g = C
    I_b = C
    x_prev = 4*(S_x)*(1-S_x)
    y_prev = 4*(L_x)*(1-S_y)
    x = x_prev
    y = y_prev
    imageMatrix,dimensionX, dimensionY, color = getImageMatrix(imageName)

    multiplicative_cipher_DecryptionImage = []
    for i in range(dimensionX):
        row = []
        for j in range(dimensionY):
            while x <0.8 and x > 0.2 :
                x = 4*x*(1-x)
            while y <0.8 and y > 0.2 :
                y = 4*y*(1-y)
            x_round = round((x*(10**4))%256)
            y_round = round((y*(10**4))%256)
            C1 = x_round ^ ((key_list[0]+x_round) % N) ^ ((C1_0 + key_list[1])%N)
            C2 = x_round ^ ((key_list[2]+y_round) % N) ^ ((C2_0 + key_list[3])%N) 
            if color:
                I_r = ((((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((I_prev_r + key_list[7]) % N) ^ imageMatrix[i][j][0]) + N-key_list[6])%N
                I_g = ((((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((I_prev_g + key_list[7]) % N) ^ imageMatrix[i][j][1]) + N-key_list[6])%N
                I_b = ((((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((I_prev_b + key_list[7]) % N) ^ imageMatrix[i][j][2]) + N-key_list[6])%N
                I_prev_r = imageMatrix[i][j][0]
                I_prev_g = imageMatrix[i][j][1]
                I_prev_b = imageMatrix[i][j][2]
                row.append((I_r,I_g,I_b))
                x = (x +  imageMatrix[i][j][0]/256 + key_list[8]/256 + key_list[9]/256) % 1
                y = (x +  imageMatrix[i][j][0]/256 + key_list[8]/256 + key_list[9]/256) % 1  
            else:
                I = ((((key_list[4]+C1) % N) ^ ((key_list[5]+C2) % N) ^ ((I_prev+key_list[7]) % N) ^ imageMatrix[i][j]) + N-key_list[6])%N
                I_prev = imageMatrix[i][j]
                row.append(I)
                x = (x +  imageMatrix[i][j]/256 + key_list[8]/256 + key_list[9]/256) % 1
                y = (x +  imageMatrix[i][j]/256 + key_list[8]/256 + key_list[9]/256) % 1
            for ki in range(12):
                key_list[ki] = (key_list[ki] + key_list[12]) % 256
                key_list[12] = key_list[12] ^ key_list[ki]
        multiplicative_cipher_DecryptionImage.append(row)
    if color:
        im = Image.new("RGB", (dimensionX, dimensionY))
    else: 
        im = Image.new("L", (dimensionX, dimensionY)) 
    pix = im.load()
    for x in range(dimensionX):
        for y in range(dimensionY):
            pix[x, y] = multiplicative_cipher_DecryptionImage[x][y]
    im.save(imageName.split('_')[0] + "_Decrypted.png", "PNG")

image = "Image"
ext = ".jpg"

# Input image for Encryption

pil_im = Image.open(image + ext, 'r')
imshow(np.asarray(pil_im))

# Output of Encrypted image

multiplicative_cipher_Encryption("Image.jpg", "abcdefghijklm")
im = Image.open("Image_Encrypted.png", 'r')
imshow(np.asarray(im))

