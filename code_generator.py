from generated.tis100Visitor import tis100Visitor
from generated.tis100Parser import tis100Parser


class CodeGenerator(tis100Visitor):
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
        # Generate code for label
        if ctx.instruction() is not None:
            print("   ", end="")
            self.visitInstruction(ctx.instruction())
        return

    def visitInstruction(self, ctx: tis100Parser.InstructionContext):
        ctx.getChild(0).accept(self)
        return

    def visitAddInstruction(self, ctx: tis100Parser.AddInstructionContext):
        # Generate code for ADD instruction
        self.visitOperand(ctx.operand())
        return

    def visitSubInstruction(self, ctx: tis100Parser.SubInstructionContext):
        # Generate code for SUB instruction
        self.visitOperand(ctx.operand())
        return

    def visitMoveInstruction(self, ctx: tis100Parser.MoveInstructionContext):
        # Generate code for MOV instruction
        self.visitOperand(ctx.operand(0))
        self.visitOperand(ctx.operand(1))
        return

    def visitConditional(self, ctx: tis100Parser.ConditionalContext):
        ctx.getChild(0).accept(self)
        return

    def visitEqualsCondition(self, ctx: tis100Parser.EqualsConditionContext):
        # Generate code for JEZ conditional
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
        print(ctx.getText())
        return
