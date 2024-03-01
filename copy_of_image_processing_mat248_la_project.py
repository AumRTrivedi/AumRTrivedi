# -*- coding: utf-8 -*-
"""Copy of Image Processing MAT248 LA Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h3RJxeBLKCRdq_Bo1daFHkFDoBv11V0S

'''We first start by building the basics, Here we are importing the library as we progress we will add more libraries as per the requirements.
note that all the given libraries are based on linear algebra since the libraries are based on the pixel colour value matrix and all the functions are applied on
those 2d array of matrices and other libraries are for representation and manipulation of image from matrix to visual format and viceversa.'''

# Adding the libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import cv2
import matplotlib.pyplot as plt
import skimage
import skimage.feature
import skimage.viewer
from PIL import Image
from skimage import img_as_uint
from skimage.io import imshow, imread
from matplotlib.image import imread
from skimage.color import rgb2gray
# %matplotlib inline

"""Numpy: Library to support Multidimentional Arrays and Matrices in python and also provides various mathematical functions.
Matplotlib: It is the plotting library for python with *numpy* as its numerical extention
skimage: Scikit-image is a library of image processing.

# Basics
## simulating Black and white pixels
"""

#lets make a chess board using pixel values: each number in the array represents a pixel value
array_1 = np.array([[255, 0,255,0,255, 0,255,0],
                    [0, 255,0,255,0, 255,0,255],[255, 0,255,0,255, 0,255,0],
                    [0, 255,0,255,0, 255,0,255],[255, 0,255,0,255, 0,255,0],
                    [0, 255,0,255,0, 255,0,255],[255, 0,255,0,255, 0,255,0],
                    [0, 255,0,255,0, 255,0,255]])
imshow(array_1, cmap = 'gray');
'''
here,
255-->white
0-->black and any number in between is a grey box (between completely black and white) as we will see next
'''

#lets make a chess board using pixel values: each number in the array represents a pixel value
array_1 = np.array([[2,1,2],
                    [1,0,1],
                    [2,1,2]])

imshow(array_1, cmap = 'gray');

array_1 = np.array([[0, 50,100,150,200, 250,255,]])
imshow(array_1, cmap = 'gray');

"""## simulating colour pixel"""

#note the pixels are a mix of Red, Green and Blue colours as we'll see here.
#Because of how the library functions, each element in the array within '[]' can
#only have 3 arguments If we add more arguments only first three are considered
#and the rest are ignored
#like array_colors = np.array([[[255, 0, 0,255]]]) would still result in a red pixel
array_colors = np.array([[[255, 0, 0],[0, 255, 0],[0, 0, 255]]])
imshow(array_colors);

"""## Getting to know how pixels work for different values of RGB"""

array_colors1 = np.array([[[255, 0, 0],[0, 255, 0],[0, 0, 255],[0,0,0],
                          [255,255,255],[125,125,125],[200,50,50],[50,200,50],
                          [50,50,200]]])
imshow(array_colors1);

"""# Lets begin working on Images now that we know about how pixels are represented in matrix format in an array
## Reading images, ploting images and getting basic information about images
"""

image = Image.open('Image Processing MAT248 LA Project image 1.jpg')
image.show()
plt.imshow(image)
print("image properties", image.size, "\n",  image.format,  "\n",   image.mode )

"""## Now let's print the array of Matrices representing the Image
note that from here onwards the image matrix when converted back to image, it uses BGR format so we apply a transfrom "cv2.cvtColor(image_matrix, cv2.COLOR_BGR2RGB)" that converts BGR to RGB again
"""

import cv2
image_matrix = cv2.imread("Image Processing MAT248 LA Project image 1.jpg")
print(image_matrix)

"""## Lets convert matrix back to the original image"""

img = cv2.cvtColor(image_matrix, cv2.COLOR_BGR2RGB)
imshow(img)

"""# More Image operations and applications of linear algebra
## Showing the red, green and blue parts of the images
"""

