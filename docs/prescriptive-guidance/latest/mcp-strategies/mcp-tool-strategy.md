---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy.html
---

# MCP tool design strategy
<a name="mcp-tool-strategy"></a>

The main job of the MCP client and server is to discover and present tools to the LLM so that it can use them to improve its responses. This makes MCP tool design one of the most important strategies for building effective MCP solutions. From the model's perspective, tools are a function that they can invoke as needed to provide more accurate and complete responses. The function interface abstracts the underlying implementation of a tool, which can range from a wrapper around a single API call to complex workflow logic.

However, you must strike a balance with the quantity of tools provided to the LLM. If there are too few tools, the LLM might not be able to collect the right context and information, so it will take the best guess with the information available within the model. If there are too many tools, the LLM may get confused about the right tool selection and sequence, leading to hallucinations. Your goal is to get the number of tools just right. The following image shows the challenges of too few and too many tools.

![Too few tools cause hallucinations, and too many tools cause confusion.](http://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/images/guide-img/2803ca34-2e01-4597-9d5d-d8b2e530a414/images/aab9b950-a63c-4273-98b1-4e20aa1d9abb.png)

The solution requires understanding how many tools to provide and how to scope each tool. The granularity of your tools, whether they map to individual API calls or complete workflows, directly impacts the total number of tools that agents need and how effectively they can use them. This section provides best practices for scoping MCP tools, creating tool definitions, discovering tools, and organizing them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
