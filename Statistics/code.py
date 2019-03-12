# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.DataFrame(pd.read_csv(path))

#Code starts here 
data.Gender.replace("-", "Agender", inplace = True)
gender_count = data.Gender.value_counts()
print(gender_count)



# --------------
#Code starts here
alignment = data.Alignment.value_counts()
plt.pie(alignment)
plt.title("Character Alignment")



# --------------
#Code starts here

sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().values[0,1]
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = sc_covariance/(sc_strength * sc_combat)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().values[0,1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = ic_covariance/(ic_intelligence * ic_combat)
print(ic_pearson)


# --------------
#Code starts here
total_high = data.Total.quantile(0.99)
super_best = data[data.Total > total_high].copy()
super_best_names = super_best.Name.tolist()
print(super_best_names)


# --------------
#Code starts here

# create 2x2 array of subplots
fig, ax_1 = plt.subplots() 
fig, ax_2 = plt.subplots() 
fig, ax_3 = plt.subplots() 
ax_1.set_title("Intelligence")
ax_2.set_title("Speed")
ax_3.set_title("Power")

# add boxplot to 1st subplot
super_best.boxplot(column='Intelligence', ax=ax_1) 
super_best.boxplot(column='Speed', ax=ax_2) 
super_best.boxplot(column='Power', ax=ax_3) 
plt.show()



