class Emulator:
    def __init__(self, instructions):
        self.instructions = instructions
        self.trace = []
        self.acc = 0
        self.pointer = 0

        self.fns = {"nop": self._nop, "acc": self._acc, "jmp": self._jmp}

    def run(self):
        self.pointer = 0
        self.acc = 0
        self.trace = []
        while self.pointer < len(self.instructions):
            if self.pointer in self.trace:
                return self.acc
            self.trace.append(self.pointer)
            inst = self.instructions[self.pointer]
            self.fns[inst[:3]](int(inst[4:]))
        return self.acc

    def run_repair(self):
        insts = self.instructions[:]
        for i in range(len(self.instructions)):
            if self.instructions[i][:3] == "acc":
                continue
            elif self.instructions[i][:3] == "jmp":
                self.instructions[i] = "nop +0"
            else:
                self.instructions[i] = "jmp " + self.instructions[i][4:]
            self.run()
            if len(self.instructions) - 1 in self.trace:
                return self.acc

            self.instructions = insts[:]
        return 0

    def _nop(self, value):
        self.pointer += 1

    def _acc(self, value):
        self.acc += value
        self.pointer += 1

    def _jmp(self, value):
        self.pointer += value


if __name__ == "__main__":
    with open("08/input.txt") as f:
        emulator = Emulator(f.readlines())
    print(emulator.run())
    print(emulator.run_repair())
