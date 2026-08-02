---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/orchestration-models.html
---

# Orchestration models: From rule-based to AI-native
<a name="orchestration-models"></a>

In event-driven serverless AI systems, orchestration is the connective logic that determines how events trigger and shape the behavior of the system. In AWS, orchestration can follow two primary models:
+ **Rule-based orchestration** is defined by developers using workflows and state machines.
+ **AI-native orchestration** is powered by agents and large language models (LLMs) that reason, plan, and act based on intent and context.

Each model plays a distinct role in building flexible, reactive, and intelligent systems. Together, they enable developers to transition from procedural automation to autonomous, goal-driven systems.

## Rule-based orchestration
<a name="rule-based-orchestration.168ec9a5-ced9-53fe-9a4a-59d397f7f7e0"></a>

[Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) provides a visual workflow engine to orchestrate services like AWS Lambda, Amazon SageMaker, Amazon Bedrock, Amazon DynamoDB, and Amazon Simple Storage Service (Amazon S3). The logic is deterministic in that steps are explicitly defined, and transitions are condition-based.

Key benefits of rule-based orchestration with Step Functions include the following:
+ Strong auditability and visibility through a visual workflow console
+ Built-in error handling, retries, and parallelism
+ Ideal for linear or branched control flows with well-defined paths

The following diagram shows the workflow of an example use case of document ingestion and processing.

![Rule-based orchestration example of document ingestion and processing.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/images/guide-img/ba00558a-f1cc-4853-9196-e287a2ba5ba5/images/92383708-ecef-4a30-82c2-aee88b03afa9.png)

In this example, a legal firm automates the analysis of uploaded contracts in the following steps:

1. **Event trigger** – Legal documents are uploaded to an Amazon S3 bucket, which triggers an Amazon EventBridge event, which routes to a Step Functions workflow.

1. **Workflow** – Step Functions performs the following steps:

   1. **Document processing** – A Lambda function cleans and performs initial optical character recognition (OCR) on the document.

   1. **Text extraction** – Amazon Textract extracts key text and data from the document.

   1. **Analysis** – Amazon Comprehend analyzes the text to classify risk levels and sentiment.

   1. **Summarization** – Amazon Bedrock generates a concise summary of the contract.

   1. **Data storage** – Results are written to Amazon OpenSearch Service for indexing.

1. **Retrieval** – The legal team can search, filter, and visualize contract analysis through dashboards.

This architecture leverages the AWS SDK integration capabilities of Step Functions to directly interact with each AWS service in the workflow. This approach reduces complexity and eliminates the need for separate Lambda functions between each processing step. The final write to OpenSearch Service is also handled through SDK integration. As a result, Step Functions can index the document analysis results, risk classifications, sentiment analysis, and AI-generated summaries directly into OpenSearch Service. The legal team can access the information through dashboards for searching, filtering, and visualizing contract analysis.

Each task is a defined state with built-in error handling. No decisions are made by the AI, and orchestration is explicit.

## AI-native orchestration with Amazon Bedrock Agents
<a name="ai-native-orchestration-with-9999999999999999br--agents.08d866e9-7e48-50cb-b3db-0456d63f6035"></a>

Where Step Functions manages how things happen, agents for Amazon Bedrock decide what should happen based on user goals. An [Amazon Bedrock agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) or agents built on Amazon Bedrock AgentCore, combine the following:
+ An LLM such as Anthropic Claude or [Amazon Nova](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html)
+ A set of tool integrations such as Lambda functions (or MCP client to execute MCP integrations)
+ Optional knowledge bases for contextual grounding
+ Built-in memory and goal tracking

Agents interpret natural language input, reason about it, and autonomously invoke tools to fulfill the user's intent, offloading orchestration logic to the model.

Key benefits of AI-native orchestration with Amazon Bedrock Agents include the following:
+ **Semantic flexibility** – Interpret varied natural language inputs.
+ **Tool autonomy** – Select the right tools at runtime.
+ **Contextual grounding** - Cite knowledge base content accurately.
+ **Minimal developer maintenance** – Define the tools, and not the flow.

The following diagram shows the workflow of an example use case of customer support automation with Amazon Bedrock Agents.

![Workflow using AI orchestration through Amazon Bedrock Agents.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/images/guide-img/ba00558a-f1cc-4853-9196-e287a2ba5ba5/images/720c62fa-4fb6-484f-9711-a7ac06c13a28.png)

In this example, a user on a retail website types a message in the support chatbot. The following workflow occurs:

1. The event trigger actions are as follows:

   1. User sends a message: "I need to return the shoes I ordered last week. Can you help?"

   1. The message is received and routed through EventBridge.

   1. EventBridge triggers the Amazon Bedrock agent.

1. The agent reasoning process is as follows:

   1. **Intent extraction** – Agent identifies the intent as "return order".

   1. **Data retrieval** – Agent queries the CRM system by using `GetOrderHistory` Lambda function.

   1. **Eligibility check** – Agent calls the `ProcessReturn` Lambda function to verify return eligibility.

   1. **Response generation** – Agent formulates appropriate response.

1. The customer communication action occurs when the agent responds "Your return is being processed. Expect a confirmation email shortly."

The entire workflow demonstrates how Amazon Bedrock Agents orchestrates complex business logic through defined action groups.

Amazon Bedrock AgentCore extends the Amazon Bedrock ecosystem beyond individual agents to provide a complete runtime and memory architecture for autonomous, event-driven AI systems.

