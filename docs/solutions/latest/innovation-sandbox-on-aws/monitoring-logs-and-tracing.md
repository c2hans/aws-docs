---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/monitoring-logs-and-tracing.html
---

# Logs and tracing
<a name="monitoring-logs-and-tracing"></a>

Innovation Sandbox emits structured JSON logs from all Lambda functions into Amazon CloudWatch Logs. Each log entry includes a correlation ID, the originating Lambda function, and searchable properties such as account IDs, lease IDs, and user emails.

## Log retention strategy
<a name="log-retention-strategy"></a>

The solution implements a multi-tier log retention strategy:

| Tier | Retention |
| --- | --- |
| Amazon CloudWatch Logs | 90 days (default) |
| Amazon S3 Standard | 1 year (default) |
| Amazon S3 Glacier | 6 additional years (default) |

Logs are automatically exported from CloudWatch to S3 every 7 days. The 90-day CloudWatch retention provides sufficient time for operational troubleshooting, while S3/Glacier archiving supports compliance with typical audit and regulatory requirements.

## Pre-populated log queries
<a name="cloudwatch-log-queries"></a>

Innovation Sandbox provides several pre-populated Amazon CloudWatch Logs Insights queries to help you troubleshoot issues.

To access log insights queries:

1. Sign in to the [Amazon CloudWatch Logs Insights console](https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights).

1. Choose **Saved and sample queries**.

1. From the sample queries, run one of these queries:
   +  **LogQuery** — Search for all logs related to a specific account, lease, lease template, or user.
   +  **ErrorLogs** — View all recent errors. Some `WARN`-level entries are expected operational events (for example, `AccountQuarantined` and `LeaseRequestRateLimited`), not solution errors.
   +  **AccountCleanupLogs** — View the logs from a specific cleanup execution.

## AWS X-Ray
<a name="aws-x-ray"></a>

Innovation Sandbox includes [AWS X-Ray](https://aws.amazon.com/xray/) tracing for all critical execution paths. Use X-Ray to identify latency bottlenecks, trace requests across Lambda functions, and pinpoint where failures occur in multi-step workflows such as lease provisioning and account cleanup.
