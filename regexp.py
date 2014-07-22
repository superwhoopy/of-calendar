# coding=utf-8
import re

################################################################################

REGEXP_DATE="\d{2}/\d{2}/\d{4}"
REGEXP_TIME="\d{2}:\d{2}"
REGEXP_PLANE="sur le (?P<plane>F-[A-Z]{4})"

REGEXP_ACTION_CONFIRMED="est confirmée"
REGEXP_ACTION_CANCELED="est annulée"
REGEXP_ACTION_MODIFIED="est remplacée par"

def regexp_resa(prefix=""):
  return "La réservation du " + \
            "(?P<" + prefix + "start_date>" + REGEXP_DATE + ") "    + \
            "(?P<" + prefix + "start_time>" + REGEXP_TIME + ") au " + \
            "(?P<" + prefix + "end_date>"   + REGEXP_DATE + ") "    + \
            "(?P<" + prefix + "end_time>"   + REGEXP_TIME + ")"

REGEXP_CONFIRM_MSG=regexp_resa() + "\s*" + REGEXP_PLANE + "\s*.*?" + \
            REGEXP_ACTION_CONFIRMED

REGEXP_CANCEL_MSG=regexp_resa() + "\s*" + REGEXP_PLANE + "\s*.*?" + \
            REGEXP_ACTION_CANCELED

REGEXP_MODIF_MSG=\
  regexp_resa("old_") + "\s*" + REGEXP_PLANE + "\s*.*?" + \
  REGEXP_ACTION_MODIFIED + "\s*" + regexp_resa("new_")
  # TODO plane a parametriser aussi...



SAMPLE_TEXT="""La réservation du 01/09/2014 18:30 au 01/09/2014 20:30
 sur le F-GGQO
avec comme pilote OHAYON Emmanuel
avec comme instructeur HUE Nicolas
 est confirmée.
Cette opération a été effectuée par OHAYON Emmanuel
La réservation du 07/09/2014 10:00 au 07/09/2014 13:00
 sur le F-GGQP
 avec comme commentaires : plage de silence
avec comme pilote OHAYON Emmanuel
avec comme instructeur HUE Nicolas
 est remplacée par La réservation du 07/09/2014 09:00 au 07/09/2014 12:00
 sur le F-GGQP
 avec comme commentaires : plage de silence
La réservation du 27/07/2014 09:00 au 27/07/2014 12:00
 sur le F-GGQP
avec comme pilote OHAYON Emmanuel
avec comme instructeur HUE Nicolas
 est annulée.
Cette opération a été effectuée par HUE Nicolas
"""

################################################################################

oneline_text = re.sub( '\n', ' ', SAMPLE_TEXT)

print(oneline_text)

match_confirm = re.finditer( REGEXP_CONFIRM_MSG, oneline_text)
match_cancel  = re.finditer( REGEXP_CANCEL_MSG, oneline_text)
match_modif   = re.finditer( REGEXP_MODIF_MSG, oneline_text)

for confirmed in match_confirm:
    print(confirmed.group("start_date", "start_time", "end_date", "end_time",\
                        "plane"))

for canceled in match_cancel:
    print(canceled.group("start_date", "start_time", "end_date", "end_time",\
                        "plane"))

for modified in match_modif:
    print(modified.group("old_start_date", "old_start_time", "old_end_date",\
                       "old_end_time", "plane", "new_start_date",\
                       "new_start_time", "new_end_date",\
                       "new_end_time"))

