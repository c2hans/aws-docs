---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/intelligence-layer.html
---

# Intelligence Layer

## Intelligence Layer Overview
<a name="intelligence-layer-overview.b6f72a74-f2f7-5dce-bb20-5f2f435d4fc7"></a>

The **Intelligence Layer** serves as the cognitive foundation of the architecture, providing automated capabilities for ontology lifecycle management, knowledge quality assurance, and contextual reasoning that bridge the gap between raw data and actionable semantic knowledge. This layer orchestrates the continuous evolution and validation of the semantic fabric, ensuring that ontologies remain aligned with business reality, knowledge graphs reflect source data truth, and agents operate with contextually grounded, episodic memory.

**Ontology Induction** enables the automated construction and enrichment of ontologies through multiple complementary approaches. **Bottom-up induction** analyzes business and technical data catalogs (AWS Glue Data Catalog, Amazon SageMaker Catalog / DataZone, DataHub, Collibra), structured and semi-structured data sources (relational schemas, JSON/XML structures, Parquet metadata), controlled vocabularies and taxonomies extracted from documents (via the Data Layer's information extraction workflows), and LLM-guided inputs from specifications and domain expert interviews to discover entity types, relationships, and constraints present in existing data. **Top-down integration** incorporates established open-source upper ontologies (e.g., BFO, DOLCE) and domain-specific ontologies (e.g., SNOMED CT for healthcare, FIBO for financial services) to provide foundational semantic structures and industry-standard vocabularies. This hybrid approach — combining data-driven discovery with expert-curated knowledge — produces ontologies that are both grounded in organizational reality and aligned with industry best practices, accelerating time-to-value while ensuring semantic interoperability.

**Ontology Evaluation and Completeness Assessment** continuously analyzes ontologies against available data sources and broader business requirements to identify gaps, inconsistencies, and opportunities for enrichment. The evaluation process compares the ontology's coverage (classes, properties, constraints) against actual data distributions, entity types present in source systems, and business concepts referenced in documentation or specifications. Industry ontologies like FIBO (Financial Industry Business Ontology) or HL7 FHIR (healthcare) serve as benchmarks, highlighting missing concepts or relationships that would enhance semantic expressiveness and enable broader use cases. Automated metrics track ontology completeness, consistency (via ELK/HermiT reasoners), and alignment with data catalogs, surfacing recommendations for ontology engineers and domain experts.

**Truth Maintenance** ensures that knowledge materialized in the Semantic Layer Graph Database remains synchronized with source data, preventing semantic drift and maintaining trust in the knowledge graph. Leveraging provenance metadata stored with every triple (source system, extraction timestamp, confidence score), the Truth Maintenance Service monitors source data changes via event streams (Neptune DB Streams, Kafka, AWS EventBridge) and triggers validation workflows when discrepancies are detected. For virtualized knowledge accessed through the VKG Service, truth is maintained by design — queries always retrieve current data from source systems. For materialized knowledge in Neptune, the service reconciles assertions against source data, flags stale or contradictory facts, and triggers re-extraction or reasoning workflows to restore consistency. This closed-loop validation ensures that agents and applications operate on verified, current knowledge.

**Short-Term Memory and Context Graphs** provide episodic, session-scoped knowledge that grounds agent reasoning in specific conversational contexts, user interactions, or workflow executions. These context graphs — stored as named graphs in Neptune or in-memory graph structures — capture entities, relationships, and events relevant to a specific agent session (e.g., a Q&A conversation, a business elicitation interview, an ontology maintenance task). Context graphs are **ontology-grounded** where appropriate, linking session-specific entities to the broader Semantic Layer ontology to enable reasoning and knowledge reuse. For example, a Q&A Agent's context graph might include the user's query history, retrieved document chunks, and inferred user intent — all linked to ontology classes like `Query`, `Document`, `Intent`. These context graphs inform agents executing in the Orchestration Layer, including **Question & Answer (Q&A) Agents** (retrieving and synthesizing knowledge), **Business Elicitation Agents** (capturing requirements and domain knowledge from stakeholders), and **Ontology Maintenance Agents** (performing entity resolution, disambiguation, and ontology refinement based on usage patterns).

## Intelligence Layer Capabilities
<a name="intelligence-layer-capabilities.abfca8ca-e29c-5163-a0aa-9cae9e053dbc"></a>

|
|
| Capability | Purpose | Key Techniques |
| --- |--- |--- |
| **Ontology Induction** | Automated ontology construction from data and domain knowledge | Bottom-up (schema analysis, LLM-guided extraction), Top-down (upper/domain ontologies) |
| **Ontology Evaluation** | Assess ontology completeness and alignment with data/business needs | Coverage metrics, industry ontology benchmarking (FIBO, SNOMED), gap analysis |
| **Truth Maintenance** | Ensure materialized knowledge reflects source data | Provenance tracking, change data capture, reconciliation workflows |
| **Context Graphs** | Episodic, session-scoped memory for agent reasoning | Named graphs, ontology-grounded entities, session lifecycle management |

This Intelligence Layer enables **self-improving semantic systems** that continuously refine ontologies based on data evolution, maintain knowledge graph fidelity through automated validation, and provide agents with contextual, episodic memory — supporting autonomous, knowledge-driven decision-making across the enterprise.

## Ontology Induction
<a name="ontology-induction.da8882b0-c553-5822-b0c4-bd0ecb961504"></a>

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/images/guide-img/5cb278fc-4bbf-4e43-a830-4b4f72516d31/images/4493e513-81ea-41e2-bb2f-5797c07e8fbf.png)

