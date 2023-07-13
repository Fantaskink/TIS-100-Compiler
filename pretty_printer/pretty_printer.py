from generated.tis100Visitor import tis100Visitor
from generated.tis100Parser import tis100Parser


class PrettyPrinter(tis100Visitor):
    def visitProgram(self, ctx: tis100Parser.ProgramContext):
        for line in ctx.line():
            self.visitLine(line)
        return

    def visitLine(self, ctx: tis100Parser.LineContext):
        ctx.getChild(0).accept(self)
        return

    def visitBreakpoint(self, ctx:tis100Parser.BreakpointContext):
        print("Breakpoint ", end="")
        return

    def visitLabel(self, ctx: tis100Parser.LabelContext):
        print("Label: " + str(ctx.Identifier()))
        if ctx.instruction() is not None:
            print("   ", end="")
            self.visitInstruction(ctx.instruction())
        return

    def visitInstruction(self, ctx: tis100Parser.InstructionContext):
        ctx.getChild(0).accept(self)
        return

    def visitAddInstruction(self, ctx: tis100Parser.AddInstructionContext):
        print("ADD Instruction")
        print("   Operand: ", end="")
        self.visitOperand(ctx.operand())
        return

    def visitSubInstruction(self, ctx: tis100Parser.SubInstructionContext):
        print("SUB Instruction")
        print("   Operand: ", end="")
        self.visitOperand(ctx.operand())
        return

    def visitMoveInstruction(self, ctx:tis100Parser.MoveInstructionContext):
        print("MOV Instruction")
        print("   SRC: ", end="")
        self.visitOperand(ctx.operand(0))
        print("   DST: ", end="")
        self.visitOperand(ctx.operand(1))
        return

    def visitConditional(self, ctx: tis100Parser.ConditionalContext):
        ctx.getChild(0).accept(self)
        return

    def visitEqualsCondition(self, ctx: tis100Parser.EqualsConditionContext):
        print("JEZ Conditional")
        print("   Label: " + ctx.Identifier().getText())
        return

    def visitGreaterCondition(self, ctx:tis100Parser.GreaterConditionContext):
        print("JGZ Conditional")
        print("   Label: " + ctx.Identifier().getText())
        return

    def visitLessCondition(self, ctx:tis100Parser.LessConditionContext):
        print("JLZ Conditional")
        print("   Label: " + ctx.Identifier().getText())
        return

    def visitMemoryInstruction(self, ctx:tis100Parser.MemoryInstructionContext):
        ctx.getChild(0).accept()
        return

    def visitJumpInstruction(self, ctx:tis100Parser.JumpInstructionContext):
        print("JMP Instruction")
        print("   Label: " + ctx.Identifier().getText())
        return

    def visitSaveInstruction(self, ctx:tis100Parser.SaveInstructionContext):
        print("SAV Instruction")
        return

    def visitSwapInstruction(self, ctx:tis100Parser.SwapInstructionContext):
        print("SWP Instruction")
        return

    def visitNoOperation(self, ctx:tis100Parser.NoOperationContext):
        print("NOP Instruction")
        return

    def visitOperand(self, ctx: tis100Parser.OperandContext):
        print(ctx.getText())
        return