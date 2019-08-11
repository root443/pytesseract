import cv2
import argparse
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

#TODO Ridisegnare lo script come una classe o un interfaccia
def binarize_image(img, thres=150, maxval=255):
    img_name = img.split("/")[-1]
    workdir = img.split("/")[:-1]
    workdir = "/".join(workdir) + "/"


    image = cv2.imread(img)
    ret, threshed = cv2.threshold(image, thres, maxval, cv2.THRESH_BINARY)
    plt.subplot(2, 3, 1+1)
    plt.imshow(threshed)

    processed_image = workdir + "binarized-%s" % img_name
    plt.imsave(processed_image, threshed)
    return processed_image