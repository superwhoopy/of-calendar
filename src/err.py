import sys

def msg(text, file="<unknown>", line="<unknown>", exit=False, errcode=1):
    """Print an error message to stderr and possibly exit the program
    
    :param text:    Message to be printed
    :param file:    Path to the source file where the error was triggered
    :param line:    Line number in the source file where the error was triggered
    :param exit:    When set to True, the program exists with ``errcode``
    :param errcode: Errorcode to return when ``exit`` is True
    """
    sys.stderr.write("[ERROR] " + file + ":" + line + " " + text + "\n");
    if (exit):
        sys.exit(errcode)
