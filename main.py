from person import Person
from state import State
from engine import Game

#----------------------------------------

p1 = Person("man 1", 1)
p2 = Person("man 2", 2)
p3 = Person("man 3", 5)
p4 = Person("man 4", 10)

all_People = [p1, p2, p3, p4]

#----------------------------------------
initial_state = State(
    left_Side=all_People,
    right_Side=[],
    lamp_Side="left",
    time_past=0,
    parent=None
)

#----------------------------------------
engine = Game(initial_state)
engine.reset()
engine.run()

#----------------------------------------
if engine.solutions:
    solution_path = engine.solutions[0]
    print("Found solution:\n")
    for index, state in enumerate(solution_path):
        left_Persons = [p.name for p in state.left_Side]
        right_Persons = [p.name for p in state.right_Side]
        print(f"Step {index}:")
        print(f"  Left Side: {left_Persons}")
        print(f"  Right Side: {right_Persons}")
        print(f"  Lamp Side: {state.lamp_Side}")
        print(f"  Time Passed: {state.time_Past}")
else:
    print("No solution found!")

#----------------------------------------