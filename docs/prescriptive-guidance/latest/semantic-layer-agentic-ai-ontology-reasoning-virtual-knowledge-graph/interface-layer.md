---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/semantic-layer-agentic-ai-ontology-reasoning-virtual-knowledge-graph/interface-layer.html
---

# Interface Layer

## Interface Layer
<a name="interface-layer.a4024ae5-9a1e-54ce-950f-beeec42e3c69"></a>

The Interface Layer establishes the formal contract between the Semantic Layer and its consumers — including User Interfaces, Services, and Agents. By supporting a broad set of protocols and query languages, it enables diverse use cases and personas to interact with semantic data in the way that best fits their needs.

**Protocol Support**
+ **Agent Protocols:** Native support for Model Context Protocol (MCP) and Agent-to-Agent (A2A), enabling autonomous agents to discover, invoke, and compose semantic capabilities
+ **Web & Service APIs:** REST, GraphQL, and WebSockets provide flexible, standards-based integration for applications and services

**Query Language Support**
+ **SPARQL:** Full CRUD operations over Ontologies and Knowledge Graphs, enabling precise semantic querying and knowledge engineering workflows
+ **SQL over JDBC:** Data and Catalog CRUD for familiar, structured access to semantic assets by data engineers and analysts

**Supported Use Cases & Personas**
+ Ontology Management & Knowledge Engineering UIs
+ Chatbots and conversational interfaces
+ Autonomous Agents operating within agentic AI pipelines

By abstracting the complexity of the Semantic Layer behind well-defined interfaces, the Interface Layer ensures interoperability, extensibility, and broad adoption across the enterprise.
+ [Model Context Protocol (MCP)](mcp-server.md)
+ [Agent-to-Agent (A2A)](agent-to-agent-a2-a-protocol.md)
+ [REST API](rest-api.md)
