---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/agentic-ai-emergence.html
---

# Timelines converge: the emergence of agentic AI
<a name="agentic-ai-emergence"></a>

## 2023-2024 - enterprise-grade agent platforms
<a name="enterprise-platform"></a>

The convergence of distributed software agent architectures and transformer-based LLMs culminated in the rise of agentic AI.
+ [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) introduced a fully managed way to build goal-driven, tool-using software agents by using foundation models from Amazon Bedrock.
+ The** **Model Context Protocol (MCP) from Anthropic defined a method for large language models to access, and interact with, external tools, environments, and memory. This is key for contextual, persistent, and autonomous behavior.

These two milestones represent the synthesis of agency and intelligence. Agents were no longer limited to static workflows or rigid automation. They could now reason across multiple steps, coordinate with tools and APIs, maintain contextual state, and learn and adapt over time.

## January-June 2025 - expanded enterprise capabilities
<a name="enterprise-advanced"></a>

In the first half of 2025, the agentic AI landscape expanded significantly with new enterprise capabilities. In February 2025, Anthropic released Claude 3.7 Sonnet, which was the first hybrid reasoning model on the market, and the MCP specification gained widespread adoption.

AI coding assistants such as [Amazon Q Developer](https://aws.amazon.com/q/developer/), Cursor, and WindSurf integrated MCP to standardize code generation, repository analysis, and development workflows. The MCP March 2025 release introduced significant enterprise-ready features, including OAuth 2.1 security integration, expanded resource types for diverse data access, and enhanced connectivity options through Streamable HTTP. Building on this foundation, AWS announced in May 2025 that it was joining the MCP steering committee and contributing to new agent-to-agent communication capabilities. This further strengthens the protocol's position as an industry standard for agentic AI interoperability.

In May 2025, AWS strengthened customer options for building agentic AI workflows by open sourcing the [Strands Agents framework](https://strandsagents.com/). This provider-independent and model-agnostic framework enables developers to use foundation models across platforms while maintaining deep AWS service integration. As highlighted in the [AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/), Strands Agents follows a model-first design philosophy that places foundation models at the core of agent intelligence. This makes it easier for customers to build and deploy sophisticated AI agents for their specific use cases.

## Emergence - agentic AI
<a name="current"></a>

The evolution of software agents, from early ideas of autonomy to modern, LLM-enabled orchestration, has been long and layered. What began with Oliver Selfridge's vision of perceiving programs has grown into a robust ecosystem of intelligent, context-aware, goal-driven software agents that can collaborate, adapt, and reason.

The convergence of distributed artificial intelligence (DAI) and transformer-based generative AI marks the beginning of a new era in which software agents are no longer only tools, but autonomous actors in intelligent systems.

Agentic AI represents the next evolution in software systems. It provides a class of intelligent agents that are autonomous, asynchronous, and agentic, and can act with delegated intent and operate purposefully within dynamic, distributed environments. Agentic AI unifies the following:
+ The architectural lineage of multi-agent systems and the actor model
+ The cognitive model of perceive, reason, act
+ The generative power of LLMs and transformers
+ The operational flexibility of cloud-native and serverless computing

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
