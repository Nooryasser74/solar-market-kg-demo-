import pandas as pd

df = pd.read_parquet(r"output\entities.parquet")

print("COLUMNS:")
print(df.columns.tolist())

print()
print("NUMBER OF ENTITIES:", len(df))

print()
print("ENTITIES:")
print(df.to_string(index=False))