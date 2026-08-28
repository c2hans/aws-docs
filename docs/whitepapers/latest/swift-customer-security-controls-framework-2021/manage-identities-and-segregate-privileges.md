---
source_url: https://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/manage-identities-and-segregate-privileges.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Requirement 5 - Manage identities and segregate privileges
<a name="manage-identities-and-segregate-privileges"></a>

## Logical access control
<a name="logical-access-control"></a>

 Here are two sample roles for managing the SWIFT infrastructure and components:
+  The SWIFT instance operator role gives privilege to individuals who require EC2 access to install and troubleshoot SWIFT software like AMH, SAG and SNL.
+  The SWIFT infrastructure role enables you to control the states of the infrastructure components like EC2, Amazon MQ, and Amazon RDS for Oracle, and the ability to view the CloudWatch Logs.

 When you create IAM policies, follow the standard security advice of granting *least privilege*, or granting only the permissions required to perform a task. Determine what users (and roles) need to do, and then craft policies that allow them to perform *only* those tasks.

 Start with a minimum set of permissions, and grant additional permissions as necessary. This is more secure than starting with permissions that are too lenient and trying to tighten them later.

 IAM provides several options to help you refine the permissions that you grant.
+  **Understand access level groupings** – You can use access level groupings to understand the level of access that a policy grants. [Policy actions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_action.html) are classified as List, Read, Write, Permissions management, or Tagging. For example, you can choose actions from the List and Read access levels to grant read-only access to your users. To learn how to use policy summaries to understand access level permissions, refer to [Use access levels to review IAM permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#use-access-levels-to-review-permissions).
+  **Validate your policies** – You can perform policy validation using [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) when you create and edit JSON policies. We recommend that you review and validate all of your existing policies. IAM Access Analyzer provides over 100 policy checks to validate your policies. It generates security warnings when a statement in your policy allows access it considers to be overly permissive. You can use the actionable recommendations that are provided through the security warnings as you work toward granting least privilege. To learn more about policy checks provided by IAM Access Analyzer, refer to [IAM Access Analyzer policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html).
+  **Generate a policy based on access activity** – To help you refine the permissions that you grant, you can generate an IAM policy that is based on the access activity for an IAM entity (user or role). IAM Access Analyzer reviews your AWS CloudTrail logs and generates a policy template that contains the permissions that have been used by the entity in your specified time frame. You can use the template to create a managed policy with fine-grained permissions, then attach it to the IAM entity. That way, you grant only the permissions that the user or role needs to interact with AWS resources for your specific use case. To learn more, refer to [Generate policies based on access activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_generate-policy.html).
+  **Use last accessed information** – Another feature that can help with least privilege is *last-accessed information*. View this information on the **Access Advisor** tab on the IAM console **Details** page for a user, group, role, or policy. Last-accessed information also includes information about the actions that were last accessed for some services, such as Amazon EC2, IAM, Lambda, and [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3). If you sign in using AWS Organizations management account credentials, you can view service last- accessed information in the **AWS Organizations** section of the IAM console.

   You can also use the AWS CLI or AWS API to retrieve a report for last-accessed information for entities or policies in IAM or Organizations. You can use this information to identify unnecessary permissions so that you can refine your IAM or Organizations policies to better adhere to the principle of least privilege. For more information, refer to [Refining permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html).
+  **Review account events in AWS CloudTrail** – To further reduce permissions, you can view your account's events in AWS CloudTrail **Event history**. CloudTrail event logs include detailed event information that you can use to reduce the policy's permissions. The logs include only the actions and resources that your IAM entities need. For more information, refer to [Viewing CloudTrail Events in the CloudTrail Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events-console.html) in the *AWS CloudTrail User Guide*.

## Token management
<a name="token-management"></a>

 The customer is responsible for having a controlled process for distributing, assigning, and revoking physical tokens.

## Physical and logical password storage
<a name="physical-and-logical-password-storage"></a>

 [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) is the recommended service to safely store the passwords that are utilized in the SWIFT secure zone, such as user IDs and passwords for connecting Amazon RDS Oracle and Amazon MQ, and the password for connecting SWIFT AMH to the SAG cluster. AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. All secrets stored in AWS Secrets Manager should be encrypted with AWS KMS, and have well-defined resource policies for the secrets.

 Secrets Manager integrates with AWS KMS to encrypt every version of every secret with a unique [data key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys) that is protected by an AWS KMS key. This integration protects your secrets under encryption keys that never leave AWS KMS unencrypted. It also enables you to set custom permissions on the AWS KMS key and audit the operations that generate, encrypt, and decrypt the data keys that protect your secrets.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
