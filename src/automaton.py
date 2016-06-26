# -*- coding:utf-8 -*-


class Automaton:

    def __init__(self, alfabet=[], state=[], init=None, transition={}, final=[]):
        self.alfabet = alfabet
        self.state = state
        self.init = init
        self.transition = transition
        self.final = final
        self.current_status = init
        self.head_position = 0

    def add_character_alfabet(self, alfabet):
        if alfabet not in self.alfabet:
            self.alfabet.append(alfabet)
            return True
        else:
            return False

    def add_state(self, state):
        if state not in self.state:
            self.state.append(state)
            self.transition[state] = {}
            return True
        else:
            return False

    def set_init(self, init):
        if init in self.state:
            self.init = init
            self.current_status = init
            return True
        else:
            return False

    def add_transition(self, current_status, character_read, next_state):
        if current_status in self.state and character_read in self.alfabet:
            if character_read not in self.transition[current_status].keys():
                self.transition[current_status][character_read] = next_state
                return True
            else:
                return False
        else:
            return False

    def add_final_state(self, final_state):
        if final_state in self.state:
            self.final.append(final_state)
            return True
        else:
            return False

    def get_state_mar_current(self):
        result = []
        for x in self.state:
            if x == self.current_status:
                result.append([x, True])
            else:
                result.append(x)
        return result

    def get_transition_table(self):
        transitions_table = []
        for x in self.transition.keys():
            for y in self.transition[x].keys():
                transitions_table.append((x, self.transition[x][y], y))
        return transitions_table

    def read_character(self, character_read):
        if character_read in self.alfabet:
            new_state = self.transition[self.current_status][character_read]
            transitions_table = []
            for x in self.transition.keys():
                for y in self.transition[x].keys():
                    if self.current_status == x and character_read == y:
                        transitions_table.append(
                            (x, self.transition[x][y], y, True)
                        )
                    else:
                        transitions_table.append(
                            (x, self.transition[x][y], y)
                        )
            self.current_status = new_state
            return transitions_table
        else:
            return []

    def validate(self):
        if len(self.transition) == len(self.state):
            for x in self.transition.keys():
                if len(self.transition[x].keys()) == len(self.alfabet):
                    return True
                else:
                    return False
        else:
            False
