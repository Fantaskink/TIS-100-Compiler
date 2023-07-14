from generated.tis100Visitor import tis100Visitor
from generated.tis100Parser import tis100Parser


def can_parse_to_int(node):
    import re
    string = node.getText().strip("\n").strip("-")
    pattern = r'^\d+$'
    return bool(re.match(pattern, string))


def parse_to_int(node):
    return int(node.getText().strip("\n").strip("-"))


def get_is_negative(node):
    return node.getText().strip("\n").startswith("-")


def get_load_register_instruction(value, register):
    return "   MOV " + register + ", #" + str(value)


def get_negate_instruction(register):
    return "   NEG " + register + ", " + register


class CodeGenerator(tis100Visitor):
    def __init__(self):
        self.code_lines = []
        self.registers = {'ACC': 'X1', 'NIL': 'X10', 'IN': 'X2', 'OUT': 'X3', 'DAT': 'X4'}

    def write_intro_boilerplate(self):
        self.code_lines.append(".global _main\n.align 3\n\n_main:")

    def write_outro_boilerplate(self):
        self.code_lines.append("MOV X0, #0\nMOV X16, #1\nSVC #0x80")

    def generate_code(self, ast):
        self.write_intro_boilerplate()

        self.visitProgram(ast)

        self.write_outro_boilerplate()
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
        self.append_instruction(str(ctx.Identifier()) + ":")
        if ctx.instruction() is not None:
            self.visitInstruction(ctx.instruction())
        return

    def visitInstruction(self, ctx: tis100Parser.InstructionContext):
        ctx.getChild(0).accept(self)
        return

    def visitAddInstruction(self, ctx: tis100Parser.AddInstructionContext):
        src = ctx.operand().accept(self)
        dst = self.registers["ACC"]
        add_instruction = "   ADD " + str(dst) + ", " + str(dst) + ", " + str(src)
        self.append_instruction(add_instruction + "\n")
        return

    def visitSubInstruction(self, ctx: tis100Parser.SubInstructionContext):
        src = ctx.operand().accept(self)
        dst = self.registers["ACC"]
        sub_instruction = "   SUB " + str(dst) + ", " + str(dst) + ", " + str(src)
        self.append_instruction(sub_instruction + "\n")
        self.visitOperand(ctx.operand())
        return

    def visitMoveInstruction(self, ctx: tis100Parser.MoveInstructionContext):
        src = ctx.operand(0).accept(self)
        dst = ctx.operand(1).accept(self)
        move_instruction = "   MOV " + str(dst) + ", " + str(src)
        self.append_instruction(move_instruction + "\n")
        return

    def visitConditional(self, ctx: tis100Parser.ConditionalContext):
        ctx.getChild(0).accept(self)
        return

    def visitEqualsCondition(self, ctx: tis100Parser.EqualsConditionContext):
        acc = self.registers["ACC"]
        compare_instruction = "   CMP " + str(acc) + ", #0"
        self.append_instruction(compare_instruction)
        branch_instruction = "   B.EQ " + str(ctx.Identifier())
        self.append_instruction(branch_instruction + "\n")
        return

    def visitGreaterCondition(self, ctx: tis100Parser.GreaterConditionContext):
        acc = self.registers["ACC"]
        compare_instruction = "   CMP " + str(acc) + ", #0"
        self.append_instruction(compare_instruction)
        branch_instruction = "   B.GT " + str(ctx.Identifier())
        self.append_instruction(branch_instruction + "\n")
        return

    def visitLessCondition(self, ctx: tis100Parser.LessConditionContext):
        acc = self.registers["ACC"]
        compare_instruction = "   CMP " + str(acc) + ", #0"
        self.append_instruction(compare_instruction)
        branch_instruction = "   B.LT " + str(ctx.Identifier())
        self.append_instruction(branch_instruction + "\n")
        return

    def visitMemoryInstruction(self, ctx: tis100Parser.MemoryInstructionContext):
        ctx.getChild(0).accept()
        return

    def visitJumpInstruction(self, ctx: tis100Parser.JumpInstructionContext):
        jump_instruction = "   B " + str(ctx.Identifier())
        self.append_instruction(jump_instruction)
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
        if not can_parse_to_int(node):
            return

        is_negative = get_is_negative(node)

        parsed_constant = parse_to_int(node)

        # If the constant is over 999, set it to 999
        if len(str(parsed_constant)) > 3:
            parsed_constant = 999

        register = "X0"

        instruction = get_load_register_instruction(parsed_constant, register)
        self.append_instruction(instruction)

        if is_negative:
            instruction = get_negate_instruction(register)
            self.append_instruction(instruction)

        return register

