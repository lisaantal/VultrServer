# test_vultrserver.py
"""
Tests for VultrServer module.
"""

import unittest
from vultrserver import VultrServer

class TestVultrServer(unittest.TestCase):
    """Test cases for VultrServer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VultrServer()
        self.assertIsInstance(instance, VultrServer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VultrServer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
