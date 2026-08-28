---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/introduction.html
---

# Introduction
<a name="introduction"></a>

## Why Now?
<a name="why-now-.9bc0bf61-ad08-5806-9932-e37726d37e63"></a>

The convergence of several technological and business forces makes this the ideal moment for semantic data foundations to enable agentic AI at enterprise scale.

**Agents with autonomy are challenging without semantic foundations.** Autonomous agents require a shared semantic foundation that encodes organizational knowledge, enabling them to understand business context, validate decisions against explicit constraints, and provide auditable reasoning, capabilities that retrieval and probabilistic models alone cannot deliver.

**LLMs have made it easier than ever to facilitate the creation and management of ontologies and associated rules/axioms.** Foundation models can now accelerate ontology induction from data catalogs, extract entities and relationships from specifications, generate semantic annotations, and propose axioms based on data patterns — tasks that previously required months of manual knowledge engineering. This democratizes semantic layer development, enabling organizations to bootstrap knowledge graphs rapidly while maintaining quality through human-in-the-loop validation workflows.

**Customers need an incremental approach to get their data ready for AI.** Enterprise data landscapes are complex, heterogeneous, and constantly evolving. Organizations cannot afford "big bang" transformations that require upfront data migration or complete system rewrites. The semantic layer approach enables incremental value delivery — virtualizing existing data sources through ontology-based data access (OBDA), materializing only what requires reasoning or cross-domain integration, and progressively enriching the knowledge graph as new use cases emerge. This reduces time-to-value, minimizes risk, and aligns with modern data mesh and data fabric architectures.

## Personas
<a name="personas.08fa39dd-71f0-57d2-89e0-a29b910010a4"></a>

This guidance addresses three primary personas who collaborate to build and leverage semantic data foundations for agentic AI:

**Administrators** — Platform engineers, cloud architects, and infrastructure specialists responsible for deploying, securing, and operating the semantic layer infrastructure. They configure AWS services (Neptune, ECS, Bedrock, Glue), implement governance policies, manage access controls, and ensure observability, scalability, and cost optimization across the semantic stack.

**Data-Focused Practitioners** — Data engineers, ontology engineers, and knowledge engineers who design ontologies, create R2RML mappings, configure reasoning rules, and manage the lifecycle of semantic artifacts. They bridge technical data structures (schemas, tables, APIs) with business semantics (ontologies, glossaries, constraints), ensuring that the semantic layer accurately represents enterprise knowledge and remains synchronized with evolving data sources.

**Business Analysts** — Domain experts, data stewards, and business analysts who understand data domains, data products, business rules, and organizational knowledge. They define business glossaries, validate ontology completeness, approve semantic changes, and ensure that the knowledge graph reflects business reality. Their domain expertise grounds the semantic layer in real-world context, enabling agents to reason about business concepts rather than just technical data structures.

## State of the Art
<a name="state-of-the-art.7ce324f8-7af9-54dc-a6d7-ea1c6a383e18"></a>

### Neurosymbolic AI
<a name="neurosymbolic-ai.d1f88429-582c-5abc-a82b-f5b9886b14fd"></a>

The semantic data foundations architecture embraces **neurosymbolic AI** — the integration of neural networks (LLMs, embeddings) with symbolic reasoning (ontologies, logic, rules) — to deliver the best of both paradigms.

**Deterministic vs. Non-Deterministic Reasoning** — Symbolic reasoning (OWL, SPARQL, SHACL, SWRL) provides deterministic, explainable inference based on formal logic and ontology axioms. Given the same knowledge graph and rules, reasoning engines produce consistent, reproducible results with full provenance. In contrast, LLMs and neural networks are non-deterministic — they generate probabilistic outputs based on learned patterns, which can vary across invocations and may produce hallucinations or inconsistent answers. By combining both approaches, the architecture leverages LLMs for semantic enrichment, natural language understanding, and flexible pattern recognition, while relying on symbolic reasoning for validation, consistency checking, and explainable inference.

**Accuracy and Explainability** — Symbolic reasoning ensures accuracy for structured queries and rule-based inference, with every conclusion traceable to specific axioms, constraints, or data assertions. This explainability is critical for regulated industries (healthcare, finance, government) where decisions must be auditable and defensible. LLMs complement this by handling ambiguous natural language, extracting entities from unstructured text, and synthesizing human-readable explanations — but their outputs are validated against ontology constraints and reasoning rules before being asserted as knowledge.

**Complementary Strengths** — LLMs excel at semantic similarity, entity disambiguation, ontology induction, and natural language generation — tasks that benefit from learned patterns across vast corpora. Symbolic reasoning excels at consistency validation, transitive inference, constraint enforcement, and logical deduction — tasks that require formal guarantees. The architecture orchestrates both: LLMs propose candidate knowledge, symbolic reasoners validate and refine it, and the combination delivers trustworthy, explainable AI that scales across enterprise use cases.

### Data-Information-Knowledge-Wisdom (DIKW) Hierarchy
<a name="data-information-knowledge-wisdom--dikw--hierarchy.a7b7acfe-5452-5668-9514-09184cbc2ae8"></a>

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/images/guide-img/5cb278fc-4bbf-4e43-a830-4b4f72516d31/images/7d2f223e-a6da-429d-9f08-ceebbfdc0d3d.png)

