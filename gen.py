#!/usr/bin/env python
from sys import argv
from sympy import *

init_printing(use_latex=True)

def pl(s):
  print r"$$" + latex(s) + r"$$\\" 

def pm(s):
  print r"$" + latex(s) + r"$"

def pr(s):
  print latex(s)

print r"\documentclass{article}"
print r"\usepackage{amsmath}"
print r"\begin{document}"
print r"\section*{Question 1}"
print r"\nonstopmode"

l = [ 5, 28, 19, 15, 20, 33, 12, 17, 10 ]
pl ( l )

h, k = symbols('h(k) k')

h = (2 * k + 5) % 9

print r"$$" + latex('h(k)') + " = "  + latex(h) + r"$$"

d = { }

for i in l: 
  j = h.subs(k,i)
  if d.has_key(j):
    d[j].append(i)
  else:
    d[j] = [ i ]   

for i in d:
    print "$$ " + latex(i) + " : " + str(d[i]) + r"$$\\"
  
print r"\section*{Question 2}"
keys = [ 10, 22, 31, 4, 15, 28, 17, 88, 5 ] 
pl ( keys )
h1, h2, h = symbols('h1,h2,h')
k, t, i = symbols('k t i')

print r"\begin{equation}"

print latex(h(k,i))
print " = " 
print latex(((h1(k) + i * h2(k)) % t))

print r"\end{equation}"

print r"\begin{equation}"

print latex(h1(k))
h1 = k % t
print ' = '
print latex(h1)

print r"\end{equation}"

print r"\begin{equation}"

print latex(h2(k))
h2 = 1 + k % (t - 1)
print ' = '
print latex(h2)

print r"\end{equation}"


hash_keys = [ h1.subs(k,key) for key in keys ]  

table = [ None for m in range(0, 11) ]

for key in keys:
  j = h1.subs(k,key).subs(t,11)
  while table[j] != None:
    j = (j + 1) % 11
  table[j] = key
print r"\subsection*{Linear Probing}"
print latex(table, mode='equation')

# Quadratic Probing ==========================================
print r"\subsection*{Quadratic Probing}"

hash_keys = [ h1.subs(k,key) for key in keys ]  

table = [ None for m in range(0, 11) ]

for key in keys:
  j = h1.subs(k,key).subs(t,11)
  while table[j] != None:
    j = (j ** 2) % 11
    print j
  table[j] = key

print latex(table, mode='equation')






















print r"\end{document}"
