
import numpy as np
import pandas as pd

np.random.seed(42)  # reproducibility

# Parameters
N = 5000  # number of children
max_time = 60  # follow-up in months (0-59 months = under-5 mortality)

# Area distribution: 60% rural, 40% urban
area = np.random.choice(['Rural', 'Urban'], size=N, p=[0.6, 0.4])

# Mother’s age at child’s birth
mother_age = np.clip(np.random.normal(28, 6, N), 15, 49).astype(int)

# Education levels
education_levels = ['None', 'Primary', 'Secondary', 'Higher']
education = np.random.choice(education_levels, size=N, p=[0.3, 0.3, 0.3, 0.1])

# Sex of child
sex = np.random.choice(['Male', 'Female'], size=N, p=[0.52, 0.48])

# Region distribution (roughly proportional to population size)
regions = ['North Central', 'North East', 'North West',
           'South East', 'South South', 'South West']
region_probs = [0.15, 0.15, 0.25, 0.1, 0.15, 0.2]
region = np.random.choice(regions, size=N, p=region_probs)

# Wealth index quintiles
wealth_levels = ['Poorest', 'Poorer', 'Middle', 'Richer', 'Richest']
wealth_index = np.random.choice(wealth_levels, size=N, p=[0.2, 0.2, 0.2, 0.2, 0.2])

# Birth order (1–6+, skewed toward lower orders)
birth_order = np.random.choice(range(1, 7), size=N, p=[0.25, 0.2, 0.2, 0.15, 0.1, 0.1])

# Baseline hazard depending on area + wealth
hazard_rural = 0.03
hazard_urban = 0.015

# Modify hazard based on area & wealth
hazard = np.where(area == 'Rural', hazard_rural, hazard_urban)
hazard *= np.where(wealth_index == 'Poorest', 1.5, 1)
hazard *= np.where(wealth_index == 'Richest', 0.7, 1)

# Generate survival times using Weibull distribution
shape = 1.5
u = np.random.uniform(size=N)
survival_time = (-np.log(u) / hazard) ** (1 / shape)

# Censor at 60 months
time = np.minimum(survival_time, max_time)
event = (survival_time <= max_time).astype(int)

# Build DataFrame
df = pd.DataFrame({
    'id': range(1, N+1),
    'area': area,
    'mother_age': mother_age,
    'education': education,
    'sex': sex,
    'region': region,
    'wealth_index': wealth_index,
    'birth_order': birth_order,
    'time': time.round(1),
    'event': event
})

print(df.head())
df.to_csv("synthetic_child_mortality_expanded.csv", index=False)
# Save to CSV