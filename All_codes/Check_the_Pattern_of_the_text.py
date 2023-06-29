'''
The code checks whether the given input string follows a specific pattern:
if the first character is a lowercase letter followed by an uppercase letter and a hyphen,
it is considered as state 1. If the first character is a digit,
it is considered as state 0. The code then determines the final state based on the type (0 or 1).
If the final state is reached, it prints either "NUM, {Value}" if the type is 0 or "ID, {Value}" if the type is 1.
If the input string does not match the specified pattern, it prints "ID,Number {Value}".
The code has a class Lexical with methods to handle the states and a Run method to execute the logic
'''
import re
class Lexical:
    def __init__(self):
        self.install = 'shayan'

    def set_install(self, install):
        self.install = install

    def check_pattern(self):
        first = self.install[0]
        if first.islower() and self.install[1:3] == "[-]":
            return 1
        elif first.isdigit():
            return 0
        else:
            return -1  # for error

    def final_state(self, type):
        if type == 0:
            for i in range(1, len(self.install)):
                if not self.check_pattern():
                    print(f"Error [{self.install}]")
                    return False
            return True
        elif type == 1:
            for i in range(1, len(self.install)):
                if not self.check_pattern():
                    print(f"Error [{self.install}]")
                    return False
            return True
        else:
            return False

    def run(self, install):
        self.set_install(install)
        if len(self.install) >= 1:
            t = self.check_pattern()
            if self.final_state(t):
                if t == 0:
                    print(f"NUM, {self.install}")
                else:
                    print(f"ID, {self.install}")
            else:
                print(f"ID, Number {self.install}")
        else:
            print("input, NULL")

if __name__ == "__main__":
    case1 = Lexical()
    A = "shayan_ebrahimi"
    split = A.split()

    for i in split:
        case1.run(i)

