
'''
get a list of words
create a dict
iterate over all of the words:
  each word check if exist in the dict
  "danny", "apple", "danny"
    if not -> store in the dict {key-word: value-counter}
              counter = 1
    if word already exist in the dict then + 1 its counter
   final result:  { "danny": 2, "apple": 1}
    { "danny": 2, "apple": 1 }
    -- [("apple", 1), ("danny", 2)]
    result = []
    for key, value in dict_counter.items():
      if value > 1:
        result.append(key)
'''
