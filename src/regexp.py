# coding=utf-8
import re
import ofevent

################################################################################

REGEXP_DATE="\d{2}/\d{2}/\d{4}"
REGEXP_TIME="\d{2}:\d{2}"

REGEXP_ACTION_CONFIRMED="est confirmée"
REGEXP_ACTION_CANCELED="est annulée"
REGEXP_ACTION_MODIFIED="est remplacée par"

def regexp_resa(prefix=""):
  return "La réservation du " + \
            "(?P<" + prefix + "start_date>" + REGEXP_DATE + ") "    + \
            "(?P<" + prefix + "start_time>" + REGEXP_TIME + ") au " + \
            "(?P<" + prefix + "end_date>"   + REGEXP_DATE + ") "    + \
            "(?P<" + prefix + "end_time>"   + REGEXP_TIME + ")"

def regexp_plane(prefix=""):
  return "sur le (?P<" + prefix + "plane>F-[A-Z]{4})"

REGEXP_MSG=regexp_resa() + "\s*" + regexp_plane() + "\s*.*?" + \
           "(?P<action>" + REGEXP_ACTION_CONFIRMED + "|" + \
                           REGEXP_ACTION_CANCELED  + "|" + \
                           REGEXP_ACTION_MODIFIED +")"

REGEXP_MODIF_MSG=\
  regexp_resa("old_") + "\s*" + regexp_plane("old_") + "\s*.*?" + \
  REGEXP_ACTION_MODIFIED + "\s*" + regexp_resa("new_") + "\s*" + \
  regexp_plane("new_")



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

ofevt_action = { REGEXP_ACTION_MODIFIED  : ofevent.ActionType.MODIFY, \
                 REGEXP_ACTION_CONFIRMED : ofevent.ActionType.CONFIRM, \
                 REGEXP_ACTION_CANCELED  : ofevent.ActionType.CANCEL }

def parse_text( text):
    actions = []
    oneline_text = re.sub( '\n', ' ', text)

    messages = re.finditer( REGEXP_MSG, oneline_text)

    start=0
    while True:
        msg = re.search( REGEXP_MSG, oneline_text)
        if msg is None:
            break

        evt1 = ofevent.OfEvent( msg.group("start_date"), \
                        msg.group("start_time"), \
                        msg.group("end_date"), \
                        msg.group("end_time"),   \
                        msg.group("plane"))
        evt2 = None
        action = ofevt_action[msg.group("action")]

        if msg.group("action")==REGEXP_ACTION_MODIFIED:
            msg = re.search( REGEXP_MODIF_MSG, oneline_text)
            evt2 = ofevent.OfEvent(msg.group("new_start_date"), \
                           msg.group("new_start_time"), \
                           msg.group("new_end_date"),   \
                           msg.group("new_end_time"),   \
                           msg.group("new_plane"))

        actions.append( ofevent.OfAction( action, evt1, evt2))
        oneline_text = oneline_text[msg.end():]

    return actions
    
