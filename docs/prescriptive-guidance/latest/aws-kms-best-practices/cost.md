---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/cost.html
---

# Cost and billing management best practices for AWS KMS
<a name="cost"></a>

Through breadth and depth, AWS services offer the flexibility to manage your costs while meeting business requirements. This section covers pricing for key storage in AWS Key Management Service (AWS KMS), and it provides recommendations to reduce costs, such as through key caching. You can also review KMS key usage to determine if there are additional opportunities to reduce costs.

**This section discusses the following cost and billing management topics:**
+ [AWS KMS pricing for key storage](#cost-key-storage)
+ [Amazon S3 bucket keys with default encryption](#cost-bucket-keys)
+ [Caching data keys by using the AWS Encryption SDK](#cost-key-caching)
+ [Alternatives to key caching and AWS KMS bucket keys](#cost-alternatives)
+ [Reviewing customer managed key usage in Amazon Athena](#cost-key-usage)

## AWS KMS pricing for key storage
<a name="cost-key-storage"></a>

Each AWS KMS key that you create in AWS KMS incurs a charge. The monthly charge is the same for symmetric keys, asymmetric keys, HMAC keys, multi-Region keys (each primary and each replica multi-Region key), keys with imported key material, and KMS keys with a key origin of either AWS CloudHSM or an external key store.

For KMS keys that you rotate automatically or on demand, the first and second rotation of the key adds an additional monthly charge (prorated hourly) in cost. After the second rotation, any subsequent rotations in that month are not billed. Please see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/) for latest pricing information.

You can use [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to configure a usage budget. AWS Budgets can alert you when the spend within your account exceeds certain thresholds. For costs related to AWS KMS, you can [create a usage budget](https://docs.aws.amazon.com/cost-management/latest/userguide/create-usage-budget.html) to alert based on KMS keys or requests. This can improve your visibility into your AWS KMS key storage and use costs.

## Amazon S3 bucket keys with default encryption
<a name="cost-bucket-keys"></a>

In some use cases, workloads that access or generate large numbers of objects in Amazon Simple Storage Service (Amazon S3) can generate high volumes of requests to AWS KMS, which increases your costs. Configuring [Amazon S3 bucket keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) can help you reduce costs by up to 99%. This is a recommended alternative to disabling encryption to help reduce costs associated with AWS KMS.

## Caching data keys by using the AWS Encryption SDK
<a name="cost-key-caching"></a>

When using the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) to perform client-side encryption, [data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/data-key-caching.html) can help improve the performance of your application, reduce the risk that your application's requests to AWS KMS are [throttled](https://docs.aws.amazon.com/kms/latest/developerguide/throttling.html), and help you reduce costs. For more information about how to get started, see [How to use data key caching](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/implement-caching.html).

## Alternatives to key caching and Amazon S3 bucket keys
<a name="cost-alternatives"></a>

If key caching is not an option for you because of your data handling requirements, you can also request AWS KMS [quota increases](https://docs.aws.amazon.com/kms/latest/developerguide/increase-quota.html) by using the AWS Management Console or the [Service Quotas API](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/Welcome.html). Consider the volume of API calls that you might make. The number of API calls that you make is a significant factor in [AWS KMS pricing](https://aws.amazon.com/kms/pricing/). If you increase the request-rate quota to scale your performance, the increasing number of requests to AWS KMS incurs additional costs.

## Managing logging costs for KMS key usage
<a name="cost-key-usage"></a>

All AWS KMS API calls are logged to AWS CloudTrail. Applications and services can generate large volumes of AWS KMS API calls (such as for cryptographic operations, including encrypting and decrypting). It can be challenging to review CloudTrail logs without a tool that helps you organize that data, investigate trends, and search for anomalous API activity. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) provides predefined data structures that can help you quickly set up tables for CloudTrail logs and start analyzing your log data. It is especially useful for ad-hoc analysis or further investigation during incident response. For more information, see [Query AWS CloudTrail logs](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html) in the Athena documentation.

Because you pay on a per-query basis for Athena, you can set up your tables in advance at no cost. There are no charges for data definition language statements. When you are responding to an incident, this helps you make sure that many prerequisites are already met. To help you prepare, it is a best practice to write your queries after creating your table, test them, and make sure that they are producing the results you want. You can save your queries in Athena for future use. For more information about how to get started with Athena, see [Getting started with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html).

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide visibility into the operations that are performed on or within a resource. These are also known as *data plane operations*. Examples include Amazon S3 `PutObject` events or Lambda function operation API calls. Data events are often high-volume activities, and you incur charges for logging them. To help control the volume of data events that are logged to trails or event data stores in CloudTrail, you can optimize your logging to reduce costs for CloudTrail, AWS KMS, and Amazon S3 by configuring advanced event selectors to limit which data events to log in CloudTrail. For more information, see [How to optimize AWS CloudTrail costs by using advanced event selectors](https://aws.amazon.com/blogs/mt/optimize-aws-cloudtrail-costs-using-advanced-event-selectors/) (AWS blog post).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