### Data Flow — Ontology Induction
<a name="data-flow---ontology-induction.8531853a-891e-5ee9-9b2f-1484d64878fa"></a>

**1. REST API → Ontology Induction Service (Amazon ECS)** A client initiates the ontology induction workflow via a **REST API** endpoint, invoking the **Ontology Induction Service** deployed as containerized tasks on **Amazon ECS** (with **Fargate** or **EC2** instances) within the VPC. The API accepts parameters specifying:
+ Induction approach (bottom-up from catalogs, top-down from reference ontologies, LLM-guided from specifications, or hybrid)
+ Target data sources (SageMaker Catalog, Glue Data Catalog, specific databases or schemas)
+ Ontology scope and namespace
+ Quality thresholds and validation requirements

The request is authenticated via JWT/OIDC bearer tokens validated by the AgentCore Gateway, and the ECS service scales horizontally based on induction workload complexity. The Ontology Induction Service implements **various techniques** including **LLM-based semantic enrichment** via Amazon Bedrock and **vector-based similarity techniques** such as **OWL2Vec**\* (generates vector embeddings from OWL ontologies for similarity computation) and **RDF2Vec** (generates vector embeddings from RDF graphs using random walks, enabling semantic similarity matching between discovered entities and reference ontologies).

**2. Ontology Induction Service → Amazon SageMaker Catalog / DataZone** Based on input parameters and availability of business data catalog information, the service inspects and analyzes **business glossary terms and metadata** from **Amazon SageMaker Catalog** and **Amazon DataZone**. The service retrieves:
+ **Business glossary terms** — Curated business definitions, synonyms, and entity relationships from DataZone's business glossary
+ **Data assets** — Datasets, features, model artifacts registered in SageMaker Catalog with business context
+ **Domain context** — DataZone domain memberships, data product classifications, and semantic tags applied by data stewards
+ **Data quality metrics** — Completeness, uniqueness, validity scores, and data profiling statistics from SageMaker Catalog
+ **Lineage information** — Upstream and downstream data flows, transformations, and dependencies

This metadata provides the **business-oriented view** of data assets, capturing how data is understood and used within the organization. The service analyzes naming conventions, glossary term associations, and lineage patterns to identify candidate ontology classes (e.g., `Customer`, `Claim`, `Transaction`) and relationships.

**3. Ontology Induction Service → AWS Glue Data Catalog** The service retrieves **technical data catalog information** from **AWS Glue Data Catalog**, analyzing database objects, tables, views, and associated columns. The service queries:
+ **Database and table schemas** — Column names, data types, constraints (primary keys, foreign keys), nullability, and cardinality
+ **Crawled metadata** — Statistics, discovered patterns, data classifications, and partitioning schemes
+ **Schema evolution history** — Version history of table schemas to understand how data structures have evolved
+ **Glue Schema Registry** — Avro, Protobuf, or JSON schemas for streaming data sources
+ **Source system mappings** — Connection metadata linking Glue tables to source databases (RDS, Redshift, Snowflake, S3)

