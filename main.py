# from pkg1 import p1,p2
from pkg1 import *
import pkg2.p1
import pkg2.p2

print p1.mysquare(5)
print p2.mysum(5)

print pkg2.p1.mysquare(5)
print pkg2.p2.mysum(5)

