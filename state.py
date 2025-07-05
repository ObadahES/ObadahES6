from experta import *

class State:
    def __init__(self, left_Side, right_Side, lamp_Side, time_past=0, parent=None):
        self.left_Side = left_Side
        self.right_Side = right_Side
        self.lamp_Side = lamp_Side
        self.time_Past = time_past
        self.parent = parent

    def __eq__(self, other):
        return (
            isinstance(other, State)
            and set(self.left_Side) == set(other.left_Side)
            and set(self.right_Side) == set(other.right_Side)
            and self.lamp_Side == other.lamp_Side
            and self.time_Past == other.time_Past
        )

    def __hash__(self):
        return hash((
            frozenset(self.left_Side),
            frozenset(self.right_Side),
            self.lamp_Side,
            self.time_Past
        ))

    #--------------------------------------------------------
    def is_Goal(self):
        if len(self.left_Side) == 0 and len(self.right_Side) == 4 and self.time_Past <= 17:
            path = []
            current = self
            while current:
                path.append(current)
                current = current.parent
            return list(reversed(path))
        else:
            return None

    #--------------------------------------------------------
    def next_States(self):
        states = []

        if self.lamp_Side == "left":
            for i in range(len(self.left_Side)):
                for j in range(i + 1, len(self.left_Side)):
                    step = (self.left_Side[i], self.left_Side[j])
                    new_state = self.movement(step)
                    if new_state.time_Past <= 17:
                        states.append(new_state)

        else:
            if not self.right_Side:
                return states
            fastest_Person = min(self.right_Side, key=lambda p: p.time)
            step = (fastest_Person,)
            new_state = self.movement(step)
            if new_state.time_Past <= 17:
                
                states.append(new_state)

        return states

    #--------------------------------------------------------
    def movement(self, move):
        if self.lamp_Side == "left":
            new_left = [p for p in self.left_Side if p not in move]
            new_right = self.right_Side + list(move)
            new_lamp = "right"
        else:
            new_right = [p for p in self.right_Side if p not in move]
            new_left = self.left_Side + list(move)
            new_lamp = "left"

        step_time = max(p.time for p in move)
        new_time = self.time_Past + step_time

        return State(new_left, new_right, new_lamp, new_time, parent=self)
