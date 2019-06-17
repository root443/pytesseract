import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER_OUT = os.path.join(BASE_DIR, "./output/local/")
TRAINING_DIR = os.path.join(BASE_DIR, "training/")
OAM = 1
LANG = "osd+ita+fas+ara"

ADDITIONAL_CONFIG_TESSERACT = " ".join([
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
])

CONFIG_TESSERACT = "--oem {oam} --tessdata-dir {tr} {additional}"\
    .format(oam=OAM, tr=TRAINING_DIR, additional=ADDITIONAL_CONFIG_TESSERACT)
