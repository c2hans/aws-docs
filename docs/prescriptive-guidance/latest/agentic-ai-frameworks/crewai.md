---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/crewai.html
---

# CrewAI
<a name="crewai"></a>

CrewAI is an open-source framework focused specifically on autonomous multi-agent orchestration, available on [GitHub](https://github.com/crewAIInc/crewAI). It provides a structured approach to creating teams of specialized autonomous agents that collaborate to solve complex tasks without human intervention. CrewAI emphasizes role-based coordination and task delegation.

## Key features of CrewAI
<a name="key-features-of-crewai.53e4d628-3e3b-51f2-98ba-28ac3de25469"></a>

CrewAI provides the following key features:
+ **Role-based agent design** – Autonomous agents are defined with specific roles, goals, and backstories to enable specialized expertise. For more information, see [Crafting Effective Agents](https://docs.crewai.com/en/guides/agents/crafting-effective-agents) in the CrewAI documentation.
+ **Task delegation** – Built-in mechanisms for autonomously assigning tasks to appropriate agents based on their capabilities. For more information, see [Tasks](https://docs.crewai.com/en/concepts/tasks) in the CrewAI documentation.
+ **Agent collaboration** – Framework for autonomous inter-agent communication and knowledge sharing without human mediation. For more information, see [Collaboration](https://docs.crewai.com/en/concepts/collaboration) in the CrewAI documentation.
+ **Process management** – Structured workflows for sequential and parallel autonomous task execution. For more information, see [Processes](https://docs.crewai.com/en/concepts/processes) in the CrewAI documentation.
+ **Foundation model selection** – Support for various foundation models including Anthropic Claude, Amazon Nova models (Premier, Pro, Lite, and Micro) on Amazon Bedrock, and others to optimize for different autonomous reasoning tasks. For more information, see [LLMs](https://docs.crewai.com/en/concepts/llms) in the CrewAI documentation.
+ **LLM API integration** – Flexible integration with multiple LLM service interfaces including Amazon Bedrock, OpenAI, and local model deployments. For more information, see [Provider Configuration Examples ](https://docs.crewai.com/en/concepts/llms#provider-configuration-examples)in the CrewAI documentation.
+ **Multimodal support** – Emerging capabilities for handling text, image, and other modalities for comprehensive autonomous agent interactions. For more information, see [Using Multimodal Agents](https://docs.crewai.com/en/learn/multimodal-agents) in the CrewAI documentation.

## When to use CrewAI
<a name="when-to-use-crewai.bf1e7a89-24f3-51ea-bc12-e2f84a26379e"></a>

CrewAI is particularly well-suited for autonomous agent scenarios including:
+ Complex problems that benefit from specialized, role-based expertise working autonomously
+ Projects that require explicit collaboration between multiple autonomous agents
+ Use cases where team-based problem decomposition improves autonomous problem-solving
+ Scenarios that require clear separation of concerns between different autonomous agent roles

## Implementation approach for CrewAI
<a name="implementation-approach-for-crewai.e62715d4-bd38-5fdb-b3d5-584780a784dd"></a>

CrewAI provides a role-based implementation of teams of AI agents approach for business stakeholders, as detailed in [Getting Started](https://github.com/crewAIInc/crewAI?tab=readme-ov-file#getting-started) in the CrewAI documentation. The framework enables organizations to:
+ Define specialized autonomous agents with specific roles, goals, and expertise areas.
+ Assign tasks to agents based on their specialized capabilities.
+ Establish clear dependencies between tasks to create structured workflows.
+ Orchestrate collaboration between multiple agents to solve complex problems.

This role-based approach mirrors human team structures, making it intuitive for business leaders to understand and implement. Organizations can create autonomous teams with specialized expertise areas that collaborate to achieve business objectives, similar to how human teams operate. However, the autonomous team can work continuously without human intervention.

## Real-world example of CrewAI
<a name="real-world-example-of-crewai.219a64c2-e605-53c9-8759-bf7718a525db"></a>

AWS has implemented autonomous multi-agent systems using CrewAI integrated with Amazon Bedrock, as detailed in the CrewAI published case study. AWS and CrewAI developed a secure, vendor‑neutral framework. The CrewAI open‑source "flows‑and‑crews" architecture seamlessly integrates with Amazon Bedrock foundation models, memory systems, and compliance guardrails.

Key elements of the implementation include:
+ **Blueprints and open sourcing** – AWS and CrewAI released [reference designs](https://aws.amazon.com/blogs/machine-learning/build-agentic-systems-with-crewai-and-amazon-bedrock) that map CrewAI agents to Amazon Bedrock models and observability tools. They also released exemplar systems such as a multi‑agent AWS security audit crew, code modernization flows, and consumer packaged goods (CPG) back‑office automation.
+ **Observability stack integration** – The solution embeds monitoring with Amazon CloudWatch, AgentOps, and LangFuse, enabling traceability and debugging from proof‑of‑concept to production.
+ **Demonstrated return on investment (ROI)** – Early pilots showcase major improvements—70 percent faster execution for a large code modernization project and about 90 percent reduction in processing time for a CPG back‑office flow.
