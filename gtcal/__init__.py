import unittest

class InitializationTests(unittest.TestCase):

    def test_sanity(self):
        """
        Check that the world is sane and 2+2=4
        """
        self.assertEquals(2 + 2, 4)