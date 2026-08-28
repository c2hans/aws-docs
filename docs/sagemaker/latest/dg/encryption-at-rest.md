---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest.html
---

# Protect Data at Rest Using Encryption
<a name="encryption-at-rest"></a>

Amazon SageMaker AI automatically encrypts your data using an AWS managed key for Amazon S3 (SSE-S3) by default for the following features: Studio notebooks, notebook instances, model-building data, model artifacts, and output from Training, Batch Transform, and Processing jobs.

For cross-account access, you must specify your own customer managed key when creating SageMaker AI resources, as the default AWS managed key for Amazon S3 can't be shared across accounts. For data output to Amazon S3 Express One Zone, the data is encrypted using server-side encryption with Amazon S3 managed keys (SSE-S3). Additionally, data output to Amazon S3 directory buckets can't be encrypted with server-side encryption using AWS Key Management Service keys (SSE-KMS). For more information on AWS KMS, see [What is AWS Key Management Service?](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)

**Topics**
+ [Studio notebooks](encryption-at-rest-studio.md)
+ [Notebook instances, SageMaker AI jobs, and Endpoints](encryption-at-rest-nbi.md)
+ [SageMaker geospatial capabilities](geospatial-encryption-at-rest.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
