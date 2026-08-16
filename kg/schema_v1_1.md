# Solar Market Knowledge Graph — Schema V1.1

## 1. Purpose

This schema supports structured and explainable analysis of relationships among Austrian solar-market policy, market and technical factors.

Schema V1.1 was developed after auditing Pilot 1. It addresses the following observed problems:

* policies and technologies classified as events or organizations;
* numerical targets not represented structurally;
* aliases represented as separate entities;
* recommendations represented as implemented actions;
* overly broad or unsupported relationships;
* insufficient representation of stakeholders and subnational geographic areas.

This is a controlled domain schema for the final knowledge graph. GraphRAG output remains a raw extraction layer and must be validated before information is mapped into this schema.

---

## 2. General modelling principles

1. Every entity must be explicitly supported by source text.
2. Every relationship must retain a reference to its supporting source text unit.
3. Recommendations, intentions, requirements and implemented measures must be distinguished.
4. Numerical values must preserve their value, unit, reference year and deadline where available.
5. Abbreviations and spelling variants must map to one canonical entity.
6. An entity must not be classified as an organization simply because no better generic GraphRAG type is available.
7. Generated descriptions and community reports are not authoritative source evidence.
8. Unsupported causal relationships must not be added to the controlled graph.
9. GraphRAG relationship weight must not be interpreted as factual confidence.
10. Missing information must remain missing rather than being inferred without evidence.

---

## 3. Entity types

### GEOGRAPHIC_AREA

A country, federal state, municipality, city or another geographic or administrative area relevant to the solar market.

Examples:

* Austria
* Vienna
* Austrian federal states
* Municipalities

Suggested properties:

* `canonical_name`
* `area_type`
* `country`
* `source_document_id`
* `text_unit_ids`

This replaces the narrower `COUNTRY` class from Schema V1.

---

### ORGANIZATION

A formally identifiable government body, regulator, company, association, research institution or other organization.

Examples:

* Federal Ministry for Climate Action, Environment, Energy, Mobility, Innovation and Technology
* BMK
* E-Control
* Climate and Energy Fund
* European Commission
* Bundesverband Photovoltaic Austria

Suggested properties:

* `canonical_name`
* `abbreviation`
* `organization_type`
* `country`
* `aliases`
* `source_document_id`
* `text_unit_ids`

Abbreviations must be linked to the canonical organization rather than retained as separate entities.

Example:

```text
BMK
    → alias of
Federal Ministry for Climate Action, Environment, Energy,
Mobility, Innovation and Technology
```

---

### STAKEHOLDER

A person, group or market-participant category involved in, affected by or responsible for solar-market development.

Examples:

* Citizens
* PV system operators
* Private investors
* Grid operators
* Building owners
* Policymakers
* Research community

Suggested properties:

* `canonical_name`
* `stakeholder_type`
* `role`
* `source_document_id`
* `text_unit_ids`

Named individuals should only be retained when they are relevant to the analytical purpose of the knowledge graph. Authors, photographers and contact persons should normally not be included.

An institution such as E-Control remains an `ORGANIZATION`, even when it also acts as a market stakeholder.

---

### TECHNOLOGY

An energy technology, technical system, installation type or technical solution.

Examples:

* Photovoltaics
* PV system
* Battery storage
* Agri-PV
* Vertical PV
* East-west-oriented PV
* Energy management system
* Heat pump
* Hydrogen technology

Suggested properties:

* `canonical_name`
* `technology_category`
* `application`
* `aliases`
* `source_document_id`
* `text_unit_ids`

PV systems and photovoltaic installations are technologies or installations, not organizations or events.

---

### INFRASTRUCTURE

Physical or digital infrastructure required for the production, distribution, storage or management of energy.

Examples:

* Public electricity grid
* Distribution grid
* Transmission grid
* Grid connection
* Energy storage infrastructure
* Digital grid infrastructure

Suggested properties:

* `canonical_name`
* `infrastructure_type`
* `geographic_scope`
* `source_document_id`
* `text_unit_ids`

---

### POLICY

