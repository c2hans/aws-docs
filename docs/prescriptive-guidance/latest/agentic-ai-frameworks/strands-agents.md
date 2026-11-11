---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/strands-agents.html
---

# Strands Agents
<a name="strands-agents"></a>

AWS initially released Strands Agents as an open-source SDK, as described in the [AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/). You can use Strands Agents to build autonomous AI agents with a model-driven approach. It provides a flexible, extensible framework that works with AWS services and remains open to integration with third-party components. Strands Agents is suited for building autonomous solutions.

## Key features of Strands Agents
<a name="key-features-of-strands-agents.3ce6e050-ef99-5250-aa04-042ea97ee241"></a>

Strands Agents includes the following key features:
+ **Model-first design** – Built around the concept that the foundation model is the core of agent intelligence, enabling sophisticated autonomous reasoning. For more information, see [Agent Loop](https://strandsagents.com/docs/user-guide/concepts/agents/agent-loop/) in the Strands Agents documentation.
+ **Multi-agent collaboration patterns** – Built-in coordination models such as Swarm, Graph, and Workflow patterns that enable scalable collaboration and governance across distributed agent networks. For more information, see [Multi-agent Patterns](https://strandsagents.com/docs/user-guide/concepts/multi-agent/multi-agent-patterns/) in the Strands Agents documentation.
+ **MCP integration** – Native support for the [Model Context Protocol](https://modelcontextprotocol.io/) (MCP), enabling standardized context provision to LLMs for consistent autonomous operation.
+ **AWS service integration** – Connection to [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/), AWS Lambda, AWS Step Functions, and other AWS services for autonomous workflows. For more information, see [AWS Weekly Roundup](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-strands-agents-aws-transform-amazon-bedrock-guardrails-aws-codebuild-and-more-may-19-2025/) (AWS Blog).
+ **Foundation model selection** – Supports various foundation models including Anthropic Claude, Amazon Nova (Premier, Pro, Lite, and Micro) on Amazon Bedrock, and others so that you can choose a model for different autonomous reasoning capabilities. For more information, see [Amazon Bedrock](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/) in the Strands Agents documentation.
+ **LLM API integration** – Flexible integration with different LLM service interfaces including Amazon Bedrock, OpenAI, and others for production deployment. For more information, see [Amazon Bedrock Basic Usage](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/#basic-usage) in the Strands Agents documentation.
+ **Multimodal capabilities** – Support for multiple modalities including text, speech, and image processing for autonomous agent interactions. For more information, see [Amazon Bedrock Multimodal Support](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/#multimodal-support) in the Strands Agents documentation.
+ **Extensible tool set** – Set of tools for AWS service interaction, with extensibility for custom tools that expand autonomous capabilities. For more information, see [Tools Overview](https://strandsagents.com/docs/user-guide/concepts/tools/) in the Strands Agents documentation.

## When to use Strands Agents
<a name="when-to-use-strands-agents.992f2178-b29e-5446-be4f-32a78fa83c68"></a>

Strands Agents is particularly well-suited for autonomous agent scenarios including:
+ Organizations that build on AWS infrastructure who want native integration with AWS services for autonomous workflows
+ Teams that require security, scalability, and compliance features for production autonomous systems
+ Projects that need flexibility in model selection across different providers for specialized autonomous tasks
+ Use cases that require integration with existing AWS workflows and resources for autonomous processes

## Implementation approach for Strands Agents
<a name="implementation-approach-for-strands-agents.749da980-cf94-517d-962c-75f364fa3d30"></a>

The Strands Agents implementation approach is outlined in the [Quickstart Guide for Python](https://strandsagents.com/docs/user-guide/quickstart/python/) and [Quickstart Guide for TypeScript](https://strandsagents.com/docs/user-guide/quickstart/typescript/). With the framework, you can:
+ Select foundation models like Amazon Nova (Premier, Pro, Lite, or Micro) on Amazon Bedrock based on specific business requirements.
+ Define custom tools that connect to enterprise systems and data sources.
+ Process multiple modalities including text, images, and speech.
+ Deploy agents that can autonomously respond to business queries and perform tasks.

This implementation approach helps teams develop and deploy autonomous agents without building or training their own AI models.

## Real-world example of Strands Agents
<a name="real-world-example-of-strands-agents.9942f663-1244-55d9-b468-47155df38a22"></a>

AWS Transform for .NET uses Strands Agents to power its application modernization capabilities, as described in [AWS Transform for .NET, the first agentic AI service for modernizing .NET applications at scale](https://aws.amazon.com/blogs/aws/aws-transform-for-net-the-first-agentic-ai-service-for-modernizing-net-applications-at-scale/) (AWS Blog). This production service uses multiple specialized autonomous agents. The agents work together to analyze legacy .NET applications, plan modernization strategies, and run code transformations to cloud-native architectures. [AWS Transform for .NET](https://aws.amazon.com/transform/net/) is an example of Strands Agents used in a production autonomous system.
