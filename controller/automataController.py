import model.automata as automata
from pyformlang.finite_automaton import State, Symbol, NondeterministicFiniteAutomaton, DeterministicFiniteAutomaton


def automataUnion(automata1: automata.Automata, automata2: automata.Automata):
    newAutomata = automata.Automata([], [], [], '', [])

 
    newAutomata.alphabet = list(
        set(automata1.alphabet) & set(automata2.alphabet))

   
    newAutomata.initial_state = automata1.initial_state + automata2.initial_state


    for state1 in automata1.states:
        for state2 in automata2.states:
            newAutomata.states.append(state1 + state2)


    for state1 in automata1.states:
        for state2 in automata2.states:
            for symbol in newAutomata.alphabet:
                next_state1 = ''
                for transition in automata1.transitions:
                    if transition.state == state1 and transition.symbol == symbol:
                        next_state1 = transition.next_state
                        break
                next_state2 = ''
                for transition in automata2.transitions:
                    if transition.state == state2 and transition.symbol == symbol:
                        next_state2 = transition.next_state
                        break
                next_state = next_state1 + next_state2
                new_state = state1 + state2
                newAutomata.transitions.append(
                    automata.Transition(new_state, symbol, next_state))

    for state1 in automata1.states:
        for state2 in automata2.states:
            if state1 in automata1.final_states or state2 in automata2.final_states:
                newAutomata.final_states.append(state1 + state2)

    newAutomata = validateTransitions(newAutomata)

    return newAutomata


def automataIntersection(automata1: automata.Automata, automata2: automata.Automata):
    newAutomata = automata.Automata([], [], [], '', [])

   
    newAutomata.alphabet = list(
        set(automata1.alphabet) & set(automata2.alphabet))

 
    newAutomata.initial_state = automata1.initial_state + automata2.initial_state


    for state1 in automata1.states:
        for state2 in automata2.states:
            newAutomata.states.append(state1 + state2)


    for state1 in automata1.states:
        for state2 in automata2.states:
            for symbol in newAutomata.alphabet:
                next_state1 = ''
                for transition in automata1.transitions:
                    if transition.state == state1 and transition.symbol == symbol:
                        next_state1 = transition.next_state
                        break
                next_state2 = ''
                for transition in automata2.transitions:
                    if transition.state == state2 and transition.symbol == symbol:
                        next_state2 = transition.next_state
                        break
                next_state = next_state1 + next_state2
                new_state = state1 + state2
                newAutomata.transitions.append(
                    automata.Transition(new_state, symbol, next_state))

    for state1 in automata1.final_states:
        for state2 in automata2.final_states:
            if state1 in automata1.final_states and state2 in automata2.final_states:
                newAutomata.final_states.append(state1 + state2)

    newAutomata = validateTransitions(newAutomata)

    return newAutomata


def automataComplement(automaton: automata.Automata):
    newAutomata = automata.Automata([], [], [], '', [])


    for state in automaton.states:
        newAutomata.states.append(state)
        if state == automaton.initial_state:
          
            newAutomata.initial_state = state
        if state in automaton.final_states:
           
            newAutomata.states.append(state)
        else:
           
            newAutomata.final_states.append(state)

  
    for transition in automaton.transitions:
        newAutomata.transitions.append(automata.Transition(
            transition.state, transition.symbol, transition.next_state))

    newAutomata = validateTransitions(newAutomata)

    return newAutomata


def automataReverse(automaton: automata.Automata):
    newAutomata = automata.Automata([], [], [], '', [])

   
    for state in automaton.states:
        newAutomata.states.append(state)
        if state == automaton.initial_state:
           
            newAutomata.final_states.append(state)
        elif state in automaton.final_states:
            newAutomata.initial_state = state 
    
    for transition in automaton.transitions:
        newAutomata.transitions.append(automata.Transition(
            transition.next_state, transition.symbol, transition.state))

    newAutomata.alphabet = automaton.alphabet

    autNFA = newAutomata

    newAutomata = build_nfa(newAutomata)
    newAutomata = nfa_to_dfa(newAutomata)

    autNFA = validateTransitions(autNFA)

    return newAutomata, autNFA


def validateTransitions(automaton: automata.Automata):

 
    while True: 
        transitionstoDelete = []
        contador = 0
        for state in automaton.states:
            for transition in automaton.transitions:
                if state in transition.next_state:
                    contador += 1

            if contador == 0 and state != automaton.initial_state:
                print(f"The state: {state} has no transitions")
                transitionstoDelete.append(state)
                automaton.states.remove(state)

            contador = 0

        print("These are the states to eliminate", transitionstoDelete)

       
        automaton.transitions = [transition for transition in automaton.transitions
                                 if transition.state not in transitionstoDelete
                                 and transition.next_state not in transitionstoDelete]

        print("These are the new transitions")
        for transition in automaton.transitions:
            print(f"State: {transition.state}, Symbol: {transition.symbol}, Next State: {transition.next_state}")
    
        if transitionstoDelete == []: 
            break
    return automaton


def isDFA(automaton: automata.Automata):
    seen_transitions = set()

    for transition in automaton.transitions:
        transition_tuple = (transition.state, transition.symbol)
        if transition_tuple in seen_transitions:
            return False
        seen_transitions.add(transition_tuple)

    return True


def nfa_to_dfa(nfa):
    dfa = nfa.to_deterministic()
    print("____________________________________________________")
    print(dfa)
    print("____________________________________________________")
    return dfa


def build_nfa(automaton):
    alphabet = set(automaton.alphabet)
    initial_state = State(automaton.initial_state)
    final_states = set(automaton.final_states)

    nfa = NondeterministicFiniteAutomaton()

    for state in automaton.states:
        nfa._states.add(State(state))
    nfa.add_start_state(initial_state)
    for final_state in final_states:
        nfa.add_final_state(State(final_state))

    for transition in automaton.transitions:
        nfa.add_transition(State(transition.state), Symbol(
            transition.symbol), State(transition.next_state))

    return nfa


