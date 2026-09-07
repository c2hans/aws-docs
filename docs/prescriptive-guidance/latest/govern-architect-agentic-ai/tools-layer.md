---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/tools-layer.html
---

# Core services: tools
<a name="tools-layer"></a>

The tools component enables agents to interact with external systems, execute functions, and perform actions beyond language processing. This layer bridges the gap between agent reasoning and real-world operations, providing the mechanisms through which agents retrieve data, invoke business logic, and integrate with enterprise systems.

![Architecture diagram core services tools](https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/images/guide-img/5961cc11-38d0-411b-a5ab-a75afdc073b4/images/a7d68409-0d1d-40c3-a776-9edc3cc324c1.png)

## Architecture patterns
<a name="architecture-patterns"></a>

Organizations can implement tool access through three primary architectural patterns, each offering tradeoffs between simplicity, governance, and operational control:

### In-runtime tools
<a name="in-runtime-tools.284877c7-78fa-569f-88d7-32ba24766253"></a>

Tools execute directly within the agent's runtime environment as inline function calls.

This pattern is characterized by:
+ Minimal latency for simple operations
+ Simplified architecture with fewer components
+ Suitable for lightweight, stateless tool operations
+ Direct integration within the agent execution context

### Direct access with remote tools
<a name="direct-access-with-remote-tools.4d1b286a-949f-5512-bcc3-5666ba46f935"></a>

Agents invoke tools through direct connections to remote services using standardized protocols such as the Model Context Protocol (MCP). Tools run in separate processes or services but are accessed without intermediary gateways.

This pattern provides:
+ Separation of concerns between agent logic and tool execution
+ Support for both local and remote tool deployment
+ Protocol-based interoperability across frameworks
+ Better isolation while maintaining reasonable latency

### Tools gateway pattern
<a name="tools-gateway-pattern.99e05c42-4e84-54d4-a5dc-31d6157c1372"></a>

A centralized gateway service manages tool discovery, security, versioning, and invocation. Agents dispatch requests to the gateway, which forwards them to the tools.

This pattern delivers:
+ Centralized tool registry and discovery - agents can search and discover available tools through a unified catalog
+ Standardized security monitoring and access control - consistent authentication, authorization, and audit across all tool invocations
+ Version management and lifecycle control - support for tool evolution, deprecation, and migration without breaking agent workflows
+ Governance enablement - approval workflows, usage tracking, quality validation, and compliance controls

## Choosing the right pattern
<a name="choosing-the-right-pattern"></a>

The choice between these patterns mirrors the decision between direct API invocation and API management in traditional enterprise architectures – organizations must balance architectural simplicity against governance requirements, scalability needs, and operational control. However, agentic systems introduce a unique constraint: unlike traditional software with predetermined API calls, LLMs must dynamically select appropriate tools at runtime, based on their description.

The table below compares these patterns across key dimensions. The choice depends primarily on three factors:
+ Governance requirements - Organizations requiring centralized control, approval workflows, and comprehensive audit trails typically favor the Tools Gateway pattern, while those prioritizing development velocity may begin with direct access approaches
+ Tool catalog scale - As the number of available tools grows, providing all tool descriptions within the LLM's context window becomes impractical and increases hallucination rates and selection errors. Use cases with a small, stable set of tools can work without centralized discovery, but scalability on the number of tools requires search and discovery capabilities such as those provided by a gateway pattern
+ Operational maturity - Teams may start with direct access for rapid prototyping and migrate to gateway-based approaches as their tool ecosystem and governance requirements mature

|
|
| Factor | In-runtime tools | Direct access with remote tools | Tools Gateway pattern |
| --- |--- |--- |--- |
| **Latency** | Lowest – inline function calls within the agent runtime | Low – direct connections, but network overhead for remote calls | Higher – additional hop through the gateway |
| **Architecture complexity** | Simplest – fewest components | Moderate – separate processes/services, but no intermediary | Most complex – requires gateway infrastructure |
| **Governance and access control** | None built in – must be implemented per tool | Limited – depends on individual tool/service controls | Centralized – approval workflows, usage tracking, compliance controls |
| **Audit and monitoring** | Manual – no centralized visibility | Per-service – inconsistent across tools | Centralized – consistent authentication, authorization, and audit |
| **Tool discovery** | N/A – tools are hardcoded in the runtime | Manual – agents must know tool endpoints | Unified catalog – agents search and discover tools dynamically |
| **Version management** | Manual – updates require redeployment | Per-service – each tool manages its own versioning | Centralized – lifecycle control, deprecation, and migration support |
| **Scalability (number of tools)** | Limited – all tools must fit in the agent context | Moderate – works with a small, stable set of tools | Best – search and discovery prevent context window overload and reduce hallucination |
| **Isolation** | None – tools share the agent's runtime | Good – separate processes provide fault isolation | Good – gateway adds an additional isolation layer |
| **Best suited for** | Lightweight, stateless operations with a small tool set | Small teams prototyping with a known set of remote tools | Enterprise environments needing governance, scale, and operational control |
| **Typical maturity stage** | Early exploration | Rapid prototyping and growing maturity | Production at scale |

## Governance considerations
<a name="governance-considerations"></a>

The tools layer requires governance controls for:
+ Tool registration and approval workflows - maintain catalogs of authorized tools with quality control and lifecycle management
+ Access control policies - define which agents can invoke specific tools, with fine-grained permission scoping
+ Usage tracking and audit logs - comprehensive logging of all tool invocations for compliance and cost management
+ Version management - support tool evolution without breaking existing agent workflows, including deprecation and migration paths
+ Quality validation - ensure tool reliability, performance standards, and security compliance
+ Discovery and search capabilities - enable agents to find appropriate tools through searchable registries

## Implementation on AWS
<a name="implementation-on-aws"></a>

The Tools gateway pattern is implemented using [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) gateway, which serves as a centralized tool server providing a unified interface where agents can discover, access, and invoke tools.

AgentCore Gateway provides:
+ Native MCP support - built with native support for the Model Context Protocol, enabling seamless agent-to-tool communication while abstracting away security, infrastructure, and protocol-level complexities
+ REST API transformation - converts existing REST APIs into MCP servers, allowing legacy systems to become discoverable tools
+ MCP server integration - treats existing MCP servers as native targets, providing a single point of control for routing, authentication, and tool management
+ Centralized tool discovery - agents can search and discover available tools through a unified catalog across multiple targets
+ Target-based architecture - each target (API, MCP server, or service) exposes multiple tools, with each function or path/method becoming a discoverable tool
+ Security and governance - handles authentication, authorization, and audit logging across all tool invocations

[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) code execution and browser Tools - In addition to the gateway pattern, Amazon Bedrock AgentCore provides secure and scalable access to isolated code execution and web browsing environments, enabling agents to perform computational tasks and interact with web content without requiring infrastructure provisioning or management.
