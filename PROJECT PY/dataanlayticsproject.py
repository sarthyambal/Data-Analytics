import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

#Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df.drop_duplicates

df['price'] = df["price"].astype(str).str.replace(",","").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

#Numerical Columns Cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

#Catregorical Cloumns Cleaning
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower()
df["flat_type"] = df["flat_type"].str.strip().str.lower()

print(df.info)
print(df)

# Questions 1: which is the most expensive flat type in the dataset?
costliest_flat_type = df.loc[df['price'].idxmax(),]
print(costliest_flat_type)

# Question 2: Which locality has the highest average price?
df.groupby("locality")["price"].mean().sort_values(ascending=False)


# Question 3: Which locality has the highest rate per square foot?
df.groupby("locality")["rate_per_sqft"].mean().sort_values(ascending=False)

# Question 4: Ready-to-move vs Under-construction pricing
df.groupby("status")["price"].median()

# Question 5: Does RERA approval affect pricing?
df.groupby("rera_approval")["price"].median()

# Question 6: How does area impact price?
sns.scatterplot(x="area", y="price", data=df)
plt.show()

# Question 7: Which BHK configuration is most expensive?
df.groupby("bhk_count")["price"].mean()

# Question 8: Which property type is the costliest?
df.groupby("flat_type")["price"].mean()


# Question 9: Do certain builders price higher?
df.groupby("company_name")["price"].mean().sort_values(ascending=False)



# Question 10: Are larger homes more expensive per sqft?
sns.scatterplot(x="area", y="rate_per_sqft", data=df)
plt.show()

