import os
from tesseract.settings import BASE_DIR
import subprocess
import logging

info_logger = logging.getLogger('info_logger')
debug_logger = logging.getLogger('debug_logger')
error_logger = logging.getLogger('error_logger')

class traineddata(object):
    #TODO Rinominare il file in modo appropriato
    _input_dir = "training"
    CMD = {
            'tesseract': ['tesseract', 'nobatch', 'box.train'],
            "unicharset": ['unicharset_extractor',],
            'character': ['mftraining',],
            'normproto': ['cntraining',],
            'tessdata': ['combine_tessdata',]
        }

    @property
    def input_dir(self):
        return self._input_dir

    def __init__(self, input_dir):
        self.input_dir = input_dir
        self.files = os.listdir(os.path.join(BASE_DIR, self.input_dir))
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
        info_logger.info(stdout)
        error_logger.error(stderr)

    def training_box(self, input_file):
        for img in input_file:
            command = self.CMD["tesseract"][:]
            command[1:2] = [img, os.path.splitext(img)[0]]
            debug_logger.debug(command)
            self._wrap(command)

    def unicharset_extractor(self, input_file):
        for box in input_file:
            command = self.CMD["unicharset"][:]
            command[1:1] = ["%s.box" % box]
            debug_logger.debug(command)
            self._wrap(command)