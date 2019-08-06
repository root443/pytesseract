import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER_OUT = os.path.join(BASE_DIR, "..output/local/")
TRAINING_DIR = os.path.join(BASE_DIR, "../training/")
TRAINING_BOXES_DIR = os.path  .join(BASE_DIR, "../training/boxes/")
OEM = 1
PSM = 1
LANG = "ita+fas+ara"

ADDITIONAL_CONFIG_TESSERACT = " ".join([])

CONFIG_TESSERACT = "--psm {psm} --oem {oem} --tessdata-dir {tr} {additional}"\
    .format(psm=PSM, oem=OEM, tr=TRAINING_DIR, additional=ADDITIONAL_CONFIG_TESSERACT)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module}:  {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'debug_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': '%s/debug.log' % os.path.join(BASE_DIR, 'tmp'),
            'formatter': 'simple'
        },
        'info_logfile': {
            'class': 'logging.FileHandler',
            'filename': '%s/info.log' % os.path.join(BASE_DIR, 'tmp'),
            'formatter': 'verbose'
        },
        'error_logfile': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': '%s/error.log' % os.path.join(BASE_DIR, 'tmp'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'error_logger': {
            'handlers': ['error_logfile'],
            'level': 'ERROR'
         },
        'info_logger': {
            'handlers': ['info_logfile'],
            'level': 'INFO'
        },
        'debug_logger': {
            'handlers': ['debug_logfile'],
            'level': 'DEBUG'
        },
    }
}