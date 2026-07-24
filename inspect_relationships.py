import pandas as pd

df = pd.read_parquet(r"output\relationships.parquet")

print("COLUMNS:")
print(df.columns.tolist())

print()
print("NUMBER OF RELATIONSHIPS:", len(df))

print()
print("RELATIONSHIPS:")
print(df.to_string(index=False))