A strategy, law, regulation, directive, action plan, programme or other policy instrument.

Examples:

* Austrian Photovoltaic Strategy 2024
* Renewable Expansion Act
* Integrated Austrian Network Infrastructure Plan
* Renewable Energy Directive III
* Electricity Industry Act
* Condominium Act Amendment 2022
* Grid Connection Action Plan 2023

Suggested properties:

* `canonical_name`
* `policy_type`
* `jurisdiction`
* `publication_year`
* `effective_date`
* `implementation_status`
* `aliases`
* `source_document_id`
* `text_unit_ids`

Recommended values for `implementation_status` include:

* `PROPOSED`
* `PLANNED`
* `ADOPTED`
* `IN_FORCE`
* `IMPLEMENTED`
* `ONGOING`
* `UNKNOWN`

A policy or strategy must not be classified as an event.

---

### SUPPORT_SCHEME

A financial, fiscal, regulatory or administrative mechanism intended to support solar-market development.

Examples:

* Investment subsidy
* Zero-percent VAT measure
* Feed-in premium
* Tax exemption
* Simplified approval procedure
* Research funding

Suggested properties:

* `canonical_name`
* `support_type`
* `eligible_recipient`
* `eligibility_condition`
* `threshold_value`
* `threshold_unit`
* `start_date`
* `end_date`
* `implementation_status`
* `source_document_id`
* `text_unit_ids`

A support scheme can be created or governed by a policy, but it is not identical to the policy itself.

---

### CONSTRAINT

A legal, administrative, economic, social or technical factor that restricts or complicates solar-market development.

Examples:

* Limited grid capacity
* Grid-connection delay
* Lengthy approval procedure
* Skilled-labour shortage
* Supply-chain dependence
* Land-use conflict
* Insufficient public acceptance

Suggested properties:

* `canonical_name`
* `constraint_type`
* `affected_area`
* `geographic_scope`
* `source_document_id`
* `text_unit_ids`

A constraint should only be created when the source explicitly describes a limitation, problem, obstacle or risk.

---

### MARKET_METRIC

A quantitative indicator used to describe the status or development of the solar market.

Examples:

* Annual PV expansion
* Installed PV capacity
* PV electricity generation
* Share of final electricity consumption
* Public funding volume
* PV system price

Suggested properties:

* `canonical_name`
* `metric_type`
* `value`
* `unit`
* `reference_year`
* `geographic_scope`
* `approximate`
* `source_document_id`
* `text_unit_ids`
* `source_quote`

Examples:

```text
Annual PV expansion
value: 2.5
unit: GW
reference_year: 2023
geographic_scope: Austria
approximate: true
```

```text
PV electricity generation
value: 6.3
unit: TWh
reference_year: 2023
geographic_scope: Austria
```

A year or unit must not be treated as an independent entity. It belongs to the structured market-metric record.

---

### TARGET

An official quantitative or qualitative objective associated with a country, organization or policy.

Examples:

* Climate neutrality by 2040
* 100% nationally balanced renewable electricity by 2030
* 41 TWh PV generation potential by 2040
* 21 TWh PV electricity generation by 2030
* 11 TWh additional PV generation by 2030

Suggested properties:

* `canonical_name`
* `target_type`
* `target_value`
* `unit`
* `baseline_value`
* `baseline_year`
* `deadline`
* `geographic_scope`
* `target_status`
* `approximate`
* `source_document_id`
* `text_unit_ids`
* `source_quote`

Recommended values for `target_status` include:

* `OFFICIAL`
* `PROPOSED`
* `PLANNED`
* `SCENARIO`
* `ASPIRATIONAL`
* `ACHIEVED`
* `UNKNOWN`

A target must preserve its value, unit and deadline whenever these are stated.

Example:

```text
41 TWh PV generation potential by 2040
target_value: 41
unit: TWh
deadline: 2040
target_status: SCENARIO
```

---

## 4. Relationship types

### HAS_TARGET

Connects a geographic area, organization or policy to an official or proposed target.

Example:

```text
Austria
    → HAS_TARGET →
Climate neutrality by 2040
```

---

