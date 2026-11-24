---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-per-agent-cost.html
---

# Monitor per-agent costs with Amazon CloudWatch

When you deploy multiple AI agents on Amazon Bedrock AgentCore Runtime, each agent calls foundation models independently. AgentCore is platform-agnostic. Your agents can call Amazon Bedrock, Anthropic directly, OpenAI, or any large language model (LLM) endpoint. AgentCore bills Runtime compute (CPU and memory) per agent, but your model provider bills tokens separately at the account level, not per agent. If you run multiple agents with different models and usage patterns, your inference bill shows total token consumption. It doesn’t tell you which agent consumed what.

This topic describes three complementary approaches to attribute per-agent costs:
+  [Bedrock IAM principal attribution](observability-per-agent-cost-iam.md) – For billing-grade cost allocation in AWS Cost Explorer with no code changes.
+  [Bedrock model invocation logs](observability-per-agent-cost-invocation-logs.md) – For real-time per-agent cost visibility through Amazon CloudWatch (CloudWatch) Logs Insights.
+  [OTEL spans with metric filters](observability-per-agent-cost-otel.md) – For continuous operational monitoring with CloudWatch alarms.

If you’re unsure which approach fits your use case, see the [Choosing the right approach](#choosing-the-right-approach) comparison table.

## Why per-agent cost visibility matters
<a name="per-agent-cost-why"></a>

Inference cost is typically the largest component of an agent’s total cost. Infrastructure (CPU and memory) makes up the remainder. A per-agent cost calculation that excludes inference omits the majority of the total cost.

Per-agent cost visibility supports the following use cases:
+  **Cost comparison**

  Per-agent cost data lets you compare an agent’s cost against the process or alternative that it replaced.
+  **Budgeting and forecasting**

  Per-agent data from existing agents provides a baseline for estimating the cost of new agents.
+  **Chargeback across teams**

  Different business units own different agents. Per-agent attribution lets you allocate costs to each team based on actual usage.
+  **Optimization targeting**

  When costs increase, per-agent visibility identifies which agent is responsible and whether the cause is invocation volume, a prompt change, or a model change.
+  **Governance**

  As agent adoption grows from pilots to production, per-agent tracking lets you set budgets and identify unexpected cost increases.

## Architecture overview
<a name="per-agent-cost-architecture"></a>

The following diagram shows how per-agent cost data flows across three layers. Each AgentCore Runtime assumes its own IAM role, which Amazon Bedrock records on every inference call. That IAM principal flows to AWS Cost Explorer for billing (Approach 1). Amazon Bedrock also writes invocation logs to Amazon CloudWatch Logs for real-time queries (Approach 2). AgentCore Runtime emits OpenTelemetry (OTEL) spans to the `aws/spans` log group, where metric filters and alarms provide monitoring (Approach 3).

![Diagram of per-agent cost data flowing from AgentCore Runtime through Amazon Bedrock to Amazon CloudWatch and Cost Explorer.](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/per-agent-cost-architecture.png)

The data flows across three layers as follows:
+ Each AgentCore Runtime assumes its own AWS Identity and Access Management (IAM) role, which Amazon Bedrock records on every inference call. That IAM principal flows to AWS Cost Explorer for billing (Approach 1).
+ Amazon Bedrock writes invocation logs to CloudWatch Logs for real-time queries (Approach 2).
+ AgentCore Runtime emits OTEL spans to the `aws/spans` log group, where metric filters and alarms provide monitoring (Approach 3).

The architecture has three layers:

 **Amazon Bedrock AgentCore Runtime**
Deploys each agent as a separate runtime with its own IAM execution role and automatic OTEL instrumentation. Each Bedrock model call generates a span containing the agent name, model ID, input token count, and output token count.

 **Amazon Bedrock**
Records the caller’s IAM principal for every inference request. This flows to AWS Cost Explorer (for billing) and to invocation logs (for real-time queries).

 **Amazon CloudWatch**
Receives OTEL spans in the `aws/spans` log group and invocation logs in a configurable log group. The GenAI Observability dashboard displays per-agent token usage natively. Metric filters and alarms provide continuous monitoring.

## What AgentCore provides by default
<a name="per-agent-cost-default-data"></a>

AgentCore Runtime automatically publishes two categories of observability data without any configuration:

 **Runtime metrics** in the `AWS/Bedrock-AgentCore` namespace include `Invocations`, `Sessions`, `Latency`, `Errors`, `Throttles`, `CPUUsed-vCPUHours`, and `MemoryUsed-GBHours`. These metrics have a `Name` dimension that contains the agent name (for example, `faqagent_faqagent::DEFAULT`). You can use this dimension to calculate per-agent Runtime compute cost directly:

```
Runtime cost per agent = CPUUsed-vCPUHours × (vCPU-hour rate) + MemoryUsed-GBHours × (GB-hour rate)
```

These runtime metrics in the `AWS/Bedrock-AgentCore` namespace (with the `Name` dimension) are your per-agent source for Runtime compute cost. For more information about per-agent model inference cost, see [Approach 1: Bedrock IAM principal attribution](observability-per-agent-cost-iam.md).

For more information about current vCPU-hour and GB-hour rates, see [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/).

 **OTEL spans** in the `aws/spans` log group contain per-invocation detail including the following:
+ Agent name (`resource.attributes.service.name`)
+ Model ID (`attributes.gen_ai.request.model`)
+ Input tokens (`attributes.gen_ai.usage.input_tokens`)
+ Output tokens (`attributes.gen_ai.usage.output_tokens`)
+ Total tokens (`attributes.gen_ai.usage.total_tokens`), emitted by some frameworks such as Strands and LangChain. Not all frameworks emit this attribute, so the metric filters in this topic calculate total tokens as input plus output.

Token counts exist only in OTEL spans (log data), not in CloudWatch Metrics. This creates a gap. The GenAI Observability dashboard reads the spans directly, but CloudWatch Alarms require metrics. The approaches in this topic bridge that gap.

## IAM role separation: security best practice
<a name="per-agent-cost-iam-separation"></a>

Deploying each agent with its own IAM role isn’t just a cost attribution technique. It’s an AWS security best practice. Separate roles per agent provide the following benefits:
+  **Confined blast radius**

  If one agent’s role is compromised, only that agent’s permissions are exposed.
+  **Separation of duties**

  Each agent gets only the permissions it needs (least privilege).
+  **Auditability**

   AWS CloudTrail logs show exactly which agent performed which action.
+  **Cost attribution**

  The same role separation enables all three approaches described in this topic.

AgentCore creates a separate role by default when you deploy with `agentcore deploy`. Each runtime gets its own role automatically.

## Choosing the right approach
<a name="choosing-the-right-approach"></a>

The following table compares the three approaches for per-agent cost attribution.

| Criteria | IAM principal attribution | Invocation logs | OTEL spans |
| --- | --- | --- | --- |
| Best for | Billing, chargeback, finance | Real-time cost, ad-hoc analysis | Operational monitoring, alerting |
| Accuracy | Billing-exact | Billing-aligned | SDK-observed |
| Latency | \~24 hours | Seconds | Seconds |
| Framework dependency | None | None | Needs OTEL instrumentation |
| Sampling | 100% | 100% | Can be sampled |
| Alerting | No | Requires scheduled query | Native metric filters \+ alarms |
| Setup effort | Tag roles \+ activate tags | Enable invocation logging | Transaction Search \+ metric filters |
| Retroactive | No | Yes | No |

 **Recommendation:** Use IAM principal attribution for finance and chargeback reporting. Use invocation logs for real-time cost dashboards and ad-hoc investigation. Use OTEL spans for continuous operational monitoring with automated alerts. The approaches complement each other. Most production deployments benefit from all three.

## Full per-agent cost picture
<a name="per-agent-cost-full-picture"></a>

The following table shows all components of per-agent cost.

| Component | Source | Metric | Pricing |
| --- | --- | --- | --- |
| Runtime CPU |  `AWS/Bedrock-AgentCore`  |  `CPUUsed-vCPUHours`  |  [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/)  |
| Runtime Memory |  `AWS/Bedrock-AgentCore`  |  `MemoryUsed-GBHours`  |  [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/)  |
| LLM Input Tokens | OTEL metric filter or invocation logs |  `InputTokens`  | Per model |
| LLM Output Tokens | OTEL metric filter or invocation logs |  `OutputTokens`  | Per model |
| LLM Cache Tokens | Invocation logs |  `CacheRead` / `CacheWrite` tokens | Per model (discounted) |

## Exporting to third-party observability tools
<a name="per-agent-cost-third-party"></a>

The following screenshot shows an Amazon CloudWatch dashboard built from this telemetry. The stacked cost chart shows cumulative cost for each agent over time. The token usage panel shows input and output token counts. The cost distribution panel shows each agent’s share of total cost.

![Amazon CloudWatch dashboard with a stacked per-agent cost chart and a token usage panel and a cost distribution panel.](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/per-agent-cost-dashboard.png)

AgentCore Runtime emits OTEL-compatible telemetry. If your organization uses a third-party observability platform (for example, NewRelic, Datadog, or Splunk), you can configure the OTEL exporter to send spans to your platform. You can send them instead of or in addition to CloudWatch.

## Cost of this solution
<a name="per-agent-cost-solution-cost"></a>

The OTEL instrumentation is included with AgentCore Runtime at no extra cost. The observability pipeline uses the standard pricing of the underlying services.

The following table lists the pricing page for each service used in this solution.

| Service | Pricing |
| --- | --- |
| Amazon Bedrock AgentCore Runtime |  [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/)  |
| Amazon CloudWatch (Logs, metrics, alarms, dashboards) |  [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/)  |
| Amazon Bedrock (model inference and model invocation logging) |  [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)  |

This topic covers the following sections.

**Topics**
