import pandas as pd

df = pd.read_csv('responses.csv', low_memory=False)

# Convert 'created_time' column to datetime format
df['created_time'] = pd.to_datetime(df['created_time'])

# Extract year from the 'created_time' column
df['year'] = df['created_time'].dt.year

"""
Group 1: Total number of users who have practiced, total number of stories on which sessions
were created, total number of sessions practiced, total number of nodes encountered as Group 1
for each brand per year.
"""
group1_cols = df.groupby(['year', 'brand_id'])
group1_agg = group1_cols.agg(
    Total_User=('user_id', 'nunique'),
    Total_Stories=('story_id', 'nunique'),
    Total_Sessions=('id', 'nunique'),
    Total_Nodes=('node_key', 'nunique'),
)
table_1 = pd.pivot_table(group1_agg, index=['year', 'brand_id'])
print(table_1)


"""
Group 2: Total number of stories on which sessions were created, total number of sessions
practiced, total number of nodes encountered as Group 2 for each brand per year.
"""
group2_cols = df.groupby(['year', 'brand_id', 'user_id'])
group2_agg = group2_cols.agg(
    Total_Stories=('story_id', 'nunique'),
    Total_Sessions=('id', 'nunique'),
    Total_Nodes=('node_key', 'nunique'),
)
table_2 = pd.pivot_table(group2_agg, index=['year', 'brand_id', 'user_id'])
print(table_2)


"""
3. Highest occurrence of a node on each story by each user for each brand per year
"""
group3_cols = df.groupby(
    ['brand_id', 'year', 'user_id', 'story_id', 'node_key']).size().reset_index(name='Node_Count')
table_3 = group3_cols.groupby(['brand_id', 'year', 'user_id', 'story_id']).apply(
    lambda x: x[x['Node_Count'] == x['Node_Count'].max()]['node_key'].tolist()
).reset_index(name='Nodes_Highest')
print(table_3)


"""
4. Least occurrence of a node on each story by each user for each brand per year
"""
group4_cols = df.groupby(['brand_id', 'year', 'user_id','story_id', 'node_key']).size().reset_index(name='Node_Count')
table_4 = group4_cols.groupby(['brand_id', 'year', 'user_id', 'story_id']).apply(
    lambda x: x[x['Node_Count'] == x['Node_Count'].min()]['node_key'].tolist()
).reset_index(name='Nodes_Least')
print(table_4)


"""
5. Distinct nodes encountered on each story by each user for each brand per year
"""
group5_cols = df.groupby(['year', 'brand_id', 'user_id', 'story_id'])
group5_agg = group5_cols.agg(
    Total_Nodes=('node_key', 'nunique'),
)
table_5 = pd.pivot_table(group5_agg, index=['year', 'brand_id', 'user_id', 'story_id'])
print(table_5)
