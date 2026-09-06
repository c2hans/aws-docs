---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_data_rest_encrypt.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC08-BP02 Enforce encryption at rest
<a name="sec_protect_data_rest_encrypt"></a>

 You should ensure that the only way to store data is by using encryption. AWS Key Management Service (AWS KMS) integrates seamlessly with many AWS services to make it easier for you to encrypt all your data at rest. For example, in Amazon Simple Storage Service (Amazon S3), you can set [default encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) on a bucket so that all new objects are automatically encrypted. Additionally, [Amazon Elastic Compute Cloud (Amazon EC2) ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default)and [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) support the enforcement of encryption by setting default encryption. You can use [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) to check automatically that you are using encryption, for example, for [Amazon Elastic Block Store (Amazon EBS) volumes](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html), [Amazon Relational Database Service (Amazon RDS) instances](https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html), and [Amazon S3 buckets](https://docs.aws.amazon.com/config/latest/developerguide/s3-default-encryption-kms.html).

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Enforce encryption at rest for Amazon Simple Storage Service (Amazon S3): Implement Amazon S3 bucket default encryption.
  +  [How do I enable default encryption for an S3 bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/default-bucket-encryption.html)
+  Use AWS Secrets Manager: Secrets Manager is an AWS service that makes it easy for you to manage secrets. Secrets can be database credentials, passwords, third-party API keys, and even arbitrary text.
  +  [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
+  Configure default encryption for new EBS volumes: Specify that you want all newly created EBS volumes to be created in encrypted form, with the option of using the default key provided by AWS, or a key that you create.
  +  [Default encryption for EBS volumes](https://aws.amazon.com/blogs/aws/new-opt-in-to-default-encryption-for-new-ebs-volumes/)
+  Configure encrypted Amazon Machine Images (AMIs): Copying an existing AMI with encryption enabled will automatically encrypt root volumes and snapshots.
  +  [AMIs with encrypted Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
+  Configure Amazon Relational Database Service (Amazon RDS) encryption: Configure encryption for your Amazon RDS database clusters and snapshots at rest by enabling the encryption option.
  +  [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html)
+  Configure encryption in additional AWS services: For the AWS services you use, determine the encryption capabilities.
  +  [AWS Documentation](https://docs.aws.amazon.com/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AMIs with encrypted Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
+  [AWS Crypto Tools](https://docs.aws.amazon.com/aws-crypto-tools)
+  [AWS Documentation](https://docs.aws.amazon.com/)
+  [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html)
+  [AWS KMS Cryptographic Details Whitepaper](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html)
+  [AWS Key Management Service](https://aws.amazon.com/kms)
+  [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
+  [AWS cryptographic services and tools](https://docs.aws.amazon.com/crypto/latest/userguide/awscryp-overview.html)
+  [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
+  [Default encryption for EBS volumes](https://aws.amazon.com/blogs/aws/new-opt-in-to-default-encryption-for-new-ebs-volumes/)
+  [Encrypting Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
+  [How do I enable default encryption for an S3 bucket?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/default-bucket-encryption.html)
+  [Protecting Amazon S3 Data Using Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html)

 **Related videos:**
+  [How Encryption Works in AWS](https://youtu.be/plv7PQZICCM)
+  [Securing Your Block Storage on AWS](https://youtu.be/Y1hE1Nkcxs8)
