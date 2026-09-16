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

To access the pre-populated queries:

1. Sign in to the [Amazon CloudWatch Log Analytics console](https://console.aws.amazon.com/cloudwatch/home#log-analytics). You can also reach this page by choosing **Log Analytics** under **Logs** in the CloudWatch console navigation pane.

1. Choose **Saved queries**.

1. Expand the **ISB-<namespace>** folder, and run one of these queries:
   +  **LogQuery** — Search for all logs related to a specific account, lease, lease template, or user.
   +  **ErrorLogs** — View all recent errors. Some `WARN`-level entries are expected operational events (for example, `AccountQuarantined` and `LeaseRequestRateLimited`), not solution errors.
   +  **AccountCleanupLogs** — View the AWS Nuke output for a specific cleanup build, including individual resource deletion failures. For more information, see [Resolving Account Cleanup Failures](administrator-guide.md#resolving-account-cleanup-failures).

**Log Analytics is now the default console experience**
This experience combines the CloudWatch Logs Insights query editor with Live Tail and Contributor Insights. If you have opted out of Log Analytics, choose **Logs Insights** under **Logs** instead. The saved queries and the steps that follow are the same. For more information, refer to [Analyzing log data with CloudWatch Log Analytics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogAnalytics.html) in the *Amazon CloudWatch Logs User Guide*.

## AWS X-Ray
<a name="aws-x-ray"></a>

Innovation Sandbox includes [AWS X-Ray](https://aws.amazon.com/xray/) tracing for all critical execution paths. Use X-Ray to identify latency bottlenecks, trace requests across Lambda functions, and pinpoint where failures occur in multi-step workflows such as lease provisioning and account cleanup.
