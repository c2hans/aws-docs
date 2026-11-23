---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/knowledge-layer.html
---

# Knowledge Layer

## Knowledge Layer Overview
<a name="knowledge-layer-overview.31dc1c5e-83a4-516f-b223-80cb308111dc"></a>

The **Knowledge Layer** serves as the semantic intelligence foundation of the architecture, enabling unified querying across heterogeneous data sources through a Virtual Knowledge Graph (VKG) approach. At its core, the layer exposes SPARQL query capabilities that allow applications, agents, and users to interact with knowledge as a unified graph — regardless of whether that knowledge resides in a dedicated graph database, relational databases, data warehouses, or data lakes. The VKG Service, deployed on **Amazon ECS** with **Fargate** or **EC2** instances, orchestrates query translation and federation, enabling seamless access to both materialized semantic knowledge and virtualized data layer sources within a single SPARQL query. [**Ontop**](https://github.com/ontop/ontop) is a strong choice for implementing the VKG Service — it's an open-source platform purpose-built for OBDA (Ontology-Based Data Access) that translates SPARQL queries over ontology-defined knowledge graphs into optimized SQL executed directly against relational sources, using R2RML mappings and lightweight OWL ontologies, with no data duplication required.

**Amazon Neptune Database** serves as the persistent graph store for knowledge that cannot or should not remain in the data layer, including entities, relationships, and propositions extracted from unstructured documents (PDFs, images, reports) and mapped to ontology classes and properties via the Information Extraction pipeline, deduction results that infer new relationships or properties through symbolic reasoning, cross-domain associations linking entities across disparate data sources, and enriched semantic metadata. Together, these represent the materialized A-Box (instance data) of the knowledge graph, capturing both directly extracted and logically derived facts as first-class graph citizens. Neptune's native RDF and SPARQL support makes it the natural home for the T-Box (ontology/schema) and this materialized A-Box, which require graph-native reasoning and traversal. Neptune DB Streams provide near real-time change data capture for all create, update, and delete operations, enabling event-driven architectures where downstream processes, such as the Symbolic Reasoning Service, can react immediately to knowledge graph mutations, maintaining consistency and triggering inference workflows without polling.

The VKG architecture's key strength lies in its ability to query the **Semantic Layer Graph Database** (Neptune), **relational databases and data warehouses** (via JDBC-connected sources like Snowflake, Redshift, Athena), and **data lakes** (Iceberg/Parquet on S3) — either independently or federated together in a single query. This eliminates data duplication while preserving the semantic richness of the knowledge graph, allowing the Knowledge Layer to serve as a true abstraction over the enterprise's distributed data landscape. Ontology-driven mappings (R2RML) define how relational and tabular data sources are virtualized as RDF, enabling SPARQL queries to transparently span both materialized and virtual knowledge without requiring applications to understand the underlying physical storage topology.

The **Symbolic Reasoning Service** maintains knowledge graph consistency, validates data quality, and derives new knowledge automatically through event-driven workflows triggered by Neptune DB Streams. Deployed on Amazon ECS, the service implements a modular ensemble architecture supporting multiple reasoning engines including **ELK** (lightweight OWL reasoning), **HermiT** (full OWL 2 DL expressivity), **SHACL** validators (constraint enforcement), and **SWRL** engines (rule-based inference). When graph mutations occur, the Symbolic Reasoning Service identifies applicable rules, retrieves necessary sub-graphs from the VKG Service (federating across Neptune and Data Layer sources), performs reasoning, and persists inferred triples, validation results, and consistency flags back to Neptune with full provenance metadata. This closed-loop architecture ensures that ontology changes, new assertions, and constraint violations are automatically validated and that inferred knowledge is materialized in near real-time, supporting autonomous agents with verified, explainable knowledge.

The Knowledge Layer includes a **Metric Store** — a governed registry of reusable, ontology-grounded metric definitions persisted alongside the T-Box, R2RML mappings, and SHACL constraints in the Semantic Layer Graph Database.

**Metric Definition**: A reusable, pre-defined calculation bound to an ontology class and its datatype properties. Each definition specifies an aggregation function, the properties involved, optional filters, and a pre-compiled SPARQL/SQL expression resolved deterministically at query time — no LLM required.

```
ex:ProcessingTime a ex:MetricDefinition ;
    rdfs:label "Processing Time" ;
    ex:metricForClass ex:Claim ;
    ex:aggregationFunction "AVG" ;
    ex:metricExpression "AVG(DATEDIFF('day', ?submissionDate, ?approvalDate))" ;
    ex:metricUnit "days" .
```

**Key properties:**
+ **Ontology-grounded** — metrics reference classes and properties, not physical tables, enabling resolution across federated sources via the VKG
+ **Deterministic** — pre-compiled expressions are injected at query time without LLM generation, supporting ACE principles (Accuracy, Consistency, Explainability)
+ **Governed** — metric definitions follow the same draft → review → publish lifecycle as ontology versions, validated by SHACL shapes
+ **Agent-discoverable** — the Q&A Agent resolves recognized metric names directly from the Metric Store during query generation, bypassing LLM-based calculation synthesis

## Virtual Knowledge Graph (VKG) Query
<a name="virtual-knowledge-graph--vkg--query.87b30d47-142f-5b7b-8c00-397554b1c889"></a>

### Data Flow - Virtual Knowledge Graph (VKG) Query
<a name="data-flow---virtual-knowledge-graph--vkg--query.81e229d4-f625-5bfa-918d-d664591de5bb"></a>

**1. SPARQL Client → Virtual Knowledge Graph Service** A SPARQL Client (application, agent, or user interface) submits a SPARQL query to the **Virtual Knowledge Graph (VKG) Service** deployed on **Amazon ECS** within the VPC. The VKG Service endpoint accepts the query via HTTPS, receiving the JWT/OIDC bearer token propagated by the AgentCore Gateway. The VKG Service extracts user identity (`sub`), authorization groups (`groups`), and agent identity (`act`) from the token for row-level security enforcement and audit logging. The VKG Service (implemented using Ontop or similar OBDA platform) parses the SPARQL query and consults the loaded ontology (T-Box) and R2RML mappings to determine the query execution plan.

**2. VKG Service Query Planning & Federation** The VKG Service analyzes the SPARQL query structure and determines which data sources are required to satisfy the query — materialized knowledge in **Neptune DB** (Step 3), virtualized data from relational/data warehouse sources (Step 4), or a federated combination of both. For triple patterns that correspond to ontology-mapped relational tables, the VKG Service translates the SPARQL query into optimized SQL using the R2RML mappings. For triple patterns representing deduced knowledge, cross-domain relationships, or ontology axioms, the query is routed to Neptune DB via SPARQL endpoint. The VKG Service applies query optimization techniques including **predicate pushdown**, **join reordering**, and **filter propagation** to achieve locality optimization and minimize data transfer from sources.

**3. VKG Service → Neptune DB (Semantic Layer Graph Database)** For SPARQL query fragments targeting materialized knowledge, the VKG Service issues a SPARQL query to **Amazon Neptune DB** via the Neptune SPARQL endpoint. Neptune executes the query against the stored RDF graph, which includes the T-Box (ontology/schema), materialized A-Box (instance data), deduction results from reasoning workflows, and cross-domain entity linkages. Neptune enforces **access control policies** at query execution time, ensuring users only retrieve authorized data. Neptune returns RDF bindings (for SELECT queries) or RDF graphs (for CONSTRUCT/DESCRIBE queries) to the VKG Service. Neptune's native support for SPARQL 1.1, named graphs, and OWL inference ensures semantic fidelity in query results.

**4. VKG Service → Data Layer (Virtualized Query Execution via JDBC)** For SPARQL query fragments mapped to relational or data warehouse sources, the VKG Service translates the SPARQL into native SQL and dispatches queries to the appropriate [**Data Layer**](data-layer.md) sources via **JDBC connections**. The VKG Service retrieves tabular result sets from these sources, converts rows and columns to RDF bindings using the R2RML mapping definitions, and integrates them with results from Neptune (Step 3) if the query is federated. SQL queries are executed directly against the source systems — no data is duplicated or moved into Neptune unless explicitly materialized by a separate ETL or reasoning process.

**5. Data Layer Sources Execute SQL Queries** Each data source in the **Data Layer** executes the translated SQL query against its native storage. Supported sources include:
+ **Amazon Athena** — queries Iceberg or Parquet tables on **S3 Tables** using Presto/Trino query engine, with federated access to **DynamoDB** and other AWS databases
+ **Amazon Redshift** — executes queries against its columnar data warehouse
+ **Snowflake** — executes queries within its cloud platform
+ **Databricks** — executes queries within its lakehouse platform

VPC peering or AWS PrivateLink ensures secure connectivity back to the VKG Service. Query results are returned as standard JDBC result sets, which the VKG Service consumes, transforms to RDF using R2RML mappings, and merges with Neptune-sourced results for the final SPARQL response.

**6. VKG Service Returns Unified SPARQL Results to Client** The VKG Service merges results from Neptune (Step 3) and Data Layer sources (Steps 4–5), applies any final SPARQL query operators (e.g., UNION, OPTIONAL, FILTER), and returns a unified SPARQL result set to the SPARQL Client. Results are serialized in the requested format — SPARQL JSON, XML, or Turtle — based on the client's `Accept` header. The VKG Service caches query plans and frequently accessed R2RML mappings to improve performance for repeated queries. OpenTelemetry traces are emitted across all steps, capturing query latency, source attribution, and row counts for observability.

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.ce37a8b0-09eb-5488-b3df-a0d1c3842db0"></a>
+ **Authentication & Authorization:**

  *Inbound Authentication* - JWT/OIDC bearer tokens authenticate inbound SPARQL queries. The AgentCore Gateway validates tokens before forwarding to the VKG Service. Required JWT claims: `sub` (user identity), `groups` (authorization), `act` (agent identity).

  *Service-Level Authorization* - IAM execution roles for the ECS tasks grant least-privilege access to Neptune, Athena, Redshift, and Secrets Manager (for JDBC credentials).
+ **Row-Level & Column-Level Security** — The VKG Service enforces row-level security (RLS) and column-level security (CLS) across all federated data sources, adapting the enforcement mechanism to the capabilities of each source:
  + **Neptune DB (Semantic Layer Graph Database)** — The VKG Service enforces RLS through SPARQL query rewriting, injecting FILTER clauses or named graph restrictions based on the user's `groups` claim and authorization policies (OPA, Lake Formation, or ontology-defined access rules). Data masking and redaction of sensitive attributes (PII, PHI) are applied based on user roles.
  + **AWS Data Layer Sources (Amazon Athena, Amazon Redshift)** — The VKG Service leverages AWS Trusted Identity Propagation (TIP) via IAM Identity Center, propagating the end-user's IdP identity to enable Lake Formation fine-grained access controls and native RLS/CLS at the source. This approach delegates security enforcement to the data platform, ensuring that access policies are evaluated natively and consistently with the organization's Lake Formation governance model.
  + **Non-AWS Data Layer Sources with Native Security (e.g., Snowflake Secure Views)** — For data platforms that support session-based or user-context security, the VKG Service establishes per-user sessions using OAuth token propagation or session-level user context variables. The data platform enforces RLS/CLS natively — for example, Snowflake Secure Views evaluate row-filtering and column-masking policies based on the session's user context, ensuring that security enforcement occurs within the source system without exposing underlying table structures.
  + **Data Layer Sources without Native Identity Propagation** — For sources that do not support identity propagation or session-based security, the VKG Service falls back to query rewriting — adding one or more predicates to restrict row selection and/or limiting column projection in the translated SQL query based on the user's authorization context. This approach ensures consistent RLS/CLS enforcement regardless of the source system's native security capabilities.

  Authorization policies are defined centrally — in the ontology, AWS Lake Formation, OPA, or a combination — and the VKG Service selects the appropriate enforcement mechanism at query planning time based on the target data source's capabilities. This layered approach ensures that security is enforced as close to the data as possible, leveraging native platform controls where available and falling back to query-level enforcement where necessary.
+ **Network Security:** VKG Service runs within a **VPC** with private subnets. Neptune is VPC-native. Data Layer sources are accessed via VPC endpoints (Athena, Redshift), VPC peering, or AWS PrivateLink (Snowflake, Databricks).
+ **Observability:** OpenTelemetry instrumentation emits traces, metrics, and logs to **AWS X-Ray** and **Amazon CloudWatch**. Traces include query parse time, Neptune query latency, SQL execution time per source, and total federation overhead.
+ **Scalability:** ECS with **Fargate** auto-scales based on query load. Neptune supports read replicas for query scalability. Data Layer sources (Athena, Redshift, Snowflake, Databricks) scale independently.
+ **Event-Driven Updates:** **Neptune DB Streams** emit change data capture events (create, update, delete) to downstream consumers such as the **Symbolic Reasoning Service**, enabling near real-time inference and knowledge graph consistency without polling.

## Event-Driven Architecture
<a name="event-driven-architecture.cfab81cd-184a-5b91-9013-d380da2c1f5f"></a>

### Data Flow - Event-Driven Architecture
<a name="data-flow---event-driven-architecture.74328bd2-a651-53d8-b8a1-0405af537138"></a>

**1. SPARQL Client → Virtual Knowledge Graph Service (Data Manipulation Query)** A SPARQL Client submits a SPARQL data manipulation query to the **Virtual Knowledge Graph (VKG) Service** running on **Amazon ECS** within the VPC. This could be an INSERT DATA, DELETE DATA, or CONSTRUCT query — including construct queries generated by reasoning processes that result in new knowledge or deductions. For example, a reasoning workflow may infer new relationships between entities based on ontology axioms and assert them as new triples. The VKG Service authenticates the request using JWT/OIDC bearer tokens propagated by the AgentCore Gateway and validates the SPARQL UPDATE syntax.

**2. VKG Service → Neptune DB (Semantic Layer Graph Database)** The VKG Service routes the SPARQL data manipulation query to **Amazon Neptune DB** via the Neptune SPARQL Update endpoint. Neptune persists the changes to the RDF graph — inserting new triples (CREATE), modifying existing statements (UPDATE), or removing triples (DELETE). Neptune enforces **access control policies** at write time, ensuring the requesting principal has authorization to modify the targeted named graphs or triples. The update is committed to Neptune's ACID-compliant transaction log, ensuring durability and consistency. Changes may target the **T-Box** (ontology/schema modifications) or **A-Box** (instance data updates, deduced relationships, cross-domain entity linkages).

**3. Neptune DB → Neptune DB Streams → AWS Lambda (Change Data Capture)** Upon successful commit of the SPARQL UPDATE, **Neptune DB Streams** automatically emit change data capture (CDC) events in near real-time. Each stream event captures the mutation type (`CREATE`, `UPDATE`, `DELETE`), the affected triples (subject, predicate, object), the named graph IRI, timestamp, and transaction metadata. Neptune DB Streams provide an ordered, durable event log with configurable retention (up to 7 days). An **AWS Lambda function** subscribes to the Neptune DB Streams and is invoked automatically as new change events arrive. The Lambda function acts as the stream event handler, deserializing the event payload and routing it to downstream subscribers based on event type and affected knowledge domain.

**4. AWS Lambda → Amazon SNS (Event Publication to Subscribers)** The Lambda function publishes the processed Neptune DB Streams event to **Amazon SNS** topics. SNS acts as a pub/sub messaging layer, enabling fan-out to multiple downstream subscribers. Subscribers receive CUD events and handle them appropriately based on their role:
+ **Symbolic Reasoning Service** — Processes updates to the **T-Box** (ontology changes) and triggers respective reasoners to validate changes. For example, **ELK** (EL\+\+ reasoner) validates ontology consistency, computes class hierarchies, and detects unsatisfiable classes. Changes to the **A-Box** (instance data) trigger data validation and reasoning workflows using **SHACL** (constraint validation), **SWRL** (rule-based inference), and **SHACL\+SPARQL** (complex validation rules). The Symbolic Reasoning Service may generate new CONSTRUCT queries that loop back to Step 1, creating a feedback cycle for iterative knowledge enrichment.
+ **Search Index Service** — Updates vector embeddings or full-text search indexes in **Amazon OpenSearch Service** to reflect knowledge graph changes, ensuring semantic search remains current.
+ **Ontology Engineering UI** — Notifies knowledge engineers of schema or mapping changes, enabling collaborative ontology management.
+ **Agent Orchestration Platform (AgentCore)** — Signals agents to refresh context, invalidate cached knowledge, or re-evaluate reasoning chains affected by the knowledge graph mutation.
+ **Audit & Governance Services** — Logs knowledge graph mutations for compliance, lineage tracking, and explainability requirements.

SNS supports both in-account subscribers (Lambda, SQS, EventBridge) and cross-account or external subscribers (HTTPS webhooks, email) for enterprise-wide event distribution. Message filtering policies can route events based on metadata attributes (e.g., `eventType`, `namedGraph`, `ontologyId`).

## Event Types & Symbolic Reasoning Triggers
<a name="event-types-9999999999999999amp--symbolic-reasoning-triggers.64331e6f-8602-5295-9da2-a852fa44a02d"></a>

|
|
| Event Type | Description | T-Box Reasoning Actions | A-Box Reasoning Actions |
| --- |--- |--- |--- |
| **CREATE** | New triples inserted into the knowledge graph | Validate ontology consistency (ELK); recompute class hierarchies | Run SHACL validation on new instances; trigger SWRL rules for new inferences |
| **UPDATE** | Existing triples modified (delete \+ insert) | Detect breaking changes to ontology axioms; revalidate dependent mappings | Revalidate affected instances against SHACL constraints; recompute SWRL-based deductions |
| **DELETE** | Triples removed from the knowledge graph | Check for orphaned subclasses or properties; validate ontology integrity | Cascade delete dependent inferences; remove invalidated SHACL validation results |

**Reasoning Outcome Handling** - All reasoning actions produce one or more of the following outcomes, persisted to Neptune with full provenance metadata: (1) *new inferred triples* stored in dedicated named graphs, distinguishing inferred from asserted knowledge; (2) *SHACL validation reports* with severity levels (violation, warning, info), focus nodes, and remediation suggestions; (3) *consistency flags* annotating axioms or instances with their validation status; (4) *invalidation signals* sent via SNS to AgentCore (triggering cache refresh and reasoning chain re-evaluation), Search Index Service (updating embeddings), and Ontology Engineering UI (notifying knowledge engineers). All outcomes emit new CDC events via Neptune DB Streams, enabling cascading reasoning workflows and maintaining a complete audit trail for compliance and explainability.

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.198c004b-462c-5ceb-a03d-5d380976a32b"></a>
+ **Event Ordering:** Neptune DB Streams guarantee ordered delivery within a shard. Lambda processes events in order to maintain consistency across reasoning workflows.
+ **Idempotency:** Lambda functions implement idempotency keys (using transaction ID from Neptune streams) to safely handle retries without duplicate processing.
+ **Error Handling:** Lambda dead-letter queues (DLQ) capture failed events for later reprocessing. CloudWatch Alarms monitor DLQ depth and Lambda error rates.
+ **Security:** Neptune DB Streams are VPC-native. Lambda functions run within the VPC with private subnet access to Neptune. SNS topics enforce IAM-based publish/subscribe authorization.
+ **Observability:** OpenTelemetry traces propagate from Neptune write → Stream event → Lambda processing → SNS publish → Symbolic Reasoning Service invocation, providing end-to-end visibility via AWS X-Ray. CloudWatch Logs capture detailed event payloads, reasoning outcomes, and validation results.
+ **Scalability:** Lambda auto-scales based on Neptune DB Streams throughput. SNS provides virtually unlimited fan-out to subscribers without backpressure on the event source. Symbolic Reasoning Service can scale horizontally to process multiple reasoning workflows in parallel.

This architecture enables **near real-time, event-driven knowledge graph workflows** — ensuring that reasoning processes, validation engines, search indexes, and downstream agents react immediately to knowledge mutations without polling Neptune. The pattern is particularly valuable for maintaining consistency in federated knowledge graphs where materialized knowledge, deduced relationships, and ontology changes must trigger automated reasoning and validation workflows to preserve semantic integrity.

## Symbolic Reasoning
<a name="symbolic-reasoning.3468e5f6-48ef-52a2-9eb3-cddaaac4c634"></a>

### Data Flow — Knowledge Layer Symbolic Reasoning
<a name="data-flow---knowledge-layer-symbolic-reasoning.6d996161-0088-5922-9f90-a72478e10423"></a>

**1. Amazon SNS → Amazon SQS (Graph Mutation Event Trigger)** The **Semantic Layer Graph Database** (Neptune DB) emits change data capture events via **Neptune DB Streams** for all knowledge graph mutations — create, update, and delete operations on ontologies (T-Box), instance data (A-Box), or relationships. These mutation events are published to an **Amazon SNS topic** configured for reasoning triggers. The SNS topic implements a fan-out pattern, publishing to an **Amazon SQS queue** dedicated to the Symbolic Reasoning Service. This event-driven architecture ensures that ontology changes, new assertions, or data deletions automatically trigger reasoning workflows without manual intervention. The SQS message contains the mutation type (CREATE, UPDATE, DELETE), affected triples (subject, predicate, object), named graph IRI, transaction metadata, and references to the modified entities.

**2. Amazon SQS → AWS Lambda (Reasoning Orchestrator)** An **AWS Lambda function** polls the SQS queue and is triggered when graph mutation events arrive. The Lambda function acts as the reasoning orchestration layer, analyzing the event payload to determine which reasoning workflows to invoke based on the type and scope of change:
+ **T-Box changes** (ontology modifications) → trigger consistency checking and class hierarchy recomputation
+ **A-Box changes** (instance data updates) → trigger constraint validation and rule-based inference
+ **Bulk updates** → batch multiple events together for efficient reasoning

The Lambda function prepares the invocation payload for the Symbolic Reasoning Service, including references to affected named graphs, ontology versions, and reasoning policies to apply. The orchestrator invokes the Reasoning Service asynchronously, enabling parallel processing of independent reasoning tasks.

**3. AWS Lambda → Symbolic Reasoning Service (Amazon ECS)** The Lambda function invokes the **Symbolic Reasoning Service** deployed as containerized tasks on **Amazon ECS** (with **Fargate** or **EC2** instances). The Reasoning Service implements a **modular, ensemble architecture** supporting multiple reasoning engines and techniques:
+ **Semantic Reasoners** — **ELK** (EL\+\+ reasoner for lightweight OWL reasoning), **HermiT** (OWL 2 DL reasoner for full expressivity), or other open-source implementations for ontology consistency checking, class hierarchy computation, and detecting unsatisfiable classes
+ **Constraint Validators** — **SHACL** validators for data quality and constraint enforcement
+ **Rule Engines** — **SWRL** engines for rule-based inference (e.g., "if X submittedBy Y and Y employedBy Z, then X affiliatedWith Z")
+ **Hybrid Validators** — **SHACL\+SPARQL** for complex validation rules combining constraints with federated queries

**Ontology and Rules Management** — The Symbolic Reasoning Service maintains **near real-time synchronization** with ontologies and rules stored in S3 Versioned Buckets or Git repositories. The service subscribes to ontology change events (via SNS/SQS) and automatically reloads updated ontologies and rule sets. This mechanism ensures that reasoning always operates against the current ontology version without manual intervention.

**Rule Set Loading and Planning** — Based on the graph mutation event details, the Symbolic Reasoning Service identifies the **related rules that need to be evaluated**. For example, if a new claim instance is asserted, only rules applicable to claims (e.g., eligibility validation, fraud detection rules) are loaded. The service then **assembles a reasoning plan** to determine what data is necessary to satisfy the rule set:
+ Identifies required sub-graphs (e.g., claim, patient, provider, policy entities and their relationships)
+ Determines whether data is materialized in Neptune or virtualized in the Data Layer
+ Optimizes query execution order to minimize data retrieval

**4. Symbolic Reasoning Service → Virtual Knowledge Graph (VKG) Service** The Symbolic Reasoning Service sends **requests to retrieve necessary sub-graphs** to the **Virtual Knowledge Graph (VKG) Service** to satisfy the rule set. The VKG Service federates queries across:
+ **Materialized knowledge** in the Semantic Layer Graph Database (Neptune DB)
+ **Virtualized data** from the Data Layer (relational databases, data warehouses) via R2RML mappings

The VKG Service translates SPARQL queries into optimized SQL (for virtualized sources) and native SPARQL (for Neptune), returning unified RDF bindings to the Symbolic Reasoning Service. This enables reasoning over both the Semantic Layer and live data from source systems without requiring full materialization.

**Once all sub-graphs have been retrieved**, the Symbolic Reasoning Service performs reasoning using the loaded rule set and selected reasoning engines:
+ **Consistency checking** — Validates that new assertions do not violate ontology axioms
+ **Inference** — Derives new triples based on OWL axioms, SWRL rules, or property chains
+ **Constraint validation** — Checks SHACL shapes to detect violations
+ **Conflict detection** — Identifies contradictory assertions or constraint violations

**5. Symbolic Reasoning Service → Neptune DB (Semantic Layer Graph Database)** Any reasoning that **results in updates** (e.g., new knowledge via deductions, inferred relationships, validation results) to the Semantic Layer Graph Database are **persisted and reflected** in **Neptune DB**. The Symbolic Reasoning Service writes:
+ **Inferred triples** — New relationships or properties derived through reasoning (e.g., transitive closure, property chains, SWRL rule conclusions), stored in dedicated named graphs to distinguish inferred knowledge from asserted knowledge
+ **Validation results** — SHACL validation reports indicating constraint violations, with severity levels (violation, warning, info), focus nodes, constraint paths, and remediation suggestions
+ **Consistency flags** — Annotations on ontology axioms or instances indicating consistency status, unsatisfiable classes detected by semantic reasoners, or conflicts requiring resolution
+ **Reasoning provenance** — Metadata linking inferred triples to the reasoning engines used, source axioms or rules that triggered the inference, timestamps, and confidence scores

Neptune DB Streams then emit events for these newly asserted triples, potentially triggering additional downstream processing (e.g., notifying agents, updating search indexes, triggering cascading reasoning workflows). This creates a **closed-loop, event-driven reasoning architecture** where reasoning results can trigger further reasoning or validation cycles.

## Reasoning Ensemble — Modular Architecture
<a name="reasoning-ensemble---modular-architecture.b39efcd3-802a-579f-a43c-52727d26d4c2"></a>

|
|
| Reasoning Engine | Purpose | Use Cases |
| --- |--- |--- |
| **ELK** (EL\+\+ reasoner) | Lightweight OWL reasoning, class hierarchy computation | Ontology consistency checking, subsumption inference |
| **HermiT** (OWL 2 DL) | Full OWL 2 expressivity, complex reasoning | Advanced ontology validation, complex class expressions |
| **SHACL Validator** | Constraint validation against shapes | Data quality enforcement, business rule validation |
| **SWRL Engine** | Rule-based inference | Domain-specific rules (eligibility, fraud detection, compliance) |
| **SHACL\+SPARQL** | Hybrid constraint validation | Complex validation rules spanning multiple entities |

*Note: These are open-source implementation options. The modular architecture allows selection and combination of reasoning engines based on use case requirements.*

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.511a348d-1acb-57da-9243-757a849b91ee"></a>
+ **Event-Driven Architecture** — Neptune DB Streams and SNS/SQS fan-out enable near real-time reasoning triggered by knowledge graph mutations, eliminating the need for batch processing or polling.
+ **Scalability** — SQS and Lambda enable elastic scaling of reasoning orchestration. ECS tasks auto-scale based on reasoning workload complexity and queue depth. Reasoning can be parallelized across independent sub-graphs.
+ **Near Real-Time Ontology Updates** — The Symbolic Reasoning Service subscribes to ontology change events and automatically reloads updated ontologies and rule sets, ensuring reasoning always operates against the current version.
+ **Federated Reasoning** — VKG Service integration enables reasoning over both materialized (Neptune) and virtualized (Data Layer) knowledge without data duplication, supporting validation rules that reference live source system data.
+ **Reasoning Isolation** — The Symbolic Reasoning Service runs with read-only access to Neptune for input and write-only access for output, preventing unvalidated modifications during reasoning.
+ **Observability** — OpenTelemetry traces propagate from SNS → SQS → Lambda → Symbolic Reasoning Service → VKG Service → Neptune write, providing end-to-end visibility via **AWS X-Ray**. CloudWatch Logs capture reasoning results, inference counts, validation violations, and processing errors. CloudWatch Metrics track reasoning latency, rule evaluation time, and sub-graph retrieval performance.
+ **Cost Optimization** — ECS Fargate Spot reduces compute costs for reasoning workloads. Reasoning plan optimization minimizes data retrieval from VKG Service. Incremental reasoning (processing only changed sub-graphs) reduces computational overhead.
+ **Provenance & Explainability** — All inferred knowledge includes metadata about the reasoning process (engine used, source rules, axioms), enabling explainability and debugging for agentic AI applications.

This Knowledge Layer Symbolic Reasoning architecture enables **continuous, event-driven reasoning** that maintains knowledge graph consistency, validates data quality, and derives new knowledge automatically as the Semantic Layer evolves — supporting autonomous agents with verified, explainable knowledge.
