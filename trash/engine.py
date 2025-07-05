# from experta import *
# from state import State

# #-----------------------------------------------
# class Game(KnowledgeEngine):
#     def __init__(self, initial_state):
#         super().__init__()
#         self.initial_state = initial_state
#         self.visited = set()
#         self.solutions = []

# #-----------------------------------------------
#     @DefFacts()
#     def _initial_action(self):
#         yield Fact(state=self.initial_state)

#     @Rule(Fact(state=MATCH.current_state))
#     def generate_next_states(self, current_state):
#         print(f"Exploring state:")
#         print(f"  Left  = {[p.name for p in current_state.left_Side]}")
#         print(f"  Right = {[p.name for p in current_state.right_Side]}")
#         print(f"  Lamp  = {current_state.lamp_Side}")
#         print(f"  Time  = {current_state.time_Past}")

#         if current_state in self.visited:
#             return
#         path = current_state.is_Goal()
#         if path:
#             self.solutions.append(path) 
#             return

#         self.visited.add(current_state)

#         for state in current_state.next_States():
#             if state not in self.visited and state.time_Past <= 17:
#                 self.declare(Fact(state=state))

# #-----------------------------------------------
































from experta import *

#-----------------------------------------------------------
class CurrentState(Fact):
    pass

class Visited(Fact):
    pass

class NextState(Fact):
    pass

#-----------------------------------------------------------
class Game(KnowledgeEngine):
    def __init__(self, initial_state):
        super().__init__()
        self.initial_state = initial_state
        self.solutions = []

    #-------------------------------------------
    @DefFacts()
    def initial_facts(self):
        yield CurrentState(state=self.initial_state)
        yield NextState(state=self.initial_state)

    #-------------------------------------------
    @Rule(CurrentState(state=MATCH.state),
          TEST(lambda state: state.is_Goal() is not None))
    def goal_found(self, state):
        print("Goal reached!")
        self.solutions.append(state.is_Goal())

    #-------------------------------------------
    @Rule(NextState(state=MATCH.state),
          NOT(Visited(state=MATCH.state)),
          TEST(lambda state: state.time_Past <= 17))
    def expand_state(self, state):
        # print(f"Exploring state:")
        # print(f"  Left  = {[p.name for p in state.left_Side]}")
        # print(f"  Right = {[p.name for p in state.right_Side]}")
        # print(f"  Lamp  = {state.lamp_Side}")
        # print(f"  Time  = {state.time_Past}")

        self.declare(Visited(state=state))

        for next_state in state.next_States():
            if next_state.time_Past <= 17:
                self.declare(CurrentState(state=next_state))
                self.declare(NextState(state=next_state))
