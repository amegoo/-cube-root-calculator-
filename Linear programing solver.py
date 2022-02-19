#   Report 2
#   Abdallah Mahmoud Ramadan
#   Section 3, Numper 5
from pulp import *
max_z = LpProblem("max_z", LpMaximize)
#Define variables
x1 = LpVariable(name="x1", lowBound=15, cat="non")
x2 = LpVariable(name="x2", lowBound=0, cat="non")
#Add the objective function
max_z += 2 * x1 + 6 * x2
print("z = ", max_z.objective)
# Add the constraints
max_z += ( x1 + 3* x2 <= 60)
max_z += (3*x1 +4* x2 <= 120)

# Solve the LP
status = max_z.solve(PULP_CBC_CMD(msg=0))
a=status
if a==1:
    print("Optimal solution exists and is found.")
elif a==-1:
    print("Infeasible, no solution exists that satisfies all of the constraints");sys.exit()
elif a==-2:
    print("Unbounded,Feasible solution hasn't been found (but may exist)"); sys.exit()
elif a==-3:
    print("Undefined"); sys.exit()   
#Print solution
for var in max_z.variables():
    print(var, "=", value(var))
print ("The optimal value of the objective function is = ", value(max_z.objective))
