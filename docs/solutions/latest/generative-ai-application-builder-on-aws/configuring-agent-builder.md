---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/configuring-agent-builder.html
---

# Configuring Agent Builder
<a name="configuring-agent-builder"></a>

Agent Builder provides comprehensive configuration options for creating production-ready AI agents. This section describes how to configure and manage Agent Builder deployments.

## System prompt configuration
<a name="system-prompt-configuration"></a>

The system prompt defines your agent’s behavior, personality, and capabilities. To configure the system prompt:

1. In the Agent Builder wizard, navigate to the **Configure Agent** step.

1. Edit the system prompt template in the text editor.

1. Include clear instructions for:
   + Agent’s role and purpose
   + How to use available tools (MCP servers)
   + Response formatting preferences
   + Behavioral guidelines

1. Use the **Reset to default** button to restore the original template if needed.

 **Best practices for agent prompts:**
+ Be specific about the agent’s capabilities and limitations
+ Provide clear examples of desired behavior
+ Include instructions for tool usage and when to invoke them
+ Define response format expectations
+ Set boundaries for agent behavior

## MCP server integration
<a name="mcp-server-integration"></a>

Model Context Protocol (MCP) servers provide agents with access to enterprise tools and data sources. To configure MCP servers:

1. In the **Configure Agent** step, locate the **MCP Servers** section.

1. Select from available MCP servers in the dropdown menu.

**Note**
MCP servers must be configured and accessible before agent deployment. The agent will automatically discover and use tools exposed by the configured MCP servers. Refer to the MCP documentation for server setup and tool configuration.

## Memory settings
<a name="memory-settings"></a>

Agent Builder provides two types of memory for maintaining context and knowledge:

 **Short-term memory**

Enabled by default for all agents:
+ Maintains conversation context within sessions
+ Automatically captures user messages and agent responses
+ Organized by actorId and sessionId for proper isolation
+ No configuration required

 **Long-term memory**

Optional feature for storing insights across sessions:

1. In the **Configure Agent** step, locate the **Memory Configuration** section.

1. Toggle **Enable long-term memory** to activate.

1. When enabled, the agent can:
   + Extract and store important information across conversations
   + Retrieve relevant context from previous sessions
   + Build knowledge about user preferences and history

**Note**
Long-term memory uses AgentCore Memory with semantic memory strategy and default retention settings.

## Monitoring Agent Builder deployments
<a name="monitoring-agent-builder"></a>

Agent Builder provides comprehensive monitoring through CloudWatch dashboards and metrics.

 **Accessing CloudWatch dashboards**

1. Navigate to the CloudWatch console in your AWS account.

1. Select **Dashboards** from the left navigation.

1. Find the dashboard named `AgentBuilder-<UseCaseId>`.

1. View real-time metrics and historical performance data.

 **Log access and analysis**

Agent logs are available in CloudWatch Logs:

1. Navigate to CloudWatch Logs in the AWS console.

1. Find log groups prefixed with `/aws/bedrock-agentcore/runtimes/`.

1. Use CloudWatch Insights to query and analyze logs.

1. Search for specific request IDs or error patterns.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
