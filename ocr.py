import argparse
import pytesseract
from PIL import Image
from datetime import datetime
from tesseract.writer.writer import writing
from tesseract.settings import *
from tesseract.dataframe.charframe import charframe
import cv2


def tesseract(img):
    config = "--psm {psm} {config}".format(psm=args["psm"], config=CONFIG_TESSERACT)
    return pytesseract.image_to_string(img, config=config, lang=LANG)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
    ap.add_argument("--psm", type=str, default=1, help="page segmentation mode")
    ap.add_argument("-o", "--out-name", type=str, default=None, help="file name")

    args = vars(ap.parse_args())

    if os.path.isdir(args["image"]):
        files = os.listdir(args["image"])
        for file in files:
            img = Image.open(args["image"] + file)
            writing(file.replace(".jpg", ".docx"), tesseract(img))
    else:
        img = cv2.imread(r'{img}'.format(img=args["image"]))
        text = tesseract(img)
        if args["out_name"]:
            writing(args["out_name"], text)
        else:
            print(text)
        #boxes = pytesseract.image_to_boxes(img, config="--oam {oam}".format(oam=OAM), lang=LANG)
    #dataframe = charframe(boxes)
    #text = "‎&b—dast, acqua per lavare le‏ أبدس\n‎mani; abluzione rituale f.‏ \n&b—dastîn, brocca per acqua f.‏ ابدستان"
    #text = "".join(dataframe.framestring[:10])

