from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt
import sys

if "-h" in sys.argv:
    print("The first two are the input image and the output image paths, and the last one is the sensibility which is optional (250 by default)")
    sys.exit()

img = plt.imread(sys.argv[1]) #We read the image in the path that the user indicated.
new_shape = list(img.shape) #We create a new shape which is gonna be the shape of the output png
new_shape[2] = 4 #We make sure it has 4 dimensions
new_img = np.ones(shape=new_shape) * 255 #We create the new image and set it the entire transparency layer to 1.
new_img[:,:,0:3] = img # We replace the non transparency layers to the original value.
if len(sys.argv) == 4: #We make sure that the user actually inputted a value for sensibility
    sensibility = int(sys.argv[3]) #We give the user value the sensibility value
else:
    sensibility = 250 #By default it's 250
new_img[:,:,3] = np.where(((new_img[:,:,0] >= sensibility) & (new_img[:,:,1] >= sensibility) & (new_img[:,:,2] >= sensibility)) , 0, new_img[:,:,3] )
#For all the pixels that look whitish enough, we will set the transparency layer to 0.
image.imsave(sys.argv[2], new_img/255) #We save the image.
print("Image created successfully at {}".format(sys.argv[2]))
