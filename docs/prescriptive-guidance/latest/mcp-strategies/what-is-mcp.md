---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/what-is-mcp.html
---

# What is MCP?
<a name="what-is-mcp"></a>

LLMs work by predicting an answer to a prompt based on their training data. This means that the LLM can only provide answers about data and events it has already seen. Methods like Retrieval Augmented Generation (RAG) and knowledge bases allow you to include contextual data. However, if you were to ask an LLM what tomorrow's weather forecast is going to be or how many customers are in your database, it would likely hallucinate or not be able to provide an answer because these fall outside of the LLM's pre-trained knowledge. To be able to answer these kinds of questions, an agent needs access to external capabilities, data, and APIs outside of the LLM's native context.

## Understanding tools
<a name="understanding-tools"></a>

We can give the LLM access to additional systems and context through tools**. ***Tools* are functions given to the LLM to achieve a clear objective. A tool could call an API, query a database, perform calculator operations, operate a code sandbox, perform a web search, and even invoke another AI system or agent-as-a-tool. Each tool should include a description that tells the LLM what the tool does, when to use it, and what parameters it accepts. This enables the LLM to make nuanced decisions about which tool or combination of tools to invoke based on the user's input. The LLM is told about what tools are available to the agent, allowing it to generate responses that instruct the agent to invoke the tool. For example, when you ask the LLM how many customers are in your database, the LLM will send a response back to the agent requesting to run the `query_database` tool with specific input parameters. The LLM determines which tool to invoke and the inputs for the tool call. The agent then executes the tool, which converts the natural language input into a syntactically correct function call and runs the query. The agent invokes the tool or tools based on the instruction from the LLM, and those results are passed back to the LLM. This takes advantage of the LLM's ability to reason over text-based input and select the appropriate tools for the job.

The following image shows how each agent manages its own tool set for each target.

![Each agent manages its own tool set for each target.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/images/guide-img/2803ca34-2e01-4597-9d5d-d8b2e530a414/images/b3d95a08-521d-4cd0-ae0d-af254e6eebd1.png)

Scaling tool access can present challenges for agentic AI solutions:
+ If every developer is creating their own tool for the same external capabilities, there is a lot of duplicated effort and non-standardized ways of interacting with these external capabilities. This produces inconsistent implementations across your agents. While you could solve that problem by developing standard tools in libraries and distributing them, this lacks centralized governance. This makes it difficult to enforce security policies, track tool usage, manage versioning across teams, or ensure compliance with organizational standards. Additionally, when you embed tools directly with the agent, you must redeploy your agent every time a new tool is created or an existing one is updated.
+ Providing tools to an LLM consumes its context window. *The context window* is the number of *tokens* (units of text that LLMs process—typically representing words, parts of words, or punctuation) that a model can consider at any one time. LLMs have a context window limits. Tools and their documentation consume that finite context window along with system prompts and user prompts. As the context window fills, LLMs can experience degraded performance due to multiple factors: difficulty in identifying relevant information, increased processing complexity, and reduced capacity for reasoning. The challenge is compounded when tool definitions, system prompts, and conversation history compete for limited context window space because they are provided on each LLM invocation.

Thus, the number of tools and how they are documented have direct impact on the LLM's performance, such as response time, and accuracy.

