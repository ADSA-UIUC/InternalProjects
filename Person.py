'''
Object to store attendance data for individuals in ADSA

Things to implement:
1. Name, email, netid
2. Events dictionary/array
3. Frequency of attendance
4. Helper functions etc.

How events is structured:
1.Dictionary containing types as keys and events as dictionaries as values
'''
class Person:
    def __init__(self,name,email,netid) :
        self.name = name
        self.email = email
        self.netid = netid
        self.events = {}
        self.attendance = self._getAttendance()

    def _getName(self) :
        return self.name

    def _setName(self,name) :
        self.name = name

    def _addEvent(self,event) :
        self.events.append(event)
        return True

    def _getAttendance(self) :
        return len(self.events)
