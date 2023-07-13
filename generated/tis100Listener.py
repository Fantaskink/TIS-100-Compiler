# Generated from /Users/johan/PycharmProjects/pythonProject/ANTLR4/tis100.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tis100Parser import tis100Parser
else:
    from tis100Parser import tis100Parser

# This class defines a complete listener for a parse tree produced by tis100Parser.
class tis100Listener(ParseTreeListener):

    # Enter a parse tree produced by tis100Parser#program.
    def enterProgram(self, ctx:tis100Parser.ProgramContext):
        pass

    # Exit a parse tree produced by tis100Parser#program.
    def exitProgram(self, ctx:tis100Parser.ProgramContext):
        pass


    # Enter a parse tree produced by tis100Parser#line.
    def enterLine(self, ctx:tis100Parser.LineContext):
        pass

    # Exit a parse tree produced by tis100Parser#line.
    def exitLine(self, ctx:tis100Parser.LineContext):
        pass


    # Enter a parse tree produced by tis100Parser#breakpoint.
    def enterBreakpoint(self, ctx:tis100Parser.BreakpointContext):
        pass

    # Exit a parse tree produced by tis100Parser#breakpoint.
    def exitBreakpoint(self, ctx:tis100Parser.BreakpointContext):
        pass


    # Enter a parse tree produced by tis100Parser#label.
    def enterLabel(self, ctx:tis100Parser.LabelContext):
        pass

    # Exit a parse tree produced by tis100Parser#label.
    def exitLabel(self, ctx:tis100Parser.LabelContext):
        pass


    # Enter a parse tree produced by tis100Parser#instruction.
    def enterInstruction(self, ctx:tis100Parser.InstructionContext):
        pass

    # Exit a parse tree produced by tis100Parser#instruction.
    def exitInstruction(self, ctx:tis100Parser.InstructionContext):
        pass


    # Enter a parse tree produced by tis100Parser#addInstruction.
    def enterAddInstruction(self, ctx:tis100Parser.AddInstructionContext):
        pass

    # Exit a parse tree produced by tis100Parser#addInstruction.
    def exitAddInstruction(self, ctx:tis100Parser.AddInstructionContext):
        pass


    # Enter a parse tree produced by tis100Parser#subInstruction.
    def enterSubInstruction(self, ctx:tis100Parser.SubInstructionContext):
        pass

    # Exit a parse tree produced by tis100Parser#subInstruction.
    def exitSubInstruction(self, ctx:tis100Parser.SubInstructionContext):
        pass


    # Enter a parse tree produced by tis100Parser#moveInstruction.
    def enterMoveInstruction(self, ctx:tis100Parser.MoveInstructionContext):
        pass

    # Exit a parse tree produced by tis100Parser#moveInstruction.
    def exitMoveInstruction(self, ctx:tis100Parser.MoveInstructionContext):
        pass


    # Enter a parse tree produced by tis100Parser#conditional.
    def enterConditional(self, ctx:tis100Parser.ConditionalContext):
        pass

    # Exit a parse tree produced by tis100Parser#conditional.
    def exitConditional(self, ctx:tis100Parser.ConditionalContext):
        pass


    # Enter a parse tree produced by tis100Parser#equalsCondition.
    def enterEqualsCondition(self, ctx:tis100Parser.EqualsConditionContext):
        pass

    # Exit a parse tree produced by tis100Parser#equalsCondition.
    def exitEqualsCondition(self, ctx:tis100Parser.EqualsConditionContext):
        pass


    # Enter a parse tree produced by tis100Parser#greaterCondition.
    def enterGreaterCondition(self, ctx:tis100Parser.GreaterConditionContext):
        pass

    # Exit a parse tree produced by tis100Parser#greaterCondition.
    def exitGreaterCondition(self, ctx:tis100Parser.GreaterConditionContext):
        pass


    # Enter a parse tree produced by tis100Parser#lessCondition.
    def enterLessCondition(self, ctx:tis100Parser.LessConditionContext):
        pass

    # Exit a parse tree produced by tis100Parser#lessCondition.
    def exitLessCondition(self, ctx:tis100Parser.LessConditionContext):
        pass


    # Enter a parse tree produced by tis100Parser#memoryInstruction.
    def enterMemoryInstruction(self, ctx:tis100Parser.MemoryInstructionContext):
        pass

    # Exit a parse tree produced by tis100Parser#memoryInstruction.
    def exitMemoryInstruction(self, ctx:tis100Parser.MemoryInstructionContext):
        pass


    # Enter a parse tree produced by tis100Parser#jumpInstruction.
    def enterJumpInstruction(self, ctx:tis100Parser.JumpInstructionContext):
        pass

    # Exit a parse tree produced by tis100Parser#jumpInstruction.
    def exitJumpInstruction(self, ctx:tis100Parser.JumpInstructionContext):
        pass


    # Enter a parse tree produced by tis100Parser#saveInstruction.
    def enterSaveInstruction(self, ctx:tis100Parser.SaveInstructionContext):
        pass

    # Exit a parse tree produced by tis100Parser#saveInstruction.
    def exitSaveInstruction(self, ctx:tis100Parser.SaveInstructionContext):
        pass


    # Enter a parse tree produced by tis100Parser#swapInstruction.
    def enterSwapInstruction(self, ctx:tis100Parser.SwapInstructionContext):
        pass

    # Exit a parse tree produced by tis100Parser#swapInstruction.
    def exitSwapInstruction(self, ctx:tis100Parser.SwapInstructionContext):
        pass


    # Enter a parse tree produced by tis100Parser#noOperation.
    def enterNoOperation(self, ctx:tis100Parser.NoOperationContext):
        pass

    # Exit a parse tree produced by tis100Parser#noOperation.
    def exitNoOperation(self, ctx:tis100Parser.NoOperationContext):
        pass


    # Enter a parse tree produced by tis100Parser#operand.
    def enterOperand(self, ctx:tis100Parser.OperandContext):
        pass

    # Exit a parse tree produced by tis100Parser#operand.
    def exitOperand(self, ctx:tis100Parser.OperandContext):
        pass



del tis100Parser