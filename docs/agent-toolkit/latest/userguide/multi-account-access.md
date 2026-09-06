---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/multi-account-access.html
---

# Multi-profile support
<a name="multi-account-access"></a>

When using the MCP Proxy for AWS with the AWS MCP Server, you can configure multiple AWS CLI profiles to switch between accounts or roles on a per-call basis. The proxy adds an `aws_profile` parameter to the server's auth-requiring tools, letting the agent route each request through a different set of credentials without restarting.

**Note**
This feature is specific to the AWS MCP Server. Profile switching is not available when proxying to other MCP servers.

**Important**
Multi-profile switching requires SigV4 authentication with the MCP Proxy for AWS. OAuth authentication does not support this feature. If you use OAuth, each session is bound to a single IAM role and switching accounts requires re-authentication.

## How it works
<a name="multi-profile-how-it-works"></a>

1. You configure the proxy with multiple profiles at startup (via the `--profile` flag or `AWS_MCP_PROXY_PROFILES` environment variable).

1. The proxy adds an `aws_profile` parameter into the tool schema for `call_aws`, `run_script`, `get_presigned_url`, and `get_tasks`.

1. When the agent makes a tool call:
   + Without `aws_profile`: the proxy signs with the default (first) profile.
   + With `aws_profile="dev"`: the proxy routes through a dedicated connection signed with the `dev` profile's credentials.
   + With an invalid profile: the proxy rejects the call with an error listing allowed profiles.

1. The `aws_profile` parameter is stripped before forwarding to the backend — the AWS MCP Server never sees it.

## Configuration
<a name="multi-profile-configuration"></a>

Configure multiple profiles using either the CLI flag or the environment variable.

**CLI flag**
The first profile is the default. Additional profiles are switchable:

```
mcp-proxy-for-aws-cli https://aws-mcp.us-east-1.api.aws/mcp --profile prod-readonly dev staging
```

**Environment variable**
Same behavior, useful for plugin integration where CLI args cannot be modified:

```
AWS_MCP_PROXY_PROFILES="prod-readonly dev staging"
```

**Note**
`AWS_MCP_PROXY_PROFILES` takes precedence over `--profile` and `AWS_PROFILE` when set.

**Example MCP config**

```
{
  "mcpServers": {
    "aws-mcp": {
      "command": "uvx",
      "args": ["mcp-proxy-for-aws-cli@latest", "https://aws-mcp.us-east-1.api.aws/mcp"],
      "env": {
        "AWS_MCP_PROXY_PROFILES": "prod-readonly dev staging"
      }
    }
  }
}
```

## Prerequisites
<a name="multi-profile-prerequisites"></a>
+ AWS CLI profiles configured in `~/.aws/config` and `~/.aws/credentials` for each profile you want to use.
+ `mcp-proxy-for-aws` version 1.6.0 or later.
+ Valid IAM permissions for each profile. Each profile should have the minimum permissions required for the operations the agent will perform.

## Security considerations
<a name="multi-profile-security"></a>
+ **Explicit allowlist:** Only profiles declared at startup are available. The agent cannot discover or use other profiles in `~/.aws/config`.
+ **Stateless routing:** Each call carries its own identity. No shared session state means parallel requests cannot interfere with each other.
+ **Least privilege:** Configure profiles with the minimum permissions needed. Consider using a read-only profile as the default and requiring explicit selection of write-capable profiles.
+ **Client-side gating:** For additional control (for example, requiring manual approval before using a production profile), configure client-side hooks or permission rules in your MCP client.

## Example use cases
<a name="multi-profile-use-cases"></a>
+ **Cross-account cost comparison:** "Compare Lambda invocation costs between my dev and prod accounts."
+ **Security audit:** "Check all S3 buckets across my three accounts for public access."
+ **Troubleshooting:** "List failed ECS tasks in staging, then check the same service config in prod."
+ **Resource inventory:** "Count EC2 instances across all my accounts."
