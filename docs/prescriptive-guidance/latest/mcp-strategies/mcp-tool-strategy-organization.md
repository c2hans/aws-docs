---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mcp-strategies/mcp-tool-strategy-organization.html
---

# Tool organization
<a name="mcp-tool-strategy-organization"></a>

Discovering the right tools and ensuring the LLM can use them effectively is one of the most critical parts of effective tool development. As you start to develop MCP servers, you need a strategy that determines:
+ How many tools go into one MCP server
+ What tools should not be put into the same MCP server
+ How to name tools to make them searchable and prevent name collisions (different tools with the same name)
+ How to document the tools and MCP server to make them easy to use by the LLM

*Namespace organization* is a design pattern that prevents tool name collisions, groups related functionality, and facilitates efficient tool identification by LLMs. The pattern establishes structured categorization that is analogous to organized storage systems rather than unstructured accumulation. We recommend the *domain-noun-verb* pattern for tool naming. For example, `github_issue_create`, `github_issue_list`, `github_issue_update`, `github_pullrequest_create`, `github_pullrequest_list`, or `github_pullrequest_merge`. The advantage of this pattern is evident when examining alphabetical sorting behavior. When tools are listed alphabetically, all issue-related operations cluster together (`create`, `list`, `update`), followed by pull request operations (`create`, `list`, `merge`). The noun (resource type) functions as an organizational boundary. This structure facilitates both LLM tool scanning and human documentation navigation because related functionality naturally groups together.

The MCP server should be bounded at the domain level but may be sub-divided based on the separation of duties for the capabilities that it provides. For example, you might have separate MCP servers for write operations and read operations to a database. To enforce this separation, it is recommended that you implement guardrails at the agent level that restrict which MCP servers can be accessed based on user intent and permissions. This can be achieved through a combination of the following:
+ **Conditional server loading** – Load the read-only MCP server only when the agent detects read operations in the user input.
+ **Permission-based filtering** – Use user authorization to grant access to only appropriate MCP servers.

Finally, you will want to create an upper bound on the number of tools provided by an MCP server. Do not make assumptions about how agents will use your MCP server. They may naively list all the available tools and provide them all to the LLM. If you have more than 50 tools in a single server, you should consider splitting it into multiple servers.

## Best practices for MPC tool organization
<a name="mcp-tool-strategy-organization-best-practices"></a>
+ **Use the domain-noun-verb naming standard for tools** – Implement strategies to prevent name collisions in both MCP servers and in agents.
+ **Set an upper bound** – Restrict the number of tools in a single MCP server.
+ **Divide MCP servers** – Use separation of duties to divide MCP servers into logical groups.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
