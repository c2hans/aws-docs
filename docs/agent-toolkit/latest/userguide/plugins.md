---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/plugins.html
---

# Plugins
<a name="plugins"></a>

Plugins for the Agent Toolkit for AWS are single-install packages that bundle the AWS MCP Server configuration and a curated set of agent skills. Instead of configuring MCP endpoints and installing skills individually, you install one plugin. Your agent is then ready to work with AWS.

Plugins work with Claude Code and Codex. They are open source and published at [Agent Toolkit for AWS repository](https://github.com/aws/agent-toolkit-for-aws) on the GitHub website. Kiro connects to the AWS MCP Server directly and does not require a plugin. For instructions on setting up Kiro, see [Setting up the AWS MCP Server](getting-started-aws-mcp-server.md).

**Topics**
+ [Available plugins](#available-plugins)
+ [Installing plugins](#installing-plugins)
+ [What a plugin contains](#what-plugin-contains)
+ [Updating plugins](#updating-plugins)

## Available plugins
<a name="available-plugins"></a>
+ **aws-core** - The primary plugin for the Agent Toolkit for AWS. Includes the AWS MCP Server configuration and default skills for common AWS workflows. Covered domains include service selection, infrastructure as code (CDK and CloudFormation), serverless, containers, databases, storage, observability, billing, SDK usage, and deployment. We recommend this plugin for all AWS developers.
+ **aws-agents** - Provides skills for building AI agents on AWS using Amazon API Gateway, Amazon Bedrock AgentCore, and related services.
+ **aws-data-analytics** - Provides skills for data lake, analytics, and ETL workflows using Amazon Simple Storage Service Tables, AWS Glue, Amazon Athena, and related services.
+ **aws-agents-for-devsecops** - Provides skills for investigating incidents, reviewing code for release readiness, scanning code for vulnerabilities, and running penetration tests using AWS DevOps Agent and AWS Security Agent.

## Installing plugins
<a name="installing-plugins"></a>

### Claude Code
<a name="install-claude-code"></a>

In Claude Code:

```
/plugin install aws-core@claude-plugins-official
/reload-plugins
```

### Codex
<a name="install-codex"></a>

In your terminal:

```
codex plugin marketplace add aws/agent-toolkit-for-aws
```

Then launch Codex and run `/plugins` to browse and install the **aws-core** plugin.

### Agents that do not support plugins
<a name="install-other-agents"></a>

If your agent does not support plugins, you can configure the AWS MCP Server directly. See [Setting up the AWS MCP Server](getting-started-aws-mcp-server.md) for instructions.

## What a plugin contains
<a name="what-plugin-contains"></a>

Each plugin contains the following:
+ **Plugin manifest** (`.claude-plugin/plugin.json` or `.codex-plugin/plugin.json`) - Contains the plugin metadata, including name, description, and version.
+ **Skills directory** (`skills/`) - Contains the agent skills that the plugin provides.
+ **MCP configuration** (`.mcp.json`) - Defines the AWS MCP Server endpoint configuration.

## Updating plugins
<a name="updating-plugins"></a>

Your agent client updates plugins automatically when it refreshes its marketplace data. To update manually, run the update command in your agent client.