The service applies **Ontology-Based Data Access (OBDA) mapping patterns** to generate candidate R2RML mappings:
+ **Tables → Ontology Classes** (e.g., `claims` table → `ex:Claim` class via R2RML `rr:TriplesMap`)
+ **Columns → Ontology Properties** (e.g., `claim_amount` column → `ex:claimAmount` datatype property via `rr:PredicateObjectMap`)
+ **Foreign Keys → Object Properties** (e.g., `customer_id` FK → `ex:submittedBy` object property linking `Claim` to `Customer` via `rr:RefObjectMap`)
+ **Primary Keys → Entity IRIs** (e.g., `claim_id` → `ex:Claim/{claim_id}` via `rr:SubjectMap` with IRI template)

These R2RML mappings define how relational data is virtualized as RDF, enabling the VKG Service to translate SPARQL queries into optimized SQL without data duplication. The mappings are generated based on schema analysis and will be refined in subsequent steps using sample data and LLM enrichment.

**Optionally, technical data catalog information is linked to business data catalog information** (if available from Step 2), reconciling technical schemas with business glossary terms to create a unified view. For example, a Glue table column `cust_id` might be linked to a DataZone business term "Customer Identifier" with a formal definition and business owner, and this business context is incorporated into the R2RML mapping annotations.

**4. Ontology Induction Service → Virtual Knowledge Graph (VKG) Service** The Ontology Induction Service calls the **Virtual Knowledge Graph (VKG) Service** to retrieve **existing ontologies** and **sample data** from both the **Semantic Layer Graph Database** (Neptune DB) and **Data Layer sources**. This step enables the induction process to:
+ **Retrieve existing ontologies** — Query Neptune for T-Box definitions (classes, properties, hierarchies, axioms) from customer-provided ontologies, previously induced ontologies, or integrated reference ontologies (SNOMED CT, FIBO, BFO, DOLCE)
+ **Retrieve existing R2RML mappings** — Query Neptune for deployed R2RML mappings to understand how existing ontology classes and properties are currently mapped to Data Layer sources, ensuring consistency with established OBDA patterns
+ **Sample materialized data** — Execute SPARQL queries against Neptune to retrieve sample instances (A-Box) of existing classes, understanding how ontology concepts are currently used in the knowledge graph
+ **Sample virtualized data** — Query the VKG Service to retrieve sample data from Data Layer sources (via existing R2RML mappings) without moving data, observing actual data distributions, value ranges, and relationship patterns in relational databases, data warehouses, and data lakes
+ **Validate catalog-to-data alignment** — Compare catalog metadata (from Steps 2 and 3) with actual sampled data to detect schema drift, verify foreign key relationships, validate data type mappings, and refine candidate R2RML mappings

The VKG Service federates these queries across Neptune (materialized graphs in Semantic Layer Graph Database) and Data Layer sources (Snowflake, Redshift, Athena, S3 Tables/Iceberg), returning unified RDF results. This provides the Ontology Induction Service with a **comprehensive, data-grounded view** of the current semantic landscape, enabling it to:
+ Avoid duplicating existing ontology concepts
+ Align newly induced classes and properties with established patterns
+ Validate that catalog metadata accurately reflects actual data
+ Generate realistic R2RML mappings based on observed data structures and existing OBDA patterns
+ Ensure consistency with the VKG Service's query translation and federation capabilities

