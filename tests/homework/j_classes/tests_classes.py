import unittest
from src.homework.j_classes.class_a import Die

class Test_Die(unittest.TestCase):

    def test_class_die_and_internals(self):
        die = Die()
        die.roll()#
        roll_out = die.get_roll()
        self.assertIn(roll_out, [1, 2, 3, 4, 5, 6], "The roll's output is in between 1 and 6.")

    def test_class_die_and_internals(self):
        die = Die()
        die.roll()#
        roll_out = die.get_roll()
        self.assertIn(roll_out, [1, 2, 3, 4, 5, 6], "The roll's output is in between 1 and 6.")

    def test_class_die_and_internals(self):
        die = Die()
        die.roll()#
        roll_out = die.get_roll()
        self.assertIn(roll_out, [1, 2, 3, 4, 5, 6], "The roll's output is in between 1 and 6.")
