---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/agents-layer.html
---

# Agents layer
<a name="agents-layer"></a>

The Agents layer serves as the central coordination hub for interactions between users, foundation models, tools, and knowledge sources. This layer contains the agent runtime environments, orchestration mechanisms, and supporting infrastructure that enable AI agents to function. Agents use LLMs for reasoning and planning, call tools to perform operations, retrieve information from knowledge bases, and maintain memory of past interactions.

![Architecture agents layer](https://docs.aws.amazon.com/prescriptive-guidance/latest/govern-architect-agentic-ai/images/guide-img/5961cc11-38d0-411b-a5ab-a75afdc073b4/images/f931d706-7a84-464b-8e91-54ed89e7578b.png)

## Agent execution
<a name="agent-execution"></a>

Agents have specific requirements that set them apart from the traditional application and microservices. Agents can run in autonomy for hours, need to retain context and at the same time be fully isolated from other agent instances. Agents need to securely discover, select and access tools and other agents via well-known protocols like MCP and A2A. Agents also require services to persist conversation across executions, and secure ways to execute code and interact with browser and web-based systems.

Organizations can implement these capabilities using:
+ [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) runtime – a foundational service for executing agents securely at scale with no infrastructure management needed. The runtime provides enterprise-grade security and dynamic scaling, session persistence and isolation, large payloads, multi-protocol support and bidirectional streaming.
+ [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) memory – provides persistence for both short-term conversation history and long-term extracted insights.
+ [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) identity – ensures seamless integration of authentication with IAM and OAuth providers for both inbound and outbound.
+ [AWS Lambda](https://aws.amazon.com/lambda/) – provides serverless computing for custom agent logic and tool implementations. Provides execution for lightweight agent operations and tool invocations.
+ [Amazon ECS](https://aws.amazon.com/ecs/) or [AWS Fargate](https://aws.amazon.com/fargate/) – provides container-based agent deployments for complex requirements, stateful operations, or resource-intensive agent workloads requiring dedicated compute environments.

## Agent registry and catalog
<a name="agent-registry-and-catalog"></a>

A centralized agent registry maintains an inventory of deployed agents, capturing:
+ Agent capabilities, permissions, and purpose
+ Metadata on ownership, version history, and dependencies
+ Performance metrics and usage statistics
+ Approval status and governance classifications

The registry supports discovery, reuse, and governance while preventing unnecessary duplication of capabilities across the organization. Registries should support self-service access requests and authorization delegation to the tool or agent owners. Registries should integrate with MCP gateway access controls to enforce the required access policies. Organizations should maintain registries documenting approved agents with quality control and lifecycle management.

## Multi-agent coordination
<a name="multi-agent-coordination"></a>

As multi-agent systems become prevalent, architectures must support agent-to-agent communication through standardized protocols such as MCP and A2A, message formatting and state sharing conventions, appropriate state isolation, authentication and authorization between collaborating agents, and permissions verification for delegated actions.

Supporting infrastructure includes:
+ [Amazon Bedrock AgentCore ](https://aws.amazon.com/bedrock/agentcore/)memory – managed memory service for storing agent state, conversation history, and long-term extracted insights that can be shared across agent sessions with fine-grained access control and storage isolation
+ [Amazon EventBridge](https://aws.amazon.com/eventbridge/) – event-driven backbone for multi-agent messaging
+ [AWS Step Functions](https://aws.amazon.com/step-functions/) – orchestration for complex multi-agent workflows with checkpoints and error recovery
+ [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) – fast, scalable storage for agent state and shared memory

## Agent quality and safety
<a name="agent-quality-and-safety"></a>

As agents become more autonomous and handle critical business operations, architectures must support comprehensive quality assurance and safety mechanisms through evaluation frameworks for reliability and accuracy, safety testing for harmful outputs or behaviors, performance monitoring and regression detection, and feedback loops for continuous improvement.

Supporting infrastructure includes:
+ [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) – manages capabilities for content filtering, denied topics, word filters, and sensitive information redaction
+ [Amazon Bedrock AgentCore ](https://aws.amazon.com/bedrock/agentcore/)Evaluations – built-in evaluation frameworks providing automated assessment tools to measure how well agents or tools perform specific tasks, handle edge cases, and maintain consistency across different inputs and contexts.
+ [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) – helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/)– evaluate LLMs and semantic retrieval systems using programmatic metrics, human evaluators and LLM-as-judge.
+ [AWS Lambda](https://aws.amazon.com/lambda/) - Serverless execution of custom validation logic and safety checks
+ [Amazon S3](https://aws.amazon.com/s3/) - Storage for evaluation datasets, test results, and safety audit logs
+ Open-source observability tools - Platforms like LangFuse for tracing, evaluation, prompt management, and metrics; [deployable on AWS](https://langfuse.com/self-hosting/deployment/aws)

## Access control and authentication
<a name="access-control-and-authentication"></a>

Effective agent operations require robust identity and permission management through identity propagation from users through agent chains, permission boundaries for agent actions and tool access, audit trails of agent decisions and actions, and circuit breakers for abnormal behavior patterns.

Supporting infrastructure includes:
+ [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) Identity – integrated identity management and authentication context propagation across agent interactions
+ [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) Gateway Interceptors – Lambda based request and response interceptor to evaluate, filter, manipulate and block MCP tool calls and responses
+ [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) Policy – Cedar-based engine to implement contextual grounded fine-grained authorization on AgentCore data plane operations
+ [AWS Identity and Access Management](https://aws.amazon.com/iam/) and [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) – enterprise authentication, authorization, and single sign-on integration with identity providers
+ [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) – secure credential storage and automatic rotation for service accounts
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) – comprehensive API activity logging and audit trail generation
+ [Amazon EventBridge](https://aws.amazon.com/eventbridge/) – real-time alerting and remediation
