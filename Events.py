'''
Object for tracking attendance for ADSA

Things to implement:
1. Name of event, id perhaps
2. Type
3. Store as json
'''
class Event:
    """docstring for ."""
    def __init__(self, event_id, type, date):
        self.event_id = event_id
        self.type = type
        self.date = date

    def _getEventId(self) :
        return self.event_id
    def _setEventId(self) :
        self.event_id = event_id
    def _getType(self) :
        return self.type
    def _setType(self) :
        self.type = type
    def _getDate(self) :
        return self.date
    def _setDate(self) :
        self.date = date
