# this is a basic python file
def add_two_number(a:int, b:int):
  return a+b

def test_add():
  assert add_two_number(1, 2) == 3
  assert add_two_number(1, -1) == 0
