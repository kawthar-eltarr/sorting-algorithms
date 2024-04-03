from random import sample
from selection import selection_sort

T = sample(range(0, 100), 20)

print("This is T before the selection sort :", T)

selection_sort(T)

print("This is T after the selection sort :", T)