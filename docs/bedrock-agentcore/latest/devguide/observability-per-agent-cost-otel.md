---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-per-agent-cost-otel.html
---

# Approach 3: OpenTelemetry (OTEL) spans with metric filters (operational monitoring)

For continuous monitoring with automated alerting, use AgentCore’s built-in OTEL instrumentation combined with Amazon CloudWatch metric filters and alarms. This approach converts per-agent token data from log entries into CloudWatch Metrics, enabling native alarms and anomaly detection.

## Step 1: Enable CloudWatch Transaction Search
<a name="per-agent-cost-otel-transaction-search"></a>

You enable Transaction Search one time for each account. If you already enabled Transaction Search as part of [Get started with AgentCore Observability](observability-get-started.md), skip this step.

1. Create a resource policy that grants AWS X-Ray (X-Ray) access to ingest spans in CloudWatch Logs:

   ```bash
   aws logs put-resource-policy \
       --policy-name TransactionSearchXRayAccess \
       --policy-document '{
           "Version": "2012-10-17",
           "Statement": [{
               "Sid": "TransactionSearchXRayAccess",
               "Effect": "Allow",
               "Principal": {"Service": "xray.amazonaws.com"},
               "Action": "logs:PutLogEvents",
               "Resource": [
                   "arn:aws:logs:REGION:ACCOUNT_ID:log-group:aws/spans:*",
                   "arn:aws:logs:REGION:ACCOUNT_ID:log-group:/aws/application-signals/data:*"
               ],
               "Condition": {
                   "ArnLike": {"aws:SourceArn": "arn:aws:xray:REGION:ACCOUNT_ID:*"},
                   "StringEquals": {"aws:SourceAccount": "ACCOUNT_ID"}
               }
           }]
       }'
   ```

1. Configure the destination of trace segments:

   ```bash
   aws xray update-trace-segment-destination --destination CloudWatchLogs
   ```

1. (Optional) Configure the sampling percentage:

   ```bash
   aws xray update-indexing-rule \
       --name "Default" \
       --rule '{"Probabilistic": {"DesiredSamplingPercentage": 100}}'
   ```

## Step 2: Deploy agents on AgentCore Runtime
<a name="per-agent-cost-otel-deploy"></a>

You deploy your agent using the AgentCore CLI. You don’t need any observability-specific configuration.

```bash
agentcore create --name myagent --defaults
cd myagent
agentcore deploy --yes
```

AgentCore Runtime automatically instruments your agent with OTEL and publishes spans to the `aws/spans` log group.

## Step 3: Verify per-agent data in the GenAI Observability dashboard
<a name="per-agent-cost-otel-verify"></a>

1. Open the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **GenAI Observability**.

The dashboard displays per-agent token usage without additional setup.

## Step 4: Query per-agent cost with CloudWatch Logs Insights
<a name="per-agent-cost-otel-query"></a>

Run the following query against the `aws/spans` log group:

```sql
fields `resource.attributes.service.name` as agent,
       `attributes.gen_ai.request.model` as model,
       `attributes.gen_ai.usage.input_tokens` as input_tok,
       `attributes.gen_ai.usage.output_tokens` as output_tok
| filter `scope.name` = "opentelemetry.instrumentation.botocore.bedrock-runtime"
    and ispresent(`attributes.gen_ai.usage.input_tokens`)
| stats sum(input_tok) as total_input,
        sum(output_tok) as total_output,
        sum(input_tok) + sum(output_tok) as total_tokens,
        count(*) as llm_calls
  by agent, model
| sort total_tokens desc
```

**Count one span for each model call**
Each Amazon Bedrock model call produces more than one span with `gen_ai.operation.name = "chat"`. The agent framework emits one span (for example, `chat` in Strands or `ChatBedrockConverse.chat` in LangChain), and the botocore Bedrock instrumentation emits another, named `chat <model-id>`. To count each call once for every framework, the query and metric filters in this topic match only the botocore span (`scope.name` = `opentelemetry.instrumentation.botocore.bedrock-runtime`). That span carries `gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens`. Total tokens are calculated as input plus output, because `gen_ai.usage.total_tokens` isn’t emitted by all frameworks.

## Step 5: Create metric filters for per-agent token metrics
<a name="per-agent-cost-otel-metric-filters"></a>

The following metric filters publish input and output tokens for each agent. They match the botocore Bedrock span, which occurs once for each model call. The following AWS CLI command creates a metric filter that publishes per-agent input tokens. Save the following as `per-agent-input-tokens-filter.json`:

```json
{
    "logGroupName": "aws/spans",
    "filterName": "PerAgentInputTokens",
    "filterPattern": "{ $.scope.name = \"opentelemetry.instrumentation.botocore.bedrock-runtime\" && $.attributes.['gen_ai.usage.input_tokens'] = * }",
    "metricTransformations": [
        {
            "metricNamespace": "AgentCore/PerAgentCost",
            "metricName": "InputTokens",
            "metricValue": "$.attributes.['gen_ai.usage.input_tokens']",
            "dimensions": {
                "AgentName": "$.resource.attributes.['service.name']",
                "ModelId": "$.attributes.['gen_ai.request.model']"
            }
        }
    ]
}
```

```bash
aws logs put-metric-filter --cli-input-json file://per-agent-input-tokens-filter.json
```

The following AWS CLI command creates a metric filter that publishes per-agent output tokens. Save the following as `per-agent-output-tokens-filter.json`:

