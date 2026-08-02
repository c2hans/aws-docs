---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-kms-best-practices/access.html
---

# Identity and access management best practices for AWS KMS
<a name="access"></a>

To use AWS Key Management Service (AWS KMS), you must have credentials that AWS can use to authenticate and authorize your requests. No AWS principal has any permissions to a KMS key unless that permission is provided explicitly and never denied. There are no implicit or automatic permissions to use or manage a KMS key. The topics in this section define security best practices to help you determine which AWS KMS access management controls you should use to secure your infrastructure.

**This section discusses the following identity and access management topics:**
+ [AWS KMS key policies and IAM policies](#access-policies)
+ [Least-privilege permissions for AWS KMS](#access-least-privilege)
+ [Role-based access control for AWS KMS](#access-rbac)
+ [Attribute-based access control for AWS KMS](#access-abac)
+ [Encryption context for AWS KMS](#access-encryption-context)
+ [Troubleshooting AWS KMS permissions](#access-troubleshooting)

## AWS KMS key policies and IAM policies
<a name="access-policies"></a>

The primary way to manage access to your AWS KMS resources is with *policies*. Policies are documents that describe which principals can access which resources. Policies that are attached to an AWS Identity and Access Management (IAM) identity (users, groups of users, or roles) are called [identity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_id-based). IAM policies that attach to resources are called [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based). AWS KMS resource policies for KMS keys are called [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html). In addition to IAM policies and AWS KMS key policies, AWS KMS supports [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html). Grants provide a flexible and powerful way to delegate permissions. You can use grants to issue time-bound KMS key access to IAM principals in your AWS account or in other AWS accounts.

All KMS keys have a key policy. If you don't provide one, AWS KMS creates one for you. The [default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html) that AWS KMS uses differs depending on whether you create the key using the AWS KMS console or you use the AWS KMS API. We recommend that you edit the default key policy to align with your organization's requirements for [least-privilege permissions](#access-least-privilege). This should also align with your strategy for using IAM policies in conjunction with key policies. For more recommendations on using IAM policies with AWS KMS, see [Best practices for IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies-best-practices.html) in the AWS KMS documentation.

You can use the key policy to delegate authorization for an IAM principal to the  identity-based policy. You can also use the key policy to refine authorization in conjunction with the identity-based policy. In either case, both the key policy and identity-based policy determine access, along with any other applicable policies that scope access, such as [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html), [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html), or [permission boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html). If the principal is in a different account than the KMS key, essentially, only cryptographic and grant actions are supported. For more information about this cross-account scenario, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the AWS KMS documentation.

You must use IAM identity-based policies in combination with key policies to control access to your KMS keys. Grants can also be used in combination with these policies to control access to a KMS key. To use an identity-based policy to control access to a KMS key, the key policy must allow the account to use identity-based policies. You can either specify a [key policy statement that enables IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#key-policy-default-allow-root-enable-iam), or you can explicitly [specify allowed principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying) in the key policy.

When writing policies, make sure that you have strong controls that restrict who can perform the following actions:
+ **Update, create, and delete IAM policies and KMS key policies**
+ **Attach and detach identity-based policies from users, roles, and groups**
+ **Attach and detach AWS KMS key polices from KMS keys**
+ **Create grants for your KMS keys** – Whether you control access to your KMS keys exclusively with key policies, or you combine key policies with IAM policies, you should restrict the ability to modify the policies. Implement an approval process for changing any existing policies. An approval process can help prevent the following:
  + **Accidental loss of IAM principal permissions** – It's possible to make changes that would prevent IAM principals from being able to manage the key or use it in cryptographic operations. In extreme scenarios, it's possible to revoke key management permissions from all users. If this happens, you need to contact [AWS Support](https://aws.amazon.com/contact-us/) to regain access to the key.
  + **Unapproved changes to KMS key policies** – If an unauthorized user gains access to the key policy, they could modify it to delegate permissions to an unintended AWS account or principal.
  + **Unapproved changes to IAM policies** – If an unauthorized user obtains a set of credentials with permissions to manage a group's membership, they could elevate their own permissions and make changes to your IAM policies, key policies, KMS key configuration, or other AWS resource configurations.

Carefully review the IAM roles and users that are associated with the IAM principals who are designated as your KMS key administrators. This can help prevent unauthorized deletion or changes. If you need to change the principals who have access to your KMS keys, verify that the new administrator principals are added to all required key policies. Test their permissions before you delete the previous managing principal. We strongly recommend following all [IAM security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) and using temporary credentials instead of the long-term credentials.

We recommend issuing time-bound access through grants if you don't know the names of the principals at the time that the policies are created or if the principals that require access frequently change. The [grantee principal](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grantee-principal) can be in the same account as the KMS key or in a different account. If the principal and KMS key are in different accounts, then you must specify an identity-based policy in addition to the grant. Grants require additional management because you must call an API to create the grant and to retire or revoke the grant when it is no longer needed.

No AWS principal, including the account root user or key creator, has any permissions to a KMS key unless they are explicitly allowed and not explicitly denied in a key policy, IAM policy, or grant. By extension, you should consider what would happen if a user gains unintended access to use a KMS key and what the impact would be. To mitigate such a risk, consider the following:
+ You can maintain different KMS keys for different categories of data. This helps you separate keys and maintain more concise key policies that contain policy statements that specifically target principal access to that data category. It also means that if relevant IAM credentials are accessed unintentionally, the identity tied to that access has access only to the keys specified in the IAM policy and only if the key policy allows access to that principal.
+ You can assess if a user with unintended access to the key can access the data. For example, with Amazon Simple Storage Service (Amazon S3), the user must also have the appropriate permissions to access encrypted objects in Amazon S3. Alternately, if a user has unintended access (by using RDP or SSH) to an Amazon EC2 instance that has a volume encrypted with a KMS key, the user could access the data by using operating system tools.

**Note**
AWS services that use AWS KMS don't expose the ciphertext to users (most current approaches to cryptoanalysis require access to the ciphertext). Additionally, ciphertext is not available for physical examination outside of an AWS data center because all storage media is physically destroyed when it is decommissioned, in accordance with NIST SP800-88 requirements.

## Least-privilege permissions for AWS KMS
<a name="access-least-privilege"></a>

Because your KMS keys protect sensitive information, we recommend following the principle of least privileged access. Delegate the minimum permissions required to perform a task when you define your key policies. Allow all actions (`kms:*`) on a KMS key policy only if you plan to further restrict permissions with additional identity-based policies. If you plan to manage permissions with identity-based policies, limit who has the ability to create and attach IAM policies to IAM principals and [monitor for policy changes](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudwatch-alarms-for-cloudtrail.html#cloudwatch-alarms-for-cloudtrail-iam-policy-changes).

If you allow all actions (`kms:*`) in both the key policy and the identity-based policy, the principal has both administrative and usage permissions to the KMS key. As a security best practice, we recommend delegating these permissions only to specific principals. Consider how you assign permissions to principals who will manage your keys and principals who will use your keys. You can do this by explicitly naming the principal in the key policy or by limiting which principals the identity-based policy is attached to. You can also use [condition keys](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html) to restrict permissions. For example, you can use the [aws:PrincipalTag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltag) to allow all actions if the principal making the API call has the tag specified in the condition rule.

For help understanding how policy statements are evaluated in AWS, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the IAM documentation. We recommend reviewing this topic before writing policies to help reduce the chance that your policy has unintended effects, such as providing access to principals that should not have access.

**Tip**
When testing an application in a non-production environment, use [AWS Identity and Access Management Access Analyzer (IAM Access Analyzer)](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to help you apply least-privilege permissions in your IAM policies.

If you use IAM users instead of IAM roles, we strongly recommend using [AWS multi-factor authentication (MFA)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) to mitigate the vulnerability of long-term credentials. You can use MFA to do the following:
+ Require that users validate their credentials with MFA before performing privileged actions, such as scheduling key deletion.
+ Split ownership of an administrator account password and MFA device between individuals to implement split authorization.

For sample policies that can help you configure least-privilege permissions, see [IAM policy examples](https://docs.aws.amazon.com/kms/latest/developerguide/customer-managed-policies.html) in the AWS KMS documentation.

## Role-based access control for AWS KMS
<a name="access-rbac"></a>

Role-based access control (RBAC) is an authorization strategy that provides users with only the permissions required to perform their job duties, and nothing more. It is an approach that can help you implement the principle of least privilege.

AWS KMS supports RBAC. It allows you to control access to your keys by specifying granular permissions within [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html). Key policies specify a resource, action, effect, principal, and optional conditions to grant access to keys. To implement RBAC in AWS KMS, we recommend separating the permissions for key users and key administrators.

For key users, assign only the permissions that the user needs. Use the following questions to help you further refine permissions:
+ Which IAM principals need access to the key?
+ Which actions does each principal need to perform with the key? For example, does the principal need only `Encrypt` and `Sign` permissions?
+ Which resources does the principal need to access?
+ Is the entity a human or an AWS service? If it's a service, you can use the [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-via-service) condition key to restrict key usage to a specific service.

For key administrators, assign only the permissions that the administrator needs. For example, an administrator's permissions might vary depending on whether the key is used in test or production environments. If you use less restrictive permissions in certain non-production environments, implement a process to test the policies before they are released to production.

For sample policies that can help you configure role-based access control for key users and administrators, see [RBAC for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/rbac.html).

## Attribute-based access control for AWS KMS
<a name="access-abac"></a>

[Attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) is an authorization strategy that defines permissions based on attributes. Like RBAC, it is an approach that can help you implement the principle of least privilege.

AWS KMS supports ABAC by allowing you to define permissions based on tags associated with the target resource, such as a KMS key, and tags associated with the principal making the API call. In AWS KMS, you can use tags and aliases to control access to your customer managed keys. For example, you can define IAM policies that use tag condition keys to allow operations when the principal's tag matches the tag associated with the KMS key. For a tutorial, see [Define permissions to access AWS resources based on tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html) in the AWS KMS documentation.

As a best practice, use ABAC strategies to simplify IAM policy management. With ABAC, administrators can use tags to allow access to new resources instead of updating existing policies. ABAC requires fewer policies because you don't have to create different policies for different job functions. For more information, see [Comparison of ABAC to the traditional RBAC model](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html#introduction_attribute-based-access-control_compare-rbac) in the IAM documentation.

Apply the best practice of least-privilege permissions to the ABAC model. Provide IAM principals with only the permissions they need to perform their jobs. Carefully control access to tagging APIs that would allow users to modify tags on roles and resources. If you use key alias condition keys to support ABAC in AWS KMS, make sure that you also have strong controls that restrict who can create keys and modify aliases.

You can also use tags to link a specific key to a business category and verify that the correct key is being used for a given action. For example, you can use AWS CloudTrail logs to verify that the key used to perform a specific AWS KMS action belongs to the same business category as the resource that it's being used on.

**Warning**
Do not include confidential or sensitive information in the tag key or tag value. Tags are not encrypted. They are accessible to many AWS services, including billing.

Before implementing an ABAC approach to your access control, consider whether the other services that you use support this approach. For help determining which services support ABAC, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the IAM documentation.

For more information about implementing ABAC for AWS KMS and the conditions keys that can help you configure policies, see [ABAC for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html).

## Encryption context for AWS KMS
<a name="access-encryption-context"></a>

All AWS KMS cryptographic operations with symmetric encryption KMS keys accept an [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html). *Encryption context* is an optional set of non-secret key–value pairs that can contain additional contextual information about the data. As a best practice, you can insert encryption context in `Encrypt` operations in AWS KMS to enhance the authorization and auditability of your decryption API calls to AWS KMS. AWS KMS uses the encryption context as additional authenticated data (AAD) to support [authenticated encryption](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#symmetric-key-0ps). The encryption context is cryptographically bound to the ciphertext so that the same encryption context is required to decrypt the data.

The encryption context is not secret and not encrypted. It appears in plaintext in AWS CloudTrail logs so that you can use it to identify and categorize your cryptographic operations. Because the encryption context is not secret, you should allow only authorized principals to access your CloudTrail log data.

You can also use the [kms:EncryptionContext:context-key](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-context) and [kms:EncryptionContextKeys ](https://docs.aws.amazon.com/kms/latest/developerguide/conditions-kms.html#conditions-kms-encryption-context-keys)condition keys to control access to a symmetric encryption KMS key based on the encryption context. You can also use these condition keys to require that encryption contexts are used in cryptographic operations. For these condition keys, review the guidance about the use of `ForAnyValue` or `ForAllValues` set operators in order to make sure that your policies reflect your intended permissions.

## Troubleshooting AWS KMS permissions
<a name="access-troubleshooting"></a>

When you write access control policies for a KMS key, consider how the IAM policy and key policy work together. The effective permissions for a principal are the permissions that are granted (and not explicitly denied) by all of the effective policies. Within an account, the permissions to a KMS key can be affected by IAM identity-based policies, key policies, permissions boundaries, service control policies, or session policies. For example, if you use both identity-based and key policies to control access to the KMS key, all policies relating to both the principal and the resource are evaluated to determine a principal's authorization to perform a given action. For more information, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the IAM documentation.

For detailed information and a flowchart for troubleshooting key access, see [Troubleshooting key access ](https://docs.aws.amazon.com/kms/latest/developerguide/policy-evaluation.html)in the AWS KMS documentation.

**To troubleshoot an access denied error message**

1. Confirm that the IAM identity-based policies and KMS key policies allow access.

1. Confirm that a [permissions boundary](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in IAM is not restricting access.

1. Confirm that a [service control policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) or [resource control policy (RCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) in AWS Organizations is not restricting access.

1. If you are using VPC endpoints, confirm that the [endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) are correct.

1. In the identity-based policies and key policies, remove any conditions or resource references that restrict access to the key. After removing these restrictions, confirm that the principal can successfully call the API that previously failed. If successful, reapply the conditions and resource references one at a time and, after each, verify that the principal still has access. This helps you identify the condition or resource reference that is causing the error.

For more information, see [Troubleshooting access denied error messages](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html) in the IAM documentation.
