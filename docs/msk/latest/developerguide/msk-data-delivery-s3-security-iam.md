---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-security-iam.html
---

# IAM and access control
<a name="msk-data-delivery-s3-security-iam"></a>

A Channel uses IAM roles for authorization. Follow least privilege:
+ Scope S3 permissions to the specific bucket and prefix used by the Channel.
+ Use `aws:SourceArn` and `aws:SourceAccount` in the trust policy to prevent confused deputy attacks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
