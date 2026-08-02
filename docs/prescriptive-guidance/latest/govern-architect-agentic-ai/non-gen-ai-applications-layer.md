---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/non-gen-ai-applications-layer.html
---

# Applications layer: non-generative-AI solutions
<a name="non-gen-ai-applications-layer"></a>

This layer consists of existing business systems, whether off-the-shelf software, custom-built applications, or industry-specific platforms, that integrate bidirectionally with agentic AI capabilities. These applications are not inherently agentic but can consume agentic AI services or expose their functions as tools that agents can invoke to perform business operations.

![Architecture non-generative AI solutions](http://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/images/guide-img/5961cc11-38d0-411b-a5ab-a75afdc073b4/images/00f684ba-dd79-4d10-855f-9f71faf74185.png)

## Purpose and characteristics
<a name="purpose-and-characteristics"></a>

The Enterprise Applications Layer provides these capabilities to agents:
+ Bidirectional integration – enables two-way communication where applications both consume AI services and provide capabilities to agents
+ Business logic access – exposes domain-specific rules and processes that agents can leverage
+ System of record integration – connects agents to authoritative data sources for reading and writing business data
+ Process automation – allows agents to initiate and participate in enterprise workflows
+ Secure delegation – enables agents to act on behalf of users with appropriate permissions

## Enterprise systems in this layer
<a name="enterprise-systems-in-this-layer"></a>

This layer encompasses diverse business systems including business management platforms such as ERP (enterprise resource planning), CRM (customer relationship management), HRMS (Human Resources Management System), and SCM (supply chain management), operational systems such as Jira, ServiceNow, and Salesforce, workflow engines, and business intelligence platforms, and content systems such as document management, enterprise wikis, and collaborative workspaces. These applications, whether off-the-shelf software, custom-built solutions, or industry-specific platforms, integrate bidirectionally with agentic AI capabilities.

## Integration approaches
<a name="integration-approaches"></a>

Enterprise applications integrate with agentic systems through tools, events and direct data access. Each of these integrations requires specific features to make it possible.

### Tool exposure
<a name="tool-exposure.0b20419e-ada6-5d51-80d3-777166db084f"></a>
+ Function wrapping – business functionality exposed as callable tools that agents can invoke using protocols such as MCP
+ Parameter validation – input validation to protect enterprise systems from malformed requests
+ Response formatting – structured outputs that agents can reliably parse

### Event-driven integration
<a name="event-driven-integration.8066efdc-f938-554a-80a1-07652fde4d1a"></a>
+ State change notifications – systems publish events when business objects change
+ Process triggers – workflow status updates that agents can subscribe to
+ Alert generation – exception conditions that prompt agent intervention

### Data access patterns
<a name="data-access-patterns.3d1c8352-7486-55f7-8244-542d37b97f06"></a>
+ Direct querying – secure, parameterized data access interfaces
+ Cached views – pre-aggregated data for efficient agent consumption
+ Permission-aware access – data access that respects user authorization contexts
+ Semantic transformation – index unstructured enterprise data such as text, audio, and video, into generative AI-friendly semantic representations using embeddings and vector databases
+ Knowledge graphs – represent complex data relations via graphs and ontologies to allow AI systems to better understand specific industry domains

### Implementation considerations
<a name="implementation-considerations.04b77479-29b7-51f3-a490-e94105dd29a6"></a>

Organizations implementing this layer should address these challenges:
+ Authentication context propagation – ensuring that user identity is preserved when agents act on their behalf, typically through token exchange solutions that issue delegated credentials, on-behalf-of tokens, to the agents
+ Rate limiting – protecting traditional enterprise systems that were designed for human access from overload due to automated agent
+ Maintenance window coordination – ensure that agents are not trying to access systems during maintenance window hours
+ Credential management –secure storage and rotation of secrets necessary for agent to access tools and other systems
+ Error handling – graceful degradation when backend systems are unavailable
+ Semantic or format transformation – converting between AI-friendly formats and enterprise data structures

### AWS implementation approaches
<a name="9999999999999999aws--implementation-approaches.a39b1287-08c0-5d51-ae02-ebbe61fb94a4"></a>

AWS provides several services to enable enterprise application integration:
+ [Amazon EventBridge](https://aws.amazon.com/eventbridge/) – serverless event bus for connecting applications with real-time data
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway/) – create and secure APIs for agent access to business functions, providing API throttling controls and bi-directional websocket transport
+ [Amazon AppFlow](https://aws.amazon.com/appflow/) – managed integration for connecting SaaS applications with AWS services
+ [AWS Glue](https://aws.amazon.com/glue/) – ETL service for preparing and transforming data
+ [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) – enterprise search capabilities for content discovery
+ [Amazon BedrockKnowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) – unified API to interact with knowledge bases backed by several popular vector databases and graph databases.

This integration layer ensures that agentic AI capabilities can access the business context, data, and operations necessary to provide value within organizational workflows while maintaining appropriate security boundaries and governance controls.
