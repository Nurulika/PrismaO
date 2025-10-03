# test_prismaorm.py
"""
Tests for PrismaORM module.
"""

import unittest
from prismaorm import PrismaORM

class TestPrismaORM(unittest.TestCase):
    """Test cases for PrismaORM class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrismaORM()
        self.assertIsInstance(instance, PrismaORM)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrismaORM()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
