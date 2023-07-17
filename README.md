# TIS-100-Compiler

## Introduction
This is a small personal project that implements a modified version of the assembly language from the Zachtronics game [TIS-100](http://www.zachtronics.com/tis-100/). Currently, the project only simulates a single Basic Instruction Node, which can print values to the console using the OUT port. TIS-100 instructions are translated to Aarch64 instructions, which can be run natively on Apple Silicon architectures using GCC.

## Example
The following program prints the numbers 10 to 1 to the console, then terminates.

``````
MOV 10, ACC
START:
 JEZ TERM
 MOV ACC, OUT
 SUB 1
 JMP START
TERM:
``````

