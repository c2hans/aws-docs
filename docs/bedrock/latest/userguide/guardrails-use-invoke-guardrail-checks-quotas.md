---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-invoke-guardrail-checks-quotas.html
---

# Quotas
<a name="guardrails-use-invoke-guardrail-checks-quotas"></a>

The following quotas are enforced for `InvokeGuardrailChecks`. Quotas marked as adjustable can be raised through Service Quotas; others are hard limits.

**InvokeGuardrailChecks quotas**

| Name | Default value | Description |
| --- | --- | --- |
| Requests per minute (RPM) | 1,500 | Maximum number of InvokeGuardrailChecks calls per account, per Region, per minute. |

**Note**
**Burst traffic** – Even when your overall traffic is below the per-minute limits, a sudden burst of requests within a short window might be throttled with a `ThrottlingException`. Smooth traffic over time and use exponential backoff with jitter on retries.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
