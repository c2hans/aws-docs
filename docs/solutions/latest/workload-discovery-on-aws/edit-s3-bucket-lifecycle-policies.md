---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/edit-s3-bucket-lifecycle-policies.html
---

# Edit S3 bucket lifecycle policies
<a name="edit-s3-bucket-lifecycle-policies"></a>

During deployment, the solution [configures lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-lifecycle.html) policies on two buckets:
+  `CostAndUsageReportBucket`
+  `AccessLogsBucket`

**Important**
These lifecycle policies delete data from these buckets after 90 days. You can [edit the lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-lifecycle.html) to fit any internal policies you have.
