# In[]
# 'Knuth-Morris-Pratt'
my_string = input()

# ['Knuth', 'Morris', 'Pratt']
my_string_split = my_string.split('-')

# ['K', 'M', 'P']
my_string_in_list = [x[0] for x in my_string_split]

# 'KMP'
expected = "".join(my_string_in_list)

print(expected)