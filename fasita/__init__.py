import argparse
from fasita.ocr import ocr
from fasita.makeboxes import makeboxes
from fasita.batch import batchtraining

def help():
    from fasita.settings import COMMANDS
    print("Choice a command: %s" % COMMANDS)
