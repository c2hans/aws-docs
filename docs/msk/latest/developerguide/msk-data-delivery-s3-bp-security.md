---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-bp-security.html
---

# Security
<a name="msk-data-delivery-s3-bp-security"></a>
+ Scope IAM permissions to the specific destination bucket used by each Channel.
+ Use the `aws:SourceArn` condition in the trust policy to prevent other clusters or services from assuming the Channel role.
+ Enable CloudTrail logging to audit all Channel API calls.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
