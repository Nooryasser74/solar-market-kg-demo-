import pandas as pd

df = pd.read_parquet(r"output\community_reports.parquet")

print("Number of reports:", len(df))
print()

print(df[["human_readable_id", "title", "summary"]].to_string(index=False))