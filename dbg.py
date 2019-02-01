import sys
import inspect

__all__ = ['dbg']


def dbg(*args, file=sys.stdout):
    curframe = inspect.currentframe()
    callframe = curframe.f_back
    callframe_info = inspect.getframeinfo(callframe)

    if callframe_info.code_context is not None:
        code_context = callframe_info.code_context[0]
        code_context = code_context[code_context.find('dbg('):]
        arg_names = code_context[4:-2].split(',')
    else:
        breakpoint()
        arg_names = ('<arg>', )

    info_str = ', '.join(f'{arg_name.strip()} = {arg!r}' for arg_name, arg in zip(arg_names, args))
    print(f'[{callframe_info.filename}:{callframe_info.lineno}] {info_str}', file=file)
