# Controlled Relationship Schema V1

## Purpose

This vocabulary normalizes relationships extracted from Austrian solar-market documents. GraphRAG may produce additional raw relationship descriptions, but the final controlled KG should map them to these relations.

## Relationship types

### HAS_TARGET

Connects a policy, strategy or organization to an explicitly stated target.

Allowed source types:
- POLICY
- ORGANIZATION

Allowed target types:
- TARGET

Example:
- ERNEUERBAREN-AUSBAU-GESETZ → HAS_TARGET → PV-AUSBAU VON MINDESTENS 11 TWH BIS 2030

---

### MEASURED_BY

Connects a technology, geographic area or market concept to an observed numerical metric.

Allowed source types:
- TECHNOLOGY
- GEOGRAPHIC_AREA
- MARKET_METRIC

Allowed target types:
- MARKET_METRIC

Example:
- PHOTOVOLTAIK → MEASURED_BY → PV-GENERATION 6.3 TWH IN 2023

---

### SUPPORTS

Connects a support scheme, policy or infrastructure measure to the technology, target or activity it explicitly supports.

Allowed source types:
- SUPPORT_SCHEME
- POLICY
- INFRASTRUCTURE

Allowed target types:
- TECHNOLOGY
- TARGET
- POLICY

---

### REGULATES

Connects a policy or legal instrument to the activity, technology, infrastructure or stakeholder it regulates.

Allowed source types:
- POLICY

Allowed target types:
- TECHNOLOGY
- INFRASTRUCTURE
- STAKEHOLDER
- ORGANIZATION

---

### IMPLEMENTED_BY

Connects a policy, measure, target or support scheme to the responsible implementing organization or stakeholder.

Allowed source types:
- POLICY
- SUPPORT_SCHEME
- TARGET

Allowed target types:
- ORGANIZATION
- STAKEHOLDER

---

### CONSTRAINS

Connects a constraint to the technology, infrastructure, target or market activity it restricts.

Allowed source types:
- CONSTRAINT

Allowed target types:
- TECHNOLOGY
- INFRASTRUCTURE
- TARGET
- MARKET_METRIC

---

### CONTRIBUTES_TO

Represents an explicitly supported contribution where the source does not establish direct causality.

Allowed source types:
- TECHNOLOGY
- POLICY
- SUPPORT_SCHEME
- INFRASTRUCTURE
- STAKEHOLDER

Allowed target types:
- TARGET
- POLICY
- TECHNOLOGY
- MARKET_METRIC

---

### LOCATED_IN

Connects an organization, infrastructure asset, technology deployment or activity to a geographic area.

Allowed source types:
- ORGANIZATION
- INFRASTRUCTURE
- TECHNOLOGY
- STAKEHOLDER

Allowed target types:
- GEOGRAPHIC_AREA

---

### PART_OF

Represents an explicitly stated hierarchical or component relationship.

Allowed source types:
- POLICY
- SUPPORT_SCHEME
- INFRASTRUCTURE
- TECHNOLOGY
- ORGANIZATION

Allowed target types:
- POLICY
- SUPPORT_SCHEME
- INFRASTRUCTURE
- TECHNOLOGY
- ORGANIZATION

---

### ALIAS_OF

Connects an extracted name variant to its canonical entity.

This relation is created during entity resolution and must not be inferred merely from similar wording.