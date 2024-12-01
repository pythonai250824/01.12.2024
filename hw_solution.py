# set list tuple dict None
# ( { )
# { [ ]
# }

# 1. string finished without closing everything
# 2. wrongly closing bracket
#    a. no similar opening bracket before at all
#    b. different opening bracket before

"""
  {
  for each character:
    reached end and there are open brackets in list -> False
      if bracket is opening
        add bracket to a list
        continue to next character
      if bracket is closing-
         check if last bracket are matched {} [] (),
           if no -> False
           if yes -> remove brackets from list
  if reached end with no open brackets -> True, otherwise -> False
"""

def check_brackets(word: str) -> bool:
    # {([  ]
    # { ( [
    # list :
    open_bracket_list : list[str] = []
    for c in word:
        if c in ["{", "[", "("]:
            open_bracket_list.append(c)
            continue
        if c in ["}", "]", ")"]:  # { [ ( ]
            if len(open_bracket_list) == 0:
                return False
            last = open_bracket_list[-1]
            if c == "}" and last == "{" or c == "]" and last == "["\
                or c == ")" and last == "(":
                open_bracket_list.pop()
            else:
                return False

    if len(open_bracket_list) == 0:
        return True
    else:
        return False

print(check_brackets("{{[[]]}}"))

"""
  1 1 1 2 2 3 3 3 4 5 6 7 7
  1 1 2 2 3 3 3 4 5 6 7 7
 #0 1 2 3 4 5 6 7 8 9  
  index = 1
  
  run on the list each item you encounter, 
    if its similar to the previous one -> remove it
    
  set index = 1
  while index < length of list:
     if list [index] == list[index-1]:
       remove item at index
    else:
      index += 1
"""

def remove_dup(numbers: list[int]) -> None:
    index = 1
    while index < len(numbers):
        if numbers[index] == numbers[index - 1]:
            numbers.pop(index)
        else:
            index += 1

numbers: list[int] = [1, 1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 7, 8]
remove_dup(numbers)
print(numbers)

"""
  |
  2 3 5 6 
  
  |
  3 4 9 9 9
  
  1 1 1 1 2 
  
  run until finished both list
    each time append the smaller item
    
  result: list[int] = []
  while True:
    if len(list1) == 0:
       result.extend(list2)
       return result
    if len(list2) == 0:
       result.extend(list1)
       return result       
    if list1[0] < list2[0]:
        result.append(list1[0])
        list1.pop(0)
    else:
        result.append(list2[0])
        list2.pop(0)   
"""
def merge(list1: list[int], list2: list[int]) -> list[int]:
    result: list[int] = []
    while True:
        if len(list1) == 0:
            result.extend(list2)
            return result

        if len(list2) == 0:
            result.extend(list1)
            return result

        if list1[0] < list2[0]:
            result.append(list1[0])
            list1.pop(0)
        else:
            result.append(list2[0])
            list2.pop(0)




