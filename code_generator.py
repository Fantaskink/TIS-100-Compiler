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
        self.instruction_count = 0
        self.registers = {'ACC': 'X20', 'NIL': 'X31', 'IN': 'X21', 'OUT': 'X22',
                          'DAT': 'X23', 'BAK': 'X24', 'TEMP': 'X25'}

    def write_intro_boilerplate(self):
        self.code_lines.append(".global _main\n.align 3\n\n_main:")
        self.code_lines.append("   MOV " + self.registers["ACC"] + ", #0")
        self.code_lines.append("   MOV " + self.registers["BAK"] + ", #0")

    def write_outro_boilerplate(self):
        self.code_lines.append("MOV X0, #0\nMOV X16, #1\nSVC #0x80\n")
        self.code_lines.append(".data\nptfStr: .asciz \"%ld\\n\"\n.align 4\n.text")

    def generate_code(self, ast):
        self.write_intro_boilerplate()

        self.visitProgram(ast)

        self.write_outro_boilerplate()
        self.write_code_to_file("output/output.s")
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
        if ctx.breakpoint() is not None:
            self.visitBreakpoint(ctx.breakpoint())
            return ctx.getChild(1).accept(self)
        else:
            return ctx.getChild(0).accept(self)

    def visitBreakpoint(self, ctx: tis100Parser.BreakpointContext):
        # Generate code for breakpoint
        return

    def visitLabel(self, ctx: tis100Parser.LabelContext):
        self.append_instruction(str(ctx.Identifier()) + ":")
        if ctx.instruction() is not None:
            self.visitInstruction(ctx.instruction())
        return

    def visitInstruction(self, ctx: tis100Parser.InstructionContext):
        self.code_lines.append(f"OP{self.instruction_count}:")
        self.instruction_count += 1
        print(self.instruction_count)
        return ctx.getChild(0).accept(self)

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
        return

    def visitMoveInstruction(self, ctx: tis100Parser.MoveInstructionContext):
        src = ctx.operand(0).accept(self)
        dst = ctx.operand(1).accept(self)
        move_instruction = "   MOV " + str(dst) + ", " + str(src)
        self.append_instruction(move_instruction + "\n")
        if dst == self.registers["OUT"]:
            self.append_printf_instruction(dst)
        return

    def append_printf_instruction(self, src):
        self.code_lines.append("   // Setup for printf")
        self.code_lines.append("   MOV X0, " + src)
        self.code_lines.append("   ADRP X0, ptfStr@PAGE")
        self.code_lines.append("   ADD X0, X0, ptfStr@PAGEOFF")
        self.code_lines.append("   MOV X10, " + str(src))
        self.code_lines.append("   STR X10, [SP, #-16]!")
        self.code_lines.append("   BL _printf\n")
        self.code_lines.append("   ADD SP, SP, #16\n")

    def visitConditional(self, ctx: tis100Parser.ConditionalContext):
        return ctx.getChild(0).accept(self)

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

    def visitNotEqualsCondition(self, ctx: tis100Parser.NotEqualsConditionContext):
        acc = self.registers["ACC"]
        compare_instruction = "   CMP " + str(acc) + ", #0"
        self.append_instruction(compare_instruction)
        branch_instruction = "   B.NE " + str(ctx.Identifier())
        self.append_instruction(branch_instruction + "\n")
        return

    def visitMemoryInstruction(self, ctx: tis100Parser.MemoryInstructionContext):
        return ctx.getChild(0).accept(self)

    def visitJumpInstruction(self, ctx: tis100Parser.JumpInstructionContext):
        jump_instruction = "   B " + str(ctx.Identifier())
        self.append_instruction(jump_instruction)
        return

    def visitSaveInstruction(self, ctx: tis100Parser.SaveInstructionContext):
        acc = self.registers["ACC"]
        bak = self.registers["BAK"]
        save_instruction = "   MOV " + str(bak) + ", " + str(acc)
        self.append_instruction(save_instruction + "\n")
        return

    def visitSwapInstruction(self, ctx: tis100Parser.SwapInstructionContext):
        acc = self.registers["ACC"]
        bak = self.registers["BAK"]
        intermediate = self.registers["TEMP"]
        swap_instruction = "   MOV " + str(intermediate) + ", " + str(acc)
        self.append_instruction(swap_instruction)
        swap_instruction = "   MOV " + str(acc) + ", " + str(bak)
        self.append_instruction(swap_instruction)
        swap_instruction = "   MOV " + str(bak) + ", " + str(intermediate)
        self.append_instruction(swap_instruction + "\n")
        return

    def visitNoOperation(self, ctx: tis100Parser.NoOperationContext):
        # Generate code for NOP instruction
        return

    def visitOperand(self, ctx: tis100Parser.OperandContext):
        return ctx.getChild(0).accept(self)

    def visitAccumulatorOperand(self, ctx: tis100Parser.AccumulatorOperandContext):
        return self.registers["ACC"]

    def visitInOperand(self, ctx: tis100Parser.InOperandContext):
        return self.registers["IN"]

    def visitOutOperand(self, ctx: tis100Parser.OutOperandContext):
        return self.registers["OUT"]

    def visitDataOperand(self, ctx: tis100Parser.DataOperandContext):
        return self.registers["DAT"]

    def visitNilOperand(self, ctx: tis100Parser.NilOperandContext):
        return self.registers["NIL"]

    def visitTerminal(self, node):
        if not can_parse_to_int(node):
            return

        is_negative = get_is_negative(node)

        parsed_constant = parse_to_int(node)

        # If the constant is over 999, set it to 999
        if len(str(parsed_constant)) > 3:
            parsed_constant = 999

        # If the constant is negative, load it into a register and negate it, then return the register
        if is_negative:
            register = self.registers["TEMP"]
            load_instruction = get_load_register_instruction(parsed_constant, register)
            self.append_instruction(load_instruction)
            neg_instruction = get_negate_instruction(register)
            self.append_instruction(neg_instruction)
            return register

        return "#" + str(parsed_constant)
