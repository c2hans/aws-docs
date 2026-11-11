---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/amazon-bedrock-agent-core.html
---

# Amazon Bedrock AgentCore
<a name="amazon-bedrock-agent-core"></a>

[Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/) is an agentic service that helps you build, deploy, and operate highly capable agents securely at scale by using any framework, model, or protocol. With AgentCore, you can do the following, all without infrastructure management:
+ Build agents faster.
+ Enable agents to take actions across tools and data.
+ Run agents securely with low-latency and extended runtimes.
+ Monitor agents in production.

AgentCore reduces the effort of building specialized agent infrastructure, so you can move your agents to production faster. You can use its services together or independently, and they are compatible with frameworks such as CrewAI, LangGraph, LlamaIndex, and Strands Agents. AgentCore is also compatible with foundation models that are available in or outside of Amazon Bedrock, providing flexibility in your model choice.

AgentCore is composed of several key services:
+ [Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)** **– Provides a secure, serverless, scalable environment to host and run your agents, without needing to manage any infrastructure required for deploying and running AI agents or tools.
+ [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)** **– Offers a managed memory system, enabling agents to retain context from interactions for more personalized and coherent conversations by maintaining both immediate and long-term knowledge.
+ [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)** **– Simplifies the process of creating, securing, and finding the right tools for agents. With AgentCore Gateway, developers can convert APIs, AWS Lambda functions, and existing services into Model Context Protocol (MCP)-compatible tools and make them available to agents.
+ [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) – Provides a secure, scalable agent identity and access management service that accelerates AI agent development. With AgentCore Identity, you can assign unique, verifiable identities to agents, enabling fine-grained access control and secure agent-powered interactions with enterprise systems.
+ [Amazon Bedrock AgentCore built-in tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-tools.html) – Enables you to use built-in tools to enhance your development and testing workflow. Use these tools to interact with your application, enabling AI agents to write and run code securely in sandbox environments. Use the browser tool to enable AI agents to interact with websites at scale.
+ [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) – Delivers logging and monitoring capabilities, giving you real-time visibility into your agent's performance and behavior to facilitate debugging and optimization.

## Key features of AgentCore
<a name="key-features-of-9999999999999999brac-.063d15b9-7380-5d25-bd2f-daefb90f7ecd"></a>

AgentCore includes the following key features:
+ **Fully managed and extensible** – AgentCore is a fully managed service, which means that AWS handles the underlying infrastructure and maintenance. It is also extensible, which allows you to customize and enhance the functionality of your agents. For more information, see [Get started with Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-getting-started.html) in the AgentCore documentation.
+ **Long-term and short-term memory** – Deliver more personalized and relevant interactions by equipping agents with a memory system to recall context from current conversations and long-term knowledge. For more information, see [Get started with AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-getting-started.html) in the AgentCore documentation.
+ **Simplified tool development and integration** – Enable your agents to discover and use tools through a single, secure endpoint. Quickly turn your existing enterprise resources into agent-ready tools with just a few lines of code, freeing developers to focus on building unique capabilities. For more information, see [Get started with AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-quick-start.html) in the AgentCore documentation.
+ **Secure and scalable infrastructure** – AgentCore provides a secure and scalable environment for deploying and operating agents. It includes features for identity and access management, data encryption, and network security. For more information, see [Get started with Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-getting-started.html) in the AgentCore documentation.
+ **Integration with a wide range of tools** – Allows you to integrate your agents with a variety of tools, including a code interpreter and a browser tool that you can build by using the AgentCore built-in tools. For more information, see [Get started with AgentCore Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-getting-started.html) and [Get started with AgentCore Browser](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-onboarding.html) in the AgentCore documentation.
+ **Comprehensive observability and monitoring** – Gain deep visibility into your agents with comprehensive tools to trace, debug, and monitor their performance in production. Visualize the agent's entire execution path to audit its reasoning and resolve failures. Use real-time dashboards and standardized telemetry data to track key operational metrics. For more information, see [Add observability to your Amazon Bedrock AgentCore resources](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html) in the AgentCore documentation.

## When to use AgentCore
<a name="when-to-use-9999999999999999brac-.131033c3-940a-5996-bac0-317205b3b950"></a>

AgentCore is particularly well-suited for autonomous agent scenarios including:
+ Organizations that want to accelerate development and lower operational overhead with a fully managed service that handles infrastructure, security, built-in tools, observability, and scaling
+ Projects that need flexibility with modular services that work together or independently and are compatible with any framework, like CrewAI or LangGraph, and any foundation model from any source
+ Use cases that require stateful, conversational agents that need to maintain context and learn from past interactions to provide personalized and relevant responses
+ Agents that perform complex tasks through simple integration with diverse applications, data sources, and APIs

## Implementation approach for AgentCore
<a name="implementation-approach-for-9999999999999999brac-.662fe5bb-d34e-5897-86d0-e42ee7055e6d"></a>

AgentCore is designed for organizations that want to move AI agents from proof of concept to production, including agents built by using open source or custom agent frameworks. With AgentCore, organizations can do the following:
+ Deploy agents securely on serverless infrastructure, supporting any framework and model, with session isolation and built-in identity and access management to help support your security and compliance requirements. Quickly create AgentCore Runtime agents for leading agent frameworks by using the starter toolkit.
+ Enhance agents by integrating persistent memory for context retention, and simplify tool development and integration through AgentCore Gateway. Use the built-in browser tool and code interpreter for advanced workflows.
+ Trace, debug, and monitor AI agents in production by using observability dashboards powered by Amazon CloudWatch and OpenTelemetry, and track key metrics of AgentCore resources (runtime, memory, gateway, and tools).
+ Accelerate deployment and innovation with fully managed, modular services. Use the services as composable building blocks together or independently with any agent framework and model provider. This flexibility helps organizations move from prototype to production faster.

This managed approach enables organizations to quickly and securely build, deploy, and run enterprise-grade AI agents and multi-agent systems at any scale.

## Real-world example of AgentCore
<a name="real-world-example-of-9999999999999999brac-.833530c6-88b2-5b9d-8384-252f0cd345f0"></a>

AWS has observed that one of Latin America's largest banks has used AI/ML for years to deliver a personalized and secure digital banking experience. The bank is expanding its agentic AI services by using AgentCore to provide customers with intuitive interactions, enhanced security, and greater automation. AgentCore is expected to support the bank's efforts to meet customer commitments at scale. AgentCore provides the bank's developers with the tools and flexibility to build and manage agents, while helping support compliance with financial regulations.
