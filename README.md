# Stack Interpreter
This is a simple and probably useless interpreted language created for fun. So far an interpreter in python has been created. The language has error handling built in just to make it slighter easier to code with (due to its limited dictionary).

# Specification
The language has a stack and 6 instructions:

`push <num>` # push a number on to the stack

`pop` # pop off the first number on the stack

`add` # pop off the top 2 items on the stack and push their sum on to the stack. (remember you can add negative numbers, so you have subtraction covered too). You can also get multiplication my creating a loop using some of the other instructions with this one.

`ifeq` <address> # examine the top of the stack, if it's 0, continue, else, jump to <address> where <address> is a line number

`jump` <address> # jump to a line number

`print` # print the value at the top of the stack

`dup` # push a copy of what's at the top of the stack back onto the stack.

`#` # any line starting with it is a comment

Run
Works with Python 3.9, run `stackinterpreter.py` and you should see hello, world!
