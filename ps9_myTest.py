__author__ = 'John'

import unittest
import ps9

class TestPs9(unittest.TestCase):

    def test_bruteforce(self):
        # Given these inputs
        maxHours =10
        testSubjects = {'1.00':(10, 5), '2.00': (9, 5), '3.00': (8, 4), '4.00': (3, 4), '5.00': (1, 1)}

        # when i call this method

        dictionary = ps9.bruteForceAdvisor(testSubjects, maxHours)

        # Then i expect

        self.assertTrue(dictionary == {'1.00':(10,5), '3.00':(8,4), '5.00':(1,1)})

if __name__ == '__main__':
    unittest.main()