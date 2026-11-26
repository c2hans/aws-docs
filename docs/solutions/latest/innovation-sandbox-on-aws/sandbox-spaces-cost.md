---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/sandbox-spaces-cost.html
---

# Cost and budget

Sandbox Spaces has usage-based costs in the sandbox account and the Hub account:
+ Amazon Bedrock model inference runs in the sandbox account of the lease. These charges accrue in the sandbox account and count toward the lease budget.
+ Amazon Bedrock AgentCore Runtime, AgentCore Memory, and the Amazon Bedrock Guardrails resource are deployed in the Hub account.

Costs vary with runtime, memory, guardrail, and model usage. For current rates, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) and [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/). For monitoring cost estimates, see [Optional feature costs](cost.md#optional-feature-costs).

Billing data lags behind usage, so the solution reads the Amazon Bedrock token usage of the sandbox account every 10 minutes. It estimates the Amazon Bedrock cost from that usage, in place of the lagging billed Amazon Bedrock cost. It then evaluates the budget thresholds of the lease against this estimate plus the billed cost of all other services. A lease with Sandbox Spaces turned on always has Amazon Bedrock token monitoring turned on. For more information, see [Budget thresholds](manager-guide.md#budget-thresholds) and [Tracking your spending](user-section.md#sandbox-spaces-budget).
