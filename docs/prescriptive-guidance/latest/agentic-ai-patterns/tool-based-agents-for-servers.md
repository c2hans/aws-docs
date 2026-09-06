---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/tool-based-agents-for-servers.html
---

# Tool-based agents for servers
<a name="tool-based-agents-for-servers"></a>

Tool-based agents for servers enhance function-calling agents by delegating tool execution to an external server that has a dedicated runtime environment for tools, scripts, and composite agents. Unlike inline function calls that the agent loop selects and invokes, server-based agents outsource the logic and execution pipeline to other agents or systems. This provides advanced capabilities like multitool chaining, isolated execution, and specialized reasoning. Tool servers are ideal for complex, stateful, or resource-intensive actions where the tools themselves may involve separate AI models, business rules, or environments.

## Architecture
<a name="architecture.3753e2e8-35bb-598e-8b6a-354b4de7eb5e"></a>

The following is a pattern for tool-based agents for servers:

![Tool-based agents for servers.](http://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/images/guide-img/cde5ee68-ed86-4053-9fb1-d0dbf7199e24/images/358e8438-9ebf-470a-8579-d91e26cf57b8.png)

## Description
<a name="description.70b5e24c-9607-5c58-8c06-8aeaf2aa2fbc"></a>

1. Receives query
   + A user or system submits a request to the agent shell.
   + The agent interprets the query and prepares to dispatch it to a tool server.

1. Runs tool server processes
   + The agent sends the task, along with structured parameters, to a tool server.
   + The tool server may then:
     + Run scripts or logic in dedicated compute systems (for example, AWS Lambda, containers, or Amazon SageMaker)
     + Use its own subagent with LLM reasoning to select and run tools
     + Manage dependencies, retries, or multistep execution flows
     + Output results to the primary agent when the task is complete

1. Uses LLM reasoning with tool output
   + The agent invokes an LLM, passing the original query and the tool server result as part of the prompt.
   + The LLM synthesizes a response that incorporates the newly acquired information.

1. Returns a response
   + The agent returns a natural-language or structured response to the user or calling system.
   + (Optional) Results may be stored in memory or audit logs.

## Capabilities
<a name="capabilities.2d76f995-dbac-5e0b-a697-c08772ed1d23"></a>
+ Tools are invoked outside of the primary agent execution loop
+ Tool execution may involve LLM calls, logic chains, or subagents
+ Agent acts as a controller or dispatcher, not just a tool wrapper
+ Enables composability, scalability, and isolation of logic

## Common use cases
<a name="common-use-cases.92bc93db-09c7-5b54-b49e-3a219069334a"></a>
+ Orchestrating model chains (for example, by combining LLM, vision, and code)
+ AI-driven automation pipelines
+ DevOps assistant agents with script runners
+ Complex financial computation, simulation, or optimization agents
+ Multimodal tools (for example, by combining audio, documentation, and action)

## Implementation guidance
<a name="implementation-guidance.4d83e5e1-8d2e-573e-a1c5-ae50cd73445d"></a>

You can build this pattern using the following AWS services:
+ Amazon Bedrock (agent host and LLM inference)
+ AWS Lambda, Amazon ECS, AWS Fargate, or Amazon SageMaker endpoints as the tool server runtime
+ Amazon API Gateway or AWS App Runner to expose tool server APIs
+ Amazon EventBridge for decoupled agent-to-tool messaging
+ AWS Step Functions or AWS AppFabric for composing multi-agent logic on the tool server

## Summary
<a name="summary.67a6bac9-449e-5331-a6ab-12597cdce78c"></a>

Tool-based agents that use servers are highly modular and scalable. They decouple decision logic from execution, which allows the primary agent to remain lightweight while offloading complex or sensitive actions to other systems. This is important for enterprise-grade agentic AI, especially in environments that require governance, observability, isolation, dynamic composition, or any combination thereof.
