---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/quick-start.html
---

# Getting started
<a name="quick-start"></a>

The fastest way to get started with the Agent Toolkit for AWS is to install the plugin for your AI coding agent. The plugin bundles the AWS MCP Server configuration and a curated set of agent skills in a single install.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="quick-start-prerequisites"></a>
+ [uv](https://docs.astral.sh/uv/) installed on your system (required for the MCP proxy).
+ (Optional) An AWS account with IAM credentials set up on your local machine. Credentials are required for tools that execute AWS API calls and run scripts, but not for searching documentation or discovering skills. If you do not have credentials configured, see [Setting up the AWS MCP Server](getting-started-aws-mcp-server.md) for detailed instructions.

## Step 1: Install
<a name="quick-start-install"></a>

**Claude Code**

In Claude Code:

```
/plugin install aws-core@claude-plugins-official
/reload-plugins
```

**Codex**

In your terminal:

```
codex plugin marketplace add aws/agent-toolkit-for-aws
```

Then launch Codex and run `/plugins` to browse and install the **aws-core** plugin.

**Kiro**

Add the following to your MCP configuration file (for example, `~/.kiro/settings/mcp.json`):

```
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "timeout": 100000,
      "transport": "stdio",
      "args": [
        "mcp-proxy-for-aws==1.6.3",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

Then install skills:

```
npx skills add aws/agent-toolkit-for-aws/skills
```

**Other agents**

If your agent supports MCP, you can configure the AWS MCP Server directly. See [Setting up the AWS MCP Server](getting-started-aws-mcp-server.md) for instructions.

Then install skills:

```
npx skills add aws/agent-toolkit-for-aws/skills
```

**AWS CLI**

If you have the AWS CLI installed (version `2.35.0` or later), you can run an interactive setup wizard that detects your installed AI coding agents, installs default AWS skills, and configures the AWS MCP Server connection in a single command:

```
aws configure agent-toolkit
```

The wizard works with multiple agents, including Kiro, Cursor, and Claude Code. For more information, including how to install and manage individual skills from the command line, see [AWS CLI](aws-cli.md).

## Step 2: Verify your connection
<a name="quick-start-verify"></a>

After you install the plugin, verify that the AWS MCP Server is connected:

1. Start a new conversation with your agent.

1. Ask: *"What AWS Regions are available?"*

If the agent returns a list of AWS Regions, the connection is working. If you see an authentication error, see [Troubleshooting authentication errors](getting-started-aws-mcp-server.md#troubleshooting-auth-errors).

## Step 3: Try it out
<a name="quick-start-try"></a>

Ask your agent to perform an AWS task:
+ "What AWS services should I use to build a serverless API?"
+ "Create an Amazon S3 bucket with versioning enabled and a lifecycle policy that transitions objects to Glacier after 90 days."
+ "Help me troubleshoot why my CloudFormation deployment failed."

The agent discovers and uses relevant skills automatically. You do not need to know which skills are available — the agent finds them based on your request.

## Additional plugins
<a name="quick-start-additional-plugins"></a>

After you install aws-core, you can install additional plugins for specialized workflows:
+ **aws-agents** — Skills for building AI agents on AWS with API Gateway and AgentCore.
+ **aws-data-analytics** — Skills for data lake, analytics, and ETL workflows.
+ **aws-agents-for-devsecops** — Skills for incident investigation, code security scanning, and penetration testing.

Install additional plugins using the same method as aws-core.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Agent Toolkit for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-toolkit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
