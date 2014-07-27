""" Main module of of-calendar

This module implements the arguments parser and calls the parsing and event
generators accordingly
"""
import os.path
import sys
import argparse

import regexp
import ofevent
import err
import export


################################################################################
# HELP MESSAGES
################################################################################

DESCRIPTION_TEXT="Reads an automatic message sent by OpenFlyers and " + \
                 "registers it into a Google Calendar. By default, the " + \
                 "message is read from standard input."
# USERNAME_HELP="Your Google account name, e.g. firstname.lastname@gmail.com"
# PWD_HELP="Your Google account password"
# CALENDAR_HELP="Name of the calendar you want to save OpenFlyers events to"
# CREDENTIALS_HELP="Path to a text file where the first line is your Google account name, the second line is your password, and the third optional line is the name of the calendar you want to register OpenFlyer's events to"
FILE_OPT_HELP="One or several text files with one or several automatic " + \
              "messages sent by OpenFlyers"
FILE_OUT_HELP="Output file name"

# Dictionnary that matches output format string (passed as '--format' argument)
# to the corresopnding generation function
FORMATS={ 'csv':export.CsvExport.actions2csv, 'ics':None }
FORMAT_HELP="Format of the output file. Accepted values are " +\
            ','.join(list(FORMATS.keys()))

################################################################################

def read_input(input_files):
    """Read from multiple input files and returns their content in a string"""
    ans = ""
    for ifile in input_files:
        try:
            f = open(ifile, 'r') if ifile!='-' else sys.stdin
            ans += f.read()
        except IOError as e:
            err.msg("Unable to read from input: " + str(e), __file__, \
                    exit=True)
        ans += "\n"
    
    return ans 

def parse_arguments():
    """"Parse the command line arguments and checks their sanity"""
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
                        default=['-'])
    parser.add_argument("-t", "--format", help=FORMAT_HELP, nargs='?', \
                        default="csv")
    parser.add_argument("-o", "--output", help=FILE_OUT_HELP, nargs='?', \
                        default='-')

    args=parser.parse_args()
    if args.format not in FORMATS:
        err.msg("Invalid output format", __file__, exit=True)

    return args


def run():
    """Main function"""
    # Parse the command line arguments
    args = parse_arguments()

    # Read the input 
    input_text = read_input(args.input_file)

    # Process the input...
    actions = regexp.parse_text(input_text)

    # Call the appropriate function to generate the output
    ans = FORMATS[args.format](actions)

    # Write the output
    try:
        f = open(args.output, 'w') if args.output!='-' else sys.stdout
        f.write(ans)
    except IOError:
        err.msg("Unable to write to the specified output file", \
                __file__, exit=True)


if __name__ == '__main__':
    run()

