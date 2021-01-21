#!/usr/bin/env python3

from time import localtime, strftime, sleep

c = '●\u001b[0m'
print('\n' * 5)

while True:
  matrix = [
    ['',''],
    ['','','',''],
    ['','',''],
    ['','','',''],
    ['','',''],
    ['','','','']
  ]
  timenow = strftime('%H%M%S', localtime())
  # timenow = "000000" # For testing

  for i in range(len(timenow)):
    tbin = bin(int(timenow[i])).split('0b')[1]
    for j in range(len(tbin)):
      if tbin[j] == '1':
        matrix[i][len(tbin) - j - 1] = '\u001b[31m'

  print(timenow[0:2] + ':' + timenow[2:4] + ':' + timenow[4:6], '\n\033[2A', end='')
  print('\033[1A' + '\b' * 10 + f'{matrix[0][0]}{c} {matrix[1][0]}{c}  {matrix[2][0]}{c} {matrix[3][0]}{c}  {matrix[4][0]}{c} {matrix[5][0]}{c}', end='')
  print('\n')
  print('\033[3A' + '\b' * 10 + f'{matrix[0][1]}{c} {matrix[1][1]}{c}  {matrix[2][1]}{c} {matrix[3][1]}{c}  {matrix[4][1]}{c} {matrix[5][1]}{c}', end='')
  print('\n' * 2)
  print('\033[4A' + '\b' * 10 + f'  {matrix[1][2]}{c}  {matrix[2][2]}{c} {matrix[3][2]}{c}  {matrix[4][2]}{c} {matrix[5][2]}{c}', end='')
  print('\n' * 3)
  print('\033[5A' + '\b' * 10 + f'  {matrix[1][3]}{c}    {matrix[3][3]}{c}    {matrix[5][3]}{c}', end='')
  print('\n' * 4)
  sleep(1)