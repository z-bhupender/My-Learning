"""
import pandas as pd
import matplotlib.pyplot as plt
"""

# To open the csv file
"""
csv_data = pd.read_csv(
    "sample_csv.csv", index_col=0, encoding="utf-8", low_memory=False
)
"""

# To print the data
# If an integer argument is passed it returns rows_no = argument
"""
print(csv_data.head())
"""

# Prints the data types of values contained
"""
print(csv_data.dtypes)
"""

# To print the technical information about Dataframe
"""
print(csv_data.info())
"""

# To fetch a column data from key
"""
age = csv_data["Age"] # Age is the column name
print(age.head())
"""

# To make a spreadsheet out of this csv file
"""
data.to_excel("details.xlsx", sheet_name="employee_details")
"""
# To open the excel file
"""
excel_data = pd.read_excel('details.xlsx',sheet_name="employee_details" )
"""

# To filter the specific rows in Data Frame according to a condition
"""
age_20 = csv_data[csv_data["Age"] > 20]
print(age_20.head())
"""

# To filter the rows in Data Frame using { isin() method, takes argument as array of values }
"""
age_2021 = csv_data[csv_data["Age"].isin([19, 20])]
print(age_2021.head())
"""

# Above command using OR ( | ) {AND ( & ) can also be usef}
"""
age_2021 = csv_data[ (csv_data["Age"] == 19) |  (csv_data["Age"] == 20)]
print(age_2021.head())
"""

# To print the name on the basis of age check
"""
names = csv_data.loc[csv_data["Age"] > 20, "Name"]
print(names.head())
"""

# To print selected rows and columns
"""
print(csv_data.iloc[<row_no_start>:<row_no_end>, <col_no_start>:<col_no_end>])
"""

# To create a plot of the data
"""
csv_data.plot()
plt.show()
"""

# To make a new column using original data
# In this similar way new column can be made using data of multiple columns
"""
csv_data["days_lived"] = csv_data["Age"] * 365
print(csv_data.head())
"""

# To rename the column names
"""
csv_data_renamed = csv_data.rename(
    columns={
        "Name" : "First Name",
        "Age" : "User's Age",
    }
)
print(csv_data_renamed.head())
"""

# To convert column names to lower case / upper case
"""
csv_data_renamed = csv_data.rename(columns=str.lower)
print(csv_data_renamed)
"""

# -------------------------------------
"""------------Statistics-----------"""
# -------------------------------------

# mean
"""
print(csv_data["Age"].mean())
"""

# median
"""
print(csv_data["Age"].median())
"""

# describe all stats
"""
print(csv_data["Age"].describe())
"""

# mean
"""
print(csv_data["Age"].mean())
"""

# aggregation
"""
print(csv_data.agg(
    {
        "Age" : ["min", "max", "median", "skew"]
    }
))
"""

# Print average age of male vs female
"""
print(csv_data[["Gender", "Age"]].groupby("Gender").mean())
"""


# Prints count of the values
"""
print(csv_data["Age"].value_counts())
"""

# Prints count of male and female
"""
print(csv_data.groupby("Gender")["Age"].count())
"""

# -------------------------------------
"""----------Table Reshaping--------"""
# -------------------------------------

# Sort data on the basis of Age | Ascending by default
"""
print(csv_data.sort_values(by="Age", ascending=False).head(7))
"""

# It makes rows based on @{ index param } with @{ value param } as data and @{ columns param } as column name
"""
csv_data.pivot(index="Gender", columns="Name", values="Age").plot.bar()
plt.show()
"""

# It gives the mean of age on the basis of gender
"""
print(csv_data.pivot_table(
    values="Age", index="Gender", columns="Name", aggfunc="mean", margins=True
))
"""