### SETS_TARGET

Connects a policy or organization to a target that it formally establishes.

Example:

```text
Renewable Expansion Act
    → SETS_TARGET →
11 TWh additional PV generation by 2030
```

Use `SETS_TARGET` only when the source identifies the policy or organization as establishing the target.

---

### CONTRIBUTES_TO

Indicates that one entity contributes to an objective or outcome.

Example:

```text
Photovoltaics
    → CONTRIBUTES_TO →
Climate neutrality by 2040
```

This relationship must not imply that the source guarantees the target will be achieved.

---

### SUPPORTS

Indicates that a policy, support scheme, technology or organization supports another entity or activity.

Example:

```text
Investment subsidy
    → SUPPORTS →
PV deployment
```

---

### CONSTRAINS

Indicates that a constraint limits or complicates a technology, market development, target or activity.

Example:

```text
Limited grid capacity
    → CONSTRAINS →
PV expansion
```

---

### IMPLEMENTS

Indicates that an organization has actually implemented or is actively implementing a policy or measure.

Example:

```text
Responsible ministry
    → IMPLEMENTS →
PV support programme
```

`IMPLEMENTS` must not be used for recommendations, proposals or future intentions.

---

### PROPOSES

Indicates that a policy document, organization or actor proposes a measure that has not necessarily been implemented.

Example:

```text
Austrian Photovoltaic Strategy
    → PROPOSES →
Further development of energy communities
```

---

### REQUIRES

Indicates an explicit obligation, technical requirement or necessary condition.

Example:

```text
PV expansion
    → REQUIRES →
Grid expansion
```

Use this relationship only when necessity or obligation is explicit in the source.

---

### RESPONSIBLE_FOR

Connects an organization, stakeholder or government level to a policy area, infrastructure or action for which it is responsible.

Example:

```text
Austrian federal states
    → RESPONSIBLE_FOR →
Spatial planning
```

---

### APPLIES_TO

Connects a policy, support scheme, requirement or constraint to the entity or group affected by it.

Example:

```text
Zero-percent VAT measure
    → APPLIES_TO →
Eligible PV systems up to 35 kWp
```

---

### REGULATES

Connects a policy or organization to the technology, market activity, infrastructure or stakeholder it regulates.

Example:

```text
Electricity Industry Act
    → REGULATES →
Grid connection
```

---

### FUNDS

Connects an organization, policy or support scheme to an activity, technology or programme receiving financial support.

Example:

```text
Climate and Energy Fund
    → FUNDS →
PV research
```

---

### MEASURED_BY

Connects a market development, technology or geographic area to a market metric.

Example:

```text
Austrian PV market
    → MEASURED_BY →
Annual PV expansion
```

---

### HAS_VALUE

Connects a metric or target to its structured quantitative observation when the implementation uses separate observation nodes.

Example:

```text
Annual PV expansion
    → HAS_VALUE →
2.5 GW in 2023
```

If value, unit and year are stored directly as properties of `MARKET_METRIC` or `TARGET`, a separate `HAS_VALUE` relationship is unnecessary.

---

### PART_OF

Represents a clear hierarchical relationship.

Example:

```text
Distribution grid
    → PART_OF →
Electricity grid
```

---

### LOCATED_IN

Connects an organization, infrastructure item, technology installation or activity to a geographic area.

Example:

```text
PV installation
    → LOCATED_IN →
Austria
```

---

### ALIAS_OF

Connects an abbreviation or spelling variant to its canonical entity during entity-resolution processing.

Example:

```text
BMK
    → ALIAS_OF →
Federal Ministry for Climate Action, Environment, Energy,
Mobility, Innovation and Technology
```

Aliases should ultimately be merged into the canonical entity in the controlled knowledge graph. `ALIAS_OF` may be retained in an intermediate mapping table for provenance.

---

## 5. Relationship modality

Each relationship should include a modality describing how strongly the source presents the statement.

Recommended values:

* `EXPLICIT_FACT`
* `LEGAL_REQUIREMENT`
* `RECOMMENDATION`
* `PROPOSAL`
* `PLANNED_ACTION`
* `SCENARIO`
* `REASONABLE_INFERENCE`

