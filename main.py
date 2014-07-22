import sys
import argparse
import parser
import ofevent

################################################################################

DESCRIPTION_TEXT="Reads an automatic message sent by OpenFlyers and registers it into a Google Calendar. By default, the message is read from standard input."
USERNAME_HELP="Your Google account name, e.g. firstname.lastname@gmail.com"
PWD_HELP="Your Google account password"
CALENDAR_HELP="Name of the calendar you want to save OpenFlyers events to"
CREDENTIALS_HELP="Path to a text file where the first line is your Google account name, the second line is your password, and the third optional line is the name of the calendar you want to register OpenFlyer's events to"
FILE_OPT_HELP="Text file with one or several automatic messages sent by OpenFlyers"

################################################################################

def run():
    parser = argparse.ArgumentParser( description=DESCRIPTION_TEXT, \
                                      add_help=True)
    parser.add_argument("-u", "--username", type=str, nargs=1, \
                        help=USERNAME_HELP)
    parser.add_argument("-p", "--password", type=str, nargs=1, \
                        help=PWD_HELP)
    parser.add_argument("-c", "--calendar", type=str, nargs=1, \
                        help=CALENDAR_HELP, default="Default")
    parser.add_argument("--credentials",  nargs=1, help=CREDENTIALS_HELP)
    parser.add_argument("-f", "--file", help=FILE_OPT_HELP, nargs=1, \
                        default=sys.stdin)

    parser.parse_args()


if __name__ == '__main__':
    run()

