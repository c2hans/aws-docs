---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/linear-integration.html
---

# Linear integration
<a name="linear-integration"></a>

With Linear integration in Amazon Quick, you can manage issues, track projects, and streamline development workflows through MCP server connectivity. This integration provides action capabilities for project management and issue tracking operations.

## What you can do
<a name="linear-integration-capabilities"></a>

Linear integration provides action connector capabilities through MCP server connectivity:
+ Create and manage issues and tasks
+ Track project progress and milestones
+ Manage team workflows and assignments
+ Update issue status and priorities
+ Create and manage project cycles
+ Generate reports and track metrics

## Available tools
<a name="linear-integration-tools"></a>

The Linear MCP server typically provides these tools:
+ `create_issue` - Create new issues
+ `update_issue` - Update issue details
+ `list_issues` - List team issues
+ `search_issues` - Search for specific issues
+ `create_project` - Create new projects
+ `list_projects` - List team projects
+ `assign_issue` - Assign issues to team members
+ `create_cycle` - Create project cycles

**Note**
The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official Linear documentation and MCP server repository.

## Setting up Linear integration
<a name="linear-integration-setup"></a>

Linear integration uses MCP server connectivity to provide action capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](mcp-integration.md).

You'll need:
+ Linear account with appropriate team permissions
+ Linear API key for authentication

## Compatibility
<a name="linear-integration-compatibility"></a>

Linear integration supports:
+ **Chat Agents:** Yes
+ **Flows:** Yes
+ **Knowledge Base:** No

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
