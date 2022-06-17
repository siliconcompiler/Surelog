import os
import subprocess
import sys

SLOG_DATA = os.path.join(os.path.dirname(__file__), 'data')
SLOG_BIN_DIR = os.path.join(SLOG_DATA, 'bin')

def _program(name, args):
    return subprocess.call([os.path.join(SLOG_BIN_DIR, name)] + args)

def surelog():
    raise SystemExit(_program('surelog', sys.argv[1:]))
