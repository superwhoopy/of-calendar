import sys
import argparse

################################################################################

DESCRIPTION_TEXT="Reads an automatic message sent by OpenFlyers and registers it into a Google Agenda. By default, the message is read from standard input."
USERNAME_HELP="Your Google account name, e.g. firstname.lastname@gmail.com"
PWD_HELP="Your Google account password"
CREDENTIALS_HELP="Path to a text file where the first line is your Google account name and the second line is your password"
FILE_OPT_HELP="Text file with one or several automatic messages sent by OpenFlyers"

################################################################################

def run():
    parser = argparse.ArgumentParser( description=DESCRIPTION_TEXT, \
                                      add_help=True)
    parser.add_argument("-u", "--username", type=str, help=USERNAME_HELP)
    parser.add_argument("-p", "--password", type=str, help=PWD_HELP)
    parser.add_argument("--credentials", help=CREDENTIALS_HELP, nargs=1)
    parser.add_argument("-f", "--file", help=FILE_OPT_HELP, nargs=1, \
                        default=sys.stdin)

    parser.parse_args()



if __name__ == '__main__':
    run()