img=cv2.imread("Image Processing MAT248 LA Project image 1.jpg",1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
R = img.copy()
G = img.copy()
B = img.copy()

R[:,:,1] = R[:,:,2] = 0 #Setting all values of matrices to 0 apart from the first column that indicates the red pixel values so [255,137,113]--> [255,0,0]
G[:,:,0] = G[:,:,2] = 0 #Setting all values of matrices to 0 apart from the second column that indicates the Green pixel values so [255,137,113]--> [0,137,0]
B[:,:,0] = B[:,:,1] = 0 #Setting all values of matrices to 0 apart from the third column that indicates the Blue pixel values so [255,137,113]--> [0,0,113]


fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(221)
bx = fig.add_subplot(222)
cx = fig.add_subplot(223)
dx = fig.add_subplot(224)


bx.imshow (R)
cx.imshow (G)
dx.imshow (B)
ax.imshow (img)

"""## Greyscaling image"""

#method one
image_gray=image.convert('LA')
plt.imshow(image_gray)
#here the jpg image is directly converted into a grayscaled image using some method

#method two
image_matrix = np.array(list(image_gray.getdata(band=0)),float)
image_matrix.shape= (image_gray.size[1], image_gray.size[0])
image_matrix =np.matrix(image_matrix)
plt.imshow(image_matrix, cmap='gray')
#here we use linear algebra to convert all the RGB values and take the mod square
#of them to find BG values and thereby plot it in image format to make a grayscale image

"""## Translation(resizing) of sides of image"""

# read the image
image = cv2.imread("Image Processing MAT248 LA Project image 1.jpg")
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("Original shape: ", image.shape)

height = 720*float(input('enter the value you want to scale the height by: '))
width = 1080*float(input('enter the value you want to scale the width by: '))
dimensions = (int(width), int(height))
new_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR)
new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
print("New shape:      ", new_image.shape)

# display the images
plt.imshow(image)
plt.imshow(new_image)

"""## Rotation of image"""

img = cv2.imread("Image Processing MAT248 LA Project image 1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
rows, cols, dim = img.shape
angle = np.radians(10)
#transformation matrix for Rotation
M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
            	[np.sin(angle), np.cos(angle), 0],
            	[0, 0, 1]])
# apply a perspective transformation to the image
rotated_img = cv2.warpPerspective(img, M, (int(cols),int(rows)))
plt.imshow(rotated_img)
plt.show()

"""## Shear of image"""

