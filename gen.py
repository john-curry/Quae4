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
print r""" 
    \usepackage{tikz}
    \usetikzlibrary{shapes,arrows}

"""
print r"\begin{document}"
print r"\maketitle"
print r"\nonstopmode"
print r"\section*{Question 1}" 
print r"\textwidth = 500pt"
print r"\linespread{1.0}"
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

for key in keys:
  start = h1.subs(k,key).subs(t,11)
  i = 0
  probe = (start) % 11

  #print "Inserting key " + str(key) + " at " + str(probe) + r"\\"

  if table[probe] == None: 
      #print r"No collisions!!\\"
      table[probe] = key

  else: # COLLISION!!
      while table[probe] != None:
          #print "Collsion at " + str(probe) + r"!!.\\"
          i = i + 1 
          probe = (start + (i ** 2)) % 11

      #print "Probe successful. Found: " + str(probe) + " for key " + str(key) + r"\\"
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
    #print "Inserting key " + str(key) + " at " + str(probe) + r"\\"
    if table[start] == None:
      #print r"No collisions!!\\"
      table[start] = key
    else: # COLLISION
        while table[probe] != None:
            #print "Collsion at " + str(probe) + r"!!.\\"
            index = index + 1
            probe = dhash.subs(k,key).subs(i,index)
        #print "Probe successful. Found: " + str(probe) + " for key " + str(key) + r"\\"
        table[probe] = key
pl ( table )
    
    
# ==========================================
print r"\section*{Question 3}"
print r"""
    \par Given $h(k, i) = h_1(k) + ih_2(k)\bmod t$ where $h_2(k)$ returns only even integers and t is even, 
    show that $h(k,i)$ will examine at most half the slots in the hash table before returning to $h_1(k)$.\\        
    \\
    Since $i * h_2(k) $ will only be even and since $h_1(k)$ is constant for any $i$, $h(k,i)$ will either only 
    examine even or odd slots in the table depending on the parity of $h_1(k)$. Therefore, for any given $k$
    $h(k,i)$ will only examine half the slots in the table.\\

    Claim: Assume $h_1(k)$ will be visited after $h(k,i)$ has visited over half the slots. Then $h(k,i)$ has used up
      it's even slots (if $h_1$ is even) of it's odd slots (if $h_1$ is odd), but that will mean that $h_1$ has been visited.
      Therefore our claim is false.\\
"""

# ==========================================
print r"\section*{Question 4}"
print r"\subsection*{a)}"
print r"""
\begin{tikzpicture}[ 
    mynode/.style = {
        circle, draw = black
      }
    ]
    \node[mynode](1) at (0,0) {1};
    \node[mynode](2) at (4,0) {2};
    \node[mynode](3) at (2,2) {3};
    \node[mynode](4) at (2,4) {4};

    \node[mynode](5) at (6,0) {5};
    \node[mynode](6) at (10,0) {6};
    \node[mynode](7) at (8,2) {7};
    \node[mynode](8) at (8,4) {8};
    \path[draw] (1) -- (2) -- (1) -- (3) -- (1) -- (4) -- (3) -- (2) -- (4);
    \path[draw] (4) -- (5) -- (6) -- (7) -- (5) -- (8) -- (7);
\end{tikzpicture}
"""
print r"\subsection*{b)}"
print r" DFS Order = 1 , 2, 3, 4, 6, 5, 7, 8\\"

# ==========================================
print r"\section*{Question 5}"
mtable = [ [ 0, 1, 1, 1, 0, 0, 0, 0], 
           [ 1, 0, 1, 1, 0, 0, 0, 0],
           [ 1, 1, 0, 1, 0, 0, 0, 0],
           [ 1, 1, 1, 0, 0, 1, 0, 0],
           [ 0, 0, 0, 0, 0, 1, 1, 1],
           [ 0, 0 ,0, 1, 1, 0, 1, 0],
           [ 0, 0, 0, 0, 1, 1, 0, 1],
           [ 0, 0, 0, 0, 1, 0, 1, 0]
        ]
print r"\subsection*{Adjacency matrix}"


print " $v$ : " + latex([i + 1 for i in range (0, 8)]) + r"\\"

for i in range (0, 8):
    print str(i + 1) + " : " + latex(mtable[i]) + r"\\"

mlist = { 1: [ 2, 3, 4 ], 
          2: [ 1, 3, 4 ], 
          3: [ 1, 2, 4 ],  
          4: [ 1, 2, 3, 6 ],
          5: [ 6, 7, 8 ],
          6: [ 4, 5, 7 ],
          7: [ 5, 6, 8 ],
          8: [ 5, 7]
        }
print r"\subsection*{Adjacency list}\\"
for i in range (1, 9):
    print str(i) + ": " + latex(mlist[i]) + r"\\"





print r"\end{document}"
