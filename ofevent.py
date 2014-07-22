class OfEvent:
    def OfEvent(self, date_start, t_start, date_end, t_end, plane ):
        self._date_start = date_start
        self._t_start    = t_start
        self._date_end   = date_end
        self._t_end      = t_end
        self._plane      = plane

class OfAction:
    def OfAction(self, action, evt1, evt2=None):
        assert action==ACTION_CANCEL or action==ACTION_MODIFY or \
               action==ACTION_CONFIRM
        assert evt2 is None or action==ACTION_MODIFY
        self._action = action
        self._evt1   = evt1
        self._evt2   = evt2

    def sync():
        # TODO
        return
