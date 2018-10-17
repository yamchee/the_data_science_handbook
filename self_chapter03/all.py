import pandas as pd

# DataFrame
df = pd.DataFrame({
    "name": ["Bob", "Alex"],
    "age": [24, 76]
})

df["age_plus_one"] = df["age"] + 1
df["over_30"] = (df["age"] > 30)

other_df = pd.read_csv("myfile.csv", ";")
print other_df["age"].apply(lambda x: x*x)

df_w_name_as_ind = df.set_index("name")
print df_w_name_as_ind.ix["Bob"]["age"]

#Series
s = pd.Series([1, 2, 3])
print s
print s+4

bobs_row = df_w_name_as_ind.ix["Bob"]
print bobs_row

# Joining and Grouping
df_w_age = pd.DataFrame({
    "name": ["A", "B", "C", "Z"],
    "age": [7, 21, 12, 77]
})

df_w_marks = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "marks": [79, 44, 13, 88]
})

joined = df_w_age.set_index("name").join(df_w_marks.set_index("name"))
print joined

df_full = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "marks": [79, 44, 13, 88],
    "gender": ['M', 'F', 'F', 'F']
})

print df_full.groupby("gender").mean()
def agg(ddf):
    return pd.Series({
        "name": max(ddf["name"]),
        "highest": max(ddf["marks"]),
        "mean_marks": ddf["marks"].mean()
    })
print df_full.groupby("gender").apply(agg)

import re

street_pattern = r"^[0-9]\s[A-Z][a-z]*" + \
    r"(Street|St|Rd|Road|Ave|Avenue|Blvd|Way|Wy)\.?$"
city_pattern = r"^[A-Z][a-z]*,\s[A-Z]{2},[0-9]{5}$"
address_pattern = street_pattern + r"\n" \
    + city_pattern

address_re = re.compile(street_pattern)
text = r"1 Penn Ave."
# doesn't work.
matches = re.findall(address_re, text)
open("addresses_w_space_between.txt",
     "w").write("\n\n".join(matches))
