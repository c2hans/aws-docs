---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/pattern-grounded-agent-ai.html
---

# Pattern 5: Grounded agent AI workflow
<a name="pattern-grounded-agent-ai"></a>

Large language models (LLMs) are powerful, but they're unbounded by default. They lack awareness of proprietary data, business rules, or operational constraints, making them risky for direct interaction with users or systems.

Enterprises face the following common challenges:
+ LLMs hallucinate when they don't know the answer, posing risks to trust and compliance.
+ Responses lack grounding in domain-specific facts, policies, or real-time state (for example, orders, accounts, and entitlements).
+ Dynamic task automation (for example, order lookups, support triage, and IT operations) often requires invoking real APIs and tools, not just generating text.
+ Building traditional intent routers, dialog managers, and rule-based flows is costly, brittle, and unscalable.

To address these challenges, businesses want agents that reason intelligently, act autonomously, and remain grounded in fact.

## The grounded agent AI workflow: Autonomous intelligence with trust and context
<a name="the-grounded-agent-ai-workflow--autonomous-intelligence-with-trust-and-context.5d2751a3-ddee-5da7-b6da-c786a1312c93"></a>

The *grounded agent AI workflow* pattern uses [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) to orchestrate semantic reasoning, tool invocation, and knowledge grounding. The agents enable AI assistants to take user input, understand intent, and complete multi-step tasks by using enterprise APIs and documents.

Unlike simple chatbots or static LLM prompts, Amazon Bedrock agents:
+ Interpret natural language goals.
+ Select and invoke tools (by using AWS Lambda functions) dynamically.
+ Search or query knowledge bases to stay grounded in enterprise truth.
+ Return contextual, multi-step responses with traceability and actionability.

The reference architecture implements each layer as follows:
+ **Event trigger** – Uses [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html), chatbot UI, or support portal to trigger agent interaction through Amazon Bedrock
+ **Processing** – Implements [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) to format input, apply security context (for example, user roles or entitlements), and enrich metadata
+ **Inference** – Uses Amazon Bedrock agent to receive the prompt, invoke Lambda tools (for example, `getOrderStatus`), perform grounding through a knowledge base, and assemble a final response
+ **Post-processing** – Uses Lambda to inspect agent output (for example, escalate if "order lost" and notify support team)
+ **Output** – Returns agent response to UI or logs it to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) (Amazon S3) or [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) for audit, training, or analytics

## Use case: Retail customer service agent
<a name="use-case--retail-customer-service-agent.84cbafba-0646-5d35-90f6-9b1f4138959c"></a>

A global retailer wants to automate responses to common customer inquiries like: "Where is my order?", "I want to return these shoes.", and "Do I need to pay for return shipping?"

The answers depend on factors such as the customer's real-time order data, return eligibility and timelines, and region-specific policies.

In response to this use case, the agent-based workflow follows these steps:

1. User enters their query by using an app or chat.

1. API Gateway routes the query to the Amazon Bedrock agent.

1. The agent performs the following actions:
   + Parses intent ("return request")
   + Invokes a Lambda tool `lookupOrderStatus`
   + Performs a policy lookup through the knowledge base
   + Calls `initiateReturn `if eligible
   + Composes a full response: "Your return has been initiated. Expect to receive a label in an email message."

All actions are grounded, logged, and performed within enterprise guardrails.

## Key features of Amazon Bedrock Agents in this pattern
<a name="key-features-of-9999999999999999brlong--agents-in-this-pattern.2841fb2d-528c-574e-8d52-fa50250fb762"></a>

For the grounded agent AI workflow pattern, Amazon Bedrock agents provide the following key features and benefits:
+ **Tool selection** enables an agent to choose the correct Lambda function (tool) for each task.
+ **Memory and session state** allows agents to maintain context across turns.
+ **Grounded answers** retrieve authoritative data from knowledge bases stored in Amazon S3.
+ **Chain of thought (CoT) reasoning** enables an agent to decompose complex prompts into subgoals and act sequentially.
+ **Security context** allows tools to be scoped according to tenant, user, or role by using AWS Identity and Access Management (IAM) and contextual parameters.

## Governance and controls best practices for the grounded agent AI workflow pattern
<a name="governance-and-controls-best-practices-for-the-grounded-agent-ai-workflow-pattern.e6997084-6e56-59bb-a7fc-8430b53148a6"></a>

To make grounded agent AI workflows enterprise-ready, organizations should consider the following controls:
+ Version control agent configurations (for example, tools, instructions, and knowledge bases).
+ Use structured logs and trace IDs for auditability.
+ Apply prompt policies, allowlists, and moderation checks.
+ Define fallback flows (for example, escalate to human or reroute to static FAQ).

These controls can be orchestrated using Lambda, EventBridge, and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) around the agent core.

## Business value of the grounded agent AI workflow pattern
<a name="business-value-of-the-grounded-agent-ai-workflow-pattern.a0a9ebbe-bc58-5e7c-b5a6-ebff264e983a"></a>

This pattern delivers value in the following areas:
+ **Customer experience** – Enables self-service resolution for 70–80 percent of inquiries without escalation
+ **Operational efficiency** – Reduces support ticket volume and triage overhead
+ **Time to resolution** – Provides instant answers using real data—not waiting on human agents
+ **Scalability** – Handles thousands of concurrent interactions with no human headcount growth
+ **Cross-domain reuse** – Applies same pattern to multiple domains such as IT support, HR helpdesk, legal Q&A, and more

The grounded agent AI workflow enables enterprises to move beyond static Q&A and into goal-driven automation, without sacrificing control, compliance, or accuracy. By combining LLM reasoning with secure, serverless API execution and knowledge retrieval, Amazon Bedrock Agents deliver AI capabilities that act, not just respond.

The grounded agent is the architecture of intelligent enterprise interaction, modular, grounded, and ready for scale.
