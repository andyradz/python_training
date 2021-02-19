import unittest

fun = lambda x:  x + 1

ope = lambda s : s + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
        ope(1)
        