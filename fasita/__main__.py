import argparse
import sys
import fasita
from fasita.settings import COMMANDS

args = sys.argv
args = args[1:]


if len(args) == 0:
    raise Exception("You have not passed any commands in!")

if args[0] not in COMMANDS:
    raise Exception("Commands %s not found" % args[0])

sys.argv = args
getattr(fasita, args[0])()


