try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

from t2d.decorators import (
    forbid_exit,
    collect_stdout_and_stderr,
)


@forbid_exit
@collect_stdout_and_stderr
def run_app_command(app, *args, **kwargs):
    app(*args, **kwargs)


def get_version():
    return importlib_metadata.version('t2d')
