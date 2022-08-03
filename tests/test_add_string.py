import unittest

from main import add_string

class AdditionTest(unittest.TestCase):
  def test_add(self):
    x = "Hello"
    y = "Weekend"
    result = add_string(x, y)
    self.assertEqual(result, "HelloWeekend")

  if __name__ == '__main__':
    unittest.main()
