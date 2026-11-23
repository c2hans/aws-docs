---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/orchestration.html
---

# Orchestration Layer

## Orchestration Layer Overview
<a name="orchestration-layer-overview.9f7db377-6083-5097-9a97-1dadfdda836b"></a>

The **Orchestration Layer** serves as the agentic intelligence hub of the architecture, coordinating autonomous agents that leverage the semantic foundations provided by the Knowledge and Intelligence Layers to deliver business value through automated reasoning, knowledge discovery, and human-in-the-loop workflows. While these agents are the primary consumers of the Orchestration Layer, the same information and capabilities they utilize are accessible to customers and other agents through the Semantic Layer's unified interfaces — ensuring that semantic knowledge, reasoning capabilities, and contextual insights are available enterprise-wide, not siloed within individual agent implementations.

The **Question & Answer (Q&A) Agent** responds to queries from the Interface Layer (primarily via MCP Server, with REST API support as well) by processing `ask` requests that require semantic understanding and knowledge retrieval. The Q&A Agent leverages the VKG Service to execute federated SPARQL queries across the Semantic Layer Graph Database and virtualized Data Layer sources, retrieves relevant document chunks and concepts from the Lexical Graph Database via GraphRAG techniques, and synthesizes responses grounded in ontology-defined knowledge with full provenance. The agent maintains short-term memory via context graphs (managed by the Intelligence Layer) that capture query history, retrieved entities, and inferred user intent, enabling multi-turn conversations with semantic continuity. Responses include citations back to source documents, knowledge graph entities, and reasoning steps, ensuring explainability and trust.

The **Business Elicitation Agent** operates as an event-driven knowledge discovery system that continuously monitors the semantic landscape to identify gaps, inconsistencies, and opportunities for human expert input. The agent subscribes to **Graph Mutation Events** (via Neptune DB Streams), **Document Ingest Pipeline** events (via SNS/SQS), and **Ontology Induction** workflows to analyze newly asserted knowledge, extracted entities, and induced ontology elements. Using LLM-based analysis via Amazon Bedrock, the agent assesses whether new knowledge aligns with existing ontologies, identifies ambiguous or conflicting assertions, and detects missing business context (e.g., undefined relationships, incomplete constraints, or entities lacking business glossary mappings). When **Human-in-the-Loop (HITL)** intervention is needed — such as resolving semantic ambiguities, validating high-impact ontology changes, or capturing domain expert knowledge for underspecified concepts — the agent triggers approval workflows via internal systems or third-party tools, notifying ontology engineers, data stewards, or domain experts with contextual information and recommended actions. This proactive elicitation ensures that the semantic layer evolves in alignment with business reality and domain expertise.

The **Ontology Maintenance / Entity Resolution Agent** ensures semantic consistency and quality across the Semantic Layer by identifying and resolving overlaps, discrepancies, and duplications in ontology structures and materialized knowledge. The agent analyzes **ontology classes, properties, constraints, and rules** to detect redundant or conflicting definitions (e.g., two classes representing the same concept with different names, properties with overlapping semantics, or contradictory cardinality constraints). Using **vector-based similarity techniques** (OWL2Vec\*, RDF2Vec) and **LLM-based semantic analysis** via Amazon Bedrock, the agent computes similarity scores between ontology elements and proposes consolidation or alignment strategies. For **entity resolution**, the agent identifies similar or duplicate entities in the **Semantic Layer Graph Database** (Neptune DB) — such as multiple patient records representing the same individual, or claim instances with overlapping identifiers — and applies disambiguation rules, probabilistic matching, or LLM-based reasoning to merge or link entities with appropriate provenance. The agent has access to **Data Layer sources via the VKG Service**, enabling it to validate entity resolution decisions against source system data, detect schema drift, and ensure that ontology maintenance reflects the current state of enterprise data. Proposed changes are written to draft named graphs and subject to governance approval workflows before promotion to production, ensuring quality control and auditability.

## Orchestration Layer Agents
<a name="orchestration-layer-agents.992f13a6-0728-570d-93dc-f8dc99d08209"></a>

