---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/key-management.html
---

# Key management best practices for AWS KMS
<a name="key-management"></a>

When using AWS Key Management Service (AWS KMS), there are some fundamental design decisions that you must make. These include whether to use a centralized or decentralized model for key management and access, the type of keys to use, and the type of key store to use. The following sections help you make decisions that are right for your organization and use cases. This section concludes with important considerations for disabling and deleting KMS keys, including actions that you should take to help protect your data and keys.

**This section contains the following topics:**
+ [Choosing a centralized or decentralized model](#key-management-model)
+ [Choosing customer managed keys, AWS managed keys, or AWS owned keys](#key-management-types)
+ [Choosing an AWS KMS key store](#key-management-stores)
+ [Deleting and disabling KMS keys](#key-management-deletion)

## Choosing a centralized or decentralized model
<a name="key-management-model"></a>

AWS recommends that you use multiple AWS accounts and manage those accounts as a single organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). There are two broad approaches to managing AWS KMS keys in multi-account environments.

The first approach is a decentralized approach, where you create keys in each account that uses those keys. When you store the KMS keys in the same accounts as the resources they protect, it is easier to delegate permissions to local administrators who understand access requirements for their AWS principals and keys. You can authorize key usage by using just a [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), or you can combine a key policy and [identity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) in AWS Identity and Access Management (IAM).

The second approach is a centralized approach, where you maintain KMS keys in one or a few designated AWS accounts. You allow other accounts to only use the keys for cryptographic operations. You manage keys, their life cycle, and their permissions from the centralized account. You permit other AWS accounts to use the key but don't allow other permissions. The external accounts cannot manage anything about the key's life cycle or access permission. This centralized model can help minimize the risk of unintended deletion of keys or privilege escalation by delegated administrators or users.

The option you choose depends on several factors. Consider the following when choosing an approach:

1. Do you have an automated or manual process for provisioning key and resource access? This includes resources such as deployment pipelines and infrastructure as code (IaC) templates. These tools can help you deploy and manage resources (such as KMS keys, key policies, IAM roles, and IAM policies) across many AWS accounts. If you don't have these deployment tools, a centralized approach to key management might be more manageable for your business.

1. Do you have administrative control over all of the AWS accounts that contain resources that use KMS keys? If so, a centralized model can simplify management and eliminate the need to switch AWS accounts to manage keys. Note, however, that IAM roles and user permissions to use keys still must be managed per account.

1. Do you need to offer access to use your KMS keys to customers or partners who have their own AWS accounts and resources? For these keys, a centralized approach can reduce administrative burden on your customers and partners.

1. Do you have authorization requirements for access to AWS resources that are better solved by either a centralized or local access approach? For example, if different applications or business units are responsible for managing the security of their own data, a decentralized approach to key management is better.

1. Are you exceeding service [resource quotas](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html) for AWS KMS? Because these quotas are set per AWS account, a decentralized model distributes the load across accounts, effectively multiplying service quotas.
**Note**
The management model for keys is irrelevant when considering [request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) because these quotas are applied to the account principal making a request against the key, not the account that owns or manages the key.

In general, we recommend that you start with a decentralized approach unless you can articulate a need for a centralized KMS key model.

## Choosing customer managed keys, AWS managed keys, or AWS owned keys
<a name="key-management-types"></a>

The KMS keys that you create and manage for use in your own cryptographic applications are known as *customer managed keys*. AWS services can use customer managed keys to encrypt the data the service stores on your behalf. Customer managed keys are recommended if you want full control over the life cycle and usage of your keys. There is a monthly cost to have a customer managed key in your account. In addition, requests to use or manage the key incur a usage cost. For more information, see [AWS KMS pricing](https://aws.amazon.com/kms/pricing/).

If you want an AWS service to encrypt your data but don't want the overhead or costs of managing keys, you can use an *AWS managed key*. This type of key exists in your account, but it can only be used under certain circumstances. It can only be used in the context of the AWS service that you're operating in, and it can only be used by principals within the account that contains the key. You cannot manage anything about the life cycle or permissions of these keys. Some AWS services use AWS managed keys. The format of an AWS managed key alias is `aws/<service code>`. For example, an `aws/ebs` key can only be used to encrypt Amazon Elastic Block Store (Amazon EBS) volumes in the same account as the key and can only be used by IAM principals in that account. An AWS managed key can be used only by users in that account and for resources in that account. You cannot share resources encrypted under an AWS managed key with other accounts. If this is a limitation for your use case, we recommend using a customer managed key instead; you can share use of that key with any other account. You are not charged for the existence of an AWS managed key in your account, but you are charged for any use of this key type by the AWS service that is assigned to the key.

An AWS managed key is a legacy key type that is no longer being created for new AWS services as of 2021. Instead, new (and legacy) AWS services are using an *AWS owned key* to encrypt your data by default. AWS owned keys are a collection of KMS keys that an AWS service owns and manages for use in multiple AWS accounts. Although these keys are not in your AWS account, an AWS service can use one to protect the resources in your account.

We recommend that you use customer managed keys when granular control is most important and use AWS owned keys when convenience is most important.

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

A *key store* is a secure location for storing and using cryptographic key material. The industry best practice for key stores is to use a device known as a hardware security module (HSM) that has been validated under the [NIST Federal Information Processing Standards (FIPS) 140 Cryptographic Module Validation Program](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/modules-in-process/IUT-List) at Security Level 3. There are other programs to support key stores that are used to process payments. [AWS Payment Cryptography](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/what-is.html) is a service you can use to protect data related to your payment workloads.

AWS KMS supports multiple key store types to help protect your key material when using AWS KMS to create and manage your encryption keys. All of the key store options supplied by AWS KMS are continually validated under FIPS 140 at Security Level 3. They are designed to prevent anyone, including AWS operators, from accessing your plaintext keys or using them without your permission. For more information about the available types of key stores, see [Key stores](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html) in the AWS KMS documentation.

The [AWS KMS standard key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html#default-key-store) is the best choice for the majority of workloads. If you need to choose a different type of key store, carefully consider whether regulatory or other requirements (such as internal) mandate making this choice, and carefully weigh the costs and benefits.

## Deleting and disabling KMS keys
<a name="key-management-deletion"></a>

The deletion of a KMS key can have significant impact. Before you delete a KMS key that you no longer intend to use, consider whether it's adequate to set the key state to **Disabled**. While a key is disabled, it cannot be used for cryptographic operations. It still exists in AWS, and you can re-enable it in the future if required. Disabled keys continue to incur storage charges. We recommend that you disable keys instead of deleting them until you are confident that the key does not protect any data or data keys.

**Important**
Deleting a key must be carefully planned. Data cannot be decrypted if the corresponding key has been deleted. AWS has no means to recover a deleted key after it's been deleted. As with other critical operations in AWS, you should apply a policy that limits who can schedule keys for deletion and require multi-factor authentication (MFA) for key deletion.

To help prevent accidental key deletion, AWS KMS enforces a default minimum waiting period of seven days after the execution of a `DeleteKey` call before it deletes the key. You can [set the waiting period](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html) to a maximum value of 30 days. During the waiting period, the key is still stored in AWS KMS in a **Pending Deletion** state. It can't be used for encrypt or decrypt operations. Any attempt to use a key that is in the **Pending Deletion** state for encryption or decryption is logged to AWS CloudTrail. You can [set an Amazon CloudWatch alarm](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html) for these events in your CloudTrail logs. If you receive alarms on these events, you can choose to cancel the deletion process if needed. Until the waiting period has expired, you can recover the key from the **Pending Deletion **state and restore it to either a **Disabled** or **Enabled** state.

Deletion of a multi-Region key requires that you delete replicas before the original copy. For more information, see [Deleting multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html).

If you are using a key with imported key material, you can delete the imported key material immediately. This is different from deleting a KMS key in several ways. When you perform the `DeleteImportedKeyMaterial` action, AWS KMS deletes the key material, and the key state changes to **Pending import**. After you delete the key material, the key is immediately unusable. There is no waiting period. To enable use of the key again, you need to import the same key material again. The waiting period for KMS key deletion also applies to KMS keys with imported key material.

If data keys are protected by a KMS key and are actively in use by AWS services, they are not immediately affected if their associated KMS key is disabled or if its imported key material is deleted. For example, say that a key with imported material was used to encrypt an object with [SSE-KMS](https://docs.aws.amazon.com/kms/latest/developerguide/services-s3.html). You are uploading the object to an Amazon Simple Storage Service (Amazon S3) bucket. Before you upload the object to the bucket, you import the material into your key. After the object is uploaded, you delete the imported key material from that key. The object remains in the bucket in an encrypted state, but no one can access the object until the deleted key material is re-imported into the key. Though this flow requires precise automation for importing and deleting key material from a key, it can provide an additional level of control within an environment.

AWS offers prescriptive guidance to help you monitor and remediate (if necessary) the scheduled deletion of KMS keys. For more information, see [Monitor and remediate scheduled deletion of AWS KMS keys](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-and-remediate-scheduled-deletion-of-aws-kms-keys.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
