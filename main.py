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
def print_tree(engine):
    print("\n--- States Tree ---\n")
    from collections import defaultdict

    tree = defaultdict(list)
    for parent_id, child_id in engine.tree_edges:
        tree[parent_id].append(child_id)

    def format_state(state):
        left = ', '.join(p.name for p in state.left_Side)
        right = ', '.join(p.name for p in state.right_Side)
        return f"Time={state.time_Past}, Lamp={state.lamp_Side}, Left=[{left}], Right=[{right}]"

    def print_node(state_id, prefix="", is_last=True):
        state = engine.all_states[state_id]
        connector = "└── " if is_last else "├── "
        print(prefix + connector + format_state(state))

        children = tree.get(state_id, [])
        for i, child_id in enumerate(children):
            last = i == (len(children) - 1)
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_node(child_id, new_prefix, last)

    print_node(engine.initial_state.id)


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
print_tree(engine)
#----------------------------------------