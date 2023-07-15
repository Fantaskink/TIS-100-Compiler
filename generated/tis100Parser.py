# Generated from /Users/johan/PycharmProjects/pythonProject/ANTLR4/tis100.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,142,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,1,3,1,58,8,1,1,1,1,1,1,1,3,1,63,8,1,1,2,1,2,1,3,1,3,
        1,3,3,3,70,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,79,8,4,1,5,1,5,1,
        5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,96,8,8,1,9,
        1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,3,
        13,112,8,13,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,3,18,130,8,18,1,19,1,19,1,20,1,20,1,
        21,1,21,1,22,1,22,1,23,1,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,1,1,0,20,21,138,0,51,
        1,0,0,0,2,57,1,0,0,0,4,64,1,0,0,0,6,66,1,0,0,0,8,78,1,0,0,0,10,80,
        1,0,0,0,12,83,1,0,0,0,14,86,1,0,0,0,16,95,1,0,0,0,18,97,1,0,0,0,
        20,100,1,0,0,0,22,103,1,0,0,0,24,106,1,0,0,0,26,111,1,0,0,0,28,113,
        1,0,0,0,30,116,1,0,0,0,32,118,1,0,0,0,34,120,1,0,0,0,36,129,1,0,
        0,0,38,131,1,0,0,0,40,133,1,0,0,0,42,135,1,0,0,0,44,137,1,0,0,0,
        46,139,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,
        0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,
        1,1,0,0,0,56,58,3,4,2,0,57,56,1,0,0,0,57,58,1,0,0,0,58,62,1,0,0,
        0,59,63,3,6,3,0,60,63,3,8,4,0,61,63,5,24,0,0,62,59,1,0,0,0,62,60,
        1,0,0,0,62,61,1,0,0,0,63,3,1,0,0,0,64,65,5,1,0,0,65,5,1,0,0,0,66,
        67,7,0,0,0,67,69,5,2,0,0,68,70,3,8,4,0,69,68,1,0,0,0,69,70,1,0,0,
        0,70,7,1,0,0,0,71,79,3,10,5,0,72,79,3,12,6,0,73,79,3,14,7,0,74,79,
        3,16,8,0,75,79,3,26,13,0,76,79,3,28,14,0,77,79,3,34,17,0,78,71,1,
        0,0,0,78,72,1,0,0,0,78,73,1,0,0,0,78,74,1,0,0,0,78,75,1,0,0,0,78,
        76,1,0,0,0,78,77,1,0,0,0,79,9,1,0,0,0,80,81,5,3,0,0,81,82,3,36,18,
        0,82,11,1,0,0,0,83,84,5,4,0,0,84,85,3,36,18,0,85,13,1,0,0,0,86,87,
        5,5,0,0,87,88,3,36,18,0,88,89,5,6,0,0,89,90,3,36,18,0,90,15,1,0,
        0,0,91,96,3,18,9,0,92,96,3,20,10,0,93,96,3,22,11,0,94,96,3,24,12,
        0,95,91,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,17,
        1,0,0,0,97,98,5,7,0,0,98,99,7,0,0,0,99,19,1,0,0,0,100,101,5,8,0,
        0,101,102,7,0,0,0,102,21,1,0,0,0,103,104,5,9,0,0,104,105,7,0,0,0,
        105,23,1,0,0,0,106,107,5,10,0,0,107,108,7,0,0,0,108,25,1,0,0,0,109,
        112,3,30,15,0,110,112,3,32,16,0,111,109,1,0,0,0,111,110,1,0,0,0,
        112,27,1,0,0,0,113,114,5,11,0,0,114,115,7,0,0,0,115,29,1,0,0,0,116,
        117,5,12,0,0,117,31,1,0,0,0,118,119,5,13,0,0,119,33,1,0,0,0,120,
        121,5,14,0,0,121,35,1,0,0,0,122,130,3,38,19,0,123,130,3,40,20,0,
        124,130,3,42,21,0,125,130,3,44,22,0,126,130,1,0,0,0,127,130,3,46,
        23,0,128,130,5,20,0,0,129,122,1,0,0,0,129,123,1,0,0,0,129,124,1,
        0,0,0,129,125,1,0,0,0,129,126,1,0,0,0,129,127,1,0,0,0,129,128,1,
        0,0,0,130,37,1,0,0,0,131,132,5,15,0,0,132,39,1,0,0,0,133,134,5,16,
        0,0,134,41,1,0,0,0,135,136,5,17,0,0,136,43,1,0,0,0,137,138,5,18,
        0,0,138,45,1,0,0,0,139,140,5,19,0,0,140,47,1,0,0,0,8,51,57,62,69,
        78,95,111,129
    ]

