---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/encryption-at-rest-studio.html
---

# Studio notebooks
<a name="encryption-at-rest-studio"></a>

In Amazon SageMaker Studio, your SageMaker Studio notebooks and data can be stored in the following locations:
+ An S3 bucket – When you onboard to Studio and enable shareable notebook resources, SageMaker AI shares notebook snapshots and metadata in an Amazon Simple Storage Service (Amazon S3) bucket.
+ An EFS volume – When you onboard to Studio, SageMaker AI attaches an Amazon Elastic File System (Amazon EFS) volume to your domain for storing your Studio notebooks and data files. The EFS volume persists after the domain is deleted.
+ An EBS volume – When you open a notebook in Studio, an Amazon Elastic Block Store (Amazon EBS) is attached to the instance that the notebook runs on. The EBS volume persists for the duration of the instance.

SageMaker AI uses the AWS Key Management Service (AWS KMS) to encrypt the S3 bucket and both volumes. By default, it uses a KMS key managed in an AWS service account. For more control, you can specify your own customer managed key when you onboard to Studio or through the SageMaker API. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md) and [CreateDomain](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDomain.html).

In the `CreateDomain` API, you use the `S3KmsKeyId` parameter to specify the customer managed key for shareable notebooks. You use the `KmsKeyId` parameter to specify the customer managed key for the EFS and EBS volumes. The same customer managed key is used for both volumes. The customer managed key for shareable notebooks can be the same customer managed key as used for the volumes or a different customer managed key.

**Important**
The working directory of your users within the storage volume is `/home/sagemaker-user`. If you specify your own AWS KMS key, everything in the working directory is encrypted using your customer managed key. If you don't specify a AWS KMS key, the data inside `/home/sagemaker-user` is encrypted with an AWS managed key. Regardless of whether you specify an AWS KMS key, all of the data outside of the working directory is encrypted with an AWS Managed Key.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
