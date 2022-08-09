import pytest

from main import add_string

def test_add_string():
   x = "Hellow"
   y = "Weekend"

   assert add_string(x, y) == "HellowWeekend"
