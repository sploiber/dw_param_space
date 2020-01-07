from pyqubo import Binary, Constraint, Placeholder
from dimod import ExactSolver

# Flagpole problem from Denny's slide 2
# On slide 3, he uses an auxiliary variable p = xy
# what other kind of variables are there?
p, x, y, z = Binary("p"), Binary("x"), Binary("y"), Binary("z")

lamda = Placeholder("lamda")
H = (p * z) + (lamda * Constraint((3 * p) + (x * y) - (2 * p * (x + y)), label="subst"))

# Can I find the minimum valid energy?
# Can I find the maximum valid energy?
# and the minimum invalid energy?
# what do they require?
model = H.compile()
bqm = model.to_dimod_bqm(feed_dict={"lamda":1.4})
exact_response = ExactSolver().sample(bqm)
for smpl, energy in exact_response.data(['sample', 'energy']):
    sol, broken, eny = model.decode_solution(smpl, vartype='BINARY', feed_dict={"lamda":0.7})
    if not broken:
        print(" Good ", sol, eny)
    if broken:
        print(" Bad ", sol, eny)
