- Install tesseract-ocr -> sudo apt-get install tesseract-ocr
# Not required:
- Install python-opencv -> sudo apt-get install python-opencv

sudo apt-get install libicu-dev
sudo apt-get install libpango1.0-dev
sudo apt-get install libcairo2-dev

# Command
- python fasita ocr --image <image path> [preprocess] [psm] [output] [show-boxes] [show-data] [show-boxes-frame]
- python fasita makeboxes -indir <training folder> -pat <pattern of the files>