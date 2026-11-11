---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/langchain-langgraph.html
---

# LangChain and LangGraph
<a name="langchain-langgraph"></a>

LangChain is an established framework for building agentic AI applications. LangGraph extends its capabilities to support complex, stateful agent workflows, as described in the [LangChain Blog](https://blog.langchain.dev/how-to-think-about-agent-frameworks/). Together, they provide orchestration capabilities for building autonomous AI agents that operate independently.

## Key features of LangChain and LangGraph
<a name="key-features-of-langchain-and-langgraph.be3df15e-1f10-5492-9e92-96bbdea2eee6"></a>

LangChain and LangGraph include the following key features:
+ **Component library** – Library of prebuilt components for various autonomous agent capabilities, enabling rapid development of specialized agents. For more information, see the [LangChain documentation](https://python.langchain.com/docs/get_started/introduction).
+ **Foundation model selection** – Support for diverse foundation models including Anthropic Claude, Amazon Nova models (Premier, Pro, Lite, and Micro) on Amazon Bedrock, and others for different reasoning capabilities. For more information, see [Inputs and outputs](https://python.langchain.com/docs/concepts/chat_models/#inputs-and-outputs) in the LangChain documentation.
+ **LLM API integration** – Standardized interfaces for multiple large language model (LLM) service providers including Amazon Bedrock, OpenAI, and others for flexible deployment. For more information, see [LLMs](https://python.langchain.com/docs/integrations/llms/) in the LangChain documentation.
+ **Multimodal processing** – Built-in support for text, image, and audio processing to enable rich multimodal autonomous agent interactions. For more information, see [Multimodality](https://python.langchain.com/docs/concepts/chat_models/#multimodality) in the LangChain documentation.
+ **Graph-based workflows** – LangGraph enables defining complex autonomous agent behaviors as state machines, supporting sophisticated decision logic. For more information, see the [LangGraph Platform GA](https://blog.langchain.dev/langgraph-platform-ga/) announcement.
+ **Memory abstractions** – Multiple options for short-term and long-term memory management, which helps autonomous agents maintain context over time. For more information, see [How to add memory to chatbots](https://python.langchain.com/docs/how_to/chatbots_memory/) in the LangChain documentation.
+ **Tool integration** – Integrations with a variety of tools, services, and APIs that extend autonomous agent capabilities. For more information, see [Tools](https://python.langchain.com/docs/how_to/#tools) in the LangChain documentation.
+ **LangGraph Platform** – Managed deployment and monitoring solution for production environments, supporting long-running autonomous agents. For more information, see the [LangGraph Platform GA](https://blog.langchain.dev/langgraph-platform-ga/) announcement.

## When to use LangChain and LangGraph
<a name="when-to-use-langchain-and-langgraph.fe5be762-fefc-5751-935e-bb2ac95fa07f"></a>

LangChain and LangGraph are particularly well-suited for autonomous agent scenarios including:
+ Complex multi-step reasoning workflows that require sophisticated orchestration for autonomous decision-making
+ Projects that need access to a wide range of prebuilt components and integrations for diverse autonomous capabilities
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
<a name="real-world-example-of-langchain-and-langgraph.003eebbb-1a7d-5972-b5d9-c8fb2e545911"></a>

A telecommunications company implemented autonomous agents using LangChain and LangGraph to enhance its data engineering and operations workflows, as detailed in a [LangChain Enterprise case study](https://blog.langchain.com/customers-vodafone/). The company built internal AI assistants that autonomously monitor performance metrics, retrieve information from documentation systems, and present actionable insights through natural language interactions.

The implementation used LangChain modular document loaders, vector integration, and support for multiple LLMs (OpenAI, Llama 3, and Gemini) to rapidly prototype and benchmark these pipelines. The team then used LangGraph to structure the multi-agent orchestration by deploying modular subagents. These agents perform collection, processing, summarization, and reasoning tasks. The team integrated these agents into their cloud systems through APIs.
