import sys
import argparse
import parser
import ofevent
import err

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

FORMAT_HELP="Format of the output file. Accepted values are " +\
            ','.join(FORMATS)

################################################################################

FORMATS=[ 'csv', 'ics' ]

def check_format():
    if format not in FORMATS:
        err.msg("Invalid output format", exit=True)
    

def run():
    parser = argparse.ArgumentParser( description=DESCRIPTION_TEXT, \
                                      add_help=True)
    # parser.add_argument("-u", "--username", type=str, nargs=1, \
    #                     help=USERNAME_HELP)
    # parser.add_argument("-p", "--password", type=str, nargs=1, \
    #                     help=PWD_HELP)
    # parser.add_argument("-c", "--calendar", type=str, nargs=1, \
    #                     help=CALENDAR_HELP, default="Default")
    # parser.add_argument("--credentials",  nargs=1, help=CREDENTIALS_HELP)
    parser.add_argument("-f", "--input-file", help=FILE_OPT_HELP, nargs='*', \
                        default=[sys.stdin])
    parser.add_argument("-t", "--format", help=FORMAT_HELP, nargs='1', \
                        default="csv")
    parser.add_argument("-o", "--output", help=FILE_OUT_HELP, nargs='?', \
                        default=sys.stdout)

    parser.parse_args()
    check_format(format)


if __name__ == '__main__':
    run()

