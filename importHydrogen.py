import pyomo.environ as pyo

# Create a Pyomo model
model = pyo.ConcreteModel()
# Yael

# Define model parameters
##########################################
############ CODE TO ADD HERE ############
##########################################

# Define model variables
##########################################
############ CODE TO ADD HERE ############
##########################################

# Define the objective functions
##########################################
############ CODE TO ADD HERE ############
##########################################

# Define the constraints
##########################################
############ CODE TO ADD HERE ############
##########################################

# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory('"C:\Users\yaelc\OneDrive\Documents\Documents\Unif\Master_1\Q2\LELME2003\gurobi.lic"')
sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################
