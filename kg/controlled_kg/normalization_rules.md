# Controlled KG Normalization Rules

## Purpose

These rules define how raw GraphRAG entities are mapped to canonical entities
in the controlled Austrian solar-market Knowledge Graph.

## Rule 1 — Singular and plural variants

Merge singular and plural forms when they refer to the same underlying concept.

Example:
- PV-ANLAGE
- PV-ANLAGEN
- PHOTOVOLTAIKANLAGEN
- FOTOVOLTAIKANLAGE

Canonical entity:
- TEC_0001 — Photovoltaikanlage

## Rule 2 — Acronym and full organization name

Merge an acronym with its full name when the descriptions and source context
confirm that they refer to the same organization.

Example:
- BMK
- Bundesministerium für Klimaschutz, Umwelt, Energie, Mobilität,
  Innovation und Technologie

Canonical entity:
- ORG_0001

## Rule 3 — Short and full policy names

Merge short and full policy names when they clearly refer to the same policy.

Example:
- PHOTOVOLTAIK-STRATEGIE
- ÖSTERREICHISCHE PHOTOVOLTAIK-STRATEGIE

Canonical entity:
- POL_0001

## Rule 4 — Do not merge related but distinct concepts

Do not merge entities merely because they are closely related.

Example:
- Photovoltaikanlage
- Agri-PV-Anlage

These remain separate because Agri-PV is a more specific technology concept.

Canonical entities:
- TEC_0001 — Photovoltaikanlage
- TEC_0002 — Agri-PV-Anlage

## Rule 5 — Evidence before merging

Do not merge entities based only on similar names.

Before merging, compare:
- entity type
- full title
- description
- source text-unit IDs
- source context where necessary

Decision values:
- MERGE
- KEEP SEPARATE
- UNCERTAIN

## Rule 6 — Preserve provenance

Every canonical entity must preserve the raw GraphRAG entity IDs from which
it was created.

Raw IDs must not be discarded because they are needed later to redirect
relationships and trace normalized entities back to GraphRAG output.

## Rule 7 — Conservative canonical descriptions

Canonical descriptions should describe the identity of the entity.

Do not copy every contextual claim from the GraphRAG-generated description
into the canonical description. Claims about targets, responsibilities,
requirements, status, or effects should later be represented as relationships
or properties when supported by evidence.
