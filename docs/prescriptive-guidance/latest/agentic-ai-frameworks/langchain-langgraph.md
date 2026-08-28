---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/langchain-langgraph.html
---

# LangChain and LangGraph
<a name="langchain-langgraph"></a>

LangChain is one of the most established frameworks in the agentic AI ecosystem. LangGraph extends its capabilities to support complex, stateful agent workflows as described in the [LangChain Blog](https://blog.langchain.dev/how-to-think-about-agent-frameworks/). Together, they provide a comprehensive solution for building sophisticated autonomous AI agents with rich orchestration capabilities for independent operation.

## Key features of LangChain and LangGraph
<a name="key-features-of-langchain-and-langgraph.34acca57-6cd4-59bb-aed5-402ddd656fe5"></a>

LangChain and LangGraph include the following key features:
+ **Component ecosystem** – Extensive library of pre-built components for various autonomous agent capabilities, enabling rapid development of specialized agents. For more information, see the [LangChain documentation](https://python.langchain.com/docs/get_started/introduction).
+ **Foundation model selection** – Support for diverse foundation models including Anthropic Claude, Amazon Nova models (Premier, Pro, Lite, and Micro) on Amazon Bedrock, and others for different reasoning capabilities. For more information, see [Inputs and outputs](https://python.langchain.com/docs/concepts/chat_models/#inputs-and-outputs) in the LangChain documentation.
+ **LLM API integration** – Standardized interfaces for multiple large language model (LLM) service providers including Amazon Bedrock, OpenAI, and others for flexible deployment. For more information, see [LLMs](https://python.langchain.com/docs/integrations/llms/) in the LangChain documentation.
+ **Multimodal processing** – Built-in support for text, image, and audio processing to enable rich multimodal autonomous agent interactions. For more information, see [Multimodality](https://python.langchain.com/docs/concepts/chat_models/#multimodality) in the LangChain documentation.
+ **Graph-based workflows** – LangGraph enables defining complex autonomous agent behaviors as state machines, supporting sophisticated decision logic. For more information, see the [LangGraph Platform GA](https://blog.langchain.dev/langgraph-platform-ga/) announcement.
+ **Memory abstractions** – Multiple options for short and long-term memory management, which is essential for autonomous agents that maintain context over time. For more information, see [How to add memory to chatbots](https://python.langchain.com/docs/how_to/chatbots_memory/) in the LangChain documentation.
+ **Tool integration** – Rich ecosystem of tool integrations across various services and APIs, extending autonomous agent capabilities. For more information, see [Tools](https://python.langchain.com/docs/how_to/#tools) in the LangChain documentation.
+ **LangGraph platform** – Managed deployment and monitoring solution for production environments, supporting long-running autonomous agents. For more information, see the [LangGraph Platform GA](https://blog.langchain.dev/langgraph-platform-ga/) announcement.

## When to use LangChain and LangGraph
<a name="when-to-use-langchain-and-langgraph.14ff5341-306d-5e52-897a-082079755daf"></a>

LangChain and LangGraph are particularly well-suited for autonomous agent scenarios including:
+ Complex multi-step reasoning workflows that require sophisticated orchestration for autonomous decision-making
+ Projects that need access to a large ecosystem of prebuilt components and integrations for diverse autonomous capabilities
+ Teams with existing Python-based machine learning (ML) infrastructure and expertise that want to build autonomous systems
+ Use cases that require complex state management across long-running autonomous agent sessions

## Implementation approach for LangChain and LangGraph
<a name="implementation-approach-for-langchain-and-langgraph.41c8210c-d4f6-5756-be37-4f62db3411a8"></a>

LangChain and LangGraph provide a structured implementation approach for business stakeholders, as detailed in the [LangGraph documentation](https://python.langchain.com/docs/langgraph). The framework enables organizations to:
+ Define sophisticated workflow graphs that represent business processes.
+ Create multi-step reasoning patterns with decision points and conditional logic.
+ Integrate multimodal processing capabilities for handling diverse data types.
+ Implement quality control through built-in review and validation mechanisms.

This graph-based approach allows business teams to model complex decision processes as autonomous workflows. Teams have clear visibility into each step of the reasoning process and the ability to audit decision paths.

## Real-world example of LangChain and LangGraph
<a name="real-world-example-of-langchain-and-langgraph.cdcb9363-35b6-5709-98ad-3a6078667ce6"></a>

Vodafone has implemented autonomous agents using LangChain (and LangGraph) to enhance its data engineering and operations workflows, as detailed in their [LangChain Enterprise case study](https://blog.langchain.com/customers-vodafone/). They built internal AI assistants that autonomously monitor performance metrics, retrieve information from documentation systems, and present actionable insights—all through natural language interactions.

The Vodafone implementation uses LangChain modular document loaders, vector integration, and support for multiple LLMs (OpenAI, LLaMA 3, and Gemini) to rapidly prototype and benchmark these pipelines. They then used LangGraph to structure the multi-agent orchestration by deploying modular sub agents. These agents perform collection, processing, summarization, and reasoning tasks. LangGraph integrated these agents through APIs into their cloud systems.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
