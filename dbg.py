import sys
import inspect

__all__ = ['dbg']


def dbg(x, file=sys.stdout):
    curframe = inspect.currentframe()
    callframe = curframe.f_back
    callframe_info = inspect.getframeinfo(callframe)

    if callframe_info.code_context is not None:
        code_context = callframe_info.code_context[0]
        code_context = code_context[code_context.find('dbg('):]
        arg_name = code_context[4:-2]
    else:
        breakpoint()
        arg_name = '<arg>'

    print(f'[{callframe_info.filename}:{callframe_info.lineno}] {arg_name} = {x!r}', file=file)
