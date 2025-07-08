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
        self.tree_edges = []  # العلاقات بين الحالات (الأب → الابن)
        self.all_states = {}  # لتخزين كل الحالات حسب id


    #-------------------------------------------
    @DefFacts()
    def initial_facts(self):
        yield CurrentState(state=self.initial_state)
        yield NextState(state=self.initial_state)
        self.all_states[self.initial_state.id] = self.initial_state
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

        self.declare(Visited(state=state))

        for next_state in state.next_States():
            if next_state.time_Past <= 17:
                self.tree_edges.append((state.id, next_state.id))
                self.all_states[next_state.id] = next_state
                self.declare(CurrentState(state=next_state))
                self.declare(NextState(state=next_state))
