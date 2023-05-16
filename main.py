import sys
import os
import math
import random

stack = []
code = []
char = ''

if len(sys.argv) == 1:
    file_argument = 'main.yx'
else:
    file_argument = sys.argv[1]

with open(file_argument, 'r') as file:
    for line in file:
        row = [char if char != ' ' else ' ' for char in line.rstrip('\n')]
        code.append(row)

code = [row + [''] * (max(len(row) for row in code) - len(row)) for row in code]

x = 0
y = 0
direction = 'r'
pw = 100

numbers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def run():
  global stack, char, code, x, y, direction, numbers, pw

  # Update direction & current command

  while y < len(code) and x < len(code[y]):
    if pw > 0:

      if direction == 'l':
        x -= 1
      
      elif direction == 'r':
        x += 1
      
      elif direction == 'u':
        y -= 1
      
      elif direction == 'd':
        y += 1
      
      char = code[y][x] if y < len(code) and x < len(code[y]) else ''
      # print(f'\033[33m{char}')


      # Mirrors, yes, I didn't find a way to use lambdas here, Rust `match` would have saved me lines :(

      if char == '/':
          if direction == 'l':
              direction = 'u'
          elif direction == 'r':
              direction = 'd'
          elif direction == 'u':
              direction = 'l'
          elif direction == 'd':
              direction = 'r'

      elif char == '\\':
          if direction == 'l':
              direction = 'd'
          elif direction == 'r':
              direction = 'u'
          elif direction == 'u':
              direction = 'r'
          elif direction == 'd':
              direction = 'l'


      elif char == 'v':
        direction = 'd'

      elif char == '^':
        direction = 'u'

      # Energy command
      
      elif char == '·':
        pw += 10 if (x | y) > 10 else pw;

      # IO

      elif char == 'n':
        stack.append(int(input()))

        pw -= 5
    
      elif char == 'a':
        a = input()
        for character in a:
          stack.append(ord(character))
    
        pw -= 10

      elif char == 'o':
        print(chr(stack.pop()))
        
        pw -= 5

      elif char == 'O':
        print(stack.pop())

        pw -= 5

      elif char == '!':
        stack.pop()

      elif char in numbers:
        stack.append(int(char, 16))

      elif char == '"':
        x += 1

        while code[y][x] != '"':
          character = code[y][x]
          stack.append(chr(character))

        pw -= 15

      elif char == ':':
        stack.append(stack[-1])

      elif char == ';':
        stack[-1], stack[-2] = stack[-2], stack[-1]

      elif char == '$':
        stack.reverse()

      elif char == '&':
        sys.exit()

      # Math

      elif char == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(b + a)

      elif char == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)

      elif char == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(b * a)

      elif char == '|':
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)

      elif char == '°':
        a = stack.pop()
        b = stack.pop()
        stack.append(b ** a)

      elif char == '%':
        a = stack.pop()
        b = stack.pop()
        stack.append(b % a)

      # Misc
      
      elif char == 'I':
        stack.append(random.randint(0,1))

      elif char == '?':
        if stack.pop() == 0:
          x += 1

    else:
      print('\n\033[31mOut of power!')
      sys.exit()
    
try: 
   run()
except KeyboardInterrupt:
   print("\nProgram exited through keyboard")