**5. Ontology Induction Service → Amazon Bedrock** Business and technical data catalog information (Steps 2-3), combined with existing ontologies, R2RML mappings, and sample data retrieved from the VKG Service (Step 4), are analyzed and **linked to existing ontologies** (e.g., customer-provided ontologies, open-source upper ontologies like BFO or DOLCE, industry domain ontologies like SNOMED CT for healthcare or FIBO for financial services) using **Amazon Bedrock** foundation models. The Ontology Induction Service invokes Bedrock to:
+ **Semantic enrichment** — Generate `rdfs:label`, `rdfs:comment`, `skos:definition`, and `skos:altLabel` annotations for classes and properties based on catalog metadata, column names, business glossary terms, and sample data values
+ **Entity disambiguation** — Resolve ambiguous terms (e.g., "status" could be order status, claim status, or account status) using context from lineage, domain metadata, business definitions, and existing ontology patterns
+ **Ontology alignment** — Map discovered entity types to concepts in existing ontologies (retrieved in Step 4) using **vector-based similarity techniques** (OWL2Vec\*, RDF2Vec) to compute semantic similarity between candidate classes and reference ontology concepts
+ **Axiom generation** — Propose domain/range constraints, cardinality restrictions, disjointness axioms, and property characteristics based on data patterns, foreign key relationships, sample data distributions, and business rules
+ **R2RML mapping refinement** — Enhance candidate R2RML mappings (from Step 3) with semantic context, optimizing IRI templates, adding conditional mappings based on data values, and incorporating business logic from glossary terms
+ **Specification extraction** — Parse technical specifications, data dictionaries, requirements documents, or domain expert interviews (text/document inputs) to extract entity types, relationships, and constraints
+ **Consistency validation** — Use LLM reasoning to validate that newly induced ontology elements and R2RML mappings are consistent with existing ontology patterns, OBDA best practices, and domain conventions

This hybrid approach combines **bottom-up discovery** (from catalogs and schemas), **data-grounded validation** (from VKG-sampled data), and **top-down integration** (from existing and reference ontologies), producing ontologies and R2RML mappings that are both aligned with organizational data reality and consistent with established semantic patterns and industry best practices.

**6. Ontology Induction Service → Neptune DB (Semantic Layer Graph Database)** Induced ontologies are added to the **Semantic Layer Graph Database** (Neptune DB). The service writes:
+ **T-Box (Ontology/Schema)** — OWL classes, object properties, datatype properties, class hierarchies (`rdfs:subClassOf`), property domains and ranges, and axioms
+ **Annotations** — `rdfs:label`, `rdfs:comment`, `skos:definition`, `skos:altLabel` for all classes and properties
+ **Provenance metadata** — Links back to source catalogs (SageMaker Catalog, Glue Catalog), source tables/columns, existing ontologies referenced, induction method (catalog-driven, LLM-assisted, vector similarity), confidence scores, and timestamps
+ **SHACL constraints** — Data quality and validation rules derived from schema metadata, data statistics, and LLM-generated business rules
+ **R2RML mappings** — R2RML mappings linking the induced ontology classes and properties to source tables and columns (informed by sample data retrieved via VKG Service in Step 4 and refined by Bedrock in Step 5), enabling immediate virtualization via the VKG Service. These mappings follow OBDA best practices and are consistent with the Knowledge Layer's VKG architecture.

**Governance is integral** — versioning and workflow management ensure quality and control:
+ **Draft Mode** — Initially induced ontologies and updates to existing ontologies are written to **draft named graphs** in Neptune (e.g., `ex:ontology/v2.0-draft`) and flagged with `ex:status "DRAFT"` annotations. Draft ontologies and R2RML mappings are not used by VKG Service or Reasoning Service workflows.
+ **Review and Approval** — Draft ontologies must be reviewed and promoted using a **customer-defined approval process**. Approval workflows may include:
  + **Human approvals** — Requiring a specified number of ontology engineers, domain experts, or data stewards to review and approve changes via Ontology Engineering UIs, Git pull requests, or workflow management systems (ServiceNow)
  + **Automated evaluation techniques** — **LLM as a Judge** patterns where foundation models assess ontology quality, completeness, consistency, and alignment with business requirements before approval
  + **Reasoning validation** — ELK or HermiT reasoners validate consistency and detect unsatisfiable classes before promotion
  + **Coverage metrics** — Automated checks ensure the ontology covers a minimum percentage of catalog entities and relationships
  + **R2RML validation** — Test queries validate that R2RML mappings produce correct RDF output and that the VKG Service can successfully translate SPARQL queries to SQL
