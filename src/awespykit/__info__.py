# coding: utf-8

try:
    import importlib.metadata as metadata
except ImportError:
    import importlib_metadata as metadata

APP_NAME = "Awespykit"
FIXED_VER = "2.0.1"
try:
    VERSION = metadata.version(APP_NAME)
except:
    VERSION = FIXED_VER
AUTHOR = "hrp/hrpzcf"

__all__ = ["APP_NAME", "AUTHOR", "FIXED_VER", "VERSION"]
