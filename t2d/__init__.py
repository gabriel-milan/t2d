try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

from t2d.bot import T2D

__version__ = importlib_metadata.version(__name__)

__all__ = [
    '__version__',
    "T2D",
]
