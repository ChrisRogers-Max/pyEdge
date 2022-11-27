# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:05:54 2022

@author: Administrator
"""
"""
To detect edges in images -> to define pyEdge function
To draw a procedure brench
In the format of command line
supports three different methods for edge detection: Canny, Sobel, Prewitt
"""

#To import library
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.filters import sobel, prewitt
from skimage.feature import canny

#provided by the user
input_filename = "xray.png"
output_filename = "xray_edges.png"

#read image and find edges
img = imread(input_filename)
#choose the method of edge detection
img_edges = canny(img, sigma = 1)

#save the file
imsave(fname = output_filename, arr = img_edges)
#Display images
fig, ax = plt.subplots(nrows=1, ncols=2, figsize = (10, 5))
ax[0].imshow(img, cmap = "gray")
ax[1].imshow(img_edges, cmap = "gray")

for a in ax:
    a.axis("off")
    
plt.show()