+ **Versioning** — Each approved ontology is assigned a semantic version (e.g., `v2.0`) and stored in a versioned named graph. S3 Versioned Buckets or Git repositories maintain version history with rollback capabilities. Neptune named graphs enable side-by-side deployment of ontology versions for A/B testing or gradual migration.
+ **Promotion to Published** — Once approved, the ontology is promoted from draft to published status, triggering updates to the VKG Service (R2RML mappings), Reasoning Service (ontology reloads), and downstream consumers. Neptune DB Streams emit events for the newly promoted ontology, notifying subscribers.

### Ontology Induction Strategies
<a name="ontology-induction-strategies.a321cb3a-9888-5e68-b1bb-3b0012b17ba2"></a>

|
|
| Strategy | Data Sources | Key Techniques |
| --- |--- |--- |
| **Bottom-Up (Catalog-Driven)** | SageMaker Catalog, Glue Data Catalog, DataZone | Schema analysis, foreign key inference, lineage analysis, statistical profiling, R2RML mapping generation |
| **Data-Grounded Validation** | VKG Service (Neptune \+ Data Layer sample data) | Sample data analysis, schema drift detection, relationship validation, value range inspection, R2RML mapping validation |
| **Top-Down (Reference Ontologies)** | SNOMED CT, FIBO, BFO, DOLCE, existing ontologies in Neptune | Ontology alignment, semantic similarity (OWL2Vec\*, RDF2Vec), concept mapping |
| **LLM-Guided (Specifications)** | Requirements docs, interviews, business glossaries | NER, relationship extraction, constraint generation via Bedrock, R2RML mapping refinement |
| **Hybrid** | All of the above | Reconciliation, consensus-based entity resolution, provenance tracking, OBDA pattern consistency |

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.372e005f-52e9-5987-b1a4-89e19dce7fc0"></a>
+ **VKG Service Integration** — By calling the VKG Service (Step 4), the Ontology Induction Service gains access to both existing ontologies and live/sample data from across the enterprise without needing direct connections to Neptune or Data Layer sources. This abstraction simplifies the induction architecture and ensures ontology induction uses the same federated query capabilities as agents and applications. The service also retrieves existing R2RML mappings to ensure consistency with established OBDA patterns.
+ **Scalability** — ECS tasks auto-scale based on the number of data sources and ontology complexity. Bedrock API calls and vector similarity computations are parallelized across multiple catalog entities for efficient processing. VKG Service queries are optimized to sample representative data without overwhelming source systems.
+ **Quality Assurance** — Induced ontologies are validated against consistency checks (ELK reasoner), completeness metrics (coverage vs. catalog), alignment with existing ontologies, and sample data patterns before being promoted to published. R2RML mappings are tested to ensure correct RDF output and successful SPARQL-to-SQL translation.
+ **Human-in-the-Loop** — Ontology engineers review induced ontologies via Ontology Engineering UIs, accepting, rejecting, or refining suggested classes, properties, and R2RML mappings before final approval. Draft mode ensures systems are not impacted by unvalidated ontologies.
+ **Versioning & Governance** — Each induction run produces a versioned ontology stored in a named graph with draft/published status flags. Approval workflows (human \+ automated) gate promotion to published. S3 Versioned Buckets or Git repositories provide version control and rollback capabilities.
+ **Observability** — OpenTelemetry traces propagate from REST API → ECS → Catalog queries → VKG Service queries → Bedrock invocations → Neptune write, providing end-to-end visibility via AWS X-Ray. CloudWatch Logs capture entity counts, LLM prompts/responses, vector similarity scores, sample data statistics, R2RML mapping generation details, and induction confidence scores.
+ **Cost Optimization** — ECS Fargate Spot reduces compute costs. Bedrock pay-per-token pricing is optimized by batching catalog metadata into structured prompts. Glue Catalog and SageMaker Catalog API calls are cached to minimize redundant queries. VKG Service sampling queries are limited to representative subsets of data. Vector similarity computations are performed only when aligning with reference ontologies.

This Ontology Induction architecture enables **rapid, automated, data-grounded ontology bootstrapping** from existing data infrastructure — reducing the time and effort required to build semantic foundations while ensuring alignment with organizational data assets, existing semantic patterns, actual data distributions, industry standards, OBDA best practices, and governance requirements. The draft-review-promote workflow ensures quality and control while accelerating time-to-value.