|
|
| Agent | Purpose | Key Capabilities |
| --- |--- |--- |
| **Question & Answer (Q&A) Agent** | Respond to semantic queries from Interface Layer | Federated SPARQL queries, GraphRAG retrieval, context graph management, provenance-based citations |
| **Business Elicitation Agent** | Proactive knowledge discovery and HITL workflow orchestration | Event-driven monitoring, gap analysis, ambiguity detection, workflow triggering |
| **Ontology Maintenance / Entity Resolution Agent** | Ensure semantic consistency and quality | Ontology overlap detection, entity disambiguation, similarity-based matching, VKG-based validation |

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.c3fcf45f-c97a-52d1-bdf8-e8ba136018d2"></a>
+ **Unified Access** — All capabilities utilized by Orchestration Layer agents (VKG Service queries, Symbolic Reasoning Service invocations, Intelligence Layer context graphs, Lexical Graph Database retrieval) are accessible to customers and other agents through the Semantic Layer's MCP Server and REST APIs, ensuring that semantic knowledge is not siloed within agent implementations.
+ **Event-Driven Architecture** — Agents subscribe to Neptune DB Streams, SNS/SQS topics, and workflow events to react in near real-time to knowledge graph mutations, document ingestion, and ontology changes, enabling proactive rather than reactive orchestration.
+ **Context-Aware Reasoning** — Agents leverage short-term memory and context graphs (Intelligence Layer) to maintain session state, track multi-turn interactions, and ground reasoning in specific conversational or workflow contexts.
+ **Human-in-the-Loop Integration** — Agents trigger approval workflows, notify domain experts, and surface recommendations via Ontology Engineering UIs, workflow management systems, or collaboration platforms when automated reasoning requires human validation or domain expertise.
+ **Provenance & Explainability** — All agent actions, reasoning steps, and knowledge assertions include provenance metadata linking back to source data, ontology axioms, and reasoning engines, enabling auditability and trust.
+ **Scalability** — Agents are deployed as containerized services on Amazon ECS (with Fargate or EC2 instances), auto-scaling based on workload complexity and event volume.
+ **Observability** — OpenTelemetry traces propagate across agent invocations, VKG Service queries, Symbolic Reasoning Service calls, and Intelligence Layer operations, providing end-to-end visibility via AWS X-Ray. CloudWatch Logs capture agent decisions, HITL triggers, entity resolution outcomes, and query results.

This Orchestration Layer enables **autonomous, knowledge-driven agents** that leverage the semantic foundations of the architecture to deliver business value through automated reasoning, proactive knowledge discovery, and human-expert collaboration — while ensuring that the same semantic capabilities are accessible enterprise-wide through unified interfaces.

## Question & Answer (Q&A) Agent
<a name="question-9999999999999999amp--answer--q9999999999999999amp-a--agent.1b5690cb-bff4-530d-847a-0834b43d7a86"></a>

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/images/guide-img/5cb278fc-4bbf-4e43-a830-4b4f72516d31/images/5fff3fe0-b83a-499c-b13f-7f1624adceed.png)

### Data Flow — Question & Answer (Q&A) Agent
<a name="data-flow---question-9999999999999999amp--answer--q9999999999999999amp-a--agent.59bd6ebd-82a5-5197-9ef5-84cae969f196"></a>

**1. MCP Interface → Question & Answer (Q&A) Agent (Bedrock AgentCore)** The **MCP Interface** provided by the Semantic Layer receives an `ask` tool invocation with the question in the request body. Additional metadata or directives (TBD) may be provided in the request to guide query processing, specify target ontologies, or set confidence thresholds. The **Question & Answer (Q&A) Agent** runs in **Amazon Bedrock AgentCore Runtime** and may be implemented in any AgentCore Runtime supported framework (e.g., **Strands**). The agent leverages **AgentCore identity** where appropriate for inbound and outbound authentication, receiving and validating the request. The agent applies **guardrails to enforce policy** — AWS provides **Amazon Bedrock Guardrails** as a guardrail capability, which may satisfy policy requirements such as identifying and redacting PII, detecting toxic content, or blocking sensitive topics. The request is authenticated via JWT/OIDC bearer tokens (or IAM SigV4 for AWS-native A2A callers at the Interface Layer). AgentCore validates the token, extracts the user identity (`sub`), authorization groups (`groups`), and agent identity (`act`) from the JWT claims, and provides session management, memory persistence (for context graphs), and secure execution isolation.

