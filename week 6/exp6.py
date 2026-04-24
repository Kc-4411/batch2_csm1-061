!pip install --upgrade pgmpy
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})

print("Dataset:")
print(data)

# Define model (NEW class)
model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])

# Fit model
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Print CPDs
print("\nCPDs:")
for cpd in model.get_cpds():
    print(cpd)

# Inference
inference = VariableElimination(model)
result = inference.query(variables=['ArriveLate'], evidence={'Rain': 'Yes'})

print("\nResult:")
print(result)