Amazon Bedrock Agents focus on orchestrating reasoning and action sequences for a single task or domain. AgentCore provides the underlying infrastructure to compose, coordinate, and persist multi-agent workflows across distributed serverless environments.

The following diagram shows the workflow of an example use case of customer support automation with AgentCore.

![Workflow of customer support automation using Eventbridge, AgentCore, and Lambda.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/images/guide-img/ba00558a-f1cc-4853-9196-e287a2ba5ba5/images/817e4b4a-799b-4055-9f10-016be899f181.png)

This example follows the same actions as the earlier Amazon Bedrock Agents example: a user on a retail website types a message in the support chatbot. The following workflow occurs:

1. User sends a message: "I need to return the shoes I ordered last week. Can you help?"

1. The message is received and routed through EventBridge.

1. EventBridge triggers the AgentCore Runtime endpoint.

AgentCoreintroduces three key capabilities that complement existing orchestration models:
+ **AgentCore Runtime** – A managed execution environment for running custom agent logic within AWS. It integrates natively with AWS Lambda and Amazon ECS to scale agent behavior on demand, removing the need to manage container or function infrastructure manually.
+ **AgentCore Memory** – Provides persistent, structured storage for context, state, and task history. This enables agents to maintain continuity across invocations and workflows, supporting both ephemeral and long-term memory modes. Memory data can be synchronized with DynamoDBor Amazon S3 for observability and compliance.
+ **AgentCore Gateway** – Managed interfaces for securely invoking AWS services and external APIs through Model Context Protocol (MCP). These connectors allow agents to interact directly with enterprise data, tools, and applications, enabling richer orchestration without custom integration code.

Together, these components make it possible to build adaptive, multi-agent systems that operate across serverless, event-driven architectures. For example, AgentCore Runtime can host multiple specialized agents that coordinate through EventBridge or Step Functions, using AgentCore Memory to share context and ensure deterministic, auditable outcomes.

By connecting customer intent with backend systems and processes, AgentCore delivers an automated yet contextually appropriate customer service experience.

The orchestration is not hardcoded. The LLM determines the workflow dynamically, making the system more resilient to variation and ambiguity in inputs.

## Rule-based or AI-native: When to use which?
<a name="rule-based-or-ai-native--when-to-use-which-.8b3dd654-b69b-5c67-be20-48f9a51d6e96"></a>

AWS Step Functions and Amazon Bedrock Agents each excel in different orchestration scenarios. As a best practice, use Step Functions for controlled processes and Amazon Bedrock Agents for natural language interaction and flexible goal fulfillment. The following table compares these services across various use case types.

|
|
| Use case type | Step Functions (Rule-based) | Amazon Bedrock Agents (AI-native) |
| --- |--- |--- |
| Deterministic workflow | Ideal | Not needed. |
| Unstructured user input | Rigid | Interprets and adapts. |
| Complex business rules | Model by using conditions | Can infer by using semantic reasoning. |
| Requires fine-grained audit trail | Full state trace | Limited trace, depending on agent logs. However, tools like weights, biases and model invocation logging can mitigate this limitation. |
| Latency-sensitive automation | Real-time coordination | Real-time, although slightly higher because of LLM processing. |
| Goal-directed user experiences | Requires explicit design | Agent can infer goal and compose flow. |

## Event-driven orchestration
<a name="event-driven-orchestration.9daba4db-3da1-52b8-b983-784cf753f6b2"></a>

Whether using rule-based or AI-native orchestration, events are the mechanism that activate intelligence in a serverless system. In both orchestration models, the following sequence occurs:

1. An event is emitted through EventBridge. Examples of an event are user inputs, document uploads, and transactions.

1. That event triggers the appropriate orchestrator:
   + Step Functions if the logic is deterministic
   + AWS Lambda or Amazon ECS tasks for AWS native runtime subscribed to EventBridge for choreographed design
   + Amazon Bedrock Agents if the logic is dynamic or conversational

1. AgentCore agents can emit and subscribe to EventBridge events natively by using the[AgentCore SDK](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-sdk-memory.html). With this approach, agents can participate directly in serverless workflows while maintaining long-term context through AgentCore Memory. This integration forms a *dual communication layer*:
   + EventBridge provides** **deterministic, auditable event routing.
   + AgentCore Memory \+ A2A** **provides semantic state sharing and capability discovery.

1. Each orchestrator coordinates AI services and emits further events such as completion, error, and downstream triggers.

This reactive model ensures scalability, resilience, and modular design, allowing parts of the system to evolve independently.

## Strategic perspective
<a name="strategic-perspective.f86014b2-5875-5022-a05b-2a482adf77b2"></a>

EDA supports both rule-based orchestration and AI-native orchestration models, and it enables both models to coexist. Step Functions provides reliable, repeatable automation and Amazon Bedrock Agents introduces dynamic, context-aware intelligence.

Together, they provide organizations with the ability to do the following:
+ Automate repetitive, high-volume processes
+ Offer intelligent, adaptive user-facing assistants
+ Scale AI without bottlenecks or architectural rigidity

Orchestration is no longer just about rules, it's about intent interpretation, tool selection, and autonomous execution. Serverless on AWS combines AWS Step Functions for structured workflows and Amazon Bedrock Agents for semantic orchestration. This unified framework enables building the next generation of agentic, serverless AI systems.
