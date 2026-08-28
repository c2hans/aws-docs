---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/agent-builder-1.html
---

# Agent Builder
<a name="agent-builder-1"></a>

The Agent Builder provides a platform for creating, deploying, and managing production-ready AI agents on Amazon Bedrock AgentCore. This section describes the technical components and implementation details.

## AgentCore integration
<a name="agentcore-integration"></a>

Agent Builder uses a configuration-based deployment approach with pre-built agent images to enable fast, secure, and scalable agent deployments.

 **Pre-built agent images**

Agent container images are built by the GAAB team during the CI/CD pipeline and published to a public ECR repository. Each image version is tied to the GAAB solution version (for example, v4.0.0 → gaab-strands-agent:v4.0.0). Images are based on the Strands SDK and include:
+ Agent runtime environment
+ MCP client integration
+ Memory management capabilities
+ OpenTelemetry instrumentation

 **ECR Pull-Through Cache**

The solution uses ECR Pull-Through Cache to automatically distribute agent images from the public ECR repository to the customer’s private ECR. This AWS-managed service:
+ Caches images on first pull (2-5 minute delay)
+ Eliminates custom image copying logic
+ Provides local image availability for subsequent deployments
+ Creates unique cache rules per deployment to avoid conflicts

 **Configuration storage**

Agent configurations are stored in DynamoDB alongside existing use case configurations. Each configuration includes:
+ System prompt template
+ Model provider and model ID
+ Model parameters (temperature, max\_tokens)
+ MCP server references and endpoints
+ Memory settings (long-term memory toggle)
+ Deployment metadata

 **Image version registry**

A DynamoDB table tracks available agent image versions and their cache URIs, enabling version management and backward compatibility.

## Agent configuration
<a name="agent-configuration"></a>

 **System prompts**

System prompts define agent behavior, personality, and capabilities. Admin users can:
+ Edit the default template through the Agent Builder UI
+ Include instructions for tool usage and response formatting
+ Reset to default template at any time

 **Model selection**

Agent Builder supports Amazon Bedrock models in v4.0.0:
+ Model provider: Amazon Bedrock (only option in v4.0.0)
+ Model selection: Claude, Nova, and other Bedrock models
+ Model parameters: Temperature, max\_tokens, top\_p, and model-specific settings

 **MCP server integration**

Model Context Protocol servers provide agents with access to enterprise tools and data:
+ Server discovery through GET /mcp API endpoint
+ Dynamic configuration without code changes
+ Authentication and endpoint management
+ Tool capability exposure to agents

## Streaming and processing
<a name="streaming-and-processing"></a>

 **Real-time streaming**

Agent Builder uses Server-Sent Events (SSE) from AgentCore bridged to WebSocket for real-time response streaming:
+ Lambda function establishes SSE connection to AgentCore Runtime
+ Streams are bridged to API Gateway WebSocket
+ Enables token-by-token response delivery to clients
+ Maintains connection for long-running requests

 **Processing constraints**

Agent processing in v4.0.0 is limited to Lambda execution timeout:
+ Maximum processing time: 15 minutes
+ Synchronous processing model
+ Suitable for conversational agents and moderate workflows
+ Extended async support planned for v4.1\+

## Memory management
<a name="memory-management"></a>

 **Short-term memory**

Enabled by default for all agents using a custom MemoryHookProvider:
+ Captures conversation events through Strands callback handlers
+ Organizes by actorId and sessionId for context isolation
+ Maintains conversation context within sessions
+ Automatic integration with AgentCore Memory

 **Long-term memory**

Optional feature using AgentCore Memory Tool from strands\_tools:
+ Simple toggle in Agent Builder UI
+ Semantic memory strategy with default settings
+ Agent-controlled access through natural tool invocation
+ Stores extracted insights across sessions
+ Uses conversationId as sessionId

## Observability
<a name="observability"></a>

 **AWS OpenTelemetry Distro (ADOT)**

Agents are automatically instrumented during container build:
+ Automatic trace generation for agent operations
+ Distributed tracing across service boundaries
+ Structured logging with correlation IDs
+ Integration with CloudWatch Transaction Search

 **Authentication flow**

Users authenticate through Amazon Cognito with JWT tokens validated by custom Lambda authorizers that retrieve IAM policies from DynamoDB based on user groups.

## Workflow Builder
<a name="workflow-builder-1"></a>

Workflow Builder enables multi-agent orchestration by creating a supervisor agent that coordinates multiple Agent Builder agents using the Agents as Tools delegation pattern.

### Workflow architecture
<a name="workflow-architecture"></a>

 **Key components**
+  **Supervisor Agent**: Entrypoint agent that receives user requests and delegates to specialized agents
+  **Specialized Agents**: Agent Builder use cases registered as tools for the supervisor
+  **Agent Registry**: DynamoDB table storing agent configurations and metadata
+  **Orchestration Layer**: Strands SDK implementation of Agents as Tools pattern

### Agent instantiation
<a name="agent-instantiation"></a>

 **Local agent creation**

All specialized agents are instantiated locally within the same AgentCore Runtime:

1. Retrieves agent configurations from DynamoDB

1. Creates local instances of each Agent Builder agent

1. Each agent maintains its own MCP server connections

1. Supervisor agent registers specialized agents as tools

1. Strands SDK manages agent selection and delegation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
