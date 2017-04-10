"""
# The JPL Data Set
Mystery Dataset 1
Standard header:

"""
from __future__ import division,print_function
import  sys
sys.dont_write_bytecode = True
from  lib import *
"""

data.dat:

"""
def run(weighFeature = False,split="median"):
  vl=1;l=2;n=3;h=4;vh=5;xh=6;_=0
  return data(indep= [
     # 0..8
     'Prec','Flex','Resl','Team','Pmat','rely','cplx','data.dat','ruse',
     # 9 .. 17
     'time','stor','pvol','acap','pcap','pcon','aexp','plex','ltex',
     # 18 .. 25
     'tool','sced','site','docu','kloc'],
    less = ['effort', 'xyz', 'abc'],
    _rows=[
      [2, 2, 2, 3, 3, 4, 5, 4, 3, 5, 6, 4, 4, 4, 3, 4, 3, 3, 1, 3, 4, 4, 77, 1830, 77, 38.5],
      [2, 2, 2, 3, 3, 5, 5, 2, 3, 5, 6, 2, 4, 3, 3, 2, 1, 2, 2, 3, 4, 4, 23.8, 648, 23.8, 11.9],
      [2, 2, 2, 3, 3, 4, 5, 3, 3, 5, 5, 4, 3, 3, 3, 3, 2, 2, 1, 3, 4, 4, 22.5, 492, 22.5, 11.25],
      [2, 2, 3, 3, 2, 4, 4, 3, 2, 3, 3, 4, 3, 3, 3, 3, 3, 4, 2, 3, 5, 3, 146, 3291.8, 122, 61],
      [2, 3, 3, 5, 3, 3, 4, 3, 2, 4, 4, 2, 5, 5, 4, 5, 1, 5, 3, 3, 6, 3, 113.19, 1080, 113.19, 56.595],
      [3, 3, 3, 3, 3, 3, 4, 3, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 2, 3, 4, 3, 184, 1042.8, 160, 80],
      [5, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 2, 3, 3, 3, 5, 3, 4, 2, 3, 5, 3, 60.5, 336, 54, 27],
      [5, 3, 3, 4, 4, 4, 5, 3, 2, 3, 3, 2, 3, 3, 3, 5, 3, 4, 2, 3, 6, 3, 50, 637, 32.89, 16.445],
      [3, 3, 3, 2, 3, 4, 5, 3, 2, 3, 3, 3, 3, 3, 3, 4, 3, 4, 2, 3, 5, 3, 253, 2519, 188, 94],
      [3, 3, 4, 3, 3, 4, 4, 3, 4, 3, 3, 2, 3, 4, 3, 3, 1, 4, 5, 3, 2, 3, 158.75, 1047.9, 131, 65.5],
      [3, 3, 3, 3, 3, 4, 5, 3, 2, 3, 3, 4, 4, 4, 5, 4, 4, 4, 2, 1, 5, 3, 324, 1735.4, 245, 122.5],
      [3, 2, 4, 4, 3, 4, 5, 3, 4, 3, 4, 5, 4, 4, 3, 4, 4, 3, 4, 2, 6, 3, 224, 691, 153, 76.5],
      [5, 2, 2, 4, 3, 4, 3, 3, 4, 5, 4, 3, 4, 4, 3, 4, 4, 4, 3, 3, 3, 3, 104.6, 320, 48, 24],
      [3, 2, 2, 4, 3, 4, 3, 3, 3, 3, 3, 2, 4, 4, 3, 4, 4, 4, 3, 3, 3, 3, 173.4, 329, 98, 49],
      [3, 2, 4, 3, 3, 4, 5, 3, 4, 3, 3, 4, 3, 4, 4, 4, 3, 3, 3, 3, 5, 3, 597, 1705, 597, 298.5],
      [4, 2, 4, 3, 5, 4, 3, 2, 3, 3, 4, 4, 2, 2, 3, 3, 5, 5, 3, 3, 5, 3, 155, 789, 129, 64.5],
      [4, 3, 3, 3, 4, 4, 4, 3, 2, 3, 3, 3, 4, 4, 3, 5, 4, 4, 2, 3, 5, 3, 170, 552, 100, 50]
    ],
    _tunings =[[
    #         vlow  low   nom   high  vhigh xhigh
    #scale factors:
    'Prec',   6.20, 4.96, 3.72, 2.48, 1.24, _ ],[
    'Flex',   5.07, 4.05, 3.04, 2.03, 1.01, _ ],[
    'Resl',   7.07, 5.65, 4.24, 2.83, 1.41, _ ],[
    'Pmat',   7.80, 6.24, 4.68, 3.12, 1.56, _ ],[
    'Team',   5.48, 4.38, 3.29, 2.19, 1.01, _ ]],
    weighFeature = weighFeature,
    _split = split,
    _dataTypes = [int]*22 + [float]*4
    )
"""

Demo code:

"""
def _JPL(): print(JPL())

#if __name__ == '__main__': eval(todo('_nasa93()'))
