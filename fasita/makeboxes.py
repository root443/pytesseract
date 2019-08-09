import argparse
import os

from PIL import Image
from pytesseract import pytesseract

from fasita.image_processing import binarize_image
from fasita.settings import CONFIG_TESSERACT, LANG, BOXES_DIR


def makeboxes(image, args):
    path = args['input']
    filename = path.split("/")[-1]
    if args['process']:
        workdir = path.split("/")[:-1]
        workdir = "/".join(workdir) + "/"
        image = binarize_image(workdir, filename)
    image = Image.open(image)
    boxes = pytesseract.image_to_boxes(image, config=CONFIG_TESSERACT, lang=LANG)
    if not args['output'].endswith("/"):
        args["output"] += "/"
    with open(args['output'] + filename.split(".")[0] + ".box", "w+") as boxfile:
        boxfile.write(boxes)
    boxfile.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="path to input image to be OCR'd")
    ap.add_argument("-o", "--output", default=BOXES_DIR, help="path to output .box file'd")
    ap.add_argument("-p", "--process", required=False, default=0, help="path to input image to be OCR'd")
    args = vars(ap.parse_args())

    if os.path.isdir(args["input"]):
        files = os.listdir(args["input"])
        for file in files:
            makeboxes(args["input"] + file, args)
    else:
        makeboxes(args['input'], args)
