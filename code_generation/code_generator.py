from generated.tis100Visitor import tis100Visitor
from generated.tis100Parser import tis100Parser


def can_parse_to_int(node):
    constant = node.getText().strip("\n")
    try:
        int(constant)
        return True
    except ValueError:
        return False


def parse_to_int(node):
    return int(node.getText().strip("\n"))


class CodeGenerator(tis100Visitor):
    def __init__(self):
        self.code_lines = []
        self.registers = {'ACC': 'X0', 'NIL': 'X10', 'UP': 'X0', 'DOWN': 'X1', 'DAT': 'X2'}

    def generate_code(self, ast):
        self.code_lines.append(".global _main\n.align 3\n\n_main:")

        self.visitProgram(ast)

        self.code_lines.append("MOV X0, #0\nMOV X16, #1\nSVC #0x80")
        self.write_code_to_file("output/program.s")
        return

    def append_instruction(self, instruction):
        self.code_lines.append(instruction)

    def write_code_to_file(self, filename):
        with open(filename, 'w') as f:
            for line in self.code_lines:
                f.write(line + "\n")

    def visitProgram(self, ctx: tis100Parser.ProgramContext):
        for line in ctx.line():
            self.visitLine(line)
        return

    def visitLine(self, ctx: tis100Parser.LineContext):
        ctx.getChild(0).accept(self)
        return

    def visitBreakpoint(self, ctx: tis100Parser.BreakpointContext):
        # Generate code for breakpoint
        return

    def visitLabel(self, ctx: tis100Parser.LabelContext):
        print("Visit label")
        self.append_instruction(str(ctx.Identifier()) + ":")
        if ctx.instruction() is not None:
            print("   ", end="")
            self.visitInstruction(ctx.instruction())
        return

    def visitInstruction(self, ctx: tis100Parser.InstructionContext):
        ctx.getChild(0).accept(self)
        return

    def visitAddInstruction(self, ctx: tis100Parser.AddInstructionContext):
        print("Visit add instruction")
        src = ctx.operand().accept(self)
        dst = self.registers["ACC"]
        add_instruction = "   ADD " + str(dst) + ", " + str(dst) + ", " + str(src)
        print(add_instruction)
        self.append_instruction(add_instruction)
        return

    def visitSubInstruction(self, ctx: tis100Parser.SubInstructionContext):
        src = ctx.operand().accept(self)
        dst = self.registers["ACC"]
        sub_instruction = "   SUB " + str(dst) + ", " + str(dst) + ", " + str(src)
        print(sub_instruction)
        self.append_instruction(sub_instruction)
        self.visitOperand(ctx.operand())
        return

    def visitMoveInstruction(self, ctx: tis100Parser.MoveInstructionContext):
        print("Visit move instruction")
        src = ctx.operand(0).accept(self)
        dst = ctx.operand(1).accept(self)
        move_instruction = "   MOV " + str(dst) + ", " + str(src)
        self.append_instruction(move_instruction)
        return

    def visitConditional(self, ctx: tis100Parser.ConditionalContext):
        ctx.getChild(0).accept(self)
        return

    def visitEqualsCondition(self, ctx: tis100Parser.EqualsConditionContext):
        print("Visit equals condition")
        acc = self.registers["ACC"]
        equals_instruction = "   CMP " + str(acc) + ", #0"
        self.append_instruction(equals_instruction)
        branch_instruction = "   B.EQ " + str(ctx.Identifier())
        self.append_instruction(branch_instruction)
        return

    def visitGreaterCondition(self, ctx: tis100Parser.GreaterConditionContext):
        # Generate code for JGZ conditional
        return

    def visitLessCondition(self, ctx: tis100Parser.LessConditionContext):
        # Generate code for JLZ conditional
        return

    def visitMemoryInstruction(self, ctx: tis100Parser.MemoryInstructionContext):
        ctx.getChild(0).accept()
        return

    def visitJumpInstruction(self, ctx: tis100Parser.JumpInstructionContext):
        # Generate code for JMP instruction
        return

    def visitSaveInstruction(self, ctx: tis100Parser.SaveInstructionContext):
        # Generate code for SAV instruction
        return

    def visitSwapInstruction(self, ctx: tis100Parser.SwapInstructionContext):
        # Generate code for SWP instruction
        return

    def visitNoOperation(self, ctx: tis100Parser.NoOperationContext):
        # Generate code for NOP instruction
        return

    def visitOperand(self, ctx: tis100Parser.OperandContext):
        return ctx.getChild(0).accept(self)

    def visitAccumulatorOperand(self, ctx: tis100Parser.AccumulatorOperandContext):
        return self.registers["ACC"]

    def visitTerminal(self, node):
        if can_parse_to_int(node):
            constant = parse_to_int(node)
            if constant > 999:
                return "#999"
            elif constant < -999:
                return "#-999"
            else:
                return "#" + str(constant)
