import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER_OUT = os.path.join(BASE_DIR, "/home/sandro/Scaricati/coletti/docx/1-30/")
TRAINING_DIR = os.path.join(BASE_DIR, "training/")
OAM = 1
LANG = "ita+fas+ara"

ADDITIONAL_CONFIG_TESSERACT = " ".join([])

CONFIG_TESSERACT = "--oem {oam} --tessdata-dir {tr} {additional}"\
    .format(oam=OAM, tr=TRAINING_DIR, additional=ADDITIONAL_CONFIG_TESSERACT)
