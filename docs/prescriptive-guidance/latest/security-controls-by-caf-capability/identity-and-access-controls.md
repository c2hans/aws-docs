---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/identity-and-access-controls.html
---

# Security control recommendations for managing identity and access
<a name="identity-and-access-controls"></a>

You can create identities in AWS, or you can connect an external identity source. Through AWS Identity and Access Management (IAM) policies, you grant users the necessary permissions so that they can access or manage AWS resources and integrated applications. Effective identity and access management helps validate that the right people and machines have access to the right resources under the right conditions. The AWS Well-Architected Framework provides [best practices for managing identities and their permissions](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/identity-and-access-management.html). Examples of best practices include relying on a centralized identity provider and using strong sign-in mechanisms, such as multi-factor authentication (MFA). The security controls in this section can help you implement these best practices.

Controls in this section:
+ [Monitor and configure notifications for root user activity](#root-user-activity)
+ [Don't create access keys for the root user](#root-user-access-keys)
+ [Enable MFA for the root user](#root-user-mfa)
+ [Follow the security best practices for IAM](#iam-best-practices)
+ [Grant least-privilege permissions](#least-privilege)
+ [Define permission guardrails at the workload level](#workload-guardrails)
+ [Rotate IAM access keys at a regular interval](#rotate-keys)
+ [Identify resources that are shared with an external entity](#resources-shared-externally)

## Monitor and configure notifications for root user activity
<a name="root-user-activity"></a>

When you first create an AWS account, you begin with a single sign-in identity called the *root user*. By default, the root user has full access to all AWS services and resources in the account. You should tightly control and monitor the root user, and you should use it only for [tasks that require root user credentials](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html).

For more information, see the following resources:
+ [Grant least-privilege access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_least_privileges.html) in the AWS Well-Architected Framework
+ [Monitor IAM root user activity](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-iam-root-user-activity.html) in AWS Prescriptive Guidance

## Don't create access keys for the root user
<a name="root-user-access-keys"></a>

The root user is the most privileged user in an AWS account. Disabling programmatic access to the root user helps reduce the risk of inadvertent exposure of the user credentials and subsequent compromise of the cloud environment. We recommend that you create and use IAM roles as temporary credentials for accessing your AWS accounts and resources.

For more information, see the following resources:
+ [IAM root user access key should not exist](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-4) in the AWS Security Hub CSPM documentation
+ [Deleting access keys for the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_delete-key.html) in the IAM documentation
+ [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the IAM documentation

## Enable MFA for the root user
<a name="root-user-mfa"></a>

We recommend that you enable multiple multi-factor authentication (MFA) devices for the AWS account root user and IAM users. This raises the security bar in AWS accounts and can simplify access management. Because a root user is a highly privileged user that can perform privileged actions, it's crucial to require MFA for the root user. You can use a hardware MFA device that generates a numeric code based on the time-based one-time password (TOTP) algorithm, a FIDO hardware security key, or a virtual authenticator application.

In 2024, MFA will be required to access the root user of any AWS account. For more information, see [Secure by Design: AWS to enhance MFA requirements](https://aws.amazon.com/blogs/security/security-by-design-aws-to-enhance-mfa-requirements-in-2024/) in 2024 in the AWS Security Blog. We strongly encourage you to extend this security practice and require MFA for all user types in your AWS environments.

If possible, we recommended that you use a hardware MFA device for the root user. Virtual MFA might not provide the same level of security as hardware MFA devices. You can use virtual MFA while waiting for hardware purchase approval or delivery.

In situations where you manage hundreds of accounts in AWS Organizations, depending on your organization's risk tolerance, it might not be scalable to use hardware-based MFA for the root user of each account in an organizational unit (OU). In this case, you can choose one account in the OU that acts as an OU management account, and then disable the root user for the other accounts in that OU. By default, the OU management account doesn't have access to the other accounts. By setting up cross-account access in advance, you can access the other accounts from the OU management account in an emergency. To set up cross-account access, you create an IAM role in the member account, and you define policies so that only the root user in the OU management account can assume this role. For more information, see [Tutorial: Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) in the IAM documentation.

We recommend that you enable multiple MFA devices for your root user credentials. You can register up to eight MFA devices of any combination.

For more information, see the following resources:
+ [Enabling a hardware TOTP token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_physical.html#enable-hw-mfa-for-root) in the IAM documentation
+ [Enabling a virtual multi-factor authentication (MFA) device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html) in the IAM documentation
+ [Enabling a FIDO security key](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_fido.html) in the IAM documentation
+ [Secure your root user sign-in with multi-factor authentication (MFA)](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-best-practices.html#ru-bp-mfa) in the IAM documentation

## Follow the security best practices for IAM
<a name="iam-best-practices"></a>

The IAM documentation includes a list of best practices that are designed to help you secure your AWS accounts and resources. It includes recommendations for configuring access and permissions according to the principle of least privilege. Examples of IAM security best practices include configuring identity federation, requiring MFA, and using temporary credentials.

For more information, see the following resources:
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation
+ [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM documentation

## Grant least-privilege permissions
<a name="least-privilege"></a>

*Least privilege* is the practice of grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions.

*Attribute-based access control (ABAC)* is an authorization strategy that defines permissions based on attributes, such as their tags. You can use group, identity, and resource attributes to dynamically define permissions at scale, rather than defining permissions for individual users. For example, you can use ABAC to allow a group of developers to access only resources that have a specific tag associated with their project.

For more information, see the following resources:
+ [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the IAM documentation
+ [What is ABAC for AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) in the IAM documentation

## Define permission guardrails at the workload level
<a name="workload-guardrails"></a>

It's best practice to use a multi-account strategy because it provides flexibility to define guardrails at the workload level. The AWS Security Reference Architecture offers prescriptive guidance about how to structure your accounts. These accounts are managed as an organization in [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/), and the accounts are grouped into *organizational units (OUs)*.

AWS services, such as [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), can help you centrally manage controls across an organization. We recommend that you define a clear purpose for each account or OU within the organization, and apply controls according to that purpose. AWS Control Tower implements preventive, detective, and proactive controls that help you govern the resources and monitor compliance. A *preventive control* is designed to prevent an event from occurring. A *detective control* is designed to detect, log, and alert after an event has occurred. A *proactive control* is designed to prevent the deployment of noncompliant resources by scanning resources before they are provisioned.

For more information, see the following resources:
+ [Separate workloads using accounts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_multi_accounts.html) in the AWS Well-Architected Framework
+ [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/) in AWS Prescriptive Guidance
+ [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) in the AWS Control Tower documentation
+ [Implementing security controls on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/) in AWS Prescriptive Guidance
+ [Use service control policies to set permission guardrails across accounts in your AWS Organization](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-to-set-permission-guardrails-across-accounts-in-your-aws-organization/?ref=wellarchitected) in the AWS Security Blog

## Rotate IAM access keys at a regular interval
<a name="rotate-keys"></a>

It's a best practice to update access keys for use cases that require long-term credentials. We recommend rotating access keys every 90 days or less. Rotating access keys reduces the risk that an access key that is associated with a compromised or terminated account is used. It also prevents access by using an old key that might have been lost, compromised, or stolen. Always update applications after rotating the access keys.

For more information, see the following resources:
+ [Update access keys when needed for use cases that require long-term credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials) in the IAM documentation
+ [Automatically rotate IAM user access keys at scale with AWS Organizations and AWS Secrets Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-rotate-iam-user-access-keys-at-scale-with-aws-organizations-and-aws-secrets-manager.html) in AWS Prescriptive Guidance
+ [Updating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the IAM documentation

## Identify resources that are shared with an external entity
<a name="resources-shared-externally"></a>

An *external entity* is a resource, application, service, or user that is outside of your AWS organization, such as another AWS accounts, a root user, an IAM user or role, a federated user, an AWS service, or an anonymous (or unauthenticated) user. It is a security best practice to use IAM Access Analyzer to identify the resources in your organization and accounts, such as Amazon Simple Storage Service (Amazon S3) buckets or IAM roles, that are shared with an external entity. This helps you identify unintended access to resources and data, which is a security risk.

For more information, see the following resources:
+ [Verify public and cross-account access to resources with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-preview-access) in the IAM documentation
+ [Analyze public and cross-account access](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_analyze_cross_account.html) in the AWS Well-Architected Framework
+ [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) in the IAM documentation
