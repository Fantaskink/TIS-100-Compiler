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
        4,1,24,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,0,1,0,1,1,3,1,46,8,1,1,1,1,1,1,1,3,1,51,8,1,1,2,1,2,1,3,
        1,3,1,3,3,3,58,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,67,8,4,1,5,1,
        5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,83,8,8,1,9,
        1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,3,12,96,8,12,1,13,
        1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,0,0,18,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,2,1,0,20,21,1,0,
        14,20,104,0,39,1,0,0,0,2,45,1,0,0,0,4,52,1,0,0,0,6,54,1,0,0,0,8,
        66,1,0,0,0,10,68,1,0,0,0,12,71,1,0,0,0,14,74,1,0,0,0,16,82,1,0,0,
        0,18,84,1,0,0,0,20,87,1,0,0,0,22,90,1,0,0,0,24,95,1,0,0,0,26,97,
        1,0,0,0,28,100,1,0,0,0,30,102,1,0,0,0,32,104,1,0,0,0,34,106,1,0,
        0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,
        1,0,0,0,40,42,1,0,0,0,41,39,1,0,0,0,42,43,5,0,0,1,43,1,1,0,0,0,44,
        46,3,4,2,0,45,44,1,0,0,0,45,46,1,0,0,0,46,50,1,0,0,0,47,51,3,6,3,
        0,48,51,3,8,4,0,49,51,5,24,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,
        1,0,0,0,51,3,1,0,0,0,52,53,5,1,0,0,53,5,1,0,0,0,54,55,7,0,0,0,55,
        57,5,2,0,0,56,58,3,8,4,0,57,56,1,0,0,0,57,58,1,0,0,0,58,7,1,0,0,
        0,59,67,3,10,5,0,60,67,3,12,6,0,61,67,3,14,7,0,62,67,3,16,8,0,63,
        67,3,24,12,0,64,67,3,26,13,0,65,67,3,32,16,0,66,59,1,0,0,0,66,60,
        1,0,0,0,66,61,1,0,0,0,66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,
        66,65,1,0,0,0,67,9,1,0,0,0,68,69,5,3,0,0,69,70,3,34,17,0,70,11,1,
        0,0,0,71,72,5,4,0,0,72,73,3,34,17,0,73,13,1,0,0,0,74,75,5,5,0,0,
        75,76,3,34,17,0,76,77,5,6,0,0,77,78,3,34,17,0,78,15,1,0,0,0,79,83,
        3,18,9,0,80,83,3,20,10,0,81,83,3,22,11,0,82,79,1,0,0,0,82,80,1,0,
        0,0,82,81,1,0,0,0,83,17,1,0,0,0,84,85,5,7,0,0,85,86,7,0,0,0,86,19,
        1,0,0,0,87,88,5,8,0,0,88,89,7,0,0,0,89,21,1,0,0,0,90,91,5,9,0,0,
        91,92,7,0,0,0,92,23,1,0,0,0,93,96,3,28,14,0,94,96,3,30,15,0,95,93,
        1,0,0,0,95,94,1,0,0,0,96,25,1,0,0,0,97,98,5,10,0,0,98,99,7,0,0,0,
        99,27,1,0,0,0,100,101,5,11,0,0,101,29,1,0,0,0,102,103,5,12,0,0,103,
        31,1,0,0,0,104,105,5,13,0,0,105,33,1,0,0,0,106,107,7,1,0,0,107,35,
        1,0,0,0,7,39,45,50,57,66,82,95
    ]

