
class OfEvent:
    ACTION_CANCEL =0
    ACTION_MODIFY =1
    ACTION_CONFIRM=2

    def OfEvent(self, date, t_start, t_end, plane, action):
        assert action==ACTION_CANCEL or action==ACTION_MODIFY or \
               action==ACTION_CONFIRM
        self._date    = date
        self._t_start = t_start
        self._t_end   = t_end
        self._plane   = plane
        self._action  = action

    def synchronize(gcal):
        # TODO: send to Google Calendar
        return

