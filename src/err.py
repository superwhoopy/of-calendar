import sys

def msg(text, exit=False):
    print ("[ERROR]" + text, file=sys.stderr);
    if (exit):
        sys.exit(1)
