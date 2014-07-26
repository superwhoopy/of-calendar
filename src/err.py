import sys

def msg(text, exit=False):
    sys.stderr.write("[ERROR]" + text + "\n");
    if (exit):
        sys.exit(1)
