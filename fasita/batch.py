import os
import argparse
from fasita.training.instructor import Instructor

def batchtraining():
    from fasita.settings import TRAINEDDATA_DIR
    ap = argparse.ArgumentParser()
    ap.add_argument("-indir", "--input-dir", required=True, help="path to input images to be OCR'd")
    ap.add_argument("-pat", "--pattern", required=True, help="images filename pattern to take to OCR'd")
    ap.add_argument("-fp", "--font-properties", required=True, help="Font properties (fontname italic bold monospace serif fraktur)'d")
    args = vars(ap.parse_args())
    instructor = Instructor(input_dir=os.path.abspath(args["input_dir"]), pattern=args["pattern"])
    instructor.font_properties = args["font_properties"]
    if os.path.isdir(args["input_dir"]):
        # instructor.training_box()
        # print("Compound training (*.tr) files from box and image files.")
        # instructor.unicharset_extractor()
        # print("Extract the charset from the box files")
        # instructor.write_font_properties()
        # print("Write font properties")
        # instructor.inttemp_generator()
        # print("inttemp files generated from tr files")
        # instructor.normproto_generator()
        # print("normproto files generated from tr files")
        # instructor.rename_files_trained()
        # print("Files trained renamed")
        instructor.combine()
        print("File traineddata generated")