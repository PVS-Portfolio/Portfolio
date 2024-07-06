# From-scratch implementation of an assembler
import tkinter as tk

ALL = tk.N + tk.E + tk.S + tk.W

NUMINST = 20

class Assembler:

    def __init__(self):
        self.regs = {'r' + chr(97 + i): 0 for i in range(8)}
        self.pc = 1
        self.rom = {i: '' for i in range(1, NUMINST)}
        self.ram = [0 for i in range(200)]
        self.flags = {'lt': 0, 'gt': 0, 'ge': 0, 'le': 0,
                      'ne': 0, 'eq': 0,
                      'zero': 0,
                      }

    def load(self, name):
        i = 1
        f = open(name, 'r')
        for line in f:
            self.rom[i] = line.rstrip()
            i += 1
        f.close()

    def get_val(self, val):
        # Load value from memory address
        if val[0] == '$':
            val = self.ram[int(val[1:])]
        # Load value from register
        elif val[0] == 'r':
            val = self.regs[val]
        # Load literal
        else:
            val = int(val)
        return val

    def reset_flags(self):
        for i in self.flags:
            self.flags[i] = 0

    def cmp(self, inst):
        self.reset_flags()
        n1 = self.get_val(inst[1])
        n2 = self.get_val(inst[2])
        diff = n1 - n2
        if diff == 0:
            self.flags['le'] = 1
            self.flags['ge'] = 1
            self.flags['eq'] = 1
        else:
            self.flags['ne'] = 1
            if diff > 0:
                self.flags['ge'] = 1
                self.flags['gt'] = 1
            else:
                self.flags['le'] = 1
                self.flags['lt'] = 1
        self.pc += 1

    def ld(self, inst):
        val = self.get_val(inst[1])
        dest = inst[2]

        # Store val in address stored in ram
        if dest[0] == '$':
            dest = self.ram[int(dest[1:])]
            self.ram[dest] = val
        # Store val in ram address
        elif dest[0] == 'x':
            self.ram[int(dest[1:])] = val
        # Store val in register
        elif dest[0] == 'r':
            self.regs[dest] = val
        self.pc += 1

    def jmp(self, inst):
        val = self.get_val(inst[1])
        self.pc = val

    def jl(self, inst):
        if self.flags['lt']:
            self.jmp(inst)
        else:
            self.pc += 1

    def jg(self, inst):
        if self.flags['gt']:
            self.jmp(inst)
        else:
            self.pc += 1

    def jle(self, inst):
        if self.flags['le']:
            self.jmp(inst)
        else:
            self.pc += 1

    def je(self, inst):
        if self.flags['eq']:
            self.jmp(inst)
        else:
            self.pc += 1

    def jge(self, inst):
        if self.flags['ge']:
            self.jmp(inst)
        else:
            self.pc += 1

    def add(self, inst):
        val = self.get_val(inst[1])
        dest = inst[2]

        if dest[0] == '$':
            dest = self.ram[int(dest[1:])]
            self.ram[dest] += val
        elif dest[0] == 'x':
            self.ram[int(dest[1:])] += val
        # Store val in register
        elif dest[0] == 'r':
            self.regs[dest] += val
        self.pc += 1

    def sub(self, inst):
        val = self.get_val(inst[1])
        dest = inst[2]

        if dest[0] == '$':
            dest = self.ram[int(dest[1:])]
            self.ram[dest] -= val
        elif dest[0] == 'x':
            self.ram[int(dest[1:])] -= val
        # Store val in register
        elif dest[0] == 'r':
            self.regs[dest] -= val
        self.pc += 1

    def exec(self):

        if not self.rom[self.pc]: return
        inst = self.rom[self.pc].split()
        if inst[0] == 'ld':
            self.ld(inst)
        if inst[0] == 'jmp':
            self.jmp(inst)
        if inst[0] == 'cmp':
            self.cmp(inst)
        if inst[0] == 'jle':
            self.jle(inst)
        if inst[0] == 'jge':
            self.jge(inst)
        if inst[0] == 'jl':
            self.jl(inst)
        if inst[0] == 'jg':
            self.jg(inst)
        if inst[0] == 'add':
            self.add(inst)
        if inst[0] == 'sub':
            self.sub(inst)

    def run(self):

        while self.rom[self.pc]:
            self.exec()

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.assembler = Assembler()

        self.registers = [tk.IntVar() for i in range(9)]
        self.flags = {i: tk.IntVar() for i in self.assembler.flags}
        self.memory = [tk.IntVar() for i in range(len(self.assembler.ram))]
        for r in self.registers: r.set(0)
        for f in self.flags.values(): f.set(0)
        for m in self.memory: m.set(0)

        self.code = [tk.StringVar() for i in range(NUMINST)]
        self.linenums = [tk.IntVar() for i in range(NUMINST)]
        for i in range(NUMINST):
            self.linenums[i].set(i+1)

        self.windowframe = tk.Frame(self.root)
        self.windowframe.grid(padx=10, pady=10, sticky=ALL)

        self.regframe = tk.LabelFrame(self.windowframe, text='Registers', background='white')
        self.regframe.grid(row=0, column=0, sticky=ALL)

        tk.Label(self.regframe, text='PC:', background='white').grid(row=0, column=0, sticky=tk.W)
        for i in range(8):
            tk.Label(self.regframe, text=f'R{chr(65 + i)}:', background='white').grid(row=i+1, column=0, sticky=tk.W)
        tk.Label(self.regframe, textvariable=self.registers[0], background='white').grid(row=0, column=1, sticky=tk.W)
        for i in range(1, 9):
            tk.Label(self.regframe, textvariable=self.registers[i], background='white').grid(row=i, column=1, sticky=tk.W)

        self.flagframe = tk.LabelFrame(self.windowframe, text='Flags', background='white')
        self.flagframe.grid(row=1, column=0, sticky=ALL)

        c = 0
        for i in self.flags:
            tk.Label(self.flagframe, text=i.upper(), background='white').grid(row=c, column=0, sticky=tk.W)
            tk.Label(self.flagframe, textvariable=self.flags[i], background='white').grid(row=c, column=1, sticky=tk.W)
            c += 1

        self.codeframe = tk.LabelFrame(self.windowframe, text='Code', background='white')
        self.codeframe.grid(row=0, column=1, rowspan=2)
        for i in range(NUMINST):
            tk.Label(self.codeframe, textvariable=self.linenums[i], background='white').grid(row=i, column=0, sticky=tk.W)
            tk.Label(self.codeframe, textvariable=self.code[i], background='white', justify=tk.LEFT).grid(row=i, column=1, sticky=tk.W)

        self.memframe = tk.LabelFrame(self.windowframe, text='Memory', background='white')
        self.memframe.grid(row=0, column=2, rowspan=2)
        for i in range(20):
            for j in range(10):
                tk.Label(self.memframe, textvariable=self.memory[i*10+j],
                         background='white', width=10).grid(row=i, column=j, sticky=tk.W)

        tk.Button(self.windowframe, text='Load', command=self.load_program).grid(row=2, column=0)
        tk.Button(self.windowframe, text='Play', command=self.play).grid(row=2, column=1)

        self.get_regs()
        self.get_flags()
        self.get_mem()

        self.root.mainloop()

    def load_program(self):
        self.assembler.load('prog2')
        self.get_code()

    def get_regs(self):
        self.registers[0].set(self.assembler.pc)
        for i in range(0,8):
            self.registers[i+1].set(self.assembler.regs['r' + chr(97 + i)])

    def get_flags(self):
        for i in self.assembler.flags:
            self.flags[i].set(self.assembler.flags[i])

    def get_mem(self):
        for i in range(len(self.memory)):
            self.memory[i].set(self.assembler.ram[i])

    def get_code(self):
        curr = self.assembler.pc
        for i in range(1, len(self.assembler.rom) + 1):
            if not self.assembler.rom[i]: continue
            if i > NUMINST: continue
            if i == self.assembler.pc:
                self.code[i-1].set('* ' + self.assembler.rom[i])
            else:
                self.code[i-1].set('  ' + self.assembler.rom[i])

    def play(self):
        self.assembler.exec()
        self.get_regs()
        self.get_flags()
        self.get_mem()
        self.get_code()

def main():
    gui = GUI()
    # gui.assembler.load('prog1')
    # gui.assembler.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()