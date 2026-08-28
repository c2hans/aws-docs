---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/frameworks.html
---

# Frameworks
<a name="frameworks"></a>

[Foundations of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/) examines the core patterns and workflows that enable autonomous, goal-directed behavior. At the heart of implementing these patterns lies the choice of framework. A *framework* is the software foundation of prewritten code that provides a structured environment and common functionality for building and managing tools, and orchestration capabilities needed to build production-ready autonomous AI agents.

Effective agentic AI frameworks provide several essential capabilities that transform raw large language model (LLM) interactions into coordinated, intelligent systems capable of reasoning, collaboration, and action:
+ **Agent orchestration** coordinates the flow of information and decision-making across single or multiple agents to achieve complex goals without human intervention.
+ **Tool integration** enables agents to interact with external systems, APIs, and data sources to extend their capabilities beyond language processing. For more information, see [Tools Overview](https://strandsagents.com/0.1.x/user-guide/concepts/tools/tools_overview/) in the Strands Agents documentation.
+ **Memory management** provides persistent or session-based state to maintain context across interactions, essential for long-running or adaptive tasks. More advanced frameworks incorporate long-term memory to store summaries and user preferences, enabling personalized and contextually aware agentic experiences. For more information, see [How to think about agent frameworks](https://blog.langchain.com/how-to-think-about-agent-frameworks/) on the LangChain Blog.
+ **Workflow definition** supports structured patterns like chains, routing, parallelization, and reflection loops that enable sophisticated autonomous reasoning.
+ **Deployment and monitoring** facilitate the transition from development to production with observability for autonomous systems. For more information, see the [Amazon Bedrock AgentCore general availability](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-is-now-generally-available/) announcement.

These capabilities are implemented with varying approaches and emphases across the framework landscape, each offering distinct advantages for different autonomous agent use cases and organizational contexts.

This section profiles and compares the leading frameworks for building agentic AI solutions, with a focus on their strengths, limitations, and ideal use cases for autonomous operation:
+ [Strands Agents](strands-agents.md)
+ [LangChain and LangGraph](langchain-langgraph.md)
+ [CrewAI](crewai.md)
+ [Amazon Bedrock Agents](bedrock-agents.md)
+ [Amazon Bedrock AgentCore](amazon-bedrock-agent-core.md)
+ [AutoGen](autogen.md)
+ [LlamaIndex](llamaindex.md)
+ [Comparing agentic AI frameworks](comparing-agentic-ai-frameworks.md)

**Note**
This section covers the frameworks that specifically support agency of the AI and doesn't cover frontend interfaces or generative AI without agency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