The **DIKW hierarchy** provides a conceptual framework for understanding how raw data evolves into actionable wisdom - a progression that inspired the layered architecture of the Semantic Layer for Agentic AI. While the architecture aligns closely with DIKW's four tiers, it extends the framework with an Intelligence tier that addresses enterprise requirements for continuous self-assessment and semantic evolution.

**Data Layer — Data Tier** Raw data from source systems (databases, data lakes, documents, APIs) represents the Data tier — facts without context or semantic meaning.

**Data Layer — Information Tier** The Data Layer transforms raw data into the Information tier through document ingestion, GraphRAG processing, and information extraction — chunking documents, extracting entities, indexing concepts with vector embeddings, and cataloging metadata. The result is indexed, contextualized information assets stored in the Lexical Graph Database and accessible through data catalogs (AWS Glue Data Catalog, Amazon SageMaker Catalog). Information is data with context — organized, structured, and prepared for semantic interpretation.

**Knowledge Layer** — The **Knowledge** tier emerges when data is organized into ontology-driven structures with explicit semantics, relationships, and constraints. The Knowledge Layer (Virtual Knowledge Graph Service, Semantic Layer Graph Database, Reasoning Service) transforms data into knowledge by applying ontologies (T-Box) to instance data (A-Box), enabling semantic queries, federated access, and inference. Knowledge is contextualized, validated, and interconnected — entities are linked by meaningful relationships, and reasoning derives implicit facts from explicit assertions.

**Intelligence Layer** — While DIKW traditionally progresses directly from Knowledge to Wisdom, this architecture introduces an Intelligence tier representing meta-knowledge — knowledge about knowledge. This extension recognizes that enterprise semantic systems require continuous self-assessment and evolution beyond static knowledge representation. The Intelligence Layer (Ontology Induction, Ontology Evaluation, Truth Maintenance, Context Graphs) continuously assesses, refines, and evolves the semantic layer based on data patterns, usage analytics, and domain expertise. It identifies gaps, resolves ambiguities, maintains alignment with source data, and provides episodic memory for agents — enabling the system to learn and adapt over time.

**Orchestration Layer** — The **Wisdom** tier represents the application of knowledge and intelligence to make decisions, answer questions, and take actions. The Orchestration Layer (Q&A Agent, Business Elicitation Agent, Ontology Maintenance Agent) embodies wisdom by leveraging semantic foundations to deliver business value — synthesizing knowledge from multiple sources, reasoning over complex scenarios, and orchestrating human-in-the-loop workflows when automated reasoning requires domain expertise.

This alignment demonstrates how the architecture operationalizes the DIKW progression, enabling organizations to move from data management to knowledge-driven decision-making and ultimately to autonomous, intelligent systems.

## Semantic Web Stack
<a name="semantic-web-stack.d48d1520-bc18-5f61-ad4d-00db2332c80e"></a>

The architecture is grounded in **Semantic Web standards** — a mature, open, and interoperable technology stack developed by the W3C for representing, querying, and reasoning over knowledge graphs at web scale.

**RDF (Resource Description Framework)** — The foundational data model representing knowledge as subject-predicate-object triples, enabling flexible, graph-native knowledge representation without rigid schemas.

**RDFS (RDF Schema) and OWL (Web Ontology Language)** — Ontology languages for defining classes, properties, hierarchies, and axioms. OWL provides rich expressivity for complex domain modeling, including property characteristics (transitive, functional), cardinality constraints, and class expressions.

**SPARQL** — The standard query language for RDF, enabling federated queries across distributed knowledge graphs and data sources. SPARQL supports SELECT (retrieve bindings), CONSTRUCT (generate new graphs), ASK (boolean queries), and DESCRIBE (entity descriptions).

**SHACL (Shapes Constraint Language)** — A constraint validation language for defining data quality rules, cardinality constraints, and business logic as shapes that validate RDF graphs.

**R2RML (RDB to RDF Mapping Language)** — The standard for defining mappings from relational databases to RDF, enabling ontology-based data access (OBDA) and virtual knowledge graphs without data duplication.

**SWRL (Semantic Web Rule Language)** — A rule language for expressing inference rules that extend OWL reasoning, enabling domain-specific business logic and complex deductions.

By adhering to Semantic Web standards, the architecture ensures **interoperability** (knowledge graphs can be shared across systems), **longevity** (standards-based implementations are future-proof), and **ecosystem compatibility** (integration with open-source tools like Ontop, Apache Jena, and commercial platforms like Stardog). This open architecture ensures that semantic capabilities are not locked into proprietary formats or vendor-specific implementations, enabling customers to leverage best-of-breed tools and evolve their semantic layer as the ecosystem matures.

This introduction establishes the strategic context (Why Now?), target audience (Personas), theoretical foundations (Neurosymbolic AI, DIKW), and technical grounding (Semantic Web Stack) for the AWS Prescriptive Guidance on Semantic Data Foundations for Agentic AI — positioning the architecture as a pragmatic, standards-based approach to enabling trustworthy, explainable, and scalable autonomous agents for enterprise use cases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
