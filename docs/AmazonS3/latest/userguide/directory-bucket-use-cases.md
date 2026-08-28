---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-use-cases.html
---

# Use cases for directory buckets
<a name="directory-bucket-use-cases"></a>

Directory buckets support bucket creation in the following bucket location types: Availability Zone or Local Zone.

For low latency use cases, you can create a directory bucket in a single Availability Zone to store data. Directory buckets in Availability Zones support the S3 Express One Zone storage class. S3 Express One Zone storage class is recommended if your application is performance sensitive and benefits from single-digit millisecond `PUT` and `GET` latencies. To learn more about creating directory buckets in Availability Zones, see [High performance workloads](directory-bucket-high-performance.md).

 For data residency use cases, you can create a directory bucket in a single AWS Dedicated Local Zone (DLZ) to store data. Directory buckets in Local Zones support the S3 One Zone-Infrequent Access (S3 One Zone-IA; Z-IA) storage class. To learn more about creating directory buckets in Local Zones, see [Data residency workloads](directory-bucket-data-residency.md).

**Topics**
+ [High performance workloads](directory-bucket-high-performance.md)
+ [Data residency workloads](directory-bucket-data-residency.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
