\# Controlled KG Normalization Checkpoint



Date: 2026-08-18



\## Project stage



The project has completed:



\- GraphRAG Pilot 1

\- Pilot 1 audit

\- domain-specific schema design

\- GraphRAG Pilot 2

\- Pilot 2 entity audit

\- Pilot 2 relationship audit

\- recall evaluation

\- alias analysis

\- community-report audit

\- schema/prompt comparison

\- GitHub checkpoint



Current stage:



\*\*Controlled Knowledge Graph normalization prototype\*\*



The purpose of this stage is to transform noisy GraphRAG output into a controlled,

traceable and validated Knowledge Graph before RDF/SPARQL, reasoning and KG embeddings.



\---



\## Current raw Pilot 2 graph



Pilot 2 contains:



\- 539 raw entities

\- 643 raw relationships

\- 17 text units



Raw GraphRAG output is treated as an extraction layer, not as the final authoritative KG.



\---



\## Entity normalization completed so far



\### TEC\_0001 — Photovoltaikanlage



Merged raw GraphRAG variants:



\- PV-ANLAGE

\- PV-ANLAGEN

\- PHOTOVOLTAIKANLAGEN

\- FOTOVOLTAIKANLAGE



Reason:



These represent singular/plural, abbreviation and spelling variants of the same

generic photovoltaic-installation concept.



\---



\### TEC\_0002 — Agri-PV-Anlage



Merged:



\- AGRI-PV-ANLAGE

\- AGRI-PV-ANLAGEN



Reason:



These are singular/plural variants of the same Agri-PV technology.



Important:



TEC\_0002 remains separate from TEC\_0001 because Agri-PV is a more specific

technology concept, not merely another name for all photovoltaic installations.



\---



\### ORG\_0001 — BMK



Canonical organization:



Bundesministerium für Klimaschutz, Umwelt, Energie, Mobilität, Innovation und Technologie (BMK)



Merged raw variants:



\- BMK

\- full ministry name

\- full ministry name with acronym



Reason:



Descriptions and source context confirm that all raw records refer to the same organization.



\---



\### POL\_0001 — Österreichische Photovoltaik-Strategie



Merged:



\- PHOTOVOLTAIK-STRATEGIE

\- ÖSTERREICHISCHE PHOTOVOLTAIK-STRATEGIE



Reason:



Both GraphRAG records refer to the same Austrian photovoltaic strategy.



\---



\## Entity-resolution rules learned



1\. Singular/plural variants may be merged when they represent the same concept.

2\. Acronyms may be merged with their verified full organization names.

3\. Short and full policy names may be merged when they refer to the same policy.

4\. Related concepts must not automatically be merged.

5\. A subtype/specialized technology stays separate from its broader concept.

6\. Similar names alone are insufficient evidence for merging.

7\. Entity type, title, description and source context should be checked.

8\. Raw GraphRAG IDs must be preserved for provenance and later relationship redirection.

9\. Canonical descriptions should describe entity identity conservatively rather than copy all LLM-generated claims.



\---



\## Relationship normalization started



\### REL\_0001



Canonical relationship:



ORG\_0001 -- RESPONSIBLE\_FOR --> POL\_0001



Modality:



EXPLICIT\_FACT



Raw GraphRAG produced two relationships after entity aliases were resolved.



One stated explicitly that BMK is listed as publisher and issuer of the Austrian

Photovoltaic Strategy.



The second represented institutional responsibility as a reasonable inference.



The duplicate raw relations were collapsed into one normalized relationship while

retaining both raw relationship IDs and supporting text-unit provenance.



Important:



GraphRAG relationship weight is not interpreted as truth probability.



\---



\## First rejected relationship case



Raw GraphRAG relationship:



AGRI-PV-ANLAGE -- PART\_OF --> FOTOVOLTAIKANLAGE



Raw relationship human-readable ID:



257



Graph relationship ID:



1b0a059f-694c-4e24-a3c7-766ebedc83a4



GraphRAG classified it as:



\- RELATION\_TYPE = PART\_OF

\- MODALITY = EXPLICIT\_FACT



The supporting text unit was inspected directly.



The source states that installations in agriculture should be designed in the form

of Agri-PV installations and discusses agricultural dual use.



The source does NOT explicitly state that an Agri-PV installation is PART\_OF a

photovoltaic installation.



Decision:



\*\*REJECTED\*\*



Reason:



PART\_OF is semantically misleading and overstates the evidence.



A possible subtype/specialization relationship may conceptually exist, but the

current Schema V1.1 does not contain SUBTYPE\_OF / IS\_A, and the schema should not

be changed based on this single case.



\---



\## Important methodological conclusion



We will NOT manually validate all 643 relationships one by one.



The current manual normalization work is a prototype used to identify error patterns

and define validation rules.



The later workflow should be:



raw GraphRAG relationships

→ automatic schema checks

→ canonical endpoint mapping

→ duplicate detection

→ predicate/modality checks

→ suspicious or uncertain cases

→ selective manual evidence review

→ controlled KG



Automatic checks should eventually include:



\- allowed predicate vocabulary

\- valid source/target entity types

\- canonical endpoint availability

\- duplicate relationships after entity merging

\- allowed modality values

\- provenance/text-unit availability

\- detection of out-of-schema predicates



Manual review should focus on uncertain, high-risk and representative evaluation cases.



\---



\## Files currently being developed



\- kg/controlled\_kg/canonical\_entities\_working.csv

\- kg/controlled\_kg/normalized\_relationships\_working.csv

\- kg/controlled\_kg/normalization\_rules.md

\- pilot\_02/inspection/inspection\_15\_entity\_normalization.ipynb



An empty/locked canonical\_entities.csv was encountered during development, so

canonical\_entities\_working.csv is currently used as the active working table.



\---



\## Exact point where work stopped



We stopped immediately after manually evaluating relationship 257:



AGRI-PV-ANLAGE -- PART\_OF --> FOTOVOLTAIKANLAGE



The source text was inspected and the relationship was classified as REJECTED.



The rejection decision exists in the notebook as a DataFrame but should next be

stored in a relationship-decision/audit table.



\---



\## Next step



On the next working session:



1\. Create/save `relationship\_decisions\_working.csv`.

2\. Add relationship 257 as the first REJECTED audit entry.

3\. Inspect a small number of additional representative relationships.

4\. Obtain examples of:

&#x20;  - accepted relationship

&#x20;  - corrected relationship

&#x20;  - rejected relationship

&#x20;  - duplicate relationship

5\. Derive automatic relationship-validation rules from those cases.

6\. Implement a small normalization/validation script rather than manually checking all 643 relationships.

7\. Produce the controlled KG prototype.

8\. Continue later with RDF/SPARQL, reasoning, KG embeddings and KG evolution.



Do not add more source documents yet.



First finish and validate this normalization prototype using the existing Pilot 2 document.

