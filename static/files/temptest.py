#!/usr/bin/python

import random


def toss():
  xh=0
  xt=0
  xe=0
    
  for x in range(0,10000):
    x = random.choice([0,1])
    if x == 1:
      xh=xh+1
    elif x == 0:
      xt=xt+1
    else:
      xe=xe+1
        
  print "heads:",xh
  print "tails:",xt
  

