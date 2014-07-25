import datetime

################################################################################
class ActionType:
    MODIFY  = 0
    CANCEL  = 1
    CONFIRM = 2

class OfEvent:
    def __init__(self, date_start, t_start, date_end, t_end, plane ):
        self._date_start = date_start
        self._t_start    = t_start
        self._date_end   = date_end
        self._t_end      = t_end
        self._plane      = plane

    def __str__(self):
        return "From " + str(self._date_start) + " " + str(self._t_start) + \
               " to " + str(self._date_end) + " " + str(self._t_end) + \
               " with " +  str(self._plane)

class OfAction:
    def __init__(self, action, evt1, evt2=None):
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

        ans = text[self._action] + " of:\n  " + str(self._evt1)
        if self._action==ActionType.MODIFY:
            ans += "\nInto:\n  " + str(self._evt2)
        return ans

    def sync():
        # TODO
        return
