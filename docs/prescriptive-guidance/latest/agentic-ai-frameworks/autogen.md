---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/autogen.html
---

# AutoGen
<a name="autogen"></a>

AutoGen is an open-source framework that was released initially by Microsoft. AutoGen focuses on enabling conversational and collaborative autonomous AI agents. It provides a flexible architecture for building multi-agent systems with an emphasis on asynchronous, event-driven interactions between agents for complex autonomous workflows.

## Key features of AutoGen
<a name="key-features-of-autogen.faa3b341-5b6d-54b0-bed9-0d71c79c3c00"></a>

AutoGen provides the following key features:
+ **Conversational agents** – Built around natural language conversations between autonomous agents, enabling sophisticated reasoning through dialogue. For more information, see [Multi-agent Conversation Framework](https://microsoft.github.io/autogen/docs/Use-Cases/agent_chat) in the AutoGen documentation.
+ **Asynchronous architecture** – Event-driven design for non-blocking autonomous agent interactions, supporting complex parallel workflows. For more information, see [Solving Multiple Tasks in a Sequence of Async Chats](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_multi_task_async_chats/) in the AutoGen documentation.
+ **Human-in-the-loop** – Strong support for optional human participation in otherwise autonomous agent workflows when needed. For more information, see [Allowing Human Feedback in Agents documentation](https://microsoft.github.io/autogen/0.2/docs/tutorial/human-in-the-loop/) in the AutoGen documentation.
+ **Code generation and execution** – Specialized capabilities for code-focused autonomous agents that can write and run code. For more information, see [Code Execution](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/code-execution-groupchat.html) in the AutoGen documentation.
+ **Customizable behaviors** – Flexible autonomous agent configuration and conversation control for diverse use cases. For more information, see [agentchat.conversable\_agent](https://microsoft.github.io/autogen/docs/reference/agentchat/conversable_agent) in the AutoGen documentation.
+ **Foundation model selection** – Support for various foundation models including Anthropic Claude, Amazon Nova models (Premier, Pro, Lite, and Micro) on Amazon Bedrock, and others for different autonomous reasoning capabilities. For more information, see [LLM Configuration](https://microsoft.github.io/autogen/docs/topics/llm_configuration) in the AutoGen documentation.
+ **LLM API integration** – Standardized configuration for multiple LLM service interfaces including Amazon Bedrock, OpenAI, and Azure OpenAI. For more information, see [oai.openai\_utils](https://microsoft.github.io/autogen/docs/reference/oai/openai_utils) in the AutoGen API Reference.
+ **Multimodal processing** – Support for text and image processing to enable rich multimodal autonomous agent interactions. For more information, see [Engaging with Multimodal Models: GPT-4V in AutoGen](https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_lmm_gpt-4v/) in the AutoGen documentation.

## When to use AutoGen
<a name="when-to-use-autogen.33854b21-fea4-582d-93eb-bfa83d94afda"></a>

AutoGen is particularly well-suited for autonomous agent scenarios including:
+ Applications that require natural conversational flows between autonomous agents for complex reasoning
+ Projects that need both fully autonomous operation and optional human oversight capabilities
+ Use cases that involve autonomous code generation, execution, and debugging without human intervention
+ Scenarios that require flexible, asynchronous autonomous agent communication patterns

## Implementation approach for AutoGen
<a name="implementation-approach-for-autogen.09e576a8-1cc5-59b0-82dc-6c56da3920b8"></a>

AutoGen provides a conversational implementation approach for business stakeholders, as detailed in [Getting Started](https://microsoft.github.io/autogen/docs/Getting-Started) in the AutoGen documentation. The framework enables organizations to:
+ Create autonomous agents that communicate through natural language conversations.
+ Implement asynchronous, event-driven interactions between multiple agents.
+ Combine fully autonomous operation with optional human oversight when needed.
+ Develop specialized agents for different business functions that collaborate through dialogue.

This conversational approach makes the autonomous system's reasoning transparent and accessible to business users. Decision-makers can observe the dialogue between agents to understand how conclusions are reached and optionally participate in the conversation when human judgment is required.

## Real-world example of AutoGen
<a name="real-world-example-of-autogen.e8d7db0d-1121-563a-a195-35d5a69fb0b4"></a>

Magentic‑One is an open‑source, generalist multi‑agent system designed to autonomously solve complex, multi‑step tasks across diverse environments, as described in the [Microsoft AI Frontiers blog](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/). At its core is the Orchestrator agent, which decomposes high‑level goals and tracks progress by using structured ledgers. This agent delegates subtasks to specialized agents (such as WebSurfer, FileSurfer, Coder, and ComputerTerminal) and adapts dynamically by re‑planning when necessary.

The system is built on the AutoGen framework and is model‑agnostic, defaulting to GPT‑4o. It achieves state‑of‑the‑art performance across benchmarks like GAIA, AssistantBench, and WebArena—all without task‑specific tuning. Additionally, it supports modular extensibility and rigorous evaluation through AutoGenBench suggestions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
