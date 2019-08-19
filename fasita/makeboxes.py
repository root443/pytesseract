import argparse
import logging
import os
from .training.instructor import Instructor
from PIL import Image

logger = logging.getLogger('fasita')

from fasita.image_processing import binarize_image

# def makeboxes(image, args):
#     path = args['input']
#     filename = path.split("/")[-1]
#     if args['process']:
#         workdir = path.split("/")[:-1]
#         workdir = "/".join(workdir) + "/"
#         image = binarize_image(workdir, filename)
#     image = Image.open(image)
#     boxes = pytesseract.image_to_boxes(image, config=CONFIG_TESSERACT, lang=LANG)
#     if not args['output'].endswith("/"):
#         args["output"] += "/"
#     with open(args['output'] + filename.split(".")[0] + ".box", "w+") as boxfile:
#         boxfile.write(boxes)
#     boxfile.close()


def makeboxes():
    logger.info(__name__)
    ap = argparse.ArgumentParser()
    ap.add_argument("-indir", "--input-dir", required=True, help="path to input images to be OCR'd")
    ap.add_argument("-pat", "--pattern", required=True, help="images filename pattern to take to OCR'd")
    ap.add_argument("-p", "--process", required=False, default=0, help="path to input image to be OCR'd")
    args = vars(ap.parse_args())

    if os.path.isdir(args["input_dir"]):
        instructor = Instructor(os.path.abspath(args["input_dir"]))
        instructor.makeboxes(args["pattern"])
        print("Boxes created")