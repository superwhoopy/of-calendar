# coding=utf-8

import re

################################################################################

REGEXP_DATE="\d{2}/\d{2}/\d{4}"
REGEXP_TIME="\d{2}:\d{2}"

REGEXP_RESA="La réservation du " + \
            "(?P<start_date>" + REGEXP_DATE + ") "    + \
            "(?P<start_time>" + REGEXP_TIME + ") au " + \
            "(?P<end_date>"   + REGEXP_DATE + ") "    + \
            "(?P<end_time>"   + REGEXP_TIME + ")"

REGEXP_REPLACE="est remplacée par"

REGEXP_PLANE="sur le (?P<plane>F-[A-Z]{4})"



SAMPLE_TEXT="""La réservation du 01/09/2014 18:30 au 01/09/2014 20:30
 sur le F-GGQO
avec comme pilote OHAYON Emmanuel
avec comme instructeur HUE Nicolas
 est confirmée.
Cette opération a été effectuée par OHAYON Emmanuel
"""

################################################################################

match_dates = re.finditer( REGEXP_RESA, SAMPLE_TEXT)
match_plane = re.finditer( REGEXP_PLANE, SAMPLE_TEXT)

# TODO replace all carriage returns by spaces in SAMPLE_TEXT

for date, plane in zip(match_dates, match_plane):
    print date.group("start_date")
    print date.group("end_time")
    print plane.group("plane")
