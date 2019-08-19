import os
import logging
import logging.handlers as handlers
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent

TRAINEDDATA_DIR = os.path.join(BASE_DIR, "data/trained/")
BOXES_DIR = os.path.join(BASE_DIR, "data/boxes/")
OEM = 1
PSM = 1
LANG = "ita+fas+ara"

ADDITIONAL_CONFIG_TESSERACT = " ".join([])

CONFIG_TESSERACT = "--psm {psm} --oem {oem} --tessdata-dir {tr} {additional}"\
    .format(psm=PSM, oem=OEM, tr=TRAINEDDATA_DIR, additional=ADDITIONAL_CONFIG_TESSERACT)

logger = logging.getLogger('fasita')
logger.setLevel(logging.DEBUG)

INFO_FILE = '%s/info.log' % os.path.join(BASE_DIR, 'tmp')
ERROR_FILE = '%s/error.log' % os.path.join(BASE_DIR, 'tmp')
DEBUG_FILE = '%s/debug.log' % os.path.join(BASE_DIR, 'tmp')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logHandler = handlers.TimedRotatingFileHandler(DEBUG_FILE, when='d', interval=1, backupCount=1)
logHandler.setLevel(logging.DEBUG)
logHandler.setFormatter(formatter)

errorLogHandler = handlers.RotatingFileHandler(ERROR_FILE, maxBytes=5000, backupCount=0)
errorLogHandler.setLevel(logging.ERROR)
errorLogHandler.setFormatter(formatter)

logger.addHandler(logHandler)
logger.addHandler(errorLogHandler)

COMMANDS = ['ocr', 'makeboxes', 'batchtraining', 'help']
