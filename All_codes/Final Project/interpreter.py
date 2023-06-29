import math
import random

class Interpreter:
    def __init__(self, prog):
        self.prog = prog
        self.function = {
            'SIN': lambda z: math.sin(self.eval(z)),
            'COS': lambda z: math.cos(self.eval(z)),
            'TAN': lambda z: math.tan(self.eval(z)),
            'ATN': lambda z: math.atan(self.eval(z)),
            'EXP': lambda z: math.exp(self.eval(z)),
            'ABS': lambda z: abs(self.eval(z)),
            'LOG': lambda z: math.log(self.eval(z)),
            'SQR': lambda z: math.sqrt(self.eval(z)),
            'RND': lambda z: random.random()
        }

        # Check for end statements
        def check_end(self):
            has_end = 0
            for lineno in self.stat:
                if self.prog[lineno][0] == ';' and not has_end:
                    has_end = lineno
            if not has_end:
                print("NO END INSTRUCTION")
                self.error = 1
                return
            if has_end != lineno:
                print("END IS NOT LAST")
                self.error = 1
            # Check loops

        def check_loops(self):
            for pc in range(len(self.stat)):
                lineno = self.stat[pc]
                if self.prog[lineno][0] == 'for':
                    forinst = self.prog[lineno]
                    loopvar = forinst[1]
                    for i in range(pc + 1, len(self.stat)):
                        if self.prog[self.stat[i]][0] == 'while':
                            nextvar = self.prog[self.stat[i]][1]
                            if nextvar != loopvar:
                                continue
                            self.loopend[pc] = i
                            break
                    else:
                        print("Error %s" % self.stat[pc])
                        self.error = 1