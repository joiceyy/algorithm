# In[]
n = int(input())
total = 0.0
for i in range(0, n):
  raw_input = input()
  raw_input_split = raw_input.split()

  lsFloat = [float(x) for x in raw_input_split]
  q, y = lsFloat
  total = total + q*y

print(total)

