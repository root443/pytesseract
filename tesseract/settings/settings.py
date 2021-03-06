import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER_OUT = os.path.join(BASE_DIR, "..output/local/")
TRAINING_DIR = os.path.join(BASE_DIR, "../training/")
TRAINING_BOXES_DIR = os.path  .join(BASE_DIR, "../training/boxes/")
OEM = 1
PSM = 1
LANG = "ita+fas+ara"

ADDITIONAL_CONFIG_TESSERACT = " ".join([])

CONFIG_TESSERACT = "--psm {psm} --oem {oem} --tessdata-dir {tr} {additional}"\
    .format(psm=PSM, oem=OEM, tr=TRAINING_DIR, additional=ADDITIONAL_CONFIG_TESSERACT)
