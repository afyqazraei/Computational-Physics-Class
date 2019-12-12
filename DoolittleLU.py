import numpy

def inputA(n):

  A = []

  for i in range(n):
    innerA = []
    for j in range(n):
      print("Member A[", i, "][", j, "]")
      ia = float(input("Insert value:"))
      innerA.append(ia)
    A.append(innerA)

  return A

def inputB(n):

  B = []

  for i in range(n):
    print("Member B[", i, "]")
    ib = float(input("Insert value:"))
    B.append(ib)

  return B

def Check2D(A,B):

  nB  = len(B)
  nA1 = len(A)

  if nB != nA1:
    print("Runtime Error: Dimensions of A & B don't match.")
    return False    
  else:
    for iA in A:
      nA2 = len(iA)
      if nA2 != nB:
        print("Runtime Error: Dimensions of A & B don't match.")
        return False
      else:
        pass

    return True

def DoolittleSumU(A, matU, matL, k, m):

  if k-1 < 0:
    return 0
  else:
    u = 0
    for j in range(k):
        u += matL[k][j]*matU[j][m]
    return u

def DoolittleSumL(A, matU, matL, i, k):

  if k-1 < 0:
    return 0
  else:
    l = 0
    for j in range(k):
        l += matL[i][j]*matU[j][k]
    return l

def DoolittleSolveL(L, i, y):
  if i == 0:
    return 0
  else:
    l = 0
    for j in range(i):
      l += L[j]*y[j]
    return l

def DoolittleSolveU(U, i, x):

  n = len(x)

  if i == 0:
    return 0
  else:
    u = 0
    for j in range(i):
      u += U[n-1-j]*x[n-1-j]
    return u

def CheckFinal(A, X, B):

  n = len(B)
  C = []

  for i in range(n):
    c = 0
    for j in range(n):
      c += A[i][j]*X[j]
    C.append(c)

  for i in range(n):
    if B[i] == C[i]:
      pass
    else:
      return False
    return True

def DoolittleSolve(A, B):

  n = len(B)

  matL = [[0 for x in range(n)] for y in range(n)]
  matU = [[0 for x in range(n)] for y in range(n)]


  for k in range(n):  
    for m in range(k, n):
      if k <= m:
        matU[k][m] = A[k][m] - DoolittleSumU(A, matU, matL, k, m)
      else:
        matU[k][m] = 0
    for i in range(k, n):
      if i == k:
        matL[i][k] = 1
      elif i > k:
        matL[i][k] = (A[i][k] - DoolittleSumL(A, matU, matL, i, k))/matU[k][k]
      else:
        matL[i][k] = 0

  y = [0 for y in range(n)]
  x = [0 for x in range(n)]

  for iy in range(n):
    y[iy] = (B[iy] - DoolittleSolveL(matL[iy], iy, y))

  for ix in range(n):
    x[n-1-ix] = (y[n-1-ix] - DoolittleSolveU(matU[n-1-ix], ix, x))/matU[n-1-ix][n-1-ix]

  if CheckFinal(A, x, B):
    print("Solution for X: ", x)
  else:
    print("Error. Solution was wrong.")

n  = int(input("No. of collumns/rows: "))
A  = inputA(n)
B  = inputB(n)
LU = DoolittleSolve(A, B)
