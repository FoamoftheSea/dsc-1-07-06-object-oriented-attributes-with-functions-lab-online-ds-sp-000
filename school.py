class School():
    def __init__(self, name, roster={}):
        self.name = name
        self._roster = roster
        
    def add_student(self, name, grade):
        if grade not in self._roster:
            self._roster[grade] = []
        temp = self._roster[grade]
        temp.append(name)
        self._roster[grade] = temp
        
    def grade(self, grade):
        return self._roster[grade]
    
    def sort_roster(self):
        sorted_roster = {}
        for grade in self._roster:
            tmp = sorted(self._roster[grade])
            sorted_roster[grade] = tmp
        return sorted_roster
        
    def roster(self):
        return self._roster