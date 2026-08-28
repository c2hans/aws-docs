---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_protect_data_rest_key_mgmt.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC08-BP01 Implement secure key management
<a name="sec_protect_data_rest_key_mgmt"></a>

 By defining an encryption approach that includes the storage, rotation, and access control of keys, you can help provide protection for your content against unauthorized users and against unnecessary exposure to authorized users. AWS Key Management Service (AWS KMS) helps you manage encryption keys and [integrates with many AWS services](https://aws.amazon.com/kms/details/#integration). This service provides durable, secure, and redundant storage for your AWS KMS keys. You can define your key aliases as well as key-level policies. The policies help you define key administrators as well as key users. Additionally, AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys in the AWS Cloud. It helps you meet corporate, contractual, and regulatory compliance requirements for data security by using FIPS 140-2 Level 3 validated HSMs.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement AWS KMS: AWS KMS makes it easy for you to create and manage keys and control the use of encryption across a wide range of AWS services and in your applications. AWS KMS is a secure and resilient service that uses FIPS 140-2 validated hardware security modules to protect your keys.
  +  [Getting started: AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html)
+  Consider AWS Encryption SDK: Use the AWS Encryption SDK with AWS KMS integration when your application needs to encrypt data client-side.
  +  [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Key Management Service](https://aws.amazon.com/kms)
+  [AWS cryptographic services and tools](https://docs.aws.amazon.com/crypto/latest/userguide/awscryp-overview.html)
+  [Getting started: AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html)
+  [Protecting Amazon S3 Data Using Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html)

 **Related videos:**
+  [How Encryption Works in AWS](https://youtu.be/plv7PQZICCM)
+  [Securing Your Block Storage on AWS](https://youtu.be/Y1hE1Nkcxs8)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
