# Tesseract
- batch.nochop:\
  tells Tesseract not to use its fancy algorithms for segmenting the picture. 
  If your files contain letters in a grid, you should use it, but otherwise you may want to remove it from the command.
- MFTRAINING:\
  mftraining takes a list of .tr files, from which it generates the files inttemp (the shape prototypes), shapetable, 
  and pffmtable (the number of expected features for each character).