class tis100Parser ( Parser ):

    grammarFileName = "tis100.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "':'", "'ADD'", "'SUB'", "'MOV'", 
                     "','", "'JEZ'", "'JGZ'", "'JLZ'", "'JNZ'", "'JMP'", 
                     "'SAV'", "'SWP'", "'NOP'", "'ACC'", "'IN'", "'OUT'", 
                     "'DAT'", "'NIL'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Constant", "Identifier", "Comment", "Whitespace", 
                      "Newline" ]

    RULE_program = 0
    RULE_line = 1
    RULE_breakpoint = 2
    RULE_label = 3
    RULE_instruction = 4
    RULE_addInstruction = 5
    RULE_subInstruction = 6
    RULE_moveInstruction = 7
    RULE_conditional = 8
    RULE_equalsCondition = 9
    RULE_greaterCondition = 10
    RULE_lessCondition = 11
    RULE_notEqualsCondition = 12
    RULE_memoryInstruction = 13
    RULE_jumpInstruction = 14
    RULE_saveInstruction = 15
    RULE_swapInstruction = 16
    RULE_noOperation = 17
    RULE_operand = 18
    RULE_accumulatorOperand = 19
    RULE_inOperand = 20
    RULE_outOperand = 21
    RULE_dataOperand = 22
    RULE_nilOperand = 23

    ruleNames =  [ "program", "line", "breakpoint", "label", "instruction", 
                   "addInstruction", "subInstruction", "moveInstruction", 
                   "conditional", "equalsCondition", "greaterCondition", 
                   "lessCondition", "notEqualsCondition", "memoryInstruction", 
                   "jumpInstruction", "saveInstruction", "swapInstruction", 
                   "noOperation", "operand", "accumulatorOperand", "inOperand", 
                   "outOperand", "dataOperand", "nilOperand" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    Constant=20
    Identifier=21
    Comment=22
    Whitespace=23
    Newline=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(tis100Parser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tis100Parser.LineContext)
            else:
                return self.getTypedRuleContext(tis100Parser.LineContext,i)


        def getRuleIndex(self):
            return tis100Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = tis100Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 19955642) != 0):
                self.state = 48
                self.line()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(tis100Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(tis100Parser.LabelContext,0)


        def instruction(self):
            return self.getTypedRuleContext(tis100Parser.InstructionContext,0)


        def Newline(self):
            return self.getToken(tis100Parser.Newline, 0)

        def breakpoint(self):
            return self.getTypedRuleContext(tis100Parser.BreakpointContext,0)


        def getRuleIndex(self):
            return tis100Parser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = tis100Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 56
                self.breakpoint()


            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21]:
                self.state = 59
                self.label()
                pass
            elif token in [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14]:
                self.state = 60
                self.instruction()
                pass
            elif token in [24]:
                self.state = 61
                self.match(tis100Parser.Newline)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakpointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_breakpoint

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakpoint" ):
                return visitor.visitBreakpoint(self)
            else:
                return visitor.visitChildren(self)




    def breakpoint(self):

        localctx = tis100Parser.BreakpointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_breakpoint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(tis100Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(tis100Parser.Identifier, 0)

        def Constant(self):
            return self.getToken(tis100Parser.Constant, 0)

        def instruction(self):
            return self.getTypedRuleContext(tis100Parser.InstructionContext,0)


        def getRuleIndex(self):
            return tis100Parser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = tis100Parser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_label)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 67
            self.match(tis100Parser.T__1)
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 68
                self.instruction()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addInstruction(self):
            return self.getTypedRuleContext(tis100Parser.AddInstructionContext,0)


        def subInstruction(self):
            return self.getTypedRuleContext(tis100Parser.SubInstructionContext,0)


        def moveInstruction(self):
            return self.getTypedRuleContext(tis100Parser.MoveInstructionContext,0)


        def conditional(self):
            return self.getTypedRuleContext(tis100Parser.ConditionalContext,0)


        def memoryInstruction(self):
            return self.getTypedRuleContext(tis100Parser.MemoryInstructionContext,0)


        def jumpInstruction(self):
            return self.getTypedRuleContext(tis100Parser.JumpInstructionContext,0)


        def noOperation(self):
            return self.getTypedRuleContext(tis100Parser.NoOperationContext,0)


        def getRuleIndex(self):
            return tis100Parser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = tis100Parser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruction)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.addInstruction()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.subInstruction()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.moveInstruction()
                pass
            elif token in [7, 8, 9, 10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.conditional()
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.memoryInstruction()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 76
                self.jumpInstruction()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 77
                self.noOperation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(tis100Parser.OperandContext,0)


        def getRuleIndex(self):
            return tis100Parser.RULE_addInstruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddInstruction" ):
                return visitor.visitAddInstruction(self)
            else:
                return visitor.visitChildren(self)




    def addInstruction(self):

        localctx = tis100Parser.AddInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_addInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(tis100Parser.T__2)
            self.state = 81
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(tis100Parser.OperandContext,0)


        def getRuleIndex(self):
            return tis100Parser.RULE_subInstruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubInstruction" ):
                return visitor.visitSubInstruction(self)
            else:
                return visitor.visitChildren(self)




    def subInstruction(self):

        localctx = tis100Parser.SubInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(tis100Parser.T__3)
            self.state = 84
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tis100Parser.OperandContext)
            else:
                return self.getTypedRuleContext(tis100Parser.OperandContext,i)


        def getRuleIndex(self):
            return tis100Parser.RULE_moveInstruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveInstruction" ):
                return visitor.visitMoveInstruction(self)
            else:
                return visitor.visitChildren(self)




    def moveInstruction(self):

        localctx = tis100Parser.MoveInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_moveInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(tis100Parser.T__4)
            self.state = 87
            self.operand()
            self.state = 88
            self.match(tis100Parser.T__5)
            self.state = 89
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalsCondition(self):
            return self.getTypedRuleContext(tis100Parser.EqualsConditionContext,0)


        def greaterCondition(self):
            return self.getTypedRuleContext(tis100Parser.GreaterConditionContext,0)


        def lessCondition(self):
            return self.getTypedRuleContext(tis100Parser.LessConditionContext,0)


        def notEqualsCondition(self):
            return self.getTypedRuleContext(tis100Parser.NotEqualsConditionContext,0)


        def getRuleIndex(self):
            return tis100Parser.RULE_conditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = tis100Parser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_conditional)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.equalsCondition()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.greaterCondition()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.lessCondition()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.notEqualsCondition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualsConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(tis100Parser.Identifier, 0)

        def Constant(self):
            return self.getToken(tis100Parser.Constant, 0)

        def getRuleIndex(self):
            return tis100Parser.RULE_equalsCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualsCondition" ):
                return visitor.visitEqualsCondition(self)
            else:
                return visitor.visitChildren(self)




    def equalsCondition(self):

        localctx = tis100Parser.EqualsConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_equalsCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(tis100Parser.T__6)
            self.state = 98
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GreaterConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(tis100Parser.Identifier, 0)

        def Constant(self):
            return self.getToken(tis100Parser.Constant, 0)

        def getRuleIndex(self):
            return tis100Parser.RULE_greaterCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterCondition" ):
                return visitor.visitGreaterCondition(self)
            else:
                return visitor.visitChildren(self)




    def greaterCondition(self):

        localctx = tis100Parser.GreaterConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_greaterCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(tis100Parser.T__7)
            self.state = 101
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LessConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(tis100Parser.Identifier, 0)

        def Constant(self):
            return self.getToken(tis100Parser.Constant, 0)

        def getRuleIndex(self):
            return tis100Parser.RULE_lessCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessCondition" ):
                return visitor.visitLessCondition(self)
            else:
                return visitor.visitChildren(self)




    def lessCondition(self):

        localctx = tis100Parser.LessConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_lessCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(tis100Parser.T__8)
            self.state = 104
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotEqualsConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(tis100Parser.Identifier, 0)

        def Constant(self):
            return self.getToken(tis100Parser.Constant, 0)

        def getRuleIndex(self):
            return tis100Parser.RULE_notEqualsCondition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqualsCondition" ):
                return visitor.visitNotEqualsCondition(self)
            else:
                return visitor.visitChildren(self)




    def notEqualsCondition(self):

        localctx = tis100Parser.NotEqualsConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_notEqualsCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(tis100Parser.T__9)
            self.state = 107
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemoryInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def saveInstruction(self):
            return self.getTypedRuleContext(tis100Parser.SaveInstructionContext,0)


        def swapInstruction(self):
            return self.getTypedRuleContext(tis100Parser.SwapInstructionContext,0)


        def getRuleIndex(self):
            return tis100Parser.RULE_memoryInstruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemoryInstruction" ):
                return visitor.visitMemoryInstruction(self)
            else:
                return visitor.visitChildren(self)




    def memoryInstruction(self):

        localctx = tis100Parser.MemoryInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_memoryInstruction)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.saveInstruction()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.swapInstruction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(tis100Parser.Identifier, 0)

        def Constant(self):
            return self.getToken(tis100Parser.Constant, 0)

        def getRuleIndex(self):
            return tis100Parser.RULE_jumpInstruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpInstruction" ):
                return visitor.visitJumpInstruction(self)
            else:
                return visitor.visitChildren(self)




    def jumpInstruction(self):

        localctx = tis100Parser.JumpInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_jumpInstruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(tis100Parser.T__10)
            self.state = 114
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaveInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_saveInstruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaveInstruction" ):
                return visitor.visitSaveInstruction(self)
            else:
                return visitor.visitChildren(self)




    def saveInstruction(self):

        localctx = tis100Parser.SaveInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_saveInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(tis100Parser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwapInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_swapInstruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwapInstruction" ):
                return visitor.visitSwapInstruction(self)
            else:
                return visitor.visitChildren(self)




    def swapInstruction(self):

        localctx = tis100Parser.SwapInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_swapInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(tis100Parser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_noOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoOperation" ):
                return visitor.visitNoOperation(self)
            else:
                return visitor.visitChildren(self)




    def noOperation(self):

        localctx = tis100Parser.NoOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_noOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(tis100Parser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accumulatorOperand(self):
            return self.getTypedRuleContext(tis100Parser.AccumulatorOperandContext,0)


        def inOperand(self):
            return self.getTypedRuleContext(tis100Parser.InOperandContext,0)


        def outOperand(self):
            return self.getTypedRuleContext(tis100Parser.OutOperandContext,0)


        def dataOperand(self):
            return self.getTypedRuleContext(tis100Parser.DataOperandContext,0)


        def nilOperand(self):
            return self.getTypedRuleContext(tis100Parser.NilOperandContext,0)


        def Constant(self):
            return self.getToken(tis100Parser.Constant, 0)

        def getRuleIndex(self):
            return tis100Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = tis100Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_operand)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.accumulatorOperand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.inOperand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.outOperand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.dataOperand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 127
                self.nilOperand()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 128
                self.match(tis100Parser.Constant)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccumulatorOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_accumulatorOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccumulatorOperand" ):
                return visitor.visitAccumulatorOperand(self)
            else:
                return visitor.visitChildren(self)




    def accumulatorOperand(self):

        localctx = tis100Parser.AccumulatorOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_accumulatorOperand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(tis100Parser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_inOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInOperand" ):
                return visitor.visitInOperand(self)
            else:
                return visitor.visitChildren(self)




    def inOperand(self):

        localctx = tis100Parser.InOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_inOperand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(tis100Parser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_outOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutOperand" ):
                return visitor.visitOutOperand(self)
            else:
                return visitor.visitChildren(self)




    def outOperand(self):

        localctx = tis100Parser.OutOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_outOperand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(tis100Parser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_dataOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataOperand" ):
                return visitor.visitDataOperand(self)
            else:
                return visitor.visitChildren(self)




    def dataOperand(self):

        localctx = tis100Parser.DataOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_dataOperand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(tis100Parser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NilOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_nilOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNilOperand" ):
                return visitor.visitNilOperand(self)
            else:
                return visitor.visitChildren(self)




    def nilOperand(self):

        localctx = tis100Parser.NilOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_nilOperand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(tis100Parser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





