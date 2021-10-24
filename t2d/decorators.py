from functools import partial
from io import StringIO
import sys


def collect_stdout_and_stderr(func, *args, **kwargs):
    """
    A decorator that collects the output of the decorated function and returns it.
    """
    def run_func(*args, **kwargs):
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        func(*args, **kwargs)
        stdout = sys.stdout.getvalue()
        stderr = sys.stderr.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        return stdout, stderr
    return partial(run_func, *args, **kwargs)


def forbid_exit(func, *args, **kwargs):
    """
    A decorator that prevents the decorated function from exiting the program.
    """
    def run_func(*args, **kwargs):
        old_exit = sys.exit
        sys.exit = lambda code: None
        res = func(*args, **kwargs)
        sys.exit = old_exit
        return res
    return partial(run_func, *args, **kwargs)
