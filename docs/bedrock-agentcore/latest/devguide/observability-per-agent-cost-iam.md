---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-per-agent-cost-iam.html
---

# Approach 1: Bedrock IAM principal attribution (billing-grade)

Because each AgentCore Runtime has its own IAM execution role, you can view per-agent inference cost directly in your billing data. Amazon Bedrock natively captures the IAM principal identity (user or role) for every inference request. This information flows directly into AWS Cost Explorer and Cost and Usage Report (CUR) 2.0. You need no code changes, no log queries, and no scripts.

Approach 1 (IAM principal attribution) gives per-agent model inference cost only. AgentCore Runtime compute bills under a separate service, Amazon Bedrock AgentCore, which IAM principal attribution does not cover. As a result, Approach 1 does not capture runtime compute cost.

## Why this approach stands out
<a name="per-agent-cost-iam-why"></a>

This approach is framework-agnostic. It works at the Bedrock API layer, not the SDK or agent framework layer. Whether your agents use Strands, LangChain, CrewAI, or raw boto3, if the call goes through Bedrock’s `bedrock-runtime` API (`InvokeModel`, `Converse`, `ChatCompletions`), the IAM role is recorded in billing. There are no instrumentation dependencies and no sampling concerns, so 100% of calls are captured.

This is particularly valuable in organizations running agents across multiple frameworks. OTEL-based token attribution works well with frameworks that have built-in GenAI semantic convention support (such as Strands) or community auto-instrumentors (such as `opentelemetry-instrumentation-langchain` for LangChain). IAM principal attribution complements OTEL by providing a single, consistent cost view across all frameworks without requiring per-framework instrumentation setup.

## To enable IAM principal attribution
<a name="per-agent-cost-iam-enable"></a>

### Step 1: Tag your IAM roles
<a name="per-agent-cost-iam-tag-roles"></a>

Tagging is optional but recommended for filtering in Cost Explorer. In the following command, replace `my-agent-role` with your role name.

The following AWS CLI command tags your IAM role:

```bash
aws iam tag-role \
    --role-name my-agent-role \
    --tags Key=team,Value=example-team Key=cost_center,Value=CC-1234
```

### Step 2: Activate cost allocation tags
<a name="per-agent-cost-iam-activate-tags"></a>

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/billing/](https://console.aws.amazon.com/billing/).

1. In the navigation pane, choose **Cost allocation tags**.

1. Filter by IAM principal.

1. Choose **Activate**.

### Step 3: View per-agent costs in Cost Explorer
<a name="per-agent-cost-iam-view-costs"></a>

1. Open AWS Cost Explorer.

1. For model inference cost, filter by **Service** and include every model-related Bedrock value, because model spend is split across multiple service labels. Select **Amazon Bedrock**, **Amazon Bedrock Service** (where third-party models such as Anthropic Claude appear), and any marketplace-style model listings such as **Claude Sonnet 5.5 (Amazon Bedrock Edition)**. If you select only one value, you miss part of your model spend. Runtime compute cost appears separately under **Amazon Bedrock AgentCore**, which isn’t attributed by IAM principal.

1. Group by your IAM principal tags.

Per-agent costs appear within 24 hours.

### (Optional) Create a CUR 2.0 data export
<a name="per-agent-cost-iam-cur"></a>

For line-item detail, create a CUR 2.0 data export with **Include caller identity (IAM principal) allocation data** selected. This provides granular per-request cost attribution in your billing data.

## Limitations
<a name="per-agent-cost-iam-limitations"></a>

Cost Explorer data has an approximately 24-hour delay. For real-time visibility, use [Approach 2: Bedrock invocation logs](observability-per-agent-cost-invocation-logs.md).

Runtime compute is billed under the separate service **Amazon Bedrock AgentCore** and isn’t attributed to the IAM principal. Get per-agent runtime cost from the `CPUUsed-vCPUHours` and `MemoryUsed-GBHours` metrics (see [Monitor per-agent costs with Amazon CloudWatch](observability-per-agent-cost.md)).
