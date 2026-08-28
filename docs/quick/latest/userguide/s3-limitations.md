---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/s3-limitations.html
---

# Limitations
<a name="s3-limitations"></a>

When using Amazon S3 integrations in Amazon Quick, be aware of the following limitations:
+ The Amazon S3 bucket must be in the same AWS Region as your Amazon Quick application.
+ Each document can have a maximum of 2,500 individual user or group ACL entries.
+ Global ACL configuration file maximum size: 100 MB.
+ Document metadata file maximum size: 5 MB.

For more information about document-level ACL limitations, see [Limitations](acl-best-practices-kb.md#acl-limitations).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
