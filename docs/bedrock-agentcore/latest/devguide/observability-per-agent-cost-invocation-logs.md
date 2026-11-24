---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-per-agent-cost-invocation-logs.html
---

# Approach 2: Bedrock invocation logs (real-time cost visibility)

If you need per-agent cost visibility without the 24-hour delay (for example, for dashboards, alerting, or ad-hoc analysis), query Bedrock model invocation logs directly. For agents that call the Amazon Bedrock `Converse` and `ConverseStream` APIs, this approach provides token-level detail within seconds.

## Step 1: Enable Bedrock model invocation logging
<a name="per-agent-cost-logs-enable"></a>

Complete this one-time setup per account:

1. Open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/).

1. In the navigation pane, choose **Settings**.

1. Under **Model invocation logging**, toggle it on.

1. Select **CloudWatch Logs** as the destination.

1. Choose or create a log group (for example, `/aws/bedrock/modelinvocations`).

1. Under **Data types**, select at least **Text**.

1. Choose **Save**.

## Step 2: Query per-agent token usage
<a name="per-agent-cost-logs-query"></a>

Run an Amazon CloudWatch Logs Insights query against your invocation log group:

In the following query, replace `my-agent-role` with your IAM role name.

```sql
fields modelId,
       output.outputBodyJson.usage.inputTokens as input_t,
       output.outputBodyJson.usage.outputTokens as output_t,
       output.outputBodyJson.usage.cacheReadInputTokens as cache_read_t,
       output.outputBodyJson.usage.cacheWriteInputTokens as cache_write_t
| filter identity.arn like "my-agent-role"
| stats sum(input_t) as total_input,
        sum(output_t) as total_output,
        sum(cache_read_t) as total_cache_read,
        sum(cache_write_t) as total_cache_write,
        count(*) as invocations
  by modelId
```

The `identity.arn` field contains the full assumed-role ARN. Filtering with `like "my-agent-role"` matches regardless of the session suffix.

**Streaming calls nest token counts**
For streaming calls (`ConverseStream`), token counts are nested at `output.outputBodyJson.usage`, not at the top-level `inputTokenCount`/`outputTokenCount` fields.

## Step 3: Calculate per-agent inference cost
<a name="per-agent-cost-logs-calculate"></a>

Use the following formula to calculate inference cost:

```
Inference cost = (input_tokens × input_price_per_token)
              + (output_tokens × output_price_per_token)
              + (cache_read_tokens × cache_read_price_per_token)
              + (cache_write_tokens × cache_write_price_per_token)
```

For the per-token prices to use in this formula, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) on the AWS website.

Cache read and cache write tokens are billed at separate, lower rates.

## Step 4: Combine with AgentCore infrastructure cost
<a name="per-agent-cost-logs-combine"></a>

Use the Amazon CloudWatch `GetMetricData` API to retrieve `CPUUsed-vCPUHours` and `MemoryUsed-GBHours` from the `AWS/Bedrock-AgentCore` namespace. Filter by the `Resource` dimension (the agent runtime ARN), or by `Name` (format `<agentName>::<endpointName>`, for example `myAgent::DEFAULT`).

```
Total agent cost = Inference cost + Infrastructure cost
```

This gives you the complete per-agent cost picture in real time.

**Set a log retention period**
Set a log group retention period (for example, 30 days) to control Amazon CloudWatch Logs storage costs. Without a retention policy, CloudWatch Logs stores logs indefinitely and continues to incur storage charges.
