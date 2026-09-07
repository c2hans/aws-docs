---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/tool-based-agents-for-calling-functions.html
---

# Tool-based agents for calling functions
<a name="tool-based-agents-for-calling-functions"></a>

Tool-based agents extend the capabilities of reasoning agents by invoking external functions or APIs to complete tasks that go beyond language-only reasoning. This pattern uses an LLM to decide which tool to use and then generates call arguments and incorporates a tool's output into its reasoning loop.

This pattern enables agents to act rather than just providing responses. The tool interface represents any callable capability, ranging from arithmetic calculations and database lookups to external APIs and cloud services.

## Architecture
<a name="architecture.b7abdd25-217a-55d5-a22d-27ef9aee5883"></a>

A tool-based agent for calling functions is shown in the following diagram:

![Tool-based agent for calling functions.](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/43d85cc3-6a29-48d3-a5c9-4480fe0878e5.png)

## Description
<a name="description.d186bc09-6d75-5791-a6dd-35a85d70fcf0"></a>

1. Receives query
   + The agent receives a natural-language query or task from the user or calling system.

1. Searches for tools
   + The agent uses internal metadata or a tool registry to search for available tools, schemas, and relevant capabilities.

1. Selects and invokes tools
   + The LLM receives the query and tool metadata (for example, function names, input types, and descriptions) in its prompt.
   + It chooses the most relevant tool, constructs input arguments, and returns a structured function call.

1. Runs the chosen tool
   + The agent shell or tool runner executes the selected function and returns the result (for example, an API output, database value, or computation).

1. Returns a response
   + The LLM passes results to the agent, either directly or as part of an updated prompt. It then returns a natural-language result.

## Capabilities
<a name="capabilities.2d71407b-4286-5b80-8055-22c0c81d67b9"></a>
+ Dynamic tool selection based on task context
+ Schema-based prompting (OpenAPI, JSON schema, AWS function interface)
+ Results interpretation and chaining of outputs into reasoning
+ Stateless or session-aware operations

## Common use cases
<a name="common-use-cases.633cc1f9-0137-561a-af5c-bd2deb9536ac"></a>
+ Virtual assistants with external data access
+ Financial calculators and estimators
+ API-based knowledge workers
+ LLMs that invoke AWS Lambda, Amazon SageMaker endpoints, and SaaS services

## Implementation guidance
<a name="implementation-guidance.89581a34-f92f-5ec6-9d25-47f59bd1403f"></a>

Use the following to create tool-based agents for calling functions:
+ Amazon Bedrock with function-calling support (Anthropic Claude)
+ AWS Lambda as a tool-execution backend
+ Amazon API Gateway or AWS Step Functions for tool orchestration
+ Amazon DynamoDB or Amazon Relational Database Service (Amazon RDS) for context-aware tool metadata
+ Amazon EventBridge pipelines or AWS Step Functions that map states to route outputs

## Summary
<a name="summary.8682fe66-24d1-52a5-be21-b55380e07941"></a>

Tool-based function-calling agents represent a shift from understanding language to performing actions. These agents invoke dynamic, context-aware tools while maintaining LLM reasoning, transforming passive assistants into systems that complete tasks, access services, and integrate business operations. This pattern is an important component of agentic AI in enterprise settings, especially when combined with declarative schemas, authorization frameworks, and multi-agent systems.
