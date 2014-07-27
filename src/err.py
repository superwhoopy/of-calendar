import sys

def msg(text, file="<unknown>", line="<unknown>", exit=False):
    sys.stderr.write("[ERROR] " + file + ":" + line + " " + text + "\n");
    if (exit):
        sys.exit(1)
