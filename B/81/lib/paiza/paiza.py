import sys
class Input:
    def __init__(self):
        self.argv = []
        self.input = ""

        if (0 < len(sys.argv)):
            self.argv = sys.argv
        elif len(first_input = input()) != 0:
            self.input = first_input

    def getInput(self):
        if len(self.input) != 0:
            print(self.input)
        elif len(sys.argv) != 0:
            print(sys.argv)

