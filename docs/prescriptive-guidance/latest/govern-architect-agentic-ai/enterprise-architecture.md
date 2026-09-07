---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/enterprise-architecture.html
---

# Agentic AI architecture in the enterprise
<a name="enterprise-architecture"></a>

The reference architecture for enterprise agentic AI systems demonstrates how organizations can implement production-grade AI capabilities while maintaining governance, security, and operational excellence.

The architecture is organized into layers that work together to enable AI agents while maintaining enterprise control. Observability, security and discoverability span multiple layers, ensuring that AI operations are monitored, auditable, and compliant with enterprise policies.

![Architecture diagram with three layers](https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/images/guide-img/5961cc11-38d0-411b-a5ab-a75afdc073b4/images/ae123839-aadb-4656-b85c-dcb20a97910b.png)

**Applications layer:**
+ [**Generative AI End-User Applications **](gen-ai-end-user-solutions-layer.md)- These are user-facing applications that enable interaction with agentic AI systems. These applications may provide conversational interfaces for natural language interaction, productivity features that augment workflows with AI assistance, and no-code tools that allow business users to create and deploy custom agents. An application can be off the shelf, like integrated development environment (IDE) and productivity tools, or custom built.
+ [**Non-GenAI Applications**](non-gen-ai-applications-layer.md) - These are business systems that may be off-the-shelf software, custom-built applications, or industry-specific platforms. Most of these applications are not inherently agentic but can consume agentic AI services or expose their functions as tools that agents can invoke to perform business operations.

[**Agents layer**](agents-layer.md) - This layer contains the components that enable AI agents to function and interact. It also provides agent discoverability. Agents typically require access to LLM to interpret user goals, to reason and plan actions, to obtain access to tools to perform operations, and to retrieve information from knowledge sources. They also need the ability to store conversations and insights derived from the conversations in short and long term memory respectively. The layer also provides the features for agent-to-agent communication and orchestration, allowing multiple agents to collaborate on complex tasks.

## Three core service categories
<a name="three-core-service-categories"></a>

The architecture defines three distinct types of services that agents interact with:
+ [**Model access component **](model-access-layer.md)– controls access to foundation models with policy enforcement, safety measures including guardrails, and cost tracking/allocation capabilities.
+ [**Tools component **](tools-layer.md)– manages discovery and secure execution of tools. This component provides authorization capabilities to ensure tools can be used only by the right actors and for the right context.
+ [**Knowledge bases component **](cross-cutting-concerns.md)– provides access to enterprise data through knowledge bases that can leverage vector stores, graph storage, and provide interfaces for semantic information retrieval. It also provides role-based access control (RBC) for the data to enforce least privilege and need-to-know principles. This component is required for retrieval-augmented generation (RAG) implementations.

## Cross-layer concerns
<a name="cross-layer-concerns"></a>

Observability, security and discoverability span multiple layers, ensuring that AI operations are monitored, auditable, and compliant with enterprise policies.
