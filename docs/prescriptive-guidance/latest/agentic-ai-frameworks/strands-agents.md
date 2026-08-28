---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/strands-agents.html
---

# Strands Agents
<a name="strands-agents"></a>

Strands Agents is an open-source SDK that was initially released by AWS, as described in the [AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/). Strands Agents is designed for building autonomous AI agents with a model-first approach It provides a flexible, extensible framework designed to work seamlessly with AWS services while remaining open to integration with third-party components. Strands Agents is ideal for building fully autonomous solutions.

## Key features of Strands Agents
<a name="key-features-of-strands-agents.595b1087-3562-5795-a101-97d8052aa260"></a>

Strands Agents includes the following key features:
+ **Model-first design** – Built around the concept that the foundation model is the core of agent intelligence, enabling sophisticated autonomous reasoning. For more information, see [Agent Loop](https://strandsagents.com/docs/user-guide/concepts/agents/agent-loop/) in the Strands Agents documentation.
+ **Multi-agent collaboration patterns** – Built-in coordination models such as Swarm, Graph and Workflow patterns that enable scalable collaboration and governance across distributed agent networks. For more information, see [Multi-agent Patterns](https://strandsagents.com/docs/user-guide/concepts/multi-agent/multi-agent-patterns/) in the Strands Agents documentation.
+ **MCP integration** – Native support for the [Model Context Protocol](https://modelcontextprotocol.io/) (MCP), enabling standardized context provision to LLMs for consistent autonomous operation.
+ **AWS service integration** – Seamless connection to Amazon Bedrock, AWS Lambda, AWS Step Functions, and other AWS services for comprehensive autonomous workflows. For more information, see [AWS Weekly Roundup](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-strands-agents-aws-transform-amazon-bedrock-guardrails-aws-codebuild-and-more-may-19-2025/) (AWS Blog).
+ **Foundation model selection** – Supports various foundation models including Anthropic Claude, Amazon Nova (Premier, Pro, Lite, and Micro) on Amazon Bedrock, and others to optimize for different autonomous reasoning capabilities. For more information, see [Amazon Bedrock](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/) in the Strands Agents documentation.
+ **LLM API integration** – Flexible integration with different LLM service interfaces including Amazon Bedrock, OpenAI, and others for production deployment. For more information, see [Amazon Bedrock Basic Usage](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/#basic-usage) in the Strands Agents documentation.
+ **Multimodal capabilities** – Support for multiple modalities including text, speech, and image processing for comprehensive autonomous agent interactions. For more information, see [Amazon Bedrock Multimodal Support](https://strandsagents.com/docs/user-guide/concepts/model-providers/amazon-bedrock/#multimodal-support) in the Strands Agents documentation.
+ **Tool ecosystem** – Rich set of tools for AWS service interaction, with extensibility for custom tools that expand autonomous capabilities. For more information, see [Tools Overview](https://strandsagents.com/docs/user-guide/concepts/tools/) in the Strands Agents documentation.

## When to use Strands Agents
<a name="when-to-use-strands-agents.a3e7d63c-7338-5cb4-a4f5-9be739346bbb"></a>

Strands Agents is particularly well-suited for autonomous agent scenarios including:
+ Organizations that build on AWS infrastructure who want native integration with AWS services for autonomous workflows
+ Teams that require enterprise-grade security, scalability, and compliance features for production autonomous systems
+ Projects that need flexibility in model selection across different providers for specialized autonomous tasks
+ Use cases that require tight integration with existing AWS workflows and resources for end-to-end autonomous processes

## Implementation approach for Strands Agents
<a name="implementation-approach-for-strands-agents.151bdf0a-2444-523a-9016-922e531f26e6"></a>

Strands Agents provides a straightforward implementation approach for business stakeholders, as outlined in its [Quickstart Guide for Python](https://strandsagents.com/docs/user-guide/quickstart/python/) and [Quickstart Guide for Typescript](https://strandsagents.com/docs/user-guide/quickstart/typescript/). The framework allows organizations to:
+ Select foundation models like Amazon Nova (Premier, Pro, Lite, or Micro) on Amazon Bedrock based on specific business requirements.
+ Define custom tools that connect to enterprise systems and data sources.
+ Process multiple modalities including text, images, and speech.
+ Deploy agents that can autonomously respond to business queries and perform tasks.

This implementation approach enables business teams to rapidly develop and deploy autonomous agents without deep technical expertise in AI model development.

## Real-world example of Strands Agents
<a name="real-world-example-of-strands-agents.2ce12d4c-f16d-54e9-b216-350bf99b1320"></a>

AWS Transform for .NET uses Strands Agents to power its application modernization capabilities, as described in [AWS Transform for .NET, the first agentic AI service for modernizing .NET applications at scale](https://aws.amazon.com/blogs/aws/aws-transform-for-net-the-first-agentic-ai-service-for-modernizing-net-applications-at-scale/) (AWS Blog). This production service employs multiple specialized autonomous agents. The agents work together to analyze legacy .NET applications, plan modernization strategies, and execute code transformations to cloud-native architectures without human intervention. [AWS Transform for .NET](https://aws.amazon.com/transform/net/) demonstrates the production readiness of Strands Agents for enterprise autonomous systems.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
