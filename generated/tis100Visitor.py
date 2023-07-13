# Generated from /Users/johan/PycharmProjects/pythonProject/ANTLR4/tis100.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tis100Parser import tis100Parser
else:
    from tis100Parser import tis100Parser

# This class defines a complete generic visitor for a parse tree produced by tis100Parser.

class tis100Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by tis100Parser#program.
    def visitProgram(self, ctx:tis100Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#line.
    def visitLine(self, ctx:tis100Parser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#breakpoint.
    def visitBreakpoint(self, ctx:tis100Parser.BreakpointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#label.
    def visitLabel(self, ctx:tis100Parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#instruction.
    def visitInstruction(self, ctx:tis100Parser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#addInstruction.
    def visitAddInstruction(self, ctx:tis100Parser.AddInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#subInstruction.
    def visitSubInstruction(self, ctx:tis100Parser.SubInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#moveInstruction.
    def visitMoveInstruction(self, ctx:tis100Parser.MoveInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#conditional.
    def visitConditional(self, ctx:tis100Parser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#equalsCondition.
    def visitEqualsCondition(self, ctx:tis100Parser.EqualsConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#greaterCondition.
    def visitGreaterCondition(self, ctx:tis100Parser.GreaterConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#lessCondition.
    def visitLessCondition(self, ctx:tis100Parser.LessConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#memoryInstruction.
    def visitMemoryInstruction(self, ctx:tis100Parser.MemoryInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#jumpInstruction.
    def visitJumpInstruction(self, ctx:tis100Parser.JumpInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#saveInstruction.
    def visitSaveInstruction(self, ctx:tis100Parser.SaveInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#swapInstruction.
    def visitSwapInstruction(self, ctx:tis100Parser.SwapInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#noOperation.
    def visitNoOperation(self, ctx:tis100Parser.NoOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#operand.
    def visitOperand(self, ctx:tis100Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#accumulatorOperand.
    def visitAccumulatorOperand(self, ctx:tis100Parser.AccumulatorOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#upOperand.
    def visitUpOperand(self, ctx:tis100Parser.UpOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#downOperand.
    def visitDownOperand(self, ctx:tis100Parser.DownOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tis100Parser#dataOperand.
    def visitDataOperand(self, ctx:tis100Parser.DataOperandContext):
        return self.visitChildren(ctx)



del tis100Parser