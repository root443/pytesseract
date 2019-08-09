import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRAINEDDATA_DIR = os.path.join(BASE_DIR, "data/trained/")
BOXES_DIR = os.path.join(BASE_DIR, "data/boxes/")
OEM = 1
PSM = 1
LANG = "ita+fas+ara"

ADDITIONAL_CONFIG_TESSERACT = " ".join([])

CONFIG_TESSERACT = "--psm {psm} --oem {oem} --tessdata-dir {tr} {additional}"\
    .format(psm=PSM, oem=OEM, tr=TRAINEDDATA_DIR, additional=ADDITIONAL_CONFIG_TESSERACT)