**2. Q&A Agent → AgentCore Gateway** The Q&A Agent calls the **AgentCore Gateway**, an **MCP Gateway that exposes REST APIs from services running in ECS as MCP tools**. The AgentCore Gateway acts as the service mesh and orchestration layer, providing:
+ **Service discovery and routing** — Routes requests to downstream services (Question Intent Classification, Query Execution Planning & Optimization, VKG Service, GraphRAG Service, Symbolic Reasoning Service)
+ **Authentication and authorization **— Validates and propagates JWT/OIDC tokens to downstream services, enforcing group-based authorization via the `groups` claim. IAM execution roles handle outbound calls to AWS services
+ **Protocol translation** — Converts agent-internal requests to service-specific protocols (REST, SPARQL, gRPC)
+ **Observability** — Emits OpenTelemetry traces for end-to-end request tracking

The Gateway receives the user's question and metadata from the Q&A Agent and prepares it for distribution to specialized processing services. **Steps 3-7 are MCP Tool invocations** orchestrated by the agent through the AgentCore Gateway.

**3. AgentCore Gateway → Question Intent Classification Service (Amazon ECS).** The AgentCore Gateway invokes the **Question Intent Classification Service** deployed on **Amazon ECS** (with Fargate or EC2 instances). The **Intent Classification component periodically retrieves the latest version of ontologies** from the Semantic Layer Graph Database (Neptune DB). The assumption is there may be **multiple ontologies** (e.g., different domains, cross-domain ontology enabled with upper ontology), and for some customers, **multiple versions of every ontology** may need to be supported. This request/response pattern may be replaced or augmented with an **event-driven pattern** (e.g., "Updates to Ontology version X, go retrieve") to ensure near real-time synchronization with ontology changes.

The Intent Classification Service determines:
+ **Type of question** — Retrieval (factual lookup), aggregation (count, sum, average), comparison, explanation, or validation
+ **Additional processing requirements** — Ranking, filtering, temporal constraints, reasoning, or document retrieval
+ **Ontology classes and relationships** — Identifies relevant classes (e.g., `Claim`, `Patient`, `Provider`) and relationships (data properties like `claimAmount`, object properties like `submittedBy`)
+ **Entity and relationship extraction** — Extracts and identifies entities and relationships **grounded by the provided ontologies**, linking natural language terms to ontology concepts
+ **Semantic similarity search** — Semantic similarity search of nodes and relationships may be appropriate here, using vector embeddings (OWL2Vec\*, RDF2Vec) to match question terms to ontology concepts when exact matches are not found
+ The service also recognizes metric names (e.g., "processing time") and maps them to `ex:MetricDefinition` instances in the Metric Store, returning intent category `METRIC_QUERY` with the resolved metric IRI and pre-compiled expression — bypassing LLM-generated calculation synthesis.

The service uses LLM-based classification via Amazon Bedrock (e.g., prompt engineering with few-shot examples, fine-tuned models) and returns:
+ Intent category (e.g., `ENTITY_LOOKUP`, `RELATIONSHIP_QUERY`, `AGGREGATION`, `VALIDATION`, `DOCUMENT_RETRIEVAL`)
+ Extracted entities and properties grounded in ontology
+ Suggested query strategy (SPARQL, vector search, hybrid, GraphRAG retrieval)
+ Confidence score

The intent classification output drives all downstream orchestration decisions. Based on the intent category and suggested query strategy, the Q&A Agent determines which subsequent steps to invoke: Query Execution Planning and VKG (for structured knowledge retrieval), GraphRAG (for document retrieval), Symbolic Reasoning (for inference and validation), or combinations thereof.