MCP establishes a universal standard for connecting agents to external capabilities. It is commonly referred to as the "USB-C for AI applications." Instead of registering tools directly with agents, MCP servers act as an intermediary for hosting tools that are discovered and invoked over [JSON-RPC 2.0](https://www.jsonrpc.org/specification). Instead of adding tens or hundreds of different tools to your agent and maintaining them over time, MCP allows you to register MCP servers that encapsulate the tools that your agent can access. This approach standardizes how tools are packaged, presented, and invoked. This can help address the scale and governance challenges of tool usage inside your agents. It also decouples agent development and operations from the tools that it uses for external capabilities.

The following figure shows agents using MCP to access external resources.

![Using Model Context Protocol to access external resources.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/images/guide-img/2803ca34-2e01-4597-9d5d-d8b2e530a414/images/2216dbc3-8b92-4547-8657-3aed5e294957.png)

However, the MCP standard does not solve all scaling and governance challenges. Implementation of MCP servers must be combined with effective tool design, hosting, and enterprise governance strategies. This guide provides best practices for each strategy to help you build and use MCP as part of your agentic AI solutions.

## When to use MCP
<a name="when-to-use-mcp"></a>

MCP provides strategic infrastructure for scaling your agentic AI initiatives. By centralizing tool management and governance, MCP servers reduce the cumulative cost of building and maintaining custom integrations across multiple agents. This delivers increasing returns as your agent ecosystem expands.

MCP likely becomes part of your strategy when:
+ You need centralized governance for how agents access enterprise systems and services, such as databases, APIs, internal tools, and third-party integrations.
+ Developers spend too much time writing custom integrations that are not consistent across implementations.
+ You have duplicated tools that could serve common capabilities.
+ You want to offer your proprietary tools or data to external consumers or third-party agentic systems through standardized, governed MCP interfaces, unlocking new revenue streams while maintaining security and control.

After you decide that MCP servers are going to be part of your strategy, evaluate whether existing open-source MCP server implementations meet your needs, whether they require enhancement, or whether you need to build custom servers. Many pre-built MCP server implementations are available in public repositories, and they cover common capabilities such as file system access, web browsing, code sandboxes, database access, and API integrations.

In many cases, pre-existing MCP servers are sufficient. For example, AWS provides the [AWS MCP Server](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html), a managed remote MCP server that provides AI assistants and agents with secure, authenticated access to AWS services through natural language interactions. You can use the AWS MCP Server to perform complex, multi-step AWS tasks by combining real-time access to AWS documentation, syntactically correct API calls, and pre-built workflows called [Agent SOPs](https://docs.aws.amazon.com/aws-mcp/latest/userguide/agent-sops.html) that follow AWS best practices. AWS continuously tests the AWS MCP Server to make sure that customer agents can use them successfully.

You should test these existing MCP servers with your agents to determine if they fulfill your use cases. If an agent fails to complete workflows, generates incorrect or suboptimal responses, fails to navigate complex multi-step processes, or misses important domain-specific best practices or security considerations, you should consider enhancements in several dimensions.

When existing MCP servers do not fully meet your needs and they struggle to use the existing tools correctly or produce accurate responses, consider these enhancement approaches before building custom servers:
+ **Enrich agent context** – If your agent struggles to correctly or efficiently use the tools in an existing MCP server, consider supplementing those tool definitions with additional documentation or examples. This helps provide additional context to the LLM.
+ **Add complementary tools** – Extend existing MCP servers with tools that access additional organizational data or context that agents need to complete workflows successfully.
+ **Improve underlying APIs** – Simplify your service APIs to make them more LLM-friendly by reducing parameter complexity, providing clearer error messages, and offering sensible defaults that agents can use.

While using existing MCP server implementations accelerates development for common capabilities, building custom MCP servers is a necessity when your use case requires specialized functionality. Custom MCP servers help you encapsulate domain expertise, enforce organizational standards, improve agent reliability for complex workflows, and support compliance with security requirements. Consider building a custom MCP server in the following situations:
+ **Domain-specific workflows** – Multi-step workflows requiring domain expertise should be encapsulated in custom MCP tools when the necessary knowledge is not captured in API documentation.** **For example, instead of letting agents orchestrate complex healthcare data pipelines that must validate Health Insurance Portability and Accountability Act (HIPAA) compliance, anonymize PII, and transform to [HL7 FHIR](https://hl7.org/fhir/) format, provide a `process_patient_data` tool that embeds the domain expertise directly. This removes the dependency on the LLM to correctly orchestrate and run the workflow steps, which improves consistency and compliance.
+ **Golden path abstractions** – Agents might struggle to implement optimal approaches because they lack organizational context and default to basic patterns rather than organizational best practices. In these scenarios, you can enforce prescriptive standards for cost, performance, or security by encapsulating these golden paths in custom MCP tools. For example, instead of letting agents deploy infrastructure with default settings that might be unsecure or inefficient, provide a `deploy_secure_infrastructure` tool that directly embeds your organization's standards.
+ **Complex multi-service orchestration** – Instead of making the agent orchestrate complex workflows by trying to infer the correct sequence and set of services to use in each step, you can deterministically build that logic inside an MCP tool. You may also want to provide expertise about optimal service integration patterns that the agent might be unaware of.** **This can also improve the accuracy and efficiency of your agents.
+ **Service-specific best practices** – This is common for security-focused tools that help agents implement encryption policies, access controls, and compliance patterns specific to the service being accessed through the agent tool. Additionally, if there are service-specific operational best practices that are not obvious, using an MCP server can help you make sure that they are implemented and not left up to an agent to reason about.
