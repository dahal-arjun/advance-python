"""

Breakpoint drops you into the debugger at the call site. Specifically, it calls
sys.breakpointhook(), passing args and kws straight through. By deault,
sys.breakpointhook() calls pdb.set_trace() expecting no arguments. In this case
it is purely an convenince function so you don't have to expectily import pdb
or type as much as code to enter the debugger.
However, sys.breakpointhook() can be set to soe other function and breakpoint()
will automatically call that, allowing you to drop into the debugger of choice.
if sys.breakpointhook() is not accessible, this function will rise RuntimeError

By default, the behavior of the breakpoint() can be changed with the
PYTHONBREAKPOINT env variable.
"""
import pdb


def debugger(a, b):
    pdb.set_trace()
    result = a / b
    return result


print(debugger(2, 5))
