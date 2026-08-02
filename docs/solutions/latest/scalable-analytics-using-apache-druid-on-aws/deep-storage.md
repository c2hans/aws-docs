---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/deep-storage.html
---

# Deep storage
<a name="deep-storage"></a>

As a default configuration, the guidance creates a new S3 bucket designated as deep storage for the Druid cluster. Additionally, it generates a [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) key to provide server-side encryption with AWS KMS (SSE-KMS) for the deep storage.
