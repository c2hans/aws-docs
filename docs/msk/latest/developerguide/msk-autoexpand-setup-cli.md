---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand-setup-cli.html
---

# Set up automatic scaling using the CLI
<a name="msk-autoexpand-setup-cli"></a>

This process describes how to use the Amazon MSK CLI to implement automatic scaling for storage.

1. Use the [ RegisterScalableTarget](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/#available-commands) command to register a storage utilization target.

1. Use the [ PutScalingPolicy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/#available-commands) command to create an auto-expansion policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