**4. AgentCore Gateway → Query Execution Planning & Optimization Service (Amazon ECS) **— Conditional, Invoked for Structured/Federated Queries. When the intent classification (Step 3) indicates structured knowledge retrieval, aggregation, relationship queries, or federated data access is required, the AgentCore Gateway invokes the Query Execution Planning & Optimization Service deployed on Amazon ECS. The **Execution Planning & Optimization component periodically retrieves the latest schema mapping for Ontologies** from the Semantic Layer. **Schema Mapping provides optimization-oriented information**, such as:
+ **Location and completeness of information by source** — Which data sources (Neptune, Snowflake, Redshift, S3) contain instances of specific ontology classes
+ **Data quality metrics** — Completeness, accuracy, and freshness scores for each source
+ **Cardinality and statistics** — Row counts, relationship cardinality, and data distributions, providing information regarding **how much data will need to be transmitted and processed**

For `METRIC_QUERY` intents, the service injects the metric's pre-compiled `ex:metricExpression` directly into the generated query, replacing LLM-generated aggregation logic. Standard optimizations apply around the injected fragment.

**Planning should consider what rules may apply** so dependent facts can be retrieved. For example, if a reasoning rule requires additional entities or relationships to evaluate, the planner ensures those sub-graphs are included in the query.

The **Execution Planning and Optimization component determines whether multiple steps are required**. It **creates an execution plan that executes in parallel or serially** based on an **optimizer algorithm that may incorporate statistics** (e.g., cardinality for ontology classes and relationships). **Cross-domain ontology questions most often require multiple steps to execute** — for example, a question spanning healthcare claims and provider networks may require separate queries to different data sources, followed by a join or federation step.

The service generates:
+ **SPARQL queries** — One or more SPARQL queries (SELECT, CONSTRUCT, ASK, DESCRIBE) aligned with the target ontology
+ **Federated query plan** — Identifies which data sources are required (Semantic Layer Graph Database in Neptune, Data Layer sources via VKG) and plans federated query execution
+ **GraphRAG retrieval plan** — If the intent classification (Step 3) indicates document retrieval is needed, specifies GraphRAG Service invocation parameters (similarity threshold, result limit, traversal depth)
+ **Query optimization** — Applies predicate pushdown, join reordering, filter propagation, and ontology-driven query rewriting (expanding with subclass hierarchies, property paths, inference rules)
+ **Execution strategy** — Parallel or serial execution plan with estimated cost and latency

**5. AgentCore Gateway → Virtual Knowledge Graph (VKG) Service (Amazon ECS) **— Conditional, Invoked When Execution Plan Requires Structured/Federated Queries. When the execution plan (Step 4) includes SPARQL queries or federated query plans, the AgentCore Gateway invokes the Virtual Knowledge Graph (VKG) Service to execute those queries. The VKG Service federates queries across:
+ **Semantic Layer Graph Database (Neptune DB)** — Queries materialized ontologies (T-Box), instance data (A-Box), and inferred knowledge
+ **Data Layer sources** — Translates SPARQL queries into optimized SQL (via R2RML mappings) and executes against relational databases, data warehouses (Snowflake, Redshift, Athena), and data lakes (S3 Tables/Iceberg)

The VKG Service returns unified RDF bindings with provenance metadata (source systems, confidence scores, extraction timestamps, data quality indicators).

**6. AgentCore Gateway → GraphRAG Service (Amazon ECS) — **Conditional, Dependent on Query Type If the query intent (Step 3) indicates that document retrieval is required, the AgentCore Gateway invokes the **GraphRAG Service** to retrieve relevant document chunks and concepts using hybrid retrieval. The GraphRAG Service:
+ Applies guardrails (via Amazon Bedrock Guardrails) to detect and redact PII or toxic content from the query
+ Generates a query embedding using Amazon Titan Embeddings (or another embedding model)
+ Executes vector similarity search against Amazon OpenSearch Service (commonly Serverless) to retrieve document chunk identifiers that meet the specified similarity threshold
+ Performs graph traversal in the Lexical Graph Database (Neptune DB) to discover related topics, concepts, and additional document chunks through multi-hop relationship following
+ Retrieves full chunk content from S3 (where chunks were cost-effectively stored by the Document Ingest Pipeline)
+ Returns ranked results with concept metadata, document chunks, provenance links, and graph context

This step enables the Q&A Agent to incorporate unstructured document content and GraphRAG-indexed concepts into its answers, complementing the structured knowledge retrieved from the VKG Service (Step 5). **This step is optional** — it is invoked only when the question requires document-grounded evidence or when the VKG Service alone cannot provide sufficient information. [170]

