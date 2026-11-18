---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-agent-setup.html
---

# Set up the Apache Spark agents
<a name="spark-troubleshooting-agent-setup"></a>

**Note**
The Apache Spark agents use cross-Region inference to process natural language requests and generate responses. For more information, see [Cross-Region processing for the Apache Spark agents](spark-troubleshooting-cross-region-processing.md).

**Note**
Both agents use the `sagemaker-unified-studio-mcp-troubleshooting` server and the `/spark-troubleshooting/mcp` endpoint, despite "troubleshooting" in the names. Only the Troubleshooting Agent uses the code recommendation server, `sagemaker-unified-studio-mcp-code-rec` (`/spark-code-recommendation/mcp`). If you use only the Optimization Agent, you can skip it.

## Prerequisites
<a name="spark-troubleshooting-agent-prerequisites"></a>

Before you begin the setup for integration with Kiro CLI, make sure that you have the following installed on your workstation:
+ [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ [Install Python 3.10\+](https://www.python.org/downloads/release/python-3100/)
+ [Install the `uv` package manager](https://docs.astral.sh/uv/getting-started/installation/) for [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file)
+ [Install Kiro CLI](https://kiro.dev/docs/cli/)
+ AWS local credentials configured (through the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html), environment variables, or IAM roles). The MCP Proxy for AWS uses these credentials to authenticate the agents' requests to AWS services as your IAM identity.

## How the agents access your resources
<a name="spark-agents-setup-access"></a>

The MCP server authorizes operations at the AWS service level using the IAM identity that your MCP client is configured with. The agents act as that identity, so they can only access what that identity is permitted to access. No separate MCP-specific permissions are required.

Point the MCP client at an AWS profile for a role that you already use to analyze your Spark jobs. The agents' access then matches your own. Make sure that the role has the permissions described in [IAM permissions for the Apache Spark agents](spark-troubleshooting-agent-iam-setup.md), so that the agents can read all the signals from your Spark jobs.

If you want tighter, scoped control over what the agents can access, see [How can I get more fine-grained control over the agents' permissions?](spark-troubleshooting-agent-troubleshooting.md#spark-agents-qa-fine-grained).

## Add the Apache Spark agents to your MCP client
<a name="spark-agents-setup-add-servers"></a>

To set your Region and add the MCP servers, run the following commands. Point `--profile` at the profile for the role that you use. This example uses the `default` profile. Replace it with your own.

```
export SMUS_MCP_REGION=<your mcp server launch region>

# Add Spark Troubleshooting MCP Server
kiro-cli-chat mcp add \
    --name "sagemaker-unified-studio-mcp-troubleshooting" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-troubleshooting/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"default\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000 \
    --scope global

# Add Spark Code Recommendation MCP Server
kiro-cli-chat mcp add \
    --name "sagemaker-unified-studio-mcp-code-rec" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-code-recommendation/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"default\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000 \
    --scope global
```

This updates `~/.kiro/settings/mcp.json` to include the MCP server configuration as follows.

```
{
  "mcpServers": {
    "sagemaker-unified-studio-mcp-troubleshooting": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-troubleshooting/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "default",
        "--region",
        "us-east-1",
        "--read-timeout",
        "180"
      ],
      "timeout": 180000,
      "disabled": false
    },
    "sagemaker-unified-studio-mcp-code-rec": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-code-recommendation/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "default",
        "--region",
        "us-east-1",
        "--read-timeout",
        "180"
      ],
      "timeout": 180000,
      "disabled": false
    }
  }
}
```

## Configure your MCP client
<a name="integration-other-mcp-clients"></a>

You can also use the preceding configuration in other MCP clients and IDEs to connect to the managed MCP server:
+ **Integration with Cline** – To use the MCP server with Cline, modify `cline_mcp_settings.json` and add the MCP server configuration shown earlier. For more information about how to manage MCP configuration, see the [Cline documentation](https://docs.cline.bot/mcp/configuring-mcp-servers).
+ **Integration with Claude Code** – To use the MCP server with Claude Code, modify the configuration file to include the MCP configuration. The file path varies depending on your operating system. For detailed setup, see [https://code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp).
+ **Integration with GitHub Copilot** – To use the MCP server with GitHub Copilot, follow the instructions in [Extending Copilot Chat with MCP](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp) to modify the corresponding configuration file, and follow the instructions for each IDE to activate the setup.
