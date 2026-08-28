---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-object-lock-batchops.html
---

# Managing S3 Object Lock using S3 Batch Operations
<a name="managing-object-lock-batchops"></a>

You can use S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects. S3 Batch Operations can perform a single operation on lists of Amazon S3 objects that you specify. A single job can perform a specified operation on billions of objects containing exabytes of data. Amazon S3 tracks progress, sends notifications, and stores a detailed completion report of all actions, providing a fully managed, auditable, and serverless experience. You can use S3 Batch Operations through the Amazon S3 console, AWS CLI, AWS SDKs, or Amazon S3 REST API.

With S3 Object Lock, you can place a legal hold on an object version. Like setting a retention period, a legal hold prevents an object version from being overwritten or deleted. However, a legal hold doesn't have an associated retention period and remains in effect until the legal hold is removed. For more information, see [S3 Object Lock legal hold](batch-ops-legal-hold.md).

To use S3 Batch Operations with Object Lock to add legal holds to many Amazon S3 objects at once, see the following topics.

**Topics**
+ [Enabling S3 Object Lock using S3 Batch Operations](batch-ops-object-lock.md)
+ [Setting Object Lock retention using Batch Operations](batch-ops-object-lock-retention.md)
+ [Using S3 Batch Operations with S3 Object Lock retention compliance mode](batch-ops-compliance-mode.md)
+ [Use S3 Batch Operations with S3 Object Lock retention governance mode](batch-ops-governance-mode.md)
+ [Using S3 Batch Operations to turn off S3 Object Lock legal holds](batch-ops-legal-hold-off.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
