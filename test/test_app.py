# -*- coding: utf-8 -*-
"""
Tests for the functionality of the application object.
"""

import unittest
from nanoasgi import App

class TestApplicationObject(unittest.TestCase):
    
    def test_setattr(self):
        app = App()
        assert app
