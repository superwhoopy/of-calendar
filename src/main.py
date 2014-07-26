import os.path
import sys
import argparse

import regexp
import ofevent
import err
import export

################################################################################

DESCRIPTION_TEXT="Reads an automatic message sent by OpenFlyers and " + \
                 "registers it into a Google Calendar. By default, the " + \
                 "message is read from standard input."
# USERNAME_HELP="Your Google account name, e.g. firstname.lastname@gmail.com"
# PWD_HELP="Your Google account password"
# CALENDAR_HELP="Name of the calendar you want to save OpenFlyers events to"
# CREDENTIALS_HELP="Path to a text file where the first line is your Google account name, the second line is your password, and the third optional line is the name of the calendar you want to register OpenFlyer's events to"
FILE_OPT_HELP="One or several text files with one or several automatic messages sent by OpenFlyers"
FILE_OUT_HELP="Output file name"

FORMATS={ 'csv':export.CsvExport.actions2csv, 'ics':None }

FORMAT_HELP="Format of the output file. Accepted values are " +\
            ','.join(list(FORMATS.keys()))

################################################################################

def read_input():
    try:
        f = open(input_file, 'r')
        ans = f.read()
    except IOError:
        err.msg("Unable to read the specified input file", exit=True)
    return ans 

def parse_arguments():
    parser = argparse.ArgumentParser( description=DESCRIPTION_TEXT, \
                                      add_help=True)
    # parser.add_argument("-u", "--username", type=str, nargs=1, \
    #                     help=USERNAME_HELP)
    # parser.add_argument("-p", "--password", type=str, nargs=1, \
    #                     help=PWD_HELP)
    # parser.add_argument("-c", "--calendar", type=str, nargs=1, \
    #                     help=CALENDAR_HELP, default="Default")
    # parser.add_argument("--credentials",  nargs=1, help=CREDENTIALS_HELP)
    parser.add_argument("-i", "--input-file", help=FILE_OPT_HELP, nargs='*', \
                        default=[sys.stdin])
    parser.add_argument("-t", "--format", help=FORMAT_HELP, nargs='?', \
                        default="csv")
    parser.add_argument("-o", "--output", help=FILE_OUT_HELP, nargs='?', \
                        default=sys.stdout)

    parser.parse_args()
    if format not in FORMATS:
        err.msg("Invalid output format", exit=True)


def run():
    launch_dir = os.getcwd()
    exec_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(exec_dir)

    parse_arguments()

    input_text = read_input()
    actions = regexp.parse_text(input_file)

    # Call the appropriate function
    ans = FORMATS[format](actions)

    try:
        f = open(output, 'w')
        f.write(ans)
    except IOError:
        err.msg("Unable to write to the specified output file", exit=True)

    os.chdir(launch_dir)


if __name__ == '__main__':
    run()

