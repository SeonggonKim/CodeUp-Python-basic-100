﻿num = int(input())
a = input().split()

for i in range(num):
  a[i] = int(a[i])

a = a[::-1]

for i in range(num):
  print(a[i], end = ' ')
