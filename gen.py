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

print r"\documentclass[a4paper,margin=1in]{article}"
print r"\usepackage{amsmath}"
print r"\usepackage[letterpaper, margin=1in]{geometry}"
print r"\usepackage{url}"
print r"""
    \author{John Curry\\
            V00755720\\
            \url{jfcurry@uvic.ca}}
    \title{CSC 225 Assignment 3}
"""
print r"\begin{document}"
print r"\maketitle"
print r"\section*{Question 1}"
print r"\nonstopmode"
print r"\textwidth = 500pt"
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

# Linear Probing ==============================================
print r"\subsection*{Linear Probing}"

hash_keys = [ h1.subs(k,key) for key in keys ]  

table = [ None for m in range(0, 11) ]

for key in keys:
  j = h1.subs(k,key).subs(t,11)
  while table[j] != None:
    j = (j + 1) % 11
  table[j] = key

pl ( table )

# Quadratic Probing ==========================================
print r"\subsection*{Quadratic Probing}"

hash_keys = [ h1.subs(k,key).subs(t, 11) for key in keys ]  

print r"Keys to be hashed: \\"
pl ( keys )

print r"Keys after they have been through $h_1(k)$ \\"
pl ( hash_keys )

table = [ None for m in range(0, 11) ]

pl ( table )

for key in keys:
  start = h1.subs(k,key).subs(t,11)
  i = 0
  probe = (start) % 11

  print "Inserting key " + str(key) + " at " + str(probe) + r"\\"

  if table[probe] == None: 
      print r"No collisions!!\\"
      table[probe] = key

  else: # COLLISION!!
      while table[probe] != None:
          print "Collsion at " + str(probe) + r"!!.\\"
          i = i + 1 
          probe = (start + (i ** 2)) % 11

      print "Probe successful. Found: " + str(probe) + " for key " + str(key) + r"\\"
      table[probe] = key
  pl ( table )

# Double Hashing ==========================================
print r"\subsection*{Double Hashing}"

dhash = symbols('Double_Hash', cls=Function)
i, k = symbols('i k')

table = [ None for m in range(0, 11) ]

dhash = ((k % 11) + i * (1 + (k % 10))) % 11

for key in keys:
    index = 0
    probe = dhash.subs(k, key).subs(i,index)
    print "Inserting key " + str(key) + " at " + str(probe) + r"\\"
    if table[start] == None:
      print r"No collisions!!\\"
      table[start] = key
    else: # COLLISION
        while table[probe] != None:
            print "Collsion at " + str(probe) + r"!!.\\"
            index = index + 1
            probe = dhash.subs(k,key).subs(i,index)
        print "Probe successful. Found: " + str(probe) + " for key " + str(key) + r"\\"
        table[probe] = key
    pl ( table )
    
    
















print r"\end{document}"
