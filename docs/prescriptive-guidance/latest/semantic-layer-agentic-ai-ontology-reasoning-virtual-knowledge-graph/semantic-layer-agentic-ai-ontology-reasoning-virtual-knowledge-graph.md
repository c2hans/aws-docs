---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph.html
---

# Semantic Layer for Agentic AI using Ontology, Symbolic Reasoning, and Virtual Knowledge Graph
<a name="semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph"></a>

*Don Simpson, Taylor Riggan, and Chun Schiros, Amazon Web Services*

## Summary
<a name="summary"></a>

This AWS Prescriptive Guidance establishes a comprehensive **ontology-driven semantic layer architecture** that enables trustworthy, explainable agentic AI systems for enterprise environments. While traditional semantic layers focus on BI metrics and data abstraction, this guide delivers a** knowledge-driven foundation **that transforms raw enterprise data into formal ontologies, automated symbolic reasoning, and virtual knowledge graphs — enabling AI agents to reason over complex business domains with **accuracy, consistency, and explainability **— the ACE principles that underpin trustworthy agentic AI. This aligns with emerging research showing that ontology-based semantic representations significantly improve LLM accuracy for enterprise question answering, where incomplete retrieval cascades into incomplete context for agent decision-making, leading to hallucinations, non-deterministic behavior, and ultimately poorer response quality and relevance (Allemang & Sequeda, 2024).

The guide addresses the critical challenge of autonomous agents requiring structured, verifiable knowledge to make decisions, validate actions, and provide auditable reasoning chains. It accomplishes this by implementing a **composable layered architecture** spanning Data, Knowledge, Intelligence, and Orchestration layers that transform raw enterprise data into ontology-driven knowledge graphs accessible through standardized interfaces (MCP and A2A protocols). The architecture is designed for flexible consumption — organizations can leverage the pre-built Q&A Agent for turnkey semantic question answering, or selectively invoke individual MCP tools (`intent_classification`, `generate_queries`, `execute_queries`, `graphrag_search`, `reasoning`) to compose custom workflows tailored to specific use cases. This composability enables teams to either adopt the full orchestration layer or integrate semantic capabilities directly into existing agents and applications, providing a spectrum of implementation options from fully managed to fully customized.

This guide is designed for data architects and engineers, chief data officers, chief AI officers, AI architects and engineers, and enterprise architects. Each role engages with different layers of the architecture — executive leaders and enterprise architects can focus on the composable design patterns, governance model, and business outcomes described above, while data and AI practitioners will find detailed implementation guidance in the technology-specific sections that follow. You do not need deep familiarity with every standard or technology referenced below to successfully leverage this architecture; the layered design intentionally abstracts complexity so that each persona can engage at the appropriate level of depth.

The architecture leverages Amazon Neptune for graph databases, Amazon Bedrock for LLM capabilities and agent runtime (AgentCore), Amazon ECS for containerized services, AWS Glue Data Catalog and Amazon SageMaker Catalog for metadata management, and Amazon OpenSearch for vector storage and semantic search. The guide incorporates open-source technologies including Ontop for virtual knowledge graph implementation, ELK and HermiT for OWL reasoning, SHACL validators for constraint enforcement, and unstructured.io for document processing. It adheres to W3C Semantic Web standards including RDF, RDFS, OWL, SPARQL, SHACL, R2RML, and SWRL to ensure interoperability and ecosystem compatibility.

This is a cloud-native architecture guide designed for greenfield semantic layer implementations or incremental modernization of existing data landscapes. The guide enables organizations to virtualize existing data sources through **ontology-based data access (OBDA)** without requiring upfront data migration, materializing only what requires reasoning or cross-domain integration. The **composable design** supports multiple adoption paths: organizations can start with high-level agent orchestration (using the `ask` tool), progressively adopt individual semantic capabilities (query generation, reasoning, GraphRAG retrieval), or build entirely custom agents that leverage the semantic layer's MCP and A2A interfaces. Key outcomes include autonomous agents with explainable reasoning, federated querying across heterogeneous data sources, automated ontology induction from data catalogs, continuous knowledge graph validation through automated reasoning, and human-in-the-loop workflows for semantic governance. The **neurosymbolic approach** combines deterministic symbolic reasoning with probabilistic LLM capabilities to deliver Accuracy, Consistency, and Explainability (ACE) for regulated industries requiring auditable AI systems.

## Attachments
<a name="attachments-5cb278fc-4bbf-4e43-a830-4b4f72516d31"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
