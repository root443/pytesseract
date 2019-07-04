#Overview Machine learning
Quick intro to Machine Learning: http://www-dimat.unipv.it/gualandi/programmazione2/QL_ML.pdf

#Overview OSD
OSD: https://static.googleusercontent.com/media/research.google.com/it//pubs/archive/35506.pdf

#Training reference Tesseract 4
Training reference: https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract-4.00

#Example Training data
Tesseract data: https://github.com/tesseract-ocr/tesseract/wiki/Data-Files

#Training tesseract model from scratch
https://www.endpoint.com/blog/2018/07/09/training-tesseract-models-from-scratch

#JTessBoxEditor:
http://vietocr.sourceforge.net/training.html

#JTessBoxEditor2.2.0:
https://sourceforge.net/projects/vietocr/files/jTessBoxEditor/jTessBoxEditor-2.2.0.zip/download

#Lios GUI: Permette di selezionare i box in una immagine e assegnare un label (Carattere)locate
https://sourceforge.net/projects/lios/files/latest/download

#Configure training
Configure parameters Tesseract: https://ai-facets.org/tesseract-ocr-best-practices/


#Example Configuration training
mkdir -p ../tesstutorial/engoutput
training/lstmtraining --debug_interval 100 \
  --traineddata ../tesstutorial/engtrain/eng/eng.traineddata \
  --net_spec '[1,36,0,1 Ct3,3,16 Mp3,3 Lfys48 Lfx96 Lrx96 Lfx256 O1c111]' \
  --model_output ../tesstutorial/engoutput/base --learning_rate 20e-4 \
  --train_listfile ../tesstutorial/engtrain/eng.training_files.txt \
  --eval_listfile ../tesstutorial/engeval/eng.training_files.txt \
  --max_iterations 5000 &>../tesstutorial/engoutput/basetrain.log

#Training set compile config:
    "--preserve_interword_spaces 1",
    "--noextract_font_properties 1",
    "--tessedit_word_for_word 1",
    "--segment_nonalphabetic_script 1",
    "--textord_noise_rowratio 20.0",
    "--textord_noise_syfract 0.6",
    "--tosp_old_to_method T",
    "--tosp_old_to_constrain_sp_kn T",
    "--tosp_old_sp_kn_th_factor 4.0",
    "--tosp_only_small_gaps_for_kern T",
    "--tosp_use_pre_chopping T"

