"""CPU functionality."""

import sys

# List of instructions codes
ADD = 0b10100000  # add
AND = 0b10101000
CALL = 0b01010000  # call
CMP = 0b10100111  # compare
DEC = 0b01100110
DIV = 0b10100011
HLT = 0b00000001  # halt the CPU and exit the emulator
INC = 0b01100101
INT = 0b01010010
IRET = 0b00010011
JEQ = 0b01010101  # equal
JGE = 0b01011010
JGT = 0b01010111
JLE = 0b01011001
JLT = 0b01011000
JMP = 0b01010100  # jump
JNE = 0b01010110  # not equal
LD = 0b10000011
# load "immediate", store a value in a register, or "set this register to this value".
LDI = 0b10000010
MOD = 0b10100100
# a pseudo-instruction that prints the numeric value stored in a register.
PRN = 0b01000111
MUL = 0b10100010  # multiply
NOP = 0b00000000
NOT = 0b01101001  # inverter
OR = 0b10101010  # two inputs one output
POP = 0b01000110  # pop off the stack
PRA = 0b01001000
PUSH = 0b01000101  # push onto the stack
RET = 0b00010001  # return
SHL = 0b10101100
SHR = 0b10101101
ST = 0b10000100
SUB = 0b10100001  # subtract
XOR = 0b10101011


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # 256 bytes of memory for cpu
        self.ram = [0] * 256
        # 8 general purpose registers
        self.register = [0] * 8
        # System program counter
        self.pc = 0
        # Stack Pointer
        self.sp = 7
        # CPU running state
        self.running = True

    def read_ram(self, address):
        if address < len(self.ram):
            return self.ram[address]
        else:
            print("Address is wrong" + str(address))
            sys.exit(1)

    def write_ram(self, value, address):
        self.ram[address] = value

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == 'SUB':
            self.reg[reg_a] -= self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass
