---
source_url: https://docs.aws.amazon.com/solutions/latest/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/overview.html
---

# Automatically copy your Amazon Glacier vault archives to an S3 bucket and storage classes
<a name="overview"></a>

Data Transfer from Amazon Glacier Vaults to Amazon S3 is a serverless Guidance that automates and optimizes the restore, copy, and transfer process of [Amazon Simple Storage Service Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) (Amazon Glacier) vault archives. The Guidance copies all of the vault's archives to a defined [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket destination and [storage class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html). Then you can attach [tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-tagging.html) to help you categorize your data, such as with data classification or cost allocation. A prebuilt [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboard provides a visualization of the copy operation progress.

**Important**
 Amazon S3 and Amazon Glacier are different AWS services.
 *Amazon Glacier* is an object storage service for low-cost data archiving and long-term backup. It stores *archives* in *vaults*. It doesn't offer storage classes. The Amazon Glacier service provides a console. However, any archive operation, such as upload, download, or deletion, requires you to use the AWS CLI or write code. There is no console support for archive operations.
 *Amazon S3* is an object storage service for any type of data. It stores *objects* in *buckets*. It offers different storage classes for frequent access, infrequent access, archives, and optimized tiering. You can interact with the Amazon S3 service by using the Amazon S3 console or [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI).
 The *Amazon Glacier Instant Retrieval, Amazon Glacier Flexible Retrieval, and S3 Glacier Deep Archive storage classes* are features of the Amazon S3 service. The Amazon Glacier Flexible Retrieval storage class offers the same features as the Amazon Glacier service. The Amazon Glacier service doesn't offer storage classes.

 For example, Saanvi works at AnyCompany Archives. Five years ago, she used the Amazon Glacier service to store scanned copies of historical documents in a vault. AnyCompany just announced that they will have a different online exhibit each month, featuring documents that are stored in the Amazon Glacier vault. To address this change of business:
+  Saanvi wants to take advantage of the storage classes offered with the Amazon S3 service, including more flexibility in how files are stored and accessed.
+  Using Data Transfer from Amazon Glacier Vaults to Amazon S3, Saanvi can copy all of her document archives from her Amazon Glacier vault to an S3 bucket. She can assign them to the S3 storage classes that best fit her use cases. For example, she can use the S3 Standard storage class for documents that will be featured in the first exhibit and accessed daily, and the S3 Glacier Deep Archive storage class for documents that won't be featured in any of the exhibits.
+  Now that the documents are stored in the Amazon S3 service, Saanvi can also apply [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) configurations, tag her data, and use the Amazon S3 console.

**Note**
 This Guidance doesn't delete the original archives or the source Amazon Glacier vault. You must manually delete the archives and vault. For more information, refer to [Deleting an Archive in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/deleting-an-archive.html) in the *Amazon Glacier Developer Guide*.
 If your source Amazon Glacier vault has a [Vault Lock policy](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock-policy.html) that prevents deletion, you must delete this policy before deleting the original archives. However, if your Vault Lock policy is in the Locked state, you can't delete it. See [Amazon Glacier Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html) and [Abort Vault Lock (DELETE lock-policy)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AbortVaultLock.html) in the Amazon Glacier Developer Guide for more information.

 This implementation guide provides an overview of the Data Transfer from Amazon Glacier Vaults to Amazon S3 Guidance, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the Guidance to the Amazon Web Services (AWS) Cloud.

 The intended audience for using this Guidance's features and capabilities in their environment includes solution architects, business decision makers, DevOps engineers, data scientists, and cloud professionals. Practical experience with the AWS Cloud, Amazon Glacier vaults, Amazon S3 buckets, and Amazon S3 storage classes is preferred.

 Use this navigation table to quickly find answers to these questions:

|  If you want to . . .  |  Read . . .  |
| --- | --- |
|  Know the cost for running this Guidance. <br /> The estimated cost for running this Guidance in the US East (Ohio) Region is USD $153.57 to copy 100,000 Amazon Glacier vault archives, totaling 100 TB of data, from an Amazon Glacier vault to an S3 bucket.  |  [Cost](cost.md)  |
|  Understand the security considerations for this Guidance.  |  [Security](security-1.md)  |
|  Know how to plan for quotas for this Guidance. <br /> This Guidance uses [AWS Lambda](https://aws.amazon.com/lambda/) functions to transfer data. This affects your account-wide Lambda concurrency limit.  |  [Quotas](quotas.md)  |
|  Know which AWS Regions support this Guidance.  |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
|  View or download the AWS CloudFormation template included in this Guidance to automatically deploy the infrastructure resources (the "stack") for this Guidance.  |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the Guidance. | [GitHub repository](https://github.com/aws-solutions/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3) |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Data Transfer from Amazon S3 Glacier Vaults to Amazon S3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
