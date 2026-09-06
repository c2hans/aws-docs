---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/security-iam-cli.html
---

# IAM for the AWS CLI
<a name="security-iam-cli"></a>

The `aws configure agent-toolkit` and `aws agent-toolkit` commands do not use IAM. These commands fetch AWS-vended skills from a public, read-only catalog over HTTPS. The AWS CLI does not sign requests or send credentials when using these commands.

You do not need to grant any IAM permissions to discover, install, update, remove, or search for skills with the AWS CLI. No IAM policies, roles, or identity configuration is required.

For information about IAM permissions required by the AWS MCP Server (the authenticated component that executes AWS API calls on your behalf), see [Identity and access management for AWS MCP Server](security-iam.md).
