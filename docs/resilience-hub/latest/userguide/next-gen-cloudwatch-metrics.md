---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-cloudwatch-metrics.html
---

# CloudWatch metrics reference
<a name="next-gen-cloudwatch-metrics"></a>

When a failure mode assessment completes successfully, Next generation Resilience Hub publishes policy achievability metrics to your account's Amazon CloudWatch (CloudWatch) under the `ResilienceHub` namespace. Metrics are emitted only upon assessment completion. If no assessment has run, or if the assessment did not produce achievability results, no metrics are reported.

Your service's permission model must include an invoker role with the `cloudwatch:PutMetricData` permission for Next generation Resilience Hub to emit metrics to your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
