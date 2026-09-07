---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-scope.html
---

# Tool scope
<a name="mcp-tool-strategy-scope"></a>

There are two approaches for developing tools: granular and coarse-grained.

## Granular
<a name="mcp-tool-strategy-scope-granular"></a>

In a granular approach, you would create a tool per API, action, or query. For example, you could create `create_issue`, `get_issue`, `add_label`, `assign_issue`, and `close_issue` tools for your Git repository. This would allow the LLM to make granular calls to each API and orchestrate each one as necessary. Consider the following prompt: "Create an issue for the product service called 'Query only returns partial results', label it as a bug and high-priority, and assign it to Alice." The following image shows how a tool-per-API approach would respond to this prompt.

![Granular approach with a tool per API.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/images/guide-img/2803ca34-2e01-4597-9d5d-d8b2e530a414/images/bc47a3b0-3a57-46dc-ad89-204ae4bf28d0.png)

In this approach the system prompt and every registered tool definition are provided to the LLM on each call. This consumes additional context and incurs a latency penalty because each tool call represents an individual call to the LLM. It also increases the complexity of handling errors within the workflow.

## Coarse-grained
<a name="mcp-tool-strategy-scope-coarse"></a>

A coarse-grained, or *workflow-driven*, approach would be tools that are workflow oriented. The tool focuses on end-to-end user intent over API structure. Instead of a tool-per-API, you have one tool that deterministically calls many APIs. Using the previous Git repository example, you could create a `create_and_setup_issue` tool that is called once by the agent. The tool implementation creates the issue, adds labels, and assigns it to a user, based on the parameters provided to the tool. The following image shows how a coarse-grained approach would process the same prompt.

![Coarse-grained approach, where tools are workflow-oriented.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/images/guide-img/2803ca34-2e01-4597-9d5d-d8b2e530a414/images/c092d56f-c25d-4c60-85b9-b7cb915665f6.png)

This approach shows how all complexity remains hidden from the LLM layer. When the orchestration logic is embedded within the tool implementation, all of the sequential steps, logging, retry logic, circuit breakers, and rate limiting are performed deterministically in the tool. The workflow-driven approach makes it simpler for the LLM to invoke the correct tool with the right parameters. It is important to note that some APIs might already provide workflow intent, such as the Amazon EC2 `RunInstances` API. In these cases, a tool-per-API might provide the workflow-oriented design you desire.

However, tools can become too coarse-grained as well. If your single workflow tool attempts to do too many things and has many possible parameters, the LLM can struggle to reason about how to correctly use the tool. It can also create challenges with parameter selection and error handling. Thus, tool development must strike a balance that aligns with user intent and avoids too little or too much functionality in a single tool. We recommend that you design tools around complete user workflows, bundling operations that commonly occur together (such as three or more API calls). We also recommend that you decompose tools that exceed eight or more parameters or handle multiple distinct user intents. Test with real prompts to verify that agents can correctly use each tool.

If you have complex and dynamic workflows that cannot easily be encapsulated as a deterministic tool, you might consider using the *agent-as-tool pattern*. Instead of your primary agent trying to orchestrate complex tasks in a workflow, a specialized agent can act as a tool. These types of tools can implement advanced decision-making and branching, and they can handle errors and retry logic that cannot be easily managed in deterministic code. This is similar to, but distinct from, the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/). The A2A protocol is complementary, providing interoperability and collaboration between agents in any agentic framework.

We recommend that you start with your workflow analysis by mapping your most common user workflows to identify the core capabilities each agent needs. This establishes your minimum viable toolset. Based on our experience developing MCP servers at scale, we recommend the following practices. When these practices conflict, prioritize user intent and workflow**.**

## Best practices for MCP tool scoping
<a name="mcp-tool-strategy-scope-best-practices"></a>
+ **Think in user stories and bundle common operations** – Tools should map directly to complete user interactions rather than requiring orchestration of multiple operations. If workflows commonly require three or more separate calls, combine them into a single tool. This reduces the cognitive load on the LLM, minimizes the number of tool calls, reduces context consumption and latency required to complete tasks, and improves accuracy and latency.
+ **Limit parameters to eight or fewer – **If a tool exceeds eight parameters, decompose it into multiple tools. LLMs struggle with parameter selection as complexity increases.
**Note**
If bundling operations requires more than eight parameters, prioritize bundling over parameter count because simplifying the workflow is more valuable than strict parameter limits.
+ **Separate read and write operations – **Provide different tools for reading data and modifying it. This separation makes it explicit when agents are performing potentially destructive operations, enables different authorization policies, and reduces the risk of unintended modifications during information gathering.
+ **Provide sensible defaults** – Design tools so that the LLM needs to specify only the parameters that are specific to the individual request. Defaults reduce parameter complexity and improve tool selection accuracy by minimizing the information that the LLM must reason about.
+ **Prefer deterministic execution – **Make tool execution and output deterministic when possible. Deterministic tools are more reliable and easier to test. For complex workflows that require intelligent orchestration, branching logic, or advanced error handling that cannot be easily managed in deterministic code, consider using specialized agents as tools. However, use this pattern selectively because it adds complexity.
