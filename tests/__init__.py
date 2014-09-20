import unittest

class InitializationTests(unittest.TestCase):

    def test_sanity(self):
        """
        Check that the world is sane and 2+2=4
        """
        self.assertEquals(2 + 2, 4)

    def test_import(self):
        """
        We're able to import the gtcal module
        """
        try:
            import gtcal
        except ImportError:
            self.fail("Could not import gtcal")