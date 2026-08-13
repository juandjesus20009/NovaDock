# test_novadock.py
"""
Tests for NovaDock module.
"""

import unittest
from novadock import NovaDock

class TestNovaDock(unittest.TestCase):
    """Test cases for NovaDock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaDock()
        self.assertIsInstance(instance, NovaDock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaDock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
