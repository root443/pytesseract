import argparse
import re

import cv2
import pytesseract
from PIL import Image
from fasita.dataframe.charframe import charframe
from fasita.settings import *
from fasita.writer.writer import writing

def tesseract(img):
    config = "{config}".format(config=CONFIG_TESSERACT)
    return pytesseract.image_to_string(img, config=config, lang=LANG)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
    ap.add_argument("--psm", type=str, default=1, help="page segmentation mode")
    ap.add_argument("-o", "--output", type=str, default=None, help="path to output text file")
    ap.add_argument("-b", "--show-boxes", type=str, default=None, help="Show boxes")
    ap.add_argument("-d", "--show-data", type=str, default=None, help="Show data")
    ap.add_argument("-f", "--show-boxes-frame", type=str, default=None, help="Show boxes frame")

    args = vars(ap.parse_args())

    if os.path.isdir(args["image"]):
        logger.info("Write file text from %s" % args["image"])
        files = os.listdir(args["image"])
        for file in files:
            img = Image.open(args["image"] + file)
            writing(re.sub(r"(\.\w+)$", ".docx", file), tesseract(img))
            print(file)
    else:
        logger.info("Write file text from %s" % args["image"])
        img = cv2.imread(r'{img}'.format(img=args["image"]))
        text = tesseract(img)
        if "out_name" in args:
            writing(args["out_name"], text)
        else:
            print(text)

        if args["show_boxes"]:
            logger.info("Show boxes")
            boxes = pytesseract.image_to_boxes(img, config="--oam {oam}".format(oam=OEM), lang=LANG)
            dataframe = charframe(boxes)
            print(dataframe.frame_from_col())

        if args["show_data"]:
            logger.info("Show data")
            data = pytesseract.image_to_data(img, config=CONFIG_TESSERACT, lang=LANG)
            dataframe = charframe(data, header=True)
            print(dataframe.dataframe)

        if args["show_boxes_frame"]:
            logger.info("Show boxes frame")
            data = pytesseract.image_to_boxes(img, config="--oam {oam}".format(oam=OEM), lang=LANG)
            dataframe = charframe(data)
            print(dataframe.frame)

main()