```json
{
    "logGroupName": "aws/spans",
    "filterName": "PerAgentOutputTokens",
    "filterPattern": "{ $.scope.name = \"opentelemetry.instrumentation.botocore.bedrock-runtime\" && $.attributes.['gen_ai.usage.output_tokens'] = * }",
    "metricTransformations": [
        {
            "metricNamespace": "AgentCore/PerAgentCost",
            "metricName": "OutputTokens",
            "metricValue": "$.attributes.['gen_ai.usage.output_tokens']",
            "dimensions": {
                "AgentName": "$.resource.attributes.['service.name']",
                "ModelId": "$.attributes.['gen_ai.request.model']"
            }
        }
    ]
}
```

```bash
aws logs put-metric-filter --cli-input-json file://per-agent-output-tokens-filter.json
```

**Match the dimension form to the namespace**
The dimension form depends on the namespace. For the custom `AgentCore/PerAgentCost` namespace, the metric filters populate the `AgentName` dimension from the OTEL span attribute `service.name`, which uses the dot form (`<agent>.DEFAULT`). Use the dot form in alarms for this namespace. The double-colon form (`<agent>::DEFAULT`) applies only to the default `AWS/Bedrock-AgentCore` runtime metrics.

## Step 6: Set up per-agent token alarms
<a name="per-agent-cost-otel-alarms"></a>

You can use static threshold alarms, anomaly detection alarms, or both.

To receive notifications, create an Amazon SNS topic and subscribe to it. In the following commands, replace `arn:aws:sns:REGION:ACCOUNT_ID:my-topic` with your topic ARN.

### Static threshold alarm
<a name="_static_threshold_alarm"></a>

Use static thresholds for hard budget limits. Create this alarm when you have a fixed token budget that should never be exceeded.

Before you begin, install and configure the AWS CLI with permissions to create CloudWatch alarms.

The following AWS CLI command creates a static threshold alarm. The alarm triggers when total tokens (input plus output) exceed 5,000 in a 5-minute period. In the command, replace the example agent name `myagent_myagent.DEFAULT` with your agent name (`my-agent-name`) and the example model ID with your model ID (`your-model-id`):

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name "AgentCore-TokenThreshold-myagent" \
    --comparison-operator GreaterThanThreshold \
    --threshold 5000 \
    --evaluation-periods 1 \
    --alarm-actions arn:aws:sns:REGION:ACCOUNT_ID:my-topic \
    --metrics '[
        {"Id": "m1", "ReturnData": false,
         "MetricStat": {"Period": 300, "Stat": "Sum",
          "Metric": {"Namespace": "AgentCore/PerAgentCost", "MetricName": "InputTokens",
           "Dimensions": [{"Name": "AgentName", "Value": "myagent_myagent.DEFAULT"},
                          {"Name": "ModelId", "Value": "us.anthropic.claude-sonnet-4-6"}]}}},
        {"Id": "m2", "ReturnData": false,
         "MetricStat": {"Period": 300, "Stat": "Sum",
          "Metric": {"Namespace": "AgentCore/PerAgentCost", "MetricName": "OutputTokens",
           "Dimensions": [{"Name": "AgentName", "Value": "myagent_myagent.DEFAULT"},
                          {"Name": "ModelId", "Value": "us.anthropic.claude-sonnet-4-6"}]}}},
        {"Id": "total", "Expression": "m1 + m2", "Label": "TotalTokens", "ReturnData": true}
    ]'
```

### Anomaly detection alarm
<a name="_anomaly_detection_alarm"></a>

The following AWS CLI command creates an alarm that uses anomaly detection on total tokens (input plus output). CloudWatch trains the anomaly detection model from the metric’s history and needs some history before the alarm can evaluate. The alarm enters the `ALARM` state when token usage rises above the expected band, and sends a notification to your SNS topic.

```bash
aws cloudwatch put-metric-alarm \
    --alarm-name "AgentCore-TokenAnomaly-myagent" \
    --comparison-operator GreaterThanUpperThreshold \
    --evaluation-periods 1 \
    --threshold-metric-id ad1 \
    --alarm-actions arn:aws:sns:REGION:ACCOUNT_ID:my-topic \
    --metrics '[
        {"Id": "m1", "ReturnData": false,
         "MetricStat": {"Period": 300, "Stat": "Sum",
          "Metric": {"Namespace": "AgentCore/PerAgentCost", "MetricName": "InputTokens",
           "Dimensions": [{"Name": "AgentName", "Value": "myagent_myagent.DEFAULT"},
                          {"Name": "ModelId", "Value": "us.anthropic.claude-sonnet-4-6"}]}}},
        {"Id": "m2", "ReturnData": false,
         "MetricStat": {"Period": 300, "Stat": "Sum",
          "Metric": {"Namespace": "AgentCore/PerAgentCost", "MetricName": "OutputTokens",
           "Dimensions": [{"Name": "AgentName", "Value": "myagent_myagent.DEFAULT"},
                          {"Name": "ModelId", "Value": "us.anthropic.claude-sonnet-4-6"}]}}},
        {"Id": "total", "Expression": "m1 + m2", "Label": "TotalTokens", "ReturnData": true},
        {"Id": "ad1", "Expression": "ANOMALY_DETECTION_BAND(total, 2)", "Label": "TotalTokens (expected)", "ReturnData": true}
    ]'
```

**Combine both alarm types**
Use static thresholds for hard budget limits and anomaly detection for catching unexpected usage patterns. The two alarm types complement each other.
