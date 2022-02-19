N = int(input())
P = []

for i in range(N):
  P.append(int(input()))
  
P.sort(reverse=True)

charge = 0

for i in range(0, N, 4):
  charge += P[i]

  if i+1 < N:
    charge += P[i+1]
  
print(charge)
