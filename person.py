class Person:
    def __init__(self, name, time):
        self.name = name
        self.time = time
    
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
