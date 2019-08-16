import os, cv2
from pathlib import Path

import pytesseract
from PIL import Image

from fasita.settings import CONFIG_TESSERACT, LANG
import subprocess
import logging

logger = logging.getLogger('fasita')

class Instructor(object):
    _font_properties = ["ocrb", 1, 0, 0, 0, 0]
    _input_dir = os.path.abspath('data/training/alfa')
    CMD = {
            'training_box': ['tesseract', 'nobatch', 'box.train'],
            "unicharset_extractor": ['unicharset_extractor',],
            "write_font_properties": [],
            'character': ['mftraining',],
            'normproto': ['cntraining',],
            'tessdata': ['combine_tessdata',]
        }

    @property
    def input_dir(self):
        return self._input_dir

    @property
    def font_properties(self):
        return self._font_properties

    @font_properties.setter
    def font_properties(self, font_properties):
        """
        default is:
            myfont      0    0      0        0      0
            fontname italic bold monospace serif fraktur
        :param font_properties: list of params for fonts
        :return: void
        """
        self._font_properties = font_properties

    def __init__(self, input_dir, **kwargs):
        self._input_dir = Path(input_dir)
        self.files = [file.name for file in os.scandir(self.input_dir) if file.is_file()]
        self.package = self.input_dir.parts[-1]
        if "font_properties" in kwargs:
            self.font_properties = kwargs["font_properties"]

    def makeboxes(self, pattern):
        logger.info(__name__)
        logger.debug(self.input_dir.glob(pattern))
        for img in self.input_dir.glob(pattern):
            if img.is_file():
                boxes = pytesseract.image_to_boxes(Image.open(img))
                filename, _ = os.path.splitext(img)
                with open(filename + ".box", "w+") as boxfile:
                    boxfile.write(boxes)

    #TODO Utilizzare process_img anzichè OpenCV
    def _get_imgs_boxes(self):
        """
        Retrieve images and boxes files from directory of training
        :return: images filename and boxes filename
        """
        imgs = boxes = []
        for img in self.files:
            try:
                var_img = cv2.imread(img)
                cv2.imshow(str(img), var_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            except Exception as e:
                print(e)

    def _wrap(self, command):
        process_out = subprocess.Popen(command,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        stdout, stderr = process_out.communicate()
        logger.info(stdout)
        logger.error(stderr)

    def training_box(self, input_file):
        for img in input_file:
            command = self.CMD[__name__][:]
            command[1:2] = [img, os.path.splitext(img)[0]]
            logger.info(command)
            self._wrap(command)

    def unicharset_extractor(self, input_file):
        for box in input_file:
            command = self.CMD[__name__][:]
            command[1:1] = ["{dir}{box}.box".format(box=box, dir=self.input_dir)]
            logger.info(command)
            self._wrap(command)

    def write_font_properties(self):
        with open("%sfont_properties" % self.input_dir, "w") as f:
            f.write(" ".join(self.font_properties))
