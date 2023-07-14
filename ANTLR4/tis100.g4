grammar tis100;

    program
        :   line* EOF
        ;

    line
        :   breakpoint? (label | instruction | Newline)
        ;

    breakpoint
        :   '!'
        ;

    label
        :  (Identifier | Constant) ':' instruction?
        ;

    instruction
        :   addInstruction
        |   subInstruction
        |   moveInstruction
        |   conditional
        |   memoryInstruction
        |   jumpInstruction
        |   noOperation
        ;

    addInstruction
        :   'ADD' operand
        ;

    subInstruction
        :   'SUB' operand
        ;

    moveInstruction
        :   'MOV' operand ',' operand
        ;

    conditional
        :   equalsCondition
        |   greaterCondition
        |   lessCondition
        |   notEqualsCondition
        ;

    equalsCondition
        :   'JEZ' (Identifier | Constant )
        ;

    greaterCondition
        :   'JGZ' (Identifier | Constant )
        ;

    lessCondition
        :   'JLZ' (Identifier | Constant )
        ;

    notEqualsCondition
        :   'JNZ' (Identifier | Constant )
        ;

    memoryInstruction
        :   saveInstruction
        |   swapInstruction
        ;

    jumpInstruction
        :   'JMP' (Identifier | Constant )
        ;

    saveInstruction
        :   'SAV'
        ;

    swapInstruction
        :   'SWP'
        ;

    noOperation
        :   'NOP'
        ;

    operand
        :   accumulatorOperand | inOperand | outOperand | dataOperand | Constant
        ;

    accumulatorOperand
        :   'ACC'
        ;

    inOperand
        :   'IN'
        ;

    outOperand
        :   'OUT'
        ;

    dataOperand
        :   'DAT'
        ;

    Constant
        :   ('-')? Digit+
        ;

    Identifier
        :   (IdentifierNondigit | Digit )+
        ;

    fragment
    IdentifierNondigit
        :   Nondigit
        ;

    fragment
    Nondigit
        :   [a-zA-Z]
        ;

    fragment
    Digit
        :   [0-9]
        ;

    Comment
        :   '#' ~[\r\n]*
            -> skip
        ;

    Whitespace
        :   [ \t]+
            -> skip
        ;

    Newline
        :   (   '\r' '\n'?
            |   '\n'
            )
        ;