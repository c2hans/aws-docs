---
source_url: https://docs.aws.amazon.com/solutions/latest/media2cloud-on-aws/lifecycle-policy.html
---

# Lifecycle policy
<a name="lifecycle-policy"></a>

 The Media2Cloud on AWS solution turns on Amazon S3 Intelligent Tiering storage class for the Amazon S3 ingestion, proxy, and web buckets.

 For the S3 ingestion bucket, the solution applies additional lifecycle policy to transition objects to Amazon Glacier storage class after 90 days and Amazon Glacier Deep Archive storage class after 180 days.

 For the S3 log bucket, the solution configures the lifecycle policy to keep the logs for seven days and turns off the versioning.
