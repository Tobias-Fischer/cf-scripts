from xonsh.execer import Execer
from xonsh.environ import Env
from xonsh.__amalgam__ import CommandPipeline
import builtins

env: Env = builtins.__xonsh__.env
execer: Execer = builtins.__xonsh__.execer


def eval_xonsh(inp: str) -> str:
    import inspect

    frame = inspect.stack()[1][0]
    glbs = frame.f_globals
    locs = frame.f_locals

    res = execer.eval(f"!({inp})", glbs=glbs, locs=locs)
    if isinstance(res, CommandPipeline):
        return res.output.strip()
    else:
        return res