**7. AgentCore Gateway → Symbolic Reasoning Service (Amazon ECS) **— Conditional, Invoked When Inference or Validation Is Required. TWhen the intent classification (Step 3) or execution plan (Step 4) indicates that inference, constraint validation, or consistency checking is required, the AgentCore Gateway invokes the Symbolic Reasoning Service with the available results from the VKG Service (Step 5) and/or the GraphRAG Service (Step 6). Responses from Query Federation and MCP Server / Tool & Data Integration are reasoned over and processed. In addition to processing the responses, **semantic reasoning may be leveraged for responses that combine data from our Data Layer**.

**Since we have Continuous Reasoning for our Semantic Layer Graph Database / Knowledge Layer, Semantic Reasoning may not need to be performed** for queries that retrieve only materialized knowledge from Neptune (which is already validated and inferred by the continuous reasoning workflows). **If data is federated and potentially combined with knowledge graphs from our Semantic Layer Graph DB, we may have to perform Semantic Reasoning** to:
+ **Validate consistency** — Ensure that virtualized data from the Data Layer is consistent with ontology axioms and constraints
+ **Infer new relationships** — Derive additional triples based on OWL axioms, SWRL rules, or property chains when combining materialized and virtualized knowledge
+ **Apply backward chaining** — **Backward-Chaining** reasoning may be used to derive facts needed to answer the question by working backward from the query goal to the available data

The Symbolic Reasoning Service applies:
+ **Inference** — Derives new triples based on OWL axioms, SWRL rules, or property chains
+ **Constraint validation** — Checks if query results satisfy SHACL constraints or business rules
+ **Consistency checking** — Validates that returned entities and relationships are consistent with ontology axioms
+ **Explanation generation** — Provides reasoning chains explaining why certain facts were inferred or how constraints were validated

The Symbolic Reasoning Service may retrieve additional sub-graphs from the VKG Service if needed for reasoning, creating a potential recursive flow between Steps 5 and 7. Reasoning results (inferred triples, validation outcomes, explanations) are returned to the AgentCore Gateway with provenance linking back to the axioms or rules that triggered the inference.

**8. AgentCore Gateway → Q&A Agent (Response Synthesis)** The AgentCore Gateway aggregates results from the invoked services (VKG Service, GraphRAG Service, Symbolic Reasoning Service, or any combination thereof as determined by Steps 3 and 4) and returns them to the Q&A Agent. The agent synthesizes the final response:
+ **Natural language generation** — Uses Amazon Bedrock foundation models to generate a coherent, contextual answer from the retrieved RDF bindings, document chunks, and reasoning results
+ **Citation generation** — Includes provenance metadata in the response, citing source documents (with chunk references), knowledge graph entities (with IRIs), and reasoning steps (with axiom/rule references)
+ **Context graph update** — Updates the short-term memory/context graph (managed by the Intelligence Layer) with the current query, retrieved entities, and inferred user intent for use in subsequent multi-turn interactions
+ **Metric provenance **— cites metric definition name, version, and publish date when a metric is used

**9. Q&A Agent → MCP Interface (Response Delivery)** The Q&A Agent returns the synthesized answer to the MCP Interface in the format specified by the `ask` tool response schema:
+ `answer: string` — The natural language answer
+ `evidence: [{ subject, predicate, object, graph }]` — Supporting evidence triples from the knowledge graph
+ `citations: [{ document_id, chunk_id, page_number, url }]` — Citations back to source documents
+ `confidence: float` — Overall confidence score for the answer
+ `reasoning_steps: []` — Optional explanation of reasoning and inference steps

The MCP Interface delivers the response to the calling application or user, completing the question-answering workflow.

## Q&A Agent Architecture — Key Services
<a name="q9999999999999999amp-a-agent-architecture---key-services.3ba3278a-e878-5ff3-80fd-ff0a0c6ca313"></a>

