from addition import add_two_number

def test_add():
  assert add_two_number(1, 2) == 3
  assert add_two_number(1, -1) == 0