#shear in x
img = cv2.imread("Image Processing MAT248 LA Project image 1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
rows, cols, dim = img.shape
M = np.float32([[1, 0.75, 0],
             	[0, 1  , 0],
            	[0, 0  , 1]])
sheared_imgM = cv2.warpPerspective(img,M,(int(cols*2),int(rows*2)))
plt.imshow(sheared_imgM)
plt.show()

#shear in y
img = cv2.imread("Image Processing MAT248 LA Project image 1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
rows, cols, dim = img.shape
N = np.float32([[1,   0, 0],
             	  [0.5, 1, 0],
             	  [0,   0, 1]])
sheared_imgN = cv2.warpPerspective(img,N,(int(cols*2),int(rows*2)))
plt.imshow(sheared_imgN)
plt.show()

"""## Reflection of an image"""

img = cv2.imread("Image Processing MAT248 LA Project image 1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
rows, cols, dim = img.shape
M = np.float32([[1,  0, 0   ],
                [0, -1, rows],
                [0,  0, 1   ]])
reflected_img = cv2.warpPerspective(img,M,(int(cols),int(rows)))
plt.imshow(reflected_img)
plt.show()

img = cv2.imread("Image Processing MAT248 LA Project image 1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
rows, cols, dim = img.shape
M = np.float32([[-1, 0, cols],
                [ 0, 1, 0   ],
                [ 0, 0, 1   ]])
reflected_img = cv2.warpPerspective(img,M,(int(cols),int(rows)))
plt.imshow(reflected_img)
plt.show()

"""## Flip about an arbitary axis"""

img = cv2.imread("Image Processing MAT248 LA Project image 1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
rows, cols, dim = img.shape
M = np.float32([[-1, 0, cols],
                [ 0, 1, 0   ],
                [ 0, 0, 1   ]])
angle = np.radians(10)
print('here the angle represents slope of y=mx + 0 line where (x(0),y(0)) is topright and +ve y axis is downwards and +ve x axis is towards right ')
N = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
            	[np.sin(angle), np.cos(angle), 0],
            	[0, 0, 1]])
rotated_img = cv2.warpPerspective(img,N,(int(int(cols)*1.5),int(int(rows)*1.5)))
Reflected_img = cv2.warpPerspective(rotated_img,M,(int(int(cols)*-1.5),int(int(rows)*1.5)))
plt.imshow(Reflected_img)
plt.show()

"""## Transposing image"""

image = Image.open("Image Processing MAT248 LA Project image 1.jpg")
Transpose_of_image = image.transpose(Image.TRANSPOSE)
plt.imshow(Transpose_of_image)

"""# Image Filering and noise reduction
(concepts like edge detection are also included)

## image bluring
"""

img = cv2.imread("fwht512.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
av3 = cv2.blur(img,(3,3))
av20 = cv2.blur(img,(35,35))
# Plot the image. This code is excluded for the rest of the article.
plt.gcf().set_size_inches(25,25)
plt.subplot(131),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(av3),plt.title('Averaging - 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(av20),plt.title('Averaging - 35x35')
plt.xticks([]), plt.yticks([])
plt.show()
print('this can also br applied to mxn')

"""## Denoising image using mean

"""

imgWO = cv2.imread('imgWOnoise.jpg')
imgWO = cv2.cvtColor(imgWO, cv2.COLOR_BGR2RGB)
plt.imshow(imgWO)

img = cv2.imread('imgWnoise.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst = cv2.fastNlMeansDenoisingColored(img,None,18,18,7,21)

plt.imshow(img)
'''
h : parameter deciding filter strength. Higher h value removes noise better, but removes details of image also. (10 is ok)
hForColorComponents : same as h, but for color images only. (normally same as h)
templateWindowSize : should be odd. (recommended 7)
searchWindowSize : should be odd. (recommended 21)
'''

plt.imshow(dst)

"""## Median Filters"""

image=cv2.imread('LENACOLOUREDIMAGE.ppm')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def noisy(image):

    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.04
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
          for i in image.shape]
    out[coords] = 1
    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
          for i in image.shape]
    out[coords] = 0
    return out
noisy_img = noisy(image)
median = cv2.medianBlur(noisy_img,3)
plt.imshow(noisy_img)

plt.imshow(median)

"""## Gaussian Filter"""

gb = cv2.GaussianBlur(image, (3,3), 10,10)
plt.imshow(gb)

"""## Bilateral Filter"""

bilateral = cv2.bilateralFilter(image,9,75,75)
plt.imshow(bilateral)

"""## Image Compression Using SVD"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
from os import mkdir, path

in_folder, ext = 'input', 'tif'
out_folder = 'output'


def IFFT(arr):
    ''' Recursive Inverse Fast Fourier Transformation implementation
    '
    '   Arguments: arr - 1d numpy array
    '   Return: 1d numpy array
    '''
    return FFT(arr, inverse=True) / arr.shape[0]


def FFT(arr, inverse=False):
    ''' Recursive Fast Fourier Transformation implementation
    '
    '   Arguments: arr - 1d numpy array, inverse - Boolean
    '   Return: 1d numpy array
    '''
    sign = 1 if inverse else -1

    if arr.shape[0] == 1:
        # Return the array of lenght 1
        return arr
    else:
        # Recursively run FFT for even and odd arr's elements
        even, odd = FFT(arr[0::2], inverse=inverse), FFT(arr[1::2],
                                                         inverse=inverse)

        # Calculate the omega value
        omega = sign * 2j * np.pi / arr.shape[0]

        # Calculate the range of values
        values = np.exp(omega * np.arange(arr.shape[0] // 2)) * odd

        return np.concatenate([even + values, even - values])


def compress(img):
    ''' Compress img using FFT and IFFT
    '
    '   Arguments: img - 2d numpy array
    '   Return: 2d numpy array
    '''
    # Do 2D FFT
    img = np.apply_along_axis(FFT, 1, img)
    img = np.apply_along_axis(FFT, 0, img)

    # Drop some values
    img[img < np.mean(img) - 13 * np.std(img)] = 0

    # Do 2D IFFT
    img = np.apply_along_axis(IFFT, 1, img)
    img = np.apply_along_axis(IFFT, 0, img)

    # Return real values of img
    return np.real(img)

plt.figure(1)
plt.semilogy(np.diag(s))
plt.title('Singular Values')
plt.show()

plt.figure(2)
plt.plot(np.cumsum(np.diag(s))/np.sum(np.diag(s)))
plt.title('Singular Values: Cumulative Sum')
plt.show()

"""# EDGE DETECTION"""

#Read the original image
img = cv2.imread('test.png')
#Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)
#Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
#Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
#Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
#Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
#Combined X and Y Sobel Edge Detection
#Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)
#Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
#Canny Edge Detection
#Display Canny Edge Detection
Image cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()