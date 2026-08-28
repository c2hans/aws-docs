---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand-setup-api.html
---

# Set up automatic-scaling for Amazon MSK using the API
<a name="msk-autoexpand-setup-api"></a>

This process describes how to use the Amazon MSK API to implement automatic scaling for storage.

1. Use the [ RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html) API to register a storage utilization target.

1. Use the [ PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html) API to create an auto-expansion policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
