---
source_url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-mcp-limits.html
---

# Quotas for AWS MCP Server
<a name="aws-mcp-limits"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for AWS MCP Server, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **AWS MCP Server**.

To request a quota increase, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota is not yet available in Service Quotas, use the [limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase).

**Topics**
+ [Connection and session quotas](#connection-quotas)
+ [Throttling quotas](#throttling-quotas)
+ [Session limits](#session-limits)
+ [Monitoring your quotas](#monitoring-quotas)

## Connection and session quotas
<a name="connection-quotas"></a>

The following quotas apply to connections and sessions for AWS MCP Server.

| Quota | Default value | Adjustable | Description |
| --- | --- | --- | --- |
| Concurrent connections per account per Region | 100 | No | The maximum number of concurrent MCP connections per AWS account in a single Region. This limit applies to authenticated requests. |
| Concurrent active sessions per account per Region | 180 | Yes | The maximum number of concurrent active sessions per AWS account in a single Region. |
| Concurrent active sessions per user per Region | 90 | Yes | The maximum number of concurrent active sessions per IAM user or role in a single Region. |

**Note**
The per-account and per-user quotas in the preceding table apply to authenticated requests. Unauthenticated requests are not subject to a per-account connection quota and have lower connection limits.

## Throttling quotas
<a name="throttling-quotas"></a>

The following quotas apply to request rates for AWS MCP Server. Requests that exceed these limits are throttled with a 429 response.

Request rate limits for AWS MCP Server vary based on whether your request is authenticated. Authenticating your requests gives you more capacity:
+ **Authenticated requests** – When you authenticate with your AWS credentials, your requests receive a per-AWS-account request rate. You can authenticate using either SigV4 through the MCP Proxy for AWS or OAuth 2.1 through AWS Sign-in. Authenticated requests also have access to the full set of AWS MCP Server tools, including the tools that run AWS API calls and execute scripts. To get more capacity, authenticate your requests.
+ **Unauthenticated requests** – Requests that you send without AWS credentials share a lower rate limit. This limit applies per source IP address rather than per account. Unauthenticated access is limited to the read-only AWS knowledge tools, such as documentation search, documentation retrieval, and regional availability. Tools that run AWS API calls or execute scripts require authentication.

For more information about authenticating with AWS MCP Server, see [OAuth 2.1 authentication for AWS MCP Server](oauth-authentication.md).

| Quota | Default value | Adjustable | Description |
| --- | --- | --- | --- |
| Authenticated requests per account per Region | 10 per second (sustained) | No | The maximum number of authenticated requests per second to the AWS MCP Server per AWS account in a single Region. AWS MCP Server does not count unauthenticated requests against this per-account quota; it limits them separately per source IP address. |
| Unauthenticated requests per source IP address per Region | 5 per second (sustained) | No | The maximum number of unauthenticated requests per second from a single source IP address in a single Region. This limit is lower than the authenticated per-account rate and applies per source IP address rather than per account. To get more capacity, authenticate your requests. |

## Session limits
<a name="session-limits"></a>

The following limits apply to individual sessions with AWS MCP Server. These limits are not adjustable.

| Limit | Value | Adjustable | Description |
| --- | --- | --- | --- |
| Maximum ephemeral storage retention | 8 hours | No | The maximum duration that ephemeral compute storage is retained for a session. After this time, ephemeral storage is reclaimed. |

## Monitoring your quotas
<a name="monitoring-quotas"></a>

AWS MCP Server publishes usage metrics to the `AWS/Usage` namespace in CloudWatch. You can use these metrics with the Service Quotas console to measure your utilization and create alarms as you approach a quota. The following usage metrics are available:
+ `CallCount` (Resource: `Request`) – The number of requests made to the AWS MCP Server
+ `ResourceCount` (Resource: `ConcurrentConnection`) – The number of concurrent connections
+ `ResourceCount` (Resource: `AccountSessionCount`) – The number of concurrent active sessions per account
+ `ResourceCount` (Resource: `UserSessionCount`) – The number of concurrent active sessions per user

For more information about these metrics, see [Usage metrics](cloudwatch-metrics.md#usage-metrics) in the [AWS MCP Server CloudWatch metrics](cloudwatch-metrics.md) section.

**Note**
Requests that are throttled before reaching the AWS MCP Server are not reflected in the `CallCount` metric. For more information about this limitation, see [Usage metrics](cloudwatch-metrics.md#usage-metrics).

For more information about monitoring your usage and setting up alarms, see [AWS usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html) in the *CloudWatch User Guide* and [Service Quotas and Amazon CloudWatch](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html) in the *Service Quotas User Guide*.
