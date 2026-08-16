\# Solar Market Knowledge Graph - Schema V1



\## Entity Types



\### COUNTRY

A geographic country relevant to the market.

Example: Austria



\### ORGANIZATION

Government bodies, regulators, companies, research institutions, and other organizations.

Examples: BMK, E-Control, Technikum Wien



\### TECHNOLOGY

Energy technologies and technical solutions.

Examples: Photovoltaics, Battery Storage, Agri-PV



\### INFRASTRUCTURE

Physical energy-system infrastructure.

Examples: Electricity Grid, Distribution Grid



\### POLICY

Strategies, laws, regulations, or policy measures.

Examples: Austrian Photovoltaic Strategy 2024



\### SUPPORT\_SCHEME

Financial or policy support mechanisms.

Examples: Investment Subsidy, VAT Exemption



\### CONSTRAINT

Factors that restrict or complicate solar-market development.

Examples: Grid Access, Supply-Chain Dependence



\### MARKET\_METRIC

Quantitative indicators describing the market.

Examples: Installed PV Capacity, System Price, Annual PV Expansion



\### TARGET

Official objectives or desired future states.

Examples: Climate Neutrality 2040, PV Expansion Target



\## Relationship Types



\### SUPPORTS

One entity provides support for another.

Example:

Investment Subsidy → SUPPORTS → Photovoltaics



\### CONSTRAINS

One entity restricts or limits another.

Example:

Grid Capacity → CONSTRAINS → PV Expansion



\### HAS\_TARGET

A policy, organization, or country has an official objective.

Example:

Austria → HAS\_TARGET → Climate Neutrality 2040



\### CONTRIBUTES\_TO

One entity contributes to achieving another objective.

Example:

Photovoltaics → CONTRIBUTES\_TO → Climate Neutrality 2040



\### IMPLEMENTS

An organization implements a policy or measure.

Example:

Austrian Government → IMPLEMENTS → Energy Policy



\### MEASURED\_BY

A market or technology development is described by a quantitative indicator.

Example:

Photovoltaic Market → MEASURED\_BY → Installed PV Capacity

