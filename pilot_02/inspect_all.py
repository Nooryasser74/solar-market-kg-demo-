from pathlib import Path
import json
import re
import pandas as pd


# ============================================================
# GraphRAG Full Inspection Script
# Experiment 1 - Austrian Photovoltaic Strategy
# ============================================================

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
INSPECTION = ROOT / "inspection"

INSPECTION.mkdir(exist_ok=True)


def save_csv(df, filename):
    """Save a dataframe so German characters display correctly in Excel."""
    path = INSPECTION / filename
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print(f"Created: {path.name}")


def load_parquet(filename):
    """Safely load a GraphRAG parquet file."""
    path = OUTPUT / filename

    if not path.exists():
        print(f"WARNING: {filename} was not found.")
        return None

    return pd.read_parquet(path)


def normalize_name(value):
    """Simple normalization used to find possible duplicate names."""
    if pd.isna(value):
        return ""

    text = str(value).upper().strip()

    # Remove punctuation and extra spaces
    text = re.sub(r"[^\wÄÖÜẞ]+", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# 1. LOAD ALL GRAPH RAG OUTPUT TABLES
# ============================================================

files = {
    "documents": "documents.parquet",
    "text_units": "text_units.parquet",
    "entities": "entities.parquet",
    "relationships": "relationships.parquet",
    "communities": "communities.parquet",
    "community_reports": "community_reports.parquet",
}

tables = {}

for name, filename in files.items():
    tables[name] = load_parquet(filename)


# ============================================================
# 2. CREATE GENERAL SUMMARY
# ============================================================

summary_lines = []

summary_lines.append("=" * 70)
summary_lines.append("GRAPH RAG FULL INSPECTION")
summary_lines.append("Austrian Photovoltaic Strategy 2024")
summary_lines.append("=" * 70)
summary_lines.append("")

for name, df in tables.items():

    if df is None:
        summary_lines.append(f"{name}: FILE NOT FOUND")
        continue

    summary_lines.append(f"{name.upper()}")
    summary_lines.append(f"Rows: {len(df)}")
    summary_lines.append(f"Columns: {', '.join(df.columns.astype(str))}")
    summary_lines.append("")


# ============================================================
# 3. ADD STATS.JSON INFORMATION
# ============================================================

stats_path = OUTPUT / "stats.json"

if stats_path.exists():

    with open(stats_path, "r", encoding="utf-8") as f:
        stats = json.load(f)

    summary_lines.append("=" * 70)
    summary_lines.append("INDEXING STATISTICS")
    summary_lines.append("=" * 70)

    summary_lines.append(
        f"Total runtime: {stats.get('total_runtime', 'unknown')} seconds"
    )

    summary_lines.append(
        f"Number of documents: {stats.get('num_documents', 'unknown')}"
    )

    summary_lines.append("")


# ============================================================
# 4. EXPORT COMPLETE RAW TABLES
# ============================================================

export_names = {
    "entities": "01_entities_all.csv",
    "relationships": "04_relationships_all.csv",
    "communities": "06_communities_all.csv",
    "community_reports": "07_community_reports_all.csv",
    "documents": "08_documents_all.csv",
    "text_units": "09_text_units_all.csv",
}

for name, filename in export_names.items():

    df = tables.get(name)

    if df is not None:
        save_csv(df, filename)


# ============================================================
# 5. ENTITY INSPECTION
# ============================================================

entities = tables.get("entities")

if entities is not None:

    # --------------------------------------------------------
    # Entity type counts
    # --------------------------------------------------------

    if "type" in entities.columns:

        type_counts = (
            entities["type"]
            .value_counts(dropna=False)
            .rename_axis("raw_graphrag_type")
            .reset_index(name="count")
        )

        save_csv(type_counts, "02_entity_type_counts.csv")

        summary_lines.append("=" * 70)
        summary_lines.append("ENTITY TYPE COUNTS")
        summary_lines.append("=" * 70)

        for _, row in type_counts.iterrows():
            summary_lines.append(
                f"{row['raw_graphrag_type']}: {row['count']}"
            )

        summary_lines.append("")

    # --------------------------------------------------------
    # Create entity review table
    # --------------------------------------------------------

    wanted_columns = [
        "human_readable_id",
        "title",
        "type",
        "description",
        "frequency",
        "degree",
        "text_unit_ids",
    ]

    existing_columns = [
        col for col in wanted_columns if col in entities.columns
    ]

    entity_review = entities[existing_columns].copy()

    # Columns for OUR controlled KG inspection
    entity_review["suggested_schema_type"] = ""
    entity_review["canonical_name"] = ""
    entity_review["keep_in_controlled_kg"] = ""
    entity_review["record_linkage_group"] = ""
    entity_review["review_notes"] = ""

    save_csv(entity_review, "03_entity_review.csv")


    # --------------------------------------------------------
    # Possible duplicate / inconsistent entity names
    # --------------------------------------------------------

    if "title" in entities.columns:

        duplicate_check = entities.copy()

        duplicate_check["normalized_title"] = (
            duplicate_check["title"].apply(normalize_name)
        )

        duplicate_mask = duplicate_check[
            "normalized_title"
        ].duplicated(keep=False)

        possible_duplicates = duplicate_check[
            duplicate_mask
        ].copy()

        if len(possible_duplicates) > 0:

            useful_columns = [
                col for col in [
                    "title",
                    "normalized_title",
                    "type",
                    "description",
                    "frequency",
                    "degree",
                ]
                if col in possible_duplicates.columns
            ]

            possible_duplicates = (
                possible_duplicates[useful_columns]
                .sort_values("normalized_title")
            )

        save_csv(
            possible_duplicates,
            "10_possible_duplicates.csv"
        )


    # --------------------------------------------------------
    # Top connected entities
    # --------------------------------------------------------

    if "degree" in entities.columns:

        top_entities = (
            entities
            .sort_values("degree", ascending=False)
            .head(30)
        )

        useful_columns = [
            col for col in [
                "title",
                "type",
                "degree",
                "frequency",
                "description",
            ]
            if col in top_entities.columns
        ]

        save_csv(
            top_entities[useful_columns],
            "11_top_connected_entities.csv"
        )


# ============================================================
# 6. RELATIONSHIP INSPECTION
# ============================================================

relationships = tables.get("relationships")

if relationships is not None:

    relationship_review = relationships.copy()

    # --------------------------------------------------------
    # Attach GraphRAG source/target entity types where possible
    # --------------------------------------------------------

    if (
        entities is not None
        and "title" in entities.columns
        and "type" in entities.columns
        and "source" in relationships.columns
        and "target" in relationships.columns
    ):

        type_map = (
            entities
            .drop_duplicates("title")
            .set_index("title")["type"]
            .to_dict()
        )

        relationship_review["source_raw_type"] = (
            relationship_review["source"].map(type_map)
        )

        relationship_review["target_raw_type"] = (
            relationship_review["target"].map(type_map)
        )

    # --------------------------------------------------------
    # Manual-review fields for controlled KG
    # --------------------------------------------------------

    relationship_review["evidence_status"] = ""
    relationship_review["suggested_relation_type"] = ""
    relationship_review["keep_in_controlled_kg"] = ""
    relationship_review["review_notes"] = ""

    save_csv(
        relationship_review,
        "05_relationship_review.csv"
    )


    # --------------------------------------------------------
    # Highest-weight relationships
    # --------------------------------------------------------

    if "weight" in relationships.columns:

        top_relationships = (
            relationships
            .sort_values("weight", ascending=False)
            .head(50)
        )

        useful_columns = [
            col for col in [
                "source",
                "target",
                "description",
                "weight",
            ]
            if col in top_relationships.columns
        ]

        save_csv(
            top_relationships[useful_columns],
            "12_top_relationships.csv"
        )


# ============================================================
# 7. COMMUNITY REPORT REVIEW TABLE
# ============================================================

community_reports = tables.get("community_reports")

if community_reports is not None:

    report_review = community_reports.copy()

    report_review["source_supported"] = ""
    report_review["possible_overgeneralization"] = ""
    report_review["review_notes"] = ""

    save_csv(
        report_review,
        "13_community_report_review.csv"
    )


# ============================================================
# 8. SAVE SUMMARY REPORT
# ============================================================

summary_path = INSPECTION / "00_summary.txt"

with open(summary_path, "w", encoding="utf-8") as f:
    f.write("\n".join(summary_lines))


# ============================================================
# 9. PRINT FINAL RESULT
# ============================================================

print()
print("=" * 70)
print("INSPECTION COMPLETE")
print("=" * 70)

print()
print(f"Inspection folder:")
print(INSPECTION)

print()

for name, df in tables.items():
    if df is not None:
        print(f"{name:20s}: {len(df)} rows")

print()
print("Open 00_summary.txt first.")
print("Then inspect 03_entity_review.csv and 05_relationship_review.csv.")