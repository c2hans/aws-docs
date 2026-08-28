---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-searching.html
---

# Discovering the registry
<a name="registry-searching"></a>

As a consumer, you can discover MCP servers, agents, skills, and other resources that have been approved and published to the registry. AWS Agent Registry supports three discovery modes on its data plane — natural-language search, paginated browsing of the approved-record catalog, and bulk retrieval by record ID — plus a Model Context Protocol (MCP) endpoint that MCP-compatible clients can invoke directly. This section covers how to use each mode.

**Topics**
+ [Search for registry records](registry-search-records.md)
+ [Browse approved records](registry-browse-records.md)
+ [Using the Registry MCP endpoint](registry-mcp-endpoint.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