|
|
| Service | Purpose | Invocation | Key Capabilities |
| --- |--- |--- |--- |
| **Question Intent Classification Service** | Analyze question intent and extract entities | Always | Intent classification, entity extraction grounded in ontology, semantic similarity search, document retrieval detection, metric recognition and resolution |
| **Query Execution Planning & Optimization Service** | Generate optimized execution plans | Conditional | (structured/federated queries) |
| **Virtual Knowledge Graph (VKG) Service** | Execute federated queries | Conditional | SPARQL-to-SQL translation, federation across Neptune and Data Layer sources |
| **GraphRAG Service** | Retrieve document chunks and concepts | Conditional | Hybrid retrieval (vector similarity \+ graph traversal), guardrails, embedding generation, S3 chunk retrieval |
| **Symbolic Reasoning Service** | Perform inference and validation | Conditional | OWL/SWRL reasoning, SHACL validation, backward chaining, explanation generation |

### Cross-Cutting Concerns
<a name="cross-cutting-concerns.2868a865-69cd-5184-98e0-452faf6323e7"></a>
+ **Intent-Driven Orchestration** — The Question Intent Classification Service (Step 3) is the sole required downstream invocation and serves as the routing decision point for all subsequent steps. Based on the classified intent, suggested query strategy, and extracted entities, the Q&A Agent selectively invokes Query Execution Planning (Step 4), VKG (Step 5), GraphRAG (Step 6), and Symbolic Reasoning (Step 7) as needed. This intent-driven pattern avoids unnecessary service invocations for questions that can be answered through a single retrieval path (e.g., pure document retrieval via GraphRAG without VKG federation).
+ **Multi-Modal Retrieval** — The Q&A Agent orchestrates multiple retrieval strategies based on the intent classification (Step 3): structured knowledge retrieval via VKG Service (Step 5) for querying the Semantic Layer Graph Database and virtualized Data Layer sources, unstructured content retrieval via GraphRAG Service (Step 6) for document chunks and concepts from the Lexical Graph Database, or both for hybrid questions requiring structured and unstructured evidence. Both results are reasoned over by the Symbolic Reasoning Service (Step 7) before final synthesis, enabling the agent to answer questions requiring both structured domain knowledge and unstructured document evidence.
+ **Open Standards and Open Architecture** — **All the services provided to the Q&A Agent must be provided to external agents, systems, and users**. The AgentCore Gateway exposes these services as MCP tools and REST APIs, ensuring that semantic capabilities (intent classification, query planning, VKG querying, GraphRAG retrieval, symbolic reasoning) are accessible enterprise-wide, not siloed within the Q&A Agent implementation.
+ **Event-Driven Ontology Updates** — Intent Classification and Query Planning services periodically retrieve ontologies and schema mappings, with potential migration to event-driven patterns (Neptune DB Streams) for near real-time synchronization with ontology changes.
+ **Multi-Step Execution** — Cross-domain ontology questions often require multiple steps (parallel or serial) to execute, with the Query Execution Planning & Optimization Service orchestrating complex federated queries and coordinating VKG and GraphRAG retrieval.
+ **Continuous Reasoning Integration** — The Symbolic Reasoning Service leverages continuous reasoning workflows in the Knowledge Layer, avoiding redundant inference for materialized knowledge while applying reasoning to federated queries combining Data Layer and Semantic Layer Graph Database sources.
+ **Observability** — OpenTelemetry traces propagate from MCP Interface → Q&A Agent → AgentCore Gateway → downstream services (Steps 3-7), providing end-to-end visibility via AWS X-Ray. CloudWatch Logs capture intent classification, query plans, execution statistics, GraphRAG retrieval results, reasoning results, and response confidence scores.
+ **Context Awareness** — The Q&A Agent maintains short-term memory via context graphs (Intelligence Layer), enabling multi-turn conversations where follow-up questions can reference previous queries and retrieved entities.
+ **Provenance & Explainability** — Every answer includes provenance metadata linking back to source data, source documents, ontology axioms, and reasoning steps, ensuring trust and auditability.
+ **Deterministic Metric Resolution** — Recognized metrics resolve from pre-compiled Metric Store expressions, bypassing LLM calculation synthesis and ensuring ACE compliance.

This Q&A Agent architecture enables **semantic, explainable question answering** that leverages federated knowledge graphs, hybrid document retrieval, reasoning engines, and LLM-based synthesis to deliver accurate, grounded answers with full provenance — while ensuring that all semantic capabilities are accessible to external agents, systems, and users through open standards and open architecture.
