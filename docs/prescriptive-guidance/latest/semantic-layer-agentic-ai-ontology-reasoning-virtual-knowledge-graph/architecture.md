---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/architecture.html
---

# Architecture
<a name="architecture"></a>

## High-Level Architecture (HLA)
<a name="high-level-architecture--hla-.4ebd0208-8328-5d69-8c44-ec50939c0967"></a>

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/images/guide-img/5cb278fc-4bbf-4e43-a830-4b4f72516d31/images/572339e9-7723-42b9-95db-8637c67bef72.png)

## Target technology stack
<a name="target-technology-stack.234aa248-3086-5037-b974-544e4afae998"></a>
+ [**Amazon Neptune**](https://aws.amazon.com/neptune/)** **–** **A fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. An Amazon Neptune-based knowledge graph finds relationships between projects and provides recommendations.
+ [**Amazon Bedrock**](https://aws.amazon.com/bedrock/)** **–** **A fully managed service providing API access to high-performing foundation models (FMs) from Amazon and leading AI companies. It supports fine-tuning, RAG-based customization, and Automated Reasoning — without managing infrastructure — with built-in security, privacy, and responsible AI capabilities for building and scaling generative AI applications on AWS.
+ [**Amazon Bedrock AgentCore**](https://aws.amazon.com/bedrock/agentcore/)** **–** **A managed platform for building, deploying, and operating enterprise-grade AI agents at scale. It provides purpose-built infrastructure, session management, memory, and security controls to move agents from proof-of-concept to production — enabling secure, reliable autonomous agent operations at enterprise scale.
+ [**Ontop**](https://github.com/ontop/ontop)** **–** **An open-source Virtual Knowledge Graph (VKG) system that exposes relational databases as virtual RDF knowledge graphs — without moving data. It translates SPARQL queries over ontology-defined knowledge graphs into SQL executed directly against relational sources, using R2RML mappings and lightweight OWL ontologies. Built on OBDA (Ontology-Based Data Access) principles, Ontop enables semantic querying over existing data infrastructure with no data duplication.
+ [**Amazon OpenSearch Service**](https://aws.amazon.com/opensearch-service/)** **–** **A managed service for real-time search, monitoring, and analysis. It provides vector storage and semantic similarity search for embedding-based retrieval in RAG and GraphRAG workflows. Available as provisioned clusters or OpenSearch Serverless (auto-scaling, pay-per-use).

## Target architecture
<a name="target-architecture.c3bff6e3-d311-5397-a2ad-6e6ccbba2b33"></a>
+ [**Interface Layer**](interface-layer.md)
+ [**Intelligence Layer**](intelligence-layer.md)
+ [**Knowledge Layer**](knowledge-layer.md)
+ [**Data Layer**](data-layer.md)
+ [**Orchestration Layer**](orchestration.md)
+ [**Governance / Security**](governance-security.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
