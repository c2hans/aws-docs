---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html
---

# Managing storage costs with Amazon S3 Intelligent-Tiering
<a name="intelligent-tiering"></a>

The S3 Intelligent-Tiering storage class is designed to optimize storage costs by automatically moving data to the most cost-effective access tier when access patterns change, without operational overhead or impact on performance. For a small monthly object monitoring and automation charge, S3 Intelligent-Tiering monitors access patterns and automatically moves objects that have not been accessed to lower-cost access tiers.

S3 Intelligent-Tiering delivers automatic storage cost savings in three low latency and high throughput access tiers. For data that can be accessed asynchronously, you can choose to activate automatic archiving capabilities within the S3 Intelligent-Tiering storage class. There are no retrieval charges in S3 Intelligent-Tiering. If an object in the Infrequent Access tier or Archive Instant Access tier is accessed later, it is automatically moved back to the Frequent Access tier. No additional tiering charges apply when objects are moved between access tiers within the S3 Intelligent-Tiering storage class.

S3 Intelligent-Tiering is the recommended storage class for data with unknown, changing, or unpredictable access patterns, independent of object size or retention period, such as data lakes, data analytics, and new applications.

 The S3 Intelligent-Tiering storage class supports all Amazon S3 features, including the following:
+ S3 Inventory, for verifying the access tier of objects
+ S3 Replication, for replicating data to any AWS Region
+ S3 Storage Lens, for viewing storage usage and activity metrics
+ Server-side encryption, for protecting object data
+ S3 Object Lock, for preventing accidental deletion of data
+ AWS PrivateLink, for accessing Amazon S3 through a private endpoint in a virtual private cloud (VPC)

For information about using S3 Intelligent-Tiering, see the following sections:

**Topics**
+ [How S3 Intelligent-Tiering works](intelligent-tiering-overview.md)
+ [Using S3 Intelligent-Tiering](using-intelligent-tiering.md)
+ [Managing S3 Intelligent-Tiering](intelligent-tiering-managing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
