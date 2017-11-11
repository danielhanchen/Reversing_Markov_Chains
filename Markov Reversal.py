from numpy import *
from numpy.linalg import *

def reverse(prev_t, prev_pop, next_pop):
    length = len(prev_t)
    top = prev_t*(multiply(prev_pop, eye(length)))
    bot = multiply(next_pop, ones((length,length)))
    return (top/bot).T

prev_t = matrix([[0.4, 0.2, 0.4],
                 [0.1, 0, 0.9],
                 [0,0,1]]).T

prev_pop = matrix([10,203,12.3]).T

next_pop = prev_t*prev_pop

print(next_pop)
print(sum(next_pop), sum(prev_pop))


print(inv(prev_t), "\n\n", inv(prev_t)*next_pop)

rev_t = reverse(prev_t, prev_pop, next_pop)
print(rev_t, "\n\n", sum(rev_t, 0))

print(rev_t*next_pop)
print(prev_pop)

