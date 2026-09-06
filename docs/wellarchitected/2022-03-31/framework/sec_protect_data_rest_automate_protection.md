---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_data_rest_automate_protection.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC08-BP03 Automate data at rest protection
<a name="sec_protect_data_rest_automate_protection"></a>

 Use automated tools to validate and enforce data at rest controls continuously, for example, verify that there are only encrypted storage resources. You can [automate validation that all EBS volumes are encrypted](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html) using [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html). [AWS Security Hub CSPM](http://aws.amazon.com/security-hub/) can also verify several different controls through automated checks against security standards. Additionally, your AWS Config Rules can automatically [remediate noncompliant resources](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html#setup-autoremediation).

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation_guidance"></a>

 *Data at rest* represents any data that you persist in non-volatile storage for any duration in your workload. This includes block storage, object storage, databases, archives, IoT devices, and any other storage medium on which data is persisted. Protecting your data at rest reduces the risk of unauthorized access, when encryption and appropriate access controls are implemented.

 Enforce encryption at rest: You should ensure that the only way to store data is by using encryption. AWS KMS integrates seamlessly with many AWS services to make it easier for you to encrypt all your data at rest. For example, in Amazon Simple Storage Service (Amazon S3) you can set [default encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) on a bucket so that all new objects are automatically encrypted. Additionally, [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) and [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) support the enforcement of encryption by setting default encryption. You can use [AWS Managed Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) to check automatically that you are using encryption, for example, for [EBS volumes](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html), [Amazon Relational Database Service (Amazon RDS) instances](https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html), and [Amazon S3 buckets](https://docs.aws.amazon.com/config/latest/developerguide/s3-default-encryption-kms.html).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Crypto Tools](https://docs.aws.amazon.com/aws-crypto-tools)
+  [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html)

 **Related videos:**
+  [How Encryption Works in AWS](https://youtu.be/plv7PQZICCM)
+  [Securing Your Block Storage on AWS](https://youtu.be/Y1hE1Nkcxs8)
