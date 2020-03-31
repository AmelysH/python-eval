# file = open('DATASET.txt')
from ruler import Ruler
import sys

filename = sys.argv[1]
file = open(filename)

i = 1
while True:
    try :
        l1 = next(file)
        l2 = next(file)
        ruler = Ruler(l1, l2)
        ruler.compute()
        print(f"====== example # {i} - distance = {ruler.distance}")
        top, bottom = ruler.report()
        print(top)
        print(bottom)
        i += 1
    except StopIteration:
        break