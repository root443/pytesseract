# USAGE
# python ocr.py --image images/example_01.png 
# python ocr.py --image images/example_02.png  --preprocess blur

# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os


folder_out = "output"
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
ap.add_argument("--psm", type=str, default=3, help="page segmentation mode")
ap.add_argument("-o", "--out-name", type=str, default="output", help="output file name")

args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)
# check to see if we should apply thresholding to preprocess the
# image
'''
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# # make a check to see if median blurring should be done to remove
# # noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
#
# # write the grayscale image to disk as a temporary file so we can
# # apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
'''
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
config = "--psm {} --oem 1 --tessdata-dir ./training".format(args["psm"])
text = pytesseract.image_to_string(Image.open(args["image"]), config=config, lang="fas+ita")
# if os.path.isfile(filename):
# 	os.remove(filename)

if not os.path.exists(folder_out):
    os.makedirs(folder_out)

with open('./{d}/{f}.txt'.format(d=folder_out, f=args["out_name"]),'wb') as f:
    f.write(text.encode())

# show the output images
# cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
#cv2.waitKey(0)