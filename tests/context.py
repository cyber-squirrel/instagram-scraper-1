# -*- coding: utf-8 -*-
import os
import sys

from igramscraper.instagram import Instagram  # noqa: F401
from igramscraper.model import media as Media  # noqa: F401

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

"""
Context Processor:
This is the context processor you can use this to import the Instagram module simply
add `from context import Instagram` if context.py is saved into root or add
`from <file location>.context import Instagram` if saved elsewhere.

"""
