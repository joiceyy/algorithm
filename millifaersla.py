# In[]
 
a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
  print('Monnei')
elif b < a and b < c:
  print('Fjee')
else:
  print('Dolladollabilljoll')

# In[]

a = int(input())
b = int(input())
c = int(input())

thisdict = {
 a: 'Monnei',
  b: 'Fjee',
  c: 'Dolladollabilljoll'
}
min_value = min(a,b,c)
print(thisdict[min_value])
# In[]
a = int(input())
b = int(input())
c = int(input())
d = int(input())

dict = {
 a: 'jeje',
  b: 'rara',
  c: 'seta',
  d: 'yusuf'
}



dict[a] += 1
dict[b] += 1
dict[c] += 1

for key, value in dict.items():
  if value > 1:
    print(key)


