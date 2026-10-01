---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html
---

# Setting up the AWS MCP Server
<a name="getting-started-aws-mcp-server"></a>

If you already have an AWS account, skip to [Set up the AWS MCP Server](#mcp-set-up-process). If you are new to AWS, [sign up for an AWS account](https://portal.aws.amazon.com/billing/signup) and then continue with the setup process.

## Set up the AWS MCP Server
<a name="mcp-set-up-process"></a>

AWS MCP Server supports two authentication methods. The following describes both options, followed by a decision guide to help you choose.
+ **Option A: OAuth (simple)** — Connect to AWS MCP Server using OAuth. If you are a human user, you authenticate in your browser. If you are running an automated agent, it authenticates by requesting a token. Works for web clients (such as Claude.ai and ChatGPT.com) and most IDE, terminal, or desktop-based clients. Use this option if you are new to AWS and use a single account, or if you interact through web clients.
+ **Option B: SigV4 (advanced)** — Authenticate using the AWS CLI, then use the MCP Proxy for AWS to sign requests with SigV4 credentials. Use this option if you use terminal or IDE-based coding agents (such as Claude Code, Kiro, and Codex), or if you need to switch between AWS accounts frequently.

### Choosing an authentication method
<a name="choosing-auth-method"></a>

Use the following questions to determine which authentication method fits your use case:

**Authentication method decision guide**

| Question | Use |
| --- | --- |
| Do you want to get started without installing uvx, installing the AWS CLI, or configuring local credentials? | OAuth |
| Does your client only support remote MCP servers (no local process)? | OAuth |
| Does your agent need access across multiple AWS accounts in the same session? | SigV4 |
| Do you need read-only mode (hide write-capable tools from the agent entirely)? | SigV4 |
| Does your organization restrict the signin:AuthorizeOAuth2Access and signin:CreateOAuth2Token permissions needed for browser-based OAuth login? | SigV4 |
| Do you need to set a default AWS Region for your agentic session (without specifying it in every query)? | SigV4 |
| Does your client not support the OAuth flow but can run a local MCP proxy? | SigV4 |

**Topics**
+ [Choosing an authentication method](#choosing-auth-method)
+ [Step 1: (If applicable) Remove conflicting MCP servers](#step-1-remove-conflicting-servers)
+ [Step 2: Configure authentication and connect](#step-2-choose-auth-method)
+ [Step 3: Test your connection](#step-3-test-connection)

### Step 1: (If applicable) Remove conflicting MCP servers
<a name="step-1-remove-conflicting-servers"></a>

If you are currently using the AWS API MCP Server or AWS Knowledge MCP Server, we recommend switching to the AWS MCP Server. The AWS MCP Server is a managed remote MCP server that reduces setup and maintenance effort and offers enhanced security controls through IAM condition keys.

To switch, remove the older servers from your MCP client configuration to avoid tool conflicts that can confuse AI agents and reduce performance.

**To remove existing AWS MCP servers:**

1. Open your MCP client configuration file (for example, `~/.kiro/settings/mcp.json` for Kiro).

1. Remove any entries for these servers:
   + `aws-api-mcp-server`
   + `aws-knowledge-mcp-server`

1. Save the configuration file.

1. Restart your MCP client to apply the changes.

### Step 2: Configure authentication and connect
<a name="step-2-choose-auth-method"></a>

AWS MCP Server supports the following AWS Regions:
+ US East (N. Virginia) – `us-east-1`: `https://aws-mcp.us-east-1.api.aws/mcp`
+ US West (Oregon) – `us-west-2`: `https://aws-mcp.us-west-2.api.aws/mcp`
+ Asia Pacific (Singapore) – `ap-southeast-1`: `https://aws-mcp.ap-southeast-1.api.aws/mcp`
+ Asia Pacific (Sydney) – `ap-southeast-2`: `https://aws-mcp.ap-southeast-2.api.aws/mcp`
+ Asia Pacific (Tokyo) – `ap-northeast-1`: `https://aws-mcp.ap-northeast-1.api.aws/mcp`
+ Europe (Frankfurt) – `eu-central-1`: `https://aws-mcp.eu-central-1.api.aws/mcp`
+ Europe (Ireland) – `eu-west-1`: `https://aws-mcp.eu-west-1.api.aws/mcp`
+ Europe (London) – `eu-west-2`: `https://aws-mcp.eu-west-2.api.aws/mcp`

The setup examples in this section use the `us-east-1` endpoint. To connect to a different AWS Region, substitute that Region in the endpoint URL (for example, `https://aws-mcp.eu-west-1.api.aws/mcp`).

------
#### [ Option A: OAuth (simple) ]

With OAuth, you can connect directly to AWS MCP Server without installing or running local proxy software. Your MCP client handles the OAuth flow automatically.

**Prerequisites**

1. Grant OAuth permissions to your IAM role or user by attaching the managed policy:

   ```
   aws iam attach-role-policy \
     --role-name MyRole \
     --policy-arn arn:aws:iam::aws:policy/AWSMCPSignInOAuthAccessPolicy
   ```

**Configure your MCP client**

The following clients fully support OAuth with the default endpoint URL:

Claude Code CLI

```
claude mcp add aws-mcp https://aws-mcp.us-east-1.api.aws/mcp --transport http
```

Claude Code for Web
Add the URL `https://aws-mcp.us-east-1.api.aws/mcp` in your web client MCP settings.

Kiro CLI (2.11 or later)

```
kiro-cli mcp add --name aws-mcp --url https://aws-mcp.us-east-1.api.aws/mcp
```

Devin Desktop
Add as a remote MCP server with URL: `https://aws-mcp.us-east-1.api.aws/mcp`

Devin CLI

```
devin mcp add aws-mcp https://aws-mcp.us-east-1.api.aws/mcp
```

The following clients support OAuth when you append `?oauth=initialize` to the endpoint URL:

Claude Desktop
Add as a remote MCP server with URL: `https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize`

Cursor
Add as a remote MCP server with URL: `https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize`

Kiro IDE
Add as a remote MCP server with URL: `https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize`

Gemini CLI

```
gemini mcp add aws-mcp https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize --transport http
```

Codex CLI and Codex Desktop

```
codex mcp add aws-mcp --url https://aws-mcp.us-east-1.api.aws/mcp?oauth=initialize
```

When you first invoke a tool, your MCP client opens a browser window to AWS Sign-in. Sign in with your existing credentials and authorize access. After you grant consent, access tokens remain valid for 1 hour. AWS Sign-in automatically refreshes them for up to 12 hours.

If your client is not listed above, use the default endpoint URL (`https://aws-mcp.us-east-1.api.aws/mcp`). Without `?oauth=initialize`, the client relies on MCP OAuth discovery to start the authorization flow automatically. If tool calls fail due to credential errors, append `?oauth=initialize` to the URL to instruct the server to explicitly trigger the OAuth flow.

For detailed OAuth setup, governance options, and token management, see [OAuth 2.1 authentication for AWS MCP Server](oauth-authentication.md).

**Note**
Multi-profile switching for cross-account workflows is not supported with OAuth. If you need to work with multiple AWS accounts in a single session, use the SigV4 authentication option instead.

------
#### [ Option B: SigV4 (advanced) ]

Use the [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws) to authenticate requests with [SigV4](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html). With this option, you can switch between multiple profiles for cross-account workflows.

**Prerequisites**

1. Install the AWS CLI (`2.32.0` or later) by following [ Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

1. Sign in and configure credentials:

   ```
   aws login
   ```

   The command auto-rotates credentials every 15 minutes for sessions up to 12 hours.

1. Verify your credentials:

   ```
   aws sts get-caller-identity
   ```

1. Install uv (if not already installed):

   ```
   # macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

For other credential methods (SSO, IAM access keys, cross-account roles), see [Sign in with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html).

**Configure your MCP client**

The endpoint Region determines which MCP server you connect to, while the `AWS_REGION` metadata parameter sets the default Region for AWS operations. Without `AWS_REGION`, operations default to `us-east-1`.

Kiro CLI or Kiro IDE

```
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "timeout": 100000,
      "transport": "stdio",
      "args": [
        "mcp-proxy-for-aws-cli@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

Cursor IDE, Claude Desktop, or Devin Desktop

```
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws-cli@latest",
        "https://aws-mcp.us-east-1.api.aws/mcp",
        "--metadata", "AWS_REGION=us-west-2"
      ]
    }
  }
}
```

Claude Code CLI

```
claude mcp add-json aws-mcp '{"type":"stdio","command":"uvx","args":["mcp-proxy-for-aws-cli@latest","https://aws-mcp.us-east-1.api.aws/mcp","--metadata","AWS_REGION=us-west-2"],"env":{}}'
```

Codex CLI

```
codex mcp add aws-mcp uvx mcp-proxy-for-aws-cli@latest https://aws-mcp.us-east-1.api.aws/mcp --metadata AWS_REGION=us-west-2
```

Devin CLI

```
devin mcp add aws-mcp -- uvx mcp-proxy-for-aws-cli@latest https://aws-mcp.us-east-1.api.aws/mcp --metadata AWS_REGION=us-west-2
```

**Tip**
To work with multiple AWS accounts in a single session, configure additional named profiles. See [Multi-profile support](multi-account-access.md) for setup instructions. Multi-profile switching is only available with SigV4 authentication.

------

### Step 3: Test your connection
<a name="step-3-test-connection"></a>

1. Start your MCP client (Kiro CLI, Cursor, Claude Desktop, or a similar client).

1. Wait for the MCP server to initialize (this might take a few minutes on the first connection).

1. Test the connection by asking your AI assistant:

   *Example: What AWS Regions are available?*

1. Verify that tools are loaded by running (in Kiro CLI):

   `/tools`

   Or to see installed MCP servers:

   `/mcp`

You should see tools like `aws___search_documentation` and `aws___retrieve_skill` listed. For more information about the tools, see [Understanding the MCP Server tools](https://docs.aws.amazon.com/aws-mcp/latest/userguide/understanding-mcp-server-tools.html).

## Troubleshooting authentication errors
<a name="troubleshooting-auth-errors"></a>

Authentication errors can prevent the MCP server from initializing. When this happens, your AI agent cannot use AWS MCP tools. If your AI agent is not using AWS MCP tools, an expired or missing credential is the most likely cause.

Use the following table to identify and resolve common authentication errors.

**Common authentication errors**

| Error | Cause | Resolution |
| --- | --- | --- |
| ExpiredTokenException: Your AWS session token has expired. | Your temporary AWS credentials have expired. This is the most common authentication error. Short-lived session tokens (default 1 hour) typically expire during development. | Refresh your credentials based on your authentication method:+ `aws login` users: Run `aws login` again to start a new session. Consider switching to this method if you experience frequent expiry, because it auto-rotates credentials every 15 minutes.<br />+ SSO users: Run `aws sso login --profile your-profile-name` to refresh your SSO session.<br />+ Assume-role users: Refresh the source profile credentials. The SDK then automatically re-assumes the role.<br />After refreshing, restart your MCP client to re-initialize the server. |
| UnrecognizedClientException: The security token included in the request is not recognized. | Your credentials are invalid. This can happen when credentials have been revoked, are from a different AWS partition, are malformed, or belong to a deleted IAM user or role. | Verify your credentials are valid:1. Run `aws sts get-caller-identity` to check if your credentials are recognized.<br />2. If the command fails, reconfigure your credentials using `aws login` or `aws configure sso`.<br />3. Ensure you are using credentials for the correct AWS partition (for example, `aws` vs. `aws-cn`). |
| InvalidSignatureException: The request signature we calculated does not match the signature you provided. | The SigV4 signature does not match. Common causes include credentials scoped to the wrong service or Region, clock skew on your machine, or a request body modified after signing. | Try the following steps:1. Verify your system clock is accurate. Run `date` and compare with an authoritative time source. SigV4 requires your clock to be within 5 minutes of AWS servers.<br />2. Ensure your credentials are configured for the correct AWS Region and service.<br />3. Reconfigure your credentials and restart your MCP client. |
| 400 error page after OAuth sign-in | Your IAM principal does not have the required OAuth permissions (signin:AuthorizeOAuth2Access and signin:CreateOAuth2Token). | Attach the `AWSMCPSignInOAuthAccessPolicy` managed policy to your IAM role or user:<pre>aws iam attach-role-policy \<br />  --role-name MyRole \<br />  --policy-arn arn:aws:iam::aws:policy/AWSMCPSignInOAuthAccessPolicy</pre><br />For more information, see [AWS managed policies for AWS MCP Server](https://docs.aws.amazon.com/aws-mcp/latest/userguide/security-iam-awsmanpol.html). |
| No AWS credentials found. | AWS credentials are not configured on your machine, or the credential provider chain cannot locate them. | Configure your credentials by following [Step 2: Configure authentication and connect](#step-2-choose-auth-method). We recommend using `aws login` for the simplest setup with automatic credential renewal. |

**Note**
To learn more about how AWS IAM authorizes AWS MCP Server requests, including how to use IAM condition context keys to restrict agent actions, see [Understanding IAM for managed AWS MCP servers](https://aws.amazon.com/blogs/security/understanding-iam-for-managed-aws-mcp-servers/) on the AWS Security Blog.
