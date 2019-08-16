import os
import argparse
from fasita.training import Instructor

def batchtraining(path):
    from fasita.settings import TRAINEDDATA_DIR
    ap = argparse.ArgumentParser()
    ap.add_argument("-tr", "--training_dir", required=True, help="path to input training'd")
    ap.add_argument("-i", "--image", required=True, help="path to input training'd")
    args = vars(ap.parse_args())
    control = Instructor(input_dir=os.path.join(TRAINEDDATA_DIR, args["training_dir"]))
    control.training_box(args["image"])