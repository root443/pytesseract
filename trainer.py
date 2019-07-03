from pytesseract import pytesseract
from PIL import Image
from tesseract.image_processing import binarize_image
import argparse
from tesseract.settings import *

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
ap.add_argument("-t", "--training-dir", required=False, default=TRAINING_BOXES_DIR,
                help="path to input image to be OCR'd")
ap.add_argument("-p", "--process", required=False, default=0, help="path to input image to be OCR'd")
args = vars(ap.parse_args())
image_path = args['image']
filename = image_path.split("/")[-1]
workdir = image_path.split("/")[:-1]
workdir = "/".join(workdir) + "/"
if args['process']:
    image = binarize_image(workdir, filename)
else:
    image = Image.open(image_path)
boxes = pytesseract.image_to_boxes(image, config=CONFIG_TESSERACT, lang=LANG)

with open(TRAINING_BOXES_DIR + filename.split(".")[0] + ".boxes", "w+") as boxesfile:
    boxesfile.write(boxes)
boxesfile.close()
