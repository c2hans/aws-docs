---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/sensitive-data.html
---

# Handling sensitive data
<a name="sensitive-data"></a>

Typically, sensitive data contains personally identifiable information (PII) or confidential information that must be secured for compliance or legal reasons. If encryption is required only on a row or column level, we recommend that you use a landing zone layer. This is *partially-sensitive* data.

However, if the entire dataset is considered sensitive, we recommend using separate Amazon Simple Storage Service (Amazon S3) buckets to contain the data. This is *highly-sensitive* data. These separate Amazon S3 buckets must be used for each data layer, and "*sensitive*" should be included in the bucket's name.

We recommend that you encrypt sensitive buckets with AWS Key Management Service (AWS KMS) by using [client-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html). You must also use client-side encryption to encrypt the AWS Glue jobs that transform your data. Client-side encryption should be configured on those buckets and the data processing pipelines roles, such as the IAM role for the AWS Glue job. These roles must have the appropriate permissions to use the configured KMS key and to read and write to the bucket.

## Using a landing zone to mask sensitive data
<a name="masking-sensitive-data"></a>

You can use a landing zone layer for partially-sensitive datasets (for example, if encryption is only required at the row or column level). This data is ingested into the landing zone's Amazon S3 bucket and is then masked. After the data is masked, it is ingested into the raw layer's Amazon S3 bucket. This bucket is encrypted with [server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) by using Amazon S3 managed keys (SSE-S3). If required, you can tag data at the object level.

Any data that is already masked can bypass the landing zone and be directly ingested into the raw layer's Amazon S3 bucket. There are two access levels in the stage and analytics layers for partially-sensitive datasets; one level has full access to all data, and the other level only has access to non-sensitive rows and columns.

The following diagram shows a data lake where partially-sensitive datasets use a landing zone to mask the sensitive data but highly-sensitive datasets use separate, encrypted Amazon S3 buckets. The landing zone is isolated by using restrictive IAM and bucket policies, and the encrypted buckets use client-side encryption with AWS KMS.

![Use different data flows and Amazon S3 buckets to process different levels of sensitive data.](https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/images/guide-img/d76f2946-d940-4cf3-ac21-937dd4709e95/images/e7792e37-4a2d-4c18-87a7-ae7eb5e19cb5.png)

The diagram shows the following workflow:

1. Highly-sensitive data is sent to an encrypted Amazon S3 bucket in the raw data layer.

1. An AWS Glue job validates and transforms the data into a consumption-ready format and then places the file into an encrypted Amazon S3 bucket in the stage layer.

1. An AWS Glue job aggregates data according to business requirements and places the data into an encrypted Amazon S3 bucket in the analytics layer.

1. Partially-sensitive data is sent to landing zone bucket.

1. Sensitive rows and columns are masked, and data is then sent to the Amazon S3 bucket in the raw layer.

1. Non-sensitive data is directly sent to the Amazon S3 bucket in the raw layer.

1. An AWS Glue job validates and transforms the data into a consumption-ready format and places the files into the Amazon S3 bucket for the stage layer.

1. An AWS Glue job aggregates the data according to your organization's requirements and places the data into an Amazon S3 bucket in the analytics layer.
