#-----------------------------------------------------------------
# pycparser: __init__.py
#
# This package file exports some convenience functions for
# interacting with pycparser
#
# Eli Bendersky [https://eli.thegreenplace.net/]
# License: BSD
#-----------------------------------------------------------------
__all__ = ['c_parser', 'c_ast']
__version__ = '2.19'

from typing import Any
from . import c_ast

def preprocess_file(filename: str, cpp_path: str='cpp', cpp_args: str='') -> str: ...
def parse_file(filename: str, use_cpp: bool=False, cpp_path: str='cpp', cpp_args: str='', parser: Any=None) -> c_ast.FileAST: ...
