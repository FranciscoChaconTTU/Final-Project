
def Backsub(R,b):
  c=[0] * len(b)
  for i in reversed(range(len(b)):
    c[i]=b[i]
    for j in range(len(i+1,len(b))):
     c[i]=c[i]-c[j]R[i][i]
     c[i]=c[i]/R[i][i]
    return c
def LS(A):
 #These are variables that we assign in our fuction
  n = len(A)
  m = len(A[0])
  V = [A[i]**(n-1) for i in range(n)]
  #These are blank matrices with the correct dimensions
  R = [[0]*n for i in range(n)]
  Q = [[0]*m for i in range(n)]
  Y = [[0]*n for i in range(n)]
  for i in range(n):
     Q_R = GS(A)
     return Q
     Q[j][i]*Y











A = [[0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.95,1.00],[1.102,1.099,1.017,1.111,1.117,1.152,1.265,1.380,1.575,1.857]]
