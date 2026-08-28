---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/kms.html
---

# AWS Key Management Service
<a name="kms"></a>

[AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data. AWS KMS integrates with most other AWS services that can encrypt your data. For a complete list, see [AWS services integrated with AWS KMS](https://aws.amazon.com/kms/features/#AWS_Service_Integration). AWS KMS also integrates with AWS CloudTrail to log use of your KMS keys for auditing, regulatory, and compliance needs.

KMS keys are the primary resource in AWS KMS, and they are logical representations of a cryptographic key. There are three primary types of KMS keys:
+ Customer managed keys are KMS keys that you create.
+ AWS managed keys are KMS keys that AWS services create in your account, on your behalf.
+ AWS owned keys are KMS keys that an AWS service owns and manages, for use in multiple AWS accounts.

For more information about these key types, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys).

In the AWS Cloud, policies are used to control who can access resources and services. For example, in AWS Identity and Access Management (IAM), *identity-based policies* define permissions for users, user groups, or roles, and *resource-based policies* attach to a resource, such as an S3 bucket, and define which principals are allowed access, supported actions, and any other conditions that must be met. Similar to IAM policies, AWS KMS uses [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) to control access to a KMS key. Each KMS key must have a key policy, and each key can have only one key policy. Note the following when defining policies that allow or deny access to KMS keys:
+ You can control the key policy for customer managed keys, but you can't directly control the key policy for AWS managed keys or for AWS owned keys.
+ Key policies allow for granting granular access to AWS KMS API calls within an AWS account. Unless the key policy explicitly allows it, you cannot use IAM policies to allow access to a KMS key. Without permission from the key policy, IAM policies that allow permissions have no effect. For more information, see [Allow IAM policies to allow access to the KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#key-policy-default-allow-root-enable-iam).
+ You can use an IAM policy to deny access to a customer managed key without corresponding permission from the key policy.
+ When designing key policies and IAM policies for multi-Region keys, consider the following:
  + Key policies are not [shared properties](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-sync-properties) of multi-Region keys and are not copied or synchronized among related multi-Region keys.
  + When a multi-Region key is created using the `CreateKey` and `ReplicateKey` actions, the [default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html) is applied unless a key policy is specified in the request.
  + You can implement condition keys, such as [aws:RequestedRegion](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requestedregion), to limit permissions to a particular AWS Region.
  + You can use grants to allow permissions to a multi-Region primary key or replica key. However, a single grant cannot be used to allow permissions to multiple KMS keys, even if they are related multi-Region keys.

When using AWS KMS and creating key policies, consider the following encryption best practices and other security best practices:
+ Adhere to the recommendations in the following resources for AWS KMS best practices:
  + [Best practices for AWS KMS grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant-best-practices) (AWS KMS documentation)
  + [Best practices for IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies-best-practices.html) (AWS KMS documentation)
+ In accordance with the separation of duties best practice, maintain separate identities for those who administer keys and those who use them:
  + Administrator roles that create and delete keys should not have the ability to use the key.
  + Some services may only need to encrypt data and should not be granted the ability to decrypt the data using the key.
+ Key policies should always follow a model of least privilege. Do not use `kms:*` for actions in IAM or key policies because this gives the principal permissions to both administer and use the key.
+ Limit the use of customer managed keys to specific AWS services by using the [kms:ViaService](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-via-service) condition key within the key policy.
+ If you have a choice between key types, customer managed keys are preferred because they provide the most granular control options, including the following:
  + [Managing authentication and access control](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html)
  + [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html)
  + [Rotating AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
  + [Tagging keys](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html)
  + [Creating aliases](https://docs.aws.amazon.com/kms/latest/developerguide/programming-aliases.html)
  + [Deleting AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html)
+ AWS KMS administrative and modification permissions must be explicitly denied to unapproved principals and AWS KMS modification permissions should not exist in an allow statement for any unauthorized principals. For more information, see [Actions, resources, and condition keys for AWS Key Management Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awskeymanagementservice.html).
+ In order to detect unauthorized usage of KMS keys, in AWS Config, implement the [iam-customer-policy-blocked-kms-actions](https://docs.aws.amazon.com/config/latest/developerguide/iam-customer-policy-blocked-kms-actions.html) and [iam-inline-policy-blocked-kms-actions](https://docs.aws.amazon.com/config/latest/developerguide/iam-inline-policy-blocked-kms-actions.html) rules. This prevents principals from using the AWS KMS decryption actions on all resources.
+ Implement service control policies (SCPs) in AWS Organizations to prevent unauthorized users or roles from deleting KMS keys, either directly as a command or through the console. For more information, see [Using SCPs as preventative controls](https://aws.amazon.com/blogs/mt/identity-guide-preventive-controls-with-aws-identity-scps/) (AWS blog post).
+ Log AWS KMS API calls in a CloudTrail log. This records the relevant event attributes, such as what requests were made, the source IP address from which the request was made, and who made the request. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html).
+ If you use [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context), it shouldn't contain any sensitive information. CloudTrail stores the encryption context in plaintext JSON files, which can be viewed by anyone with access to the S3 bucket containing the information.
+ When monitoring usage of customer managed keys, configure events to notify you if specific actions are detected, such as key creation, updates to customer managed key policies, or import of key material are detected. It's also recommended that you implement automated responses, such as an AWS Lambda function that disables the key or performs any other incident response actions as dictated by your organizational policies.
+ [Multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-auth.html) are recommended for specific scenarios, such as compliance, disaster recovery, or backups. The security properties of multi-Region keys are significantly different than single-Region keys. The following recommendations apply when authorizing the creation, management, and use of multi-Region keys:
  + Allow principals to replicate a multi-Region key only into AWS Regions that require them.
  + Give permission for multi-Region keys only to principals who need them and only for tasks that require them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
