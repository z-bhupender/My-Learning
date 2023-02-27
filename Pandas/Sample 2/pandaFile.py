import pandas as pd

male = pd.read_csv("male.csv", encoding="utf-8")
female = pd.read_csv("female.csv", encoding="utf-8")

# ----------------------------------------
"""Combining data from different tables"""
# ----------------------------------------

# Concat Method
"""
new_table = pd.concat([male, female])
print(new_table)
"""

# Merge Method
"""
new_table = pd.merge(male, female, how="left", on="id")
print(new_table)
"""

# ----------------------------------------
"""-------- Handling Strings ----------"""
# ----------------------------------------

# len method
"""
print(male["name"].str.len())
"""

# lower method / upper method
"""
print(male["name"].str.lower())
"""

# split method
"""
print(male["name"].str.split("a"))
"""

# get method
"""
male["split_value"] = male["name"].str.split("a").str.get(0)
"""

# contains method
"""
print(male[male["name"].str.contains("Bhupender")])
"""

# replace method
"""
print(male["name"].replace({"Ayush":"Bhupender"}))
"""