"""
      0 1 2 3 4 5 6  7  8  9
fibb: 1 1 2 3 5 8 13 21 34 55 ...
          a b
function x 7 ==> 13
           9 ==> 34
1 1 2
  a b c

a = 1
b = 1
c = a + b == 2

 a = b
 b = c

 start with a = 1 , b = 1
 calc c = a + b
 put a = b, b = c
"""
from typing import final


#       a b c
#       0 1 2 3 4 5 6  7  8  9
# fibb: 1 1 2 3 5 8 13 21 34 55 ...
def get_fibb(index: int) -> int:
    a: int = 1  # index 1
    b: int = 1  # index 2
    c: int = 1  # 1, 2
    for _ in range(index - 1):
        c = a + b
        a = b
        b = c
    return c

print(get_fibb(9))




