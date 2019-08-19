import os, cv2
from pathlib import Path

import magic
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
            "unicharset_extractor": ['unicharset_extractor', "--output_unicharset"],
            "write_font_properties": [],
            'inttemp_generator': ['mftraining', '-F', 'font_properties', '-U', 'unicharset', '-O ', 'unicharset'],
            'normproto_generator': ['cntraining',],
            'combine': ['combine_tessdata',]
        }

    @property
    def input_dir(self):
        return self._input_dir

    @property
    def pattern(self):
        return self._pattern

    @pattern.setter
    def pattern(self, val):
        self._pattern = val

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

    def __init__(self, input_dir, pattern, **kwargs):
        self._input_dir = Path(input_dir)
        self._pattern = pattern
        self.files = [file.name for file in os.scandir(self.input_dir) if file.is_file()]
        self.package = self.input_dir.parts[-1]
        if "font_properties" in kwargs:
            self.font_properties = kwargs["font_properties"]

    def makeboxes(self, pattern=None):
        if not pattern:
            pattern = self.pattern
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

    def _wrap(self, command, cwd=None):
        if isinstance(cwd, Path):
            cwd = "%s/" % cwd
        process_out = subprocess.Popen(command, cwd=cwd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        stdout, stderr = process_out.communicate()
        logger.info(stdout)
        logger.error(stderr)

    def _is_image(self, filepath):
        mime = magic.Magic(mime=True)
        filetype = mime.from_file(filepath)
        return "image" in filetype

    def training_box(self):
        for img in self.input_dir.glob(self.pattern):
            if not self._is_image(os.path.join(self.input_dir, img.name)):
                continue
            command = self.CMD[self.training_box.__name__][:]
            command[1:2] = [str(img), os.path.splitext(img)[0]]
            print(" ".join(command))
            self._wrap(command)

    def unicharset_extractor(self):
        #TODO il comando viene generato bene, ma non lo esegue correttamente. Lo stesso comando printato su terminale
        # produce il file unicharset correttamente
        command = self.CMD[self.unicharset_extractor.__name__][:]
        command.append("%s.unicharset" % self.input_dir.name)
        files = [box.name for box in self.input_dir.glob("%s.box" % self.pattern)]
        command.append(" ".join(files))
        print(" ".join(command))
        self._wrap(command, cwd=self.input_dir)

    def write_font_properties(self):
        with open("%s/font_properties" % self.input_dir, "w") as f:
            f.write(" ".join(self.font_properties))

    def inttemp_generator(self):
        files = [tr.name for tr in self.input_dir.glob("%s.tr" % self.pattern)]
        command = self.CMD[self.inttemp_generator.__name__][:]
        command[-1] = "%s.%s" % (self.input_dir.name, command[-1])
        command.append(" ".join(files))
        print(" ".join(command))
        self._wrap(command, self.input_dir)

    def normproto_generator(self):
        files = [tr.name for tr in self.input_dir.glob("%s.tr" % self.pattern)]
        command = self.CMD[self.normproto_generator.__name__][:]
        command.append(" ".join(files))
        print(" ".join(command))
        self._wrap(command, self.input_dir)

    def rename_files_trained(self):
        for trainedfile in ["inttemp", "normproto", "pffmtable", "shapetable"]:
            old = "%s/%s" % (self.input_dir, trainedfile)
            new = "%s/%s.%s" % (self.input_dir, self.input_dir.name, trainedfile)
            os.rename(old, new)

    def combine(self):
        command = self.CMD[self.combine.__name__][:]
        command.append("%s." % self.input_dir.name)
        print(" ".join(command))
        self._wrap(command, self.input_dir)