import cv2
import argparse
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def binarize_image(workdir, filename):
    image_path = workdir + filename
    image = cv2.imread(image_path)
    ret, threshed = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    plt.subplot(2, 3, 1+1)
    plt.imshow(threshed)
    processed_image = workdir + "processed-%s" % filename
    plt.imsave(processed_image, threshed)
    return Image.open(processed_image)


#
# if __name__ == "__main__":
#     ap = argparse.ArgumentParser()
#     ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
#     args = vars(ap.parse_args())
#     binarize_image(image_path=args['image'])
