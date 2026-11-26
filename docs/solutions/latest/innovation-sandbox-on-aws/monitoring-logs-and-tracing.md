---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/monitoring-logs-and-tracing.html
---

# Logs and tracing

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

The Sandbox Spaces agent writes its application logs to the `/aws/bedrock-agentcore/runtimes/<runtime-id>-DEFAULT` log group, which Amazon Bedrock AgentCore creates. `<runtime-id>` is the ID of the `ISB_<namespace>_SandboxAgentRuntime` agent runtime. The retention tiers in the preceding table don’t apply to this log group, and the solution doesn’t archive it to Amazon S3. Set its retention to match your policy.

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

## Sandbox Spaces observability
<a name="sandbox-spaces-observability"></a>

The Sandbox Spaces agent runs in Amazon Bedrock AgentCore Runtime in the Hub account. AgentCore publishes service metrics for the agent, such as invocations, sessions, latency, and errors, to Amazon CloudWatch without any setup. To also see the agent’s sessions, traces, and spans, turn on [CloudWatch Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html) in the Hub account, in the Region where you deployed the solution. The solution does not turn it on for you, and sandbox accounts need no setup. Until you turn it on, CloudWatch shows no Sandbox Spaces sessions or traces.

Transaction Search is an account-level setting for the Region. It applies to every workload in that Region of the Hub account that sends traces to X-Ray, including the solution’s Lambda functions. Before you turn it on, read [What Sandbox Spaces traces contain](#sandbox-spaces-trace-content).

### Turning on Transaction Search
<a name="sandbox-spaces-enable-transaction-search"></a>

To turn on Transaction Search in the console:

1. Sign in to the Hub account and open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/) in the Region where you deployed the solution.

1. In the navigation pane, under **Application Signals (APM)**, choose **Transaction search**.

1. Choose **Enable Transaction Search**.

1. Select the check box to ingest spans as structured logs.

1. Keep the percentage of spans to index at 1%, and choose **Save**.

To turn on Transaction Search with the AWS CLI, run the following commands with credentials for the Hub account. The first command allows X-Ray to write spans to CloudWatch Logs. The second command sets CloudWatch Logs as the destination for spans. Replace `<region>` with the Region where you deployed the solution and `<hub-account-id>` with the ID of the Hub account.

```bash
aws logs put-resource-policy --region <region> --policy-name TransactionSearchXRayAccess --policy-document '{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "TransactionSearchXRayAccess",
    "Effect": "Allow",
    "Principal": { "Service": "xray.amazonaws.com" },
    "Action": "logs:PutLogEvents",
    "Resource": [
      "arn:aws:logs:<region>:<hub-account-id>:log-group:aws/spans:*",
      "arn:aws:logs:<region>:<hub-account-id>:log-group:/aws/application-signals/data:*"
    ],
    "Condition": {
      "ArnLike": { "aws:SourceArn": "arn:aws:xray:<region>:<hub-account-id>:*" },
      "StringEquals": { "aws:SourceAccount": "<hub-account-id>" }
    }
  }]
}'

aws xray update-trace-segment-destination --region <region> --destination CloudWatchLogs
```

To confirm the change, run `aws xray get-trace-segment-destination --region <region>`. When Transaction Search is active, the response shows `"Destination": "CloudWatchLogs"` and `"Status": "ACTIVE"`.

After you turn on Transaction Search, spans can take about 10 minutes to appear. For the required permissions and other options, refer to [Enable transaction search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html) in the *Amazon CloudWatch User Guide*.

**Note**
Transaction Search charges are based on the volume of spans ingested. Indexing 1% of spans as trace summaries is included at no extra charge, and the spans do not also incur CloudWatch Logs ingestion charges. While Transaction Search is off, the agent incurs no span charges. For rates, refer to [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

### What Sandbox Spaces traces contain
<a name="sandbox-spaces-trace-content"></a>

The solution configures the agent to send its spans to the shared `aws/spans` log group in the Hub account. Spans from other workloads in the Hub account are stored in the same log group.

The spans contain the full conversation: the user’s messages, the agent’s replies, the system prompt, and the AWS CLI commands that the agent runs in sandbox accounts, with their output. All of this content is stored in the Hub account.

If Transaction Search is already on in the Hub account, the solution starts storing Sandbox Spaces conversations as soon as you deploy version 1.4.0 and turn on Sandbox Spaces. There is no separate opt-in.

The solution’s Amazon Bedrock guardrail detects and masks AWS access key IDs, AWS secret access keys, and passwords in the conversation before the model receives it, and in the model’s replies. It also masks email addresses in the model’s replies. Because masking depends on detection, the guardrail might miss some keys or passwords.

The guardrail doesn’t change the spans, which store command output as the command returned it. For example, if a user reads an AWS Systems Manager SecureString parameter or an AWS Secrets Manager secret through the agent, the spans store the decrypted value. For more information about the guardrail, see [Sandbox Spaces](sandbox-spaces-architecture.md).

To protect this data, use these controls in the Hub account:
+  **Read access** – Any principal with `logs:StartQuery`, `logs:FilterLogEvents`, or `logs:GetLogEvents` on the `aws/spans` log group can read the conversation content of every lease. Use IAM to limit read access to the administrators who troubleshoot Sandbox Spaces.
+  **Retention** – Set the retention period of the `aws/spans` log group to match your data handling policy. For instructions, refer to [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide*.
+  **Masking** – To redact more content, add a CloudWatch Logs data protection policy to the `aws/spans` log group. The policy masks only log events ingested after you create it, and users with the `logs:Unmask` permission can still view the original values. For more information, refer to [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).

Tell your users that their chat content, including command output, is kept in the Hub account for the retention period that you set.

### Viewing agent sessions and traces
<a name="sandbox-spaces-view-traces"></a>

To view Sandbox Spaces data, open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability) in the Hub account, in the Region where you deployed the solution. Choose **GenAI Observability**, and then choose **Bedrock AgentCore**.
+  **Agent view** – Lists the agents in the account with their metrics, such as sessions, traces, token usage, errors, and latency. Choose the `ISB_<namespace>_SandboxAgentRuntime` agent to see its dashboards.
+  **Sessions view** – Lists agent sessions. Choose a session to see its metrics and its traces.
+  **Traces view** – Lists individual traces. Choose a trace to see its summary, spans, and content.

This guide does not describe the **Memory** and **Gateway** views. For more information, refer to [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AgentCore-Agents.html) in the *Amazon CloudWatch User Guide* and [View observability data for your Amazon Bedrock AgentCore agents](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-view.html) in the *Amazon Bedrock AgentCore Developer Guide*.
