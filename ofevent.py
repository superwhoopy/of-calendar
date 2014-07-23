import datetime

################################################################################
class ActionType:
    MODIFY  = 0
    CANCEL  = 1
    CONFIRM = 2

class OfEvent:
    def OfEvent(self, date_start, t_start, date_end, t_end, plane ):
        self._date_start = date_start
        self._t_start    = t_start
        self._date_end   = date_end
        self._t_end      = t_end
        self._plane      = plane

    def __str__(self):
        return "From " + str(date_start) + " " + str(t_start) + " to " + \
               str(date_end) + " " + str(t_end) + " with " + str(plane)

class OfAction:
    def OfAction(self, action, evt1, evt2=None):
        assert action==ActionType.CANCEL or action==ActionType.MODIFY or \
               action==ActionType.CONFIRM
        assert evt2 is None or action==ActionType.MODIFY
        self._action = action
        self._evt1   = evt1
        self._evt2   = evt2

    def __str__(self):
        text = { ActionType.MODIFY  : "Modification" , \
                 ActionType.CANCEL  : "Cancellation" , \
                 ActionType.CONFIRM : "Confirmation" }

        ans = text[_action] + " of:\n  " + str(_evt1)
        if self._action==ACTION_MODIFY:
            ans += "\nInto:\n  " + str(_evt2)
        return ans

    def sync():
        # TODO
        return
