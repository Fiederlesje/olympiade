import random as r

K = r.randint(0,256)
WR = ['N', 'O','Z','W']
opg = ''

for i in range(K):
  random_wr = r.choice(WR)
  opg = opg + str(random_wr)

o = opg.count('O')
n = opg.count('N')
z = opg.count('Z')
w = opg.count('W')

ver = abs(n - z)
hor = abs(o - w)

min_aant_stap = ver + hor

print('K = ', K)
print('Opdrachten = ', opg)
print('minimaal aantal stappen =', min_aant_stap)