---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/deep-storage.html
---

# Deep storage
<a name="deep-storage"></a>

As a default configuration, the guidance creates a new S3 bucket designated as deep storage for the Druid cluster. Additionally, it generates a [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) key to provide server-side encryption with AWS KMS (SSE-KMS) for the deep storage.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Scalable Analytics Using Apache Druid on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
