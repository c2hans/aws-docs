---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/key-management.html
---

# Key management best practices for AWS KMS
<a name="key-management"></a>

When you use AWS Key Management Service (AWS KMS), you must make fundamental design decisions. These include whether to use a centralized or decentralized model for key management and access, the type of keys to use, and the type of key store to use. The following sections help you make decisions that fit your organization and use cases. This section concludes with considerations for disabling and deleting KMS keys, including actions that you can take to help protect your data and keys.

**This section contains the following topics:**
+ [Choosing a centralized or decentralized model](#key-management-model)
+ [Choosing customer managed keys, AWS managed keys, or AWS owned keys](#key-management-types)
+ [Choosing an AWS KMS key store](#key-management-stores)
+ [Deleting and disabling KMS keys](#key-management-deletion)

## Choosing a centralized or decentralized model
<a name="key-management-model"></a>

AWS recommends that you use multiple AWS accounts and manage those accounts as a single organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). There are two broad approaches to managing AWS KMS keys in multi-account environments.

The first approach is a decentralized approach, where you create keys in each account that uses those keys. When you store the KMS keys in the same accounts as the resources they protect, it is easier to delegate permissions to local administrators who understand access requirements for their AWS principals and keys. You can authorize key usage by using just a [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), or you can combine a key policy and [identity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) in AWS Identity and Access Management (IAM).

The second approach is a centralized approach, where you maintain KMS keys in one or a few designated AWS accounts. You manage keys, their life cycle, and their permissions from the centralized account. You permit other AWS accounts to use the keys only for cryptographic operations. Those accounts can't manage the key's life cycle or access permissions. This centralized model can help minimize the risk of unintended deletion of keys or privilege escalation by delegated administrators or users.

The option you choose depends on several factors. Consider the following when choosing an approach:

1. Do you have an automated or manual process for provisioning key and resource access? This includes resources such as deployment pipelines and infrastructure as code (IaC) templates. These tools can help you deploy and manage resources (such as KMS keys, key policies, IAM roles, and IAM policies) across many AWS accounts. If you don't have these deployment tools, a centralized approach to key management might be more manageable for your business.

1. Do you have administrative control over all of the AWS accounts that contain resources that use KMS keys? If so, a centralized model can simplify management and reduce the need to switch AWS accounts to manage keys. Note, however, that you must still manage IAM roles and user permissions to use keys in each account.

1. Do you need to offer access to use your KMS keys to customers or partners who have their own AWS accounts and resources? For these keys, a centralized approach can reduce administrative burden on your customers and partners.

1. Do you have authorization requirements for access to AWS resources that either a centralized or local access approach addresses more effectively? For example, if different applications or business units are responsible for managing the security of their own data, a decentralized approach to key management might be more suitable.

1. Are you exceeding service [resource quotas](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html) for AWS KMS? Because these quotas are set per AWS account, a decentralized model distributes the load across accounts, effectively multiplying service quotas.
**Note**
The management model for keys is irrelevant when considering [request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) because these quotas are applied to the account principal making a request against the key, not the account that owns or manages the key.

In general, we recommend that you start with a decentralized approach unless you can articulate a need for a centralized KMS key model.

## Choosing customer managed keys, AWS managed keys, or AWS owned keys
<a name="key-management-types"></a>

The KMS keys that you create and manage for use in your own cryptographic applications are known as *customer managed keys*. AWS services can use customer managed keys to encrypt the data the service stores on your behalf. We recommend customer managed keys if you want full control over the life cycle and usage of your keys. A customer managed key incurs a monthly cost in your account. In addition, requests to use or manage the key incur a usage cost. For more information, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/).

If you want an AWS service to encrypt your data but don't want the overhead or costs of managing keys, you can use an *AWS managed key*. This type of key exists in your account, but its use is restricted. You can use it only in the context of the AWS service that you're operating in, and only principals within the account that contains the key can use it.

An AWS managed key is a legacy key type that is no longer created for new AWS services as of 2021. Instead, new (and legacy) AWS services use an *AWS owned key* to encrypt your data by default.

We recommend that you use customer managed keys when you need granular control and use AWS owned keys when you prioritize convenience.

The following table describes the key policy, logging, management, and pricing differences between each key type. For more information about key types, see [AWS KMS concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html).

|
|
| **Consideration** | **Customer managed keys** | **AWS managed keys** | **AWS owned keys** |
| --- |--- |--- |--- |
| **Key policy** | Exclusively controlled by the customer | Controlled by service; viewable by customer | Exclusively controlled and only viewable by the AWS service that encrypts your data |
| **Logging** | AWS CloudTrail customer trail or event data store | CloudTrail customer trail or event data store | Not viewable by the customer |
| **Life cycle management** | Customer manages rotation, deletion, and AWS Region | AWS service manages rotation (annual), deletion, and Region | AWS service manages rotation (annual), deletion, and Region |
| **Pricing** | Monthly fee for key existence (pro-rated hourly); the caller is charged for API usage | No charge for key existence; the caller is charged for API usage | No charges to customer |

## Choosing an AWS KMS key store
<a name="key-management-stores"></a>

A *key store* is a secure location for storing and using cryptographic key material. A common industry practice for key stores is to use a device known as a hardware security module (HSM) that has been validated under the [NIST Federal Information Processing Standards (FIPS) 140 Cryptographic Module Validation Program](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/modules-in-process/IUT-List) at Security Level 3. Other programs support key stores that are used to process payments. [AWS Payment Cryptography](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/what-is.html) is a service you can use to protect data related to your payment workloads.

AWS KMS supports multiple key store types to help protect your key material when using AWS KMS to create and manage your encryption keys. All of the key store options supplied by AWS KMS are continually validated under FIPS 140-3 at Security Level 3. They are designed to prevent anyone, including AWS operators, from accessing your plaintext keys or using them without your permission. For more information about the available types of key stores, see [Key stores](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) in the AWS KMS documentation.

The [AWS KMS standard key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html#default-key-store) is designed to meet the needs of most workloads. If you consider a different type of key store, determine whether regulatory or other requirements (such as internal policies) require this choice, and weigh the costs and benefits.

## Deleting and disabling KMS keys
<a name="key-management-deletion"></a>

The deletion of a KMS key can have significant impact. Before you delete a KMS key that you no longer intend to use, consider whether it's adequate to set the key state to **Disabled**. While a key is disabled, it cannot be used for cryptographic operations. It still exists in AWS, and you can re-enable it in the future if required. Disabled keys continue to incur storage charges. We recommend that you disable keys instead of deleting them until you are confident that the key does not protect any data or data keys.

**Important**
Plan key deletion carefully. You can't decrypt data after you delete the corresponding key. AWS can't recover a deleted key. As with other critical operations in AWS, apply a policy that limits who can schedule keys for deletion, and require multi-factor authentication (MFA) for key deletion.

To help prevent accidental key deletion, AWS KMS enforces a waiting period of 7–30 days after you submit a `ScheduleKeyDeletion` call before it deletes the key. The default waiting period is 30 days, and the minimum is 7 days. You can [set the waiting period](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html) to any value in that range. During the waiting period, the key is still stored in AWS KMS in a **Pending Deletion** state. You can't use it for encrypt or decrypt operations. AWS CloudTrail logs any attempt to use a key in the **Pending Deletion** state for encryption or decryption. You can [set an Amazon CloudWatch alarm](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html) for these events in your CloudTrail logs. If you receive alarms on these events, you can cancel the deletion process if needed. Until the waiting period expires, you can recover the key from the **Pending Deletion** state and restore it to either a **Disabled** or **Enabled** state.

Deletion of a multi-Region key requires that you delete replicas before the original copy. For more information, see [Deleting multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html).

If you are using a key with imported key material, you can delete the imported key material immediately. This is different from deleting a KMS key in several ways. When you perform the `DeleteImportedKeyMaterial` action, AWS KMS deletes the key material, and the key state changes to **Pending import**. After you delete the key material, the key is immediately unusable. There is no waiting period. To enable use of the key again, you need to import the same key material again. The waiting period for KMS key deletion also applies to KMS keys with imported key material.

If a KMS key protects data keys that AWS services actively use, disabling the KMS key or deleting its imported key material doesn't immediately affect those data keys. For example, say that you use a key with imported material to encrypt an object with [SSE-KMS](https://docs.aws.amazon.com/kms/latest/developerguide/services-s3.html). You upload the object to an Amazon Simple Storage Service (Amazon S3) bucket. Before you upload the object to the bucket, you import the material into your key. After you upload the object, you delete the imported key material from that key. The object remains in the bucket in an encrypted state, but no one can access the object until you re-import the deleted key material into the key. Though this flow requires precise automation for importing and deleting key material from a key, it can provide an additional level of control within an environment.

AWS offers prescriptive guidance to help you monitor and remediate (if necessary) the scheduled deletion of KMS keys. For more information, see [Monitor and remediate scheduled deletion of AWS KMS keys](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-and-remediate-scheduled-deletion-of-aws-kms-keys.html).