class tis100Parser ( Parser ):

    grammarFileName = "tis100.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "':'", "'ADD'", "'SUB'", "'MOV'", 
                     "','", "'JEZ'", "'JGZ'", "'JLZ'", "'JMP'", "'SAV'", 
                     "'SWP'", "'NOP'", "'ACC'", "'UP'", "'LEFT'", "'DOWN'", 
                     "'RIGHT'", "'DAT'" ]

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
    RULE_memoryInstruction = 12
    RULE_jumpInstruction = 13
    RULE_saveInstruction = 14
    RULE_swapInstruction = 15
    RULE_noOperation = 16
    RULE_operand = 17

    ruleNames =  [ "program", "line", "breakpoint", "label", "instruction", 
                   "addInstruction", "subInstruction", "moveInstruction", 
                   "conditional", "equalsCondition", "greaterCondition", 
                   "lessCondition", "memoryInstruction", "jumpInstruction", 
                   "saveInstruction", "swapInstruction", "noOperation", 
                   "operand" ]

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

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
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 19939258) != 0):
                self.state = 36
                self.line()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

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
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 44
                self.breakpoint()


            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21]:
                self.state = 47
                self.label()
                pass
            elif token in [3, 4, 5, 7, 8, 9, 10, 11, 12, 13]:
                self.state = 48
                self.instruction()
                pass
            elif token in [24]:
                self.state = 49
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakpoint" ):
                listener.enterBreakpoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakpoint" ):
                listener.exitBreakpoint(self)

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
            self.state = 52
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

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
            self.state = 54
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(tis100Parser.T__1)
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 56
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = tis100Parser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_instruction)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.addInstruction()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.subInstruction()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.moveInstruction()
                pass
            elif token in [7, 8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.conditional()
                pass
            elif token in [11, 12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.memoryInstruction()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 6)
                self.state = 64
                self.jumpInstruction()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 65
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddInstruction" ):
                listener.enterAddInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddInstruction" ):
                listener.exitAddInstruction(self)

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
            self.state = 68
            self.match(tis100Parser.T__2)
            self.state = 69
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubInstruction" ):
                listener.enterSubInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubInstruction" ):
                listener.exitSubInstruction(self)

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
            self.state = 71
            self.match(tis100Parser.T__3)
            self.state = 72
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveInstruction" ):
                listener.enterMoveInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveInstruction" ):
                listener.exitMoveInstruction(self)

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
            self.state = 74
            self.match(tis100Parser.T__4)
            self.state = 75
            self.operand()
            self.state = 76
            self.match(tis100Parser.T__5)
            self.state = 77
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


        def getRuleIndex(self):
            return tis100Parser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = tis100Parser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_conditional)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.equalsCondition()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.greaterCondition()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.lessCondition()
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualsCondition" ):
                listener.enterEqualsCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualsCondition" ):
                listener.exitEqualsCondition(self)

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
            self.state = 84
            self.match(tis100Parser.T__6)
            self.state = 85
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterCondition" ):
                listener.enterGreaterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterCondition" ):
                listener.exitGreaterCondition(self)

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
            self.state = 87
            self.match(tis100Parser.T__7)
            self.state = 88
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessCondition" ):
                listener.enterLessCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessCondition" ):
                listener.exitLessCondition(self)

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
            self.state = 90
            self.match(tis100Parser.T__8)
            self.state = 91
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemoryInstruction" ):
                listener.enterMemoryInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemoryInstruction" ):
                listener.exitMemoryInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemoryInstruction" ):
                return visitor.visitMemoryInstruction(self)
            else:
                return visitor.visitChildren(self)




    def memoryInstruction(self):

        localctx = tis100Parser.MemoryInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_memoryInstruction)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.saveInstruction()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpInstruction" ):
                listener.enterJumpInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpInstruction" ):
                listener.exitJumpInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpInstruction" ):
                return visitor.visitJumpInstruction(self)
            else:
                return visitor.visitChildren(self)




    def jumpInstruction(self):

        localctx = tis100Parser.JumpInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_jumpInstruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(tis100Parser.T__9)
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


    class SaveInstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tis100Parser.RULE_saveInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaveInstruction" ):
                listener.enterSaveInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaveInstruction" ):
                listener.exitSaveInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSaveInstruction" ):
                return visitor.visitSaveInstruction(self)
            else:
                return visitor.visitChildren(self)




    def saveInstruction(self):

        localctx = tis100Parser.SaveInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_saveInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(tis100Parser.T__10)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwapInstruction" ):
                listener.enterSwapInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwapInstruction" ):
                listener.exitSwapInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwapInstruction" ):
                return visitor.visitSwapInstruction(self)
            else:
                return visitor.visitChildren(self)




    def swapInstruction(self):

        localctx = tis100Parser.SwapInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_swapInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(tis100Parser.T__11)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoOperation" ):
                listener.enterNoOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoOperation" ):
                listener.exitNoOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoOperation" ):
                return visitor.visitNoOperation(self)
            else:
                return visitor.visitChildren(self)




    def noOperation(self):

        localctx = tis100Parser.NoOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_noOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(tis100Parser.T__12)
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

        def Constant(self):
            return self.getToken(tis100Parser.Constant, 0)

        def getRuleIndex(self):
            return tis100Parser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = tis100Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2080768) != 0)):
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





