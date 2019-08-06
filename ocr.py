import argparse

import cv2
import pytesseract
from PIL import Image

from tesseract.dataframe.charframe import charframe
from tesseract.image_processing import binarize_image
from tesseract.settings import *
from tesseract.writer.writer import writing


def tesseract(img):
    config = "{config}".format(config=CONFIG_TESSERACT)
    return pytesseract.image_to_string(img, config=config, lang=LANG)


def ocr():
    img = cv2.imread(r'{img}'.format(img=args["image"]))
    if args['preprocess']:
        img = binarize_image(r'{img}'.format(img=args["image"]))
    text = tesseract(img)
    if args["out_name"]:
        writing(args["out_name"], text)
    else:
        print(text)

    if args["show_boxes"]:
        boxes = pytesseract.image_to_boxes(img, config="--oam {oam}".format(oam=OEM), lang=LANG)
        dataframe = charframe(boxes)
        print(dataframe.frame_from_col())

    if args["show_data"]:
        data = pytesseract.image_to_data(img, config=CONFIG_TESSERACT, lang=LANG)
        dataframe = charframe(data, header=True)
        print(dataframe.dataframe)

    if args["show_boxes_frame"]:
        data = pytesseract.image_to_boxes(img, config="--oam {oam}".format(oam=OEM), lang=LANG)
        dataframe = charframe(data)
        print(dataframe.frame)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
    ap.add_argument("--psm", type=str, default=1, help="page segmentation mode")
    ap.add_argument("-o", "--out-name", type=str, default=None, help="path to output text file")
    ap.add_argument("-sb", "--show-boxes", type=str, default=None, help="Show boxes")
    ap.add_argument("-sd", "--show-data", type=str, default=None, help="Show data")
    ap.add_argument("-sbf", "--show-boxes-frame", type=str, default=None, help="Show boxes frame")

    args = vars(ap.parse_args())

    if os.path.isdir(args["image"]):
        files = os.listdir(args["image"])
        for file in files:
            ocr()
            # img = Image.open(args["image"] + file)
            # writing(file.replace(".tiff", ".docx"), tesseract(img))
            # print(file)
    else:
        ocr()







