from pyqubo import Binary
from dimod import ExactSolver

# Flagpole problem from Denny's slide 2
# On slide 3, he uses an auxiliary variable p = xy
# what other kind of variables are there?
p, x, y, z = Binary("p"), Binary("x"), Binary("y"), Binary("z")

lamda = 1.7
H = (p * z) + (lamda * ((3 * p) + (x * y) - (2 * p * (x + y))))

model = H.compile()
qubo, offset = model.to_qubo()
print(offset)
print(qubo)
bqm = model.to_dimod_bqm(offset)
exact_response = ExactSolver().sample(bqm)
solns = model.decode_dimod_response(exact_response)

# Confirm slide 5
for sol in solns:
    print(sol)
# x = 0, y = 0, z = 0, and p = 1: 3 lambda
# ({'p': 1, 'x': 0, 'y': 0, 'z': 0}, {}, 4.199999999999999)
# x = 0, y = 0, z = 1, and p = 1: 3 lambda + 1
# ({'p': 1, 'x': 0, 'y': 0, 'z': 1}, {}, 5.199999999999999)
# y = 1 and p = 1: lambda
({'p': 1, 'x': 0, 'y': 1, 'z': 0}, {}, 1.3999999999999995)
# x = 0 and y = 1 and z = 1 and p = 1: lambda + 1
({'p': 1, 'x': 0, 'y': 1, 'z': 1}, {}, 2.3999999999999995)
# lambda
({'p': 1, 'x': 1, 'y': 0, 'z': 0}, {}, 1.3999999999999995)
# lambda + 1
({'p': 1, 'x': 1, 'y': 0, 'z': 1}, {}, 2.3999999999999995)
# lambda
({'p': 0, 'x': 1, 'y': 1, 'z': 0}, {}, 1.4)
# lambda
({'p': 0, 'x': 1, 'y': 1, 'z': 1}, {}, 1.4)
