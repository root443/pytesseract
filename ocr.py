import argparse
import pytesseract
from PIL import Image
from datetime import datetime
from tesseract.writer.writer import writing
from tesseract.settings import *


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
    ap.add_argument("--psm", type=str, default=3, help="page segmentation mode")
    ap.add_argument("-o", "--out-name", type=str, default=datetime.now().strftime("%m-%d-%Y_%H-%M-%S"), help="file name")

    args = vars(ap.parse_args())

    config = "--psm {psm} --oem {oam} --tessdata-dir {tr}".format(psm=args["psm"], oam=OAM, tr=TRAINING_DIR)

    text = pytesseract.image_to_string(Image.open(args["image"]), config=config, lang=LANG)
    writing(args["out_name"], text)
