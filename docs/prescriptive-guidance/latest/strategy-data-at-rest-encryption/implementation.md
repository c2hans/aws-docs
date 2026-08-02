---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/implementation.html
---

# Implementation
<a name="implementation"></a>

In this strategy, *architecture* refers to the technical implementation of your encryption standards. This section includes information about how AWS services, such as [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) and [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html), can help you implement your data-at-rest encryption strategy according to your policy and standards.

AWS KMS is a managed service that helps you create and control the cryptographic keys that are used to protect your data. KMS keys never leave the service unencrypted. To use or manage your KMS keys, you interact with AWS KMS, and many AWS services are integrated with AWS KMS.

CloudHSM is a cryptographic service for creating and maintaining *hardware security modules* (HSMs) in your AWS environment. HSMs are computing devices that process cryptographic operations and provide secure storage for cryptographic keys. If your standards requires you to use FIPS 140-2 Level 3 validated hardware, or if your standards dictate use of industry-standard APIs, such as PKCS\#11, Java Cryptography Extensions (JCE), and Microsoft CryptoNG (CNG), then you might consider using CloudHSM.

You can configure CloudHSM as a custom key store for AWS KMS. This solution combines the convenience and service integration of AWS KMS with the added control and compliance benefits of using a CloudHSM cluster in your AWS account. For more information, see [Custom key stores](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) (AWS KMS documentation).

This document discusses AWS KMS features at a high level and explains how AWS KMS can address your policy and standards.

## Cost, convenience, and control
<a name="cost-convenience-control"></a>

AWS KMS offers different types of keys. Some are owned or managed by AWS, and others are created and managed by customers. You can choose between these options based on the level of control you want to have over the key and cost considerations:
+ **AWS owned keys** – AWS owns and manages these keys, and they are used in multiple AWS accounts. Some AWS services support AWS owned keys. You can use these keys for no charge. This key type relieves you from the cost and administrative overhead of managing the key lifecycle and access to it. For more information about this type of key, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) (AWS KMS documentation).
+ **AWS managed keys** – If an AWS service is integrated with AWS KMS, it can create, manage, and use this type of keys on your behalf, in order to protect your resources in that service. These keys are created in your AWS account, and only AWS services can use them. There is no monthly fee for an AWS managed key. They can be subject to fees for use in excess of the free tier, but some AWS services cover these costs for you. You can use identity policies to control view and audit access for these keys, but AWS manages the key lifecycle. For more information about this type of key, see [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (AWS KMS documentation). For a comprehensive list of the AWS services that integrate with AWS KMS, see [AWS service integration](https://aws.amazon.com/kms/features/#AWS_Service_Integration) (AWS marketing).
+ **Customer managed keys** – You create, own, and manage this type of key, and you have full control over the key lifecycle. For segregation of duties, you can use both identity and resource-based policies to control access to the key. You can also set up automated [key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html). Customer managed keys incur a monthly fee, and if you exceed the free tier, they also incur a fee for use. For more information about this type of key, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) (AWS KMS documentation).

For more information about key storage and usage, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/) (AWS marketing).

## Performance and encryption types
<a name="performance"></a>

Based upon the chosen encryption type in standards, you can use two types of KMS keys.
+ **Symmetric** – All of the AWS KMS key types support symmetric encryption. When encrypting customer managed keys, you can use a single-strength key for encryption and decryption with AES-256-GCM.
+ **Asymmetric** – Customer managed keys support asymmetric encryption. You can choose between different key strengths and algorithms, based upon your intended use. Asymmetric keys can encrypt and decrypt with RSA and can sign and verify operations with RSA or ECC. Asymmetric key algorithms inherently provide separation of roles and simplify key management. When using asymmetric encryption with AWS KMS, some operations aren't supported, such as rotating keys and importing external key material.

For more information about the AWS KMS operations that symmetric and asymmetric keys support, see [Key type reference](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-compare.html) (AWS KMS documentation).

### Envelope encryption
<a name="envelope-encryption.950598df-312e-5385-b9d6-e59b1ab59059"></a>

Envelope encryption is built into AWS KMS. In AWS KMS, you generate data keys in either plaintext or encrypted format. Encrypted data keys are encrypted with a KMS key. You can store the KMS key in a custom key store in an AWS CloudHSM cluster. For more information about the benefits of envelope encryption, see [About envelope encryption](about-data-encryption.md#about-envelope-encryption).

## Key storage location
<a name="storage"></a>

You use policies to manage access to AWS KMS resources. *Policies* describe who can access which resources. Policies attached to an AWS Identity and Access Management (IAM) principal are called *identity-based policies* or *IAM policies*. Policies attached to other kinds of resources are called *resource policies*. AWS KMS resource policies for AWS KMS keys are called *key policies*. Every KMS key has a key policy.

Key policies provide flexibility to store the encryption key in a central location or store it closer to the data, in a distributed manner. Consider the following AWS KMS features when you're deciding where to store KMS keys in your AWS account:
+ **Single-Region infrastructure support** – By default, KMS keys are Region-specific, and they never leave AWS KMS unencrypted. If your standards have strict requirements for controlling keys in a specific geographical location, explore using single-Region keys.
+ **Multi-Region** **infrastructure support** – AWS KMS also supports special-purpose key type called *multi-Region keys*. Storing data in multiple AWS Regions is a common configuration for disaster recovery. By using multi-Region keys, you can transfer data between Regions without re-encrypting it, and you can manage the data as if you had the same key in each Region. This functionality is highly useful if your standards require that your encryption infrastructure spans multiple Regions in an active-active configuration. For more information, see [Multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) (AWS KMS documentation).
+ **Centralized management** – If your standards require that you store keys in a centralized location, you can use AWS KMS to store all of your encryption keys in a single AWS account. You use key policies to grant access to other applications, which can be in different accounts in the same Region. Centralized key management can reduce the administrative overhead of managing the key lifecycle and key access control.
+ **External key material** – You can import externally generated key material into AWS KMS. Support for this functionality is available for single and multi-Region symmetric keys. Because the material of the symmetric key is generated externally, you are responsible for protecting the generated key materials. For more information, see [Imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) (AWS KMS documentation).

## Access control
<a name="controlling-access"></a>

In AWS KMS, you can implement granular-level access control by using the following policy mechanisms: [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), [IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html), and [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html). Using these controls, you can set-up your separation of duties based on roles, such as administrators, key users who can encrypt the data, key users who can decrypt the data, and key users who can both encrypt and decrypt the data. For more information, see [Authentication and access control](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) (AWS KMS documentation).

## Auditing and logging
<a name="auditing-and-logging"></a>

AWS KMS integrates with AWS CloudTrail and Amazon EventBridge for logging and monitoring purposes. All AWS KMS API operations are recorded and auditable in CloudTrail logs. You can use Amazon CloudWatch, EventBridge, and AWS Lambda to set up custom monitoring solutions to configure notifications and automatic remediation. For more information, see [Logging and monitoring](https://docs.aws.amazon.com/kms/latest/developerguide/security-logging-monitoring.html) (AWS KMS documentation).
