from operators import arith_operators as AO
from operators import logical_operators
from operators import sum


# call sum function from operators package
r = sum(4,5)

# call logical_and function from logical_operators module
logical_operators.logical_and()
print(r)

# Print name form arith_operators module
print(AO.name)


