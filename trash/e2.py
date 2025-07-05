from experta import *
#-----------------------------------------------------------

class CurrentState(Fact):
    pass

class Visited(Fact):
    pass

class GoalReached(Fact):
    pass

class NextStates(Fact):
    pass

#-----------------------------------------------------------
class Game(KnowledgeEngine):
    def __init__(self, initial_state):
        super().__init__()
        self.initial_state = initial_state
        self.solutions = []
        self.visited = set()

    #-------------------------------------------
    @DefFacts()
    def initial_facts(self):
        yield CurrentState(state=self.initial_state)
        yield NextStates(state=self.initial_state)

    #-------------------------------------------
    # @Rule(CurrentState(state=MATCH.state),
    #       TEST(lambda state: state in Game.visited_set))
    # def already_visited(self, state):
    #     pass

    #-------------------------------------------
    @Rule(CurrentState(state=MATCH.state),
          TEST(lambda state: state.is_Goal() is not None))
    def goal_found(self, state):
        print("Goal reached!")
        self.solutions.append(state.is_Goal())

    #-------------------------------------------
    @Rule(NextStates(state=MATCH.state),
          TEST(lambda state: state not in Game.visited_set and state.time_Past <= 17))
    def expand_state(self, state):
        print(f"Exploring state:")
        print(f"  Left  = {[p.name for p in state.left_Side]}")
        print(f"  Right = {[p.name for p in state.right_Side]}")
        print(f"  Lamp  = {state.lamp_Side}")
        print(f"  Time  = {state.time_Past}")

        Game.visited_set.add(state)
        self.declare(Visited(state=state))

        for next_state in state.next_States():
            if next_state.time_Past <= 17:
                self.declare(CurrentState(state=next_state))
                self.declare(NextStates(state=next_state))

    #-------------------------------------------
    @staticmethod
    def reset_visited():
        Game.visited_set = set()

#-------------------------------------------
Game.reset_visited()