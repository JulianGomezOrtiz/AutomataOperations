import automata.automata as automata
import showAutomata.showAutomata as showAutomata
import logic.logicAutomata as automataController


def main():
    while True:
        isValidInput = True
        while isValidInput:
            states = input(
                "Enter the states of automaton 1 separated by commas: ").split(",")
            if len(states) > 4:
                print("The automaton can only have 4 states!")
            else:
                isValidInput = False
        isValidInput = True
        alphabet = input(
            "Enter the alphabet of automaton 1 separated by commas: ").split(",")
        transitions = []
        for state in states:
            for symbol in alphabet:
                isValidInput = True
                while isValidInput:
                    next_state = input(
                        f"Enter the next state of state {state} with symbol {symbol}: ")
                    if next_state not in states:
                        print("The state does not belong to the automaton!")
                    else:
                        isValidInput = False
                        transitions.append(automata.Transition(
                            state, symbol, next_state))

        isValidInput = True

        while isValidInput:
            initial_state = input("Enter the initial state of automaton 1: ")
            if initial_state not in states:
                print("The state does not belong to the automaton!")
            else:
                isValidInput = False
        isValidInput = True

        while isValidInput:
            final_states = input(
                "Enter the final states of automaton 1 separated by commas: ").split(",")
            for state in final_states:
                if state not in states:
                    print("The state does not belong to the automaton!")
                    break
            else:
                isValidInput = False

        isValidInput = True

        automaton1 = automata.Automata(
            states, alphabet, transitions, initial_state, final_states)

        while isValidInput:
            states = input(
                "Enter the states of automaton 2 separated by commas: ").split(",")
            if len(states) > 4:
                print("The automaton can only have 4 states!")
            else:
                isValidInput = False

        alphabet = input(
            "Enter the alphabet of automaton 2 separated by commas: ").split(",")
        transitions = []
        for state in states:
            for symbol in alphabet:
                isValidInput = True
                while isValidInput:
                    next_state = input(
                        f"Enter the next state of state {state} with symbol {symbol}: ")
                    if next_state not in states:
                        print("The state does not belong to the automaton!")
                    else:
                        isValidInput = False
                        transitions.append(automata.Transition(
                            state, symbol, next_state))

        isValidInput = True
        while isValidInput:
            initial_state = input("Enter the initial state of automaton 2: ")
            if initial_state not in states:
                print("The state does not belong to the automaton!")
            else:
                isValidInput = False
        isValidInput = True

        while isValidInput:
            final_states = input(
                "Enter the final states of automaton 2 separated by commas: ").split(",")
            for state in final_states:
                if state not in states:
                    print("The state does not belong to the automaton!")
                    break
                else:
                    isValidInput = False

        automaton2 = automata.Automata(
            states, alphabet, transitions, initial_state, final_states)

        print("Do you want to enter a third automaton? (y : yes, any other key : no)")

        option = input("Enter an option: ")

        automaton3 = None
        if option.lower() == "y":
            isValidInput = True
            while isValidInput:
                states = input(
                    "Enter the states of automaton 3 separated by commas: ").split(",")
                if len(states) > 4:
                    print("The automaton can only have 4 states!")
                else:
                    isValidInput = False

            alphabet = input(
                "Enter the alphabet of automaton 3 separated by commas: ").split(",")
            transitions = []
            for state in states:
                for symbol in alphabet:
                    isValidInput = True
                    while isValidInput:
                        next_state = input(
                            f"Enter the next state of state {state} with symbol {symbol}: ")
                        if next_state not in states:
                            print("The state does not belong to the automaton!")
                        else:
                            isValidInput = False
                            transitions.append(automata.Transition(
                                state, symbol, next_state))

            isValidInput = True
            while isValidInput:
                initial_state = input(
                    "Enter the initial state of automaton 3: ")
                if initial_state not in states:
                    print("The state does not belong to the automaton!")
                else:
                    isValidInput = False
            isValidInput = True

            while isValidInput:
                final_states = input(
                    "Enter the final states of automaton 3 separated by commas: ").split(",")
                for state in final_states:
                    if state not in states:
                        print("The state does not belong to the automaton!")
                        break
                    else:
                        isValidInput = False

            automaton3 = automata.Automata(
                states, alphabet, transitions, initial_state, final_states)

        print("Which automaton do you want to use for the complement? (1 : Union, 2 : Intersection)")

        option = input("Enter an option: ")

        if automaton3 is None:
            automatonUnion = automataController.automataUnion(
                automaton1, automaton2)
            showAutomata.showAutomata(automatonUnion, "Union")
            automatonIntersection = automataController.automataIntersection(
                automaton1, automaton2)
            showAutomata.showAutomata(automatonIntersection, "Intersection")

            automatonComplement = None
            if option == "1":
                automatonComplement = automataController.automataComplement(
                    automatonUnion)
            else:
                automatonComplement = automataController.automataComplement(
                    automatonIntersection)
            showAutomata.showAutomata(automatonComplement, "Complement")
            automatonReverse = automataController.automataReverse(
                automatonIntersection)
            showAutomata.showAutomata(automatonReverse[1], "SimpleReverse")
            showAutomata.showAutomata(automatonReverse[0], "Reverse")

        else:
            automatonUnion = automataController.automataUnion(
                automataController.automataUnion(automaton1, automaton2), automaton3)
            showAutomata.showAutomata(automatonUnion, "Union")
            automatonIntersection = automataController.automataIntersection(
                automataController.automataIntersection(automaton1, automaton2), automaton3)
            showAutomata.showAutomata(automatonIntersection, "Intersection")

            automatonComplement = None
            if option == "1":
                automatonComplement = automataController.automataComplement(
                    automatonUnion)
            else:
                automatonComplement = automataController.automataComplement(
                    automatonIntersection)
            showAutomata.showAutomata(automatonComplement, "Complement")
            automatonReverse = automataController.automataReverse(
                automatonIntersection)
            showAutomata.showAutomata(automatonReverse[1], "SimpleReverse")
            showAutomata.showAutomata(automatonReverse[0], "Reverse")

        print("This is the initial state of the union automaton",
              automatonUnion.initial_state)
        print("This is the initial state of the intersection automaton",
              automatonIntersection.initial_state)

        print("Do you want to continue? (y : yes, any other key : no)")

        option = input("Enter an option: ")

        if option.lower() != "y":
            break


if __name__ == "__main__":
    main()