Suggested relationship properties:

* `source_document_id`
* `text_unit_ids`
* `source_quote`
* `modality`
* `implementation_status`
* `valid_from`
* `valid_to`
* `auditor_status`

Recommended values for `auditor_status` include:

* `DIRECTLY_SUPPORTED`
* `PARTIALLY_SUPPORTED`
* `INFERRED`
* `UNSUPPORTED`
* `REJECTED`

---

## 6. Entity-resolution rules

The controlled knowledge graph should use one canonical entity for abbreviations, spelling variants and grammatical variants.

Examples:

```text
BMK
Bundesministerium für Klimaschutz, Umwelt, Energie,
Mobilität, Innovation und Technologie
    → one canonical ORGANIZATION
```

```text
ÖNIP
NIP
Integrierter österreichischer Netzinfrastrukturplan
    → one canonical POLICY
```

```text
PV
Photovoltaik
Photovoltaics
    → one canonical TECHNOLOGY
```

```text
PV-Anlage
PV-Anlagen
Photovoltaikanlage
Photovoltaikanlagen
    → one canonical TECHNOLOGY
```

Entity resolution must consider meaning and context. Similar strings should not be merged automatically when they refer to different concepts.

---

## 7. Source and provenance requirements

Every accepted entity and relationship should preserve:

* source document identifier;
* source document title;
* supporting text-unit identifier;
* source section or page where available;
* exact or concise supporting quotation;
* extraction method;
* validation status.

Community reports may help identify candidates, but they must not be used as the sole authoritative source for a controlled KG statement.

The original source document remains the authoritative reference.

---

## 8. Exclusion rules

The following items should normally be excluded unless directly relevant to the research question:

* document page numbers;
* addresses;
* telephone numbers;
* email addresses;
* photographers;
* publication metadata;
* generic words such as “science” or “economy” without a bounded meaning;
* isolated years;
* isolated numerical values;
* formatting artefacts;
* repeated headers and footers;
* entities introduced only by an LLM-generated description;
* unsupported causal statements.

---

## 9. GraphRAG mapping guidance

The controlled schema and GraphRAG configuration are related but are not identical.

For Pilot 2, the GraphRAG extraction categories should be mapped as follows:

| Controlled KG type | Pilot 2 GraphRAG extraction category |
| ------------------ | ------------------------------------ |
| GEOGRAPHIC_AREA    | geographic_area                      |
| ORGANIZATION       | organization                         |
| STAKEHOLDER        | stakeholder                          |
| TECHNOLOGY         | technology                           |
| INFRASTRUCTURE     | infrastructure                       |
| POLICY             | policy                               |
| SUPPORT_SCHEME     | support_scheme                       |
| CONSTRAINT         | constraint                           |
| MARKET_METRIC      | market_metric                        |
| TARGET             | target                               |

The extraction prompt must include definitions, positive examples and exclusion rules for these categories.

The controlled relationship vocabulary should primarily be enforced through the extraction prompt and downstream validation. The `entity_types` list in `settings.yaml` controls the available entity categories but does not fully define relationship semantics or entity-resolution rules.

---

## 10. Schema V1.1 summary

Schema V1.1 contains ten controlled entity types:

```text
GEOGRAPHIC_AREA
ORGANIZATION
STAKEHOLDER
TECHNOLOGY
INFRASTRUCTURE
POLICY
SUPPORT_SCHEME
CONSTRAINT
MARKET_METRIC
TARGET
```

Its principal relationship types are:

```text
HAS_TARGET
SETS_TARGET
CONTRIBUTES_TO
SUPPORTS
CONSTRAINS
IMPLEMENTS
PROPOSES
REQUIRES
RESPONSIBLE_FOR
APPLIES_TO
REGULATES
FUNDS
MEASURED_BY
HAS_VALUE
PART_OF
LOCATED_IN
ALIAS_OF
```

This schema is intended to improve domain relevance, entity typing, numerical representation, policy modality, provenance and entity resolution in Pilot 2.
