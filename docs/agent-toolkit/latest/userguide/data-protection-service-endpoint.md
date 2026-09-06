---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/data-protection-service-endpoint.html
---

# Data protection for the AWS CLI
<a name="data-protection-service-endpoint"></a>

This topic describes data protection when you use the AWS CLI to discover and install AWS-vended agent skills (the `aws configure agent-toolkit` and `aws agent-toolkit` commands). These commands communicate with an unauthenticated, read-only endpoint over HTTPS. For data protection information about the AWS MCP Server (the authenticated component that executes AWS API calls on your behalf), see [Data protection in AWS MCP Server](data-protection.md).

## No customer data
<a name="service-endpoint-no-customer-data"></a>

The AWS CLI does not send customer data when fetching or searching for skills. The endpoint has no concept of customer identity and persists no per-customer state.

## What the AWS CLI sends
<a name="service-endpoint-data-sent"></a>

When you run `aws configure agent-toolkit` or an `aws agent-toolkit` command, the AWS CLI sends only the following data:
+ Skill identifiers (for example, via `--skill-name` or via `--skill-version`) or in case of the `aws agent-toolkit search-skills` command, a search query that you provide with `--search-query` on the command line.
+ Standard HTTP request metadata, such as the `User-Agent` header and your client's source IP address.

The AWS CLI does not send your AWS credentials, account information, or IAM principal when fetching skills. For more information, see [IAM for the AWS CLI](security-iam-cli.md).

## Trust model for skills
<a name="service-endpoint-trust-model"></a>

Skills fetched by the AWS CLI are AWS-vended content. Treat them the same as AWS-published guidance: they describe operations that an AI coding agent can perform on your behalf using *your* IAM credentials. The skill content itself does not carry AWS permissions — the agent uses your existing credentials to execute any operation it derives from a skill, so IAM remains the authoritative authorization control. To constrain what an agent can do, scope down the IAM role you use with the AWS MCP Server to the minimum permissions required for the task. For more information, see [Identity and access management for AWS MCP Server](security-iam.md).

## Search query privacy
<a name="service-endpoint-search-queries"></a>

When you use commands such as `aws agent-toolkit search-skills`, the natural-language search query you provide (for example, "deploy a Lambda with environment variables") is sent to AWS over TLS and may appear in service operational logs.

**Important**
Do not include confidential or sensitive information in search queries. As with tags and other free-form text fields you submit to AWS services, treat search queries as potentially observable by AWS for operational purposes.
