---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/authentication.html
---

# Authentication and authorization
<a name="authentication"></a>

Central cloud administrators and end users can use AWS IAM Identity Center to manage access to multiple AWS accounts and business applications. When you set up a landing zone, AWS Control Tower gives you two options for authentication:
+ AWS managed account access with IAM Identity Center
+ Self-managed AWS account access with IAM Identity Center or another method

If you are setting up a new landing zone and would like IAM Identity Center to set up and manage access to your accounts based on AWS best practices, choose the first option. If you have an existing landing zone and use IAM Identity Center or a third-party identity provider, choose the second option. In this case, you have to install AWS Control Tower in the same AWS Region as your existing IAM Identity Center deployment. If you're using an existing IAM Identity Center identity source, AWS Control Tower won't delete or modify your configuration. You will still be able to manage any further changes to IAM Identity Center configuration yourself.

For a new landing zone, if you choose the AWS Control Tower setup option, you can choose an IAM Identity Center directory, a SAML 2.0-compatible identity provider (IdP), or Active Directory as your [identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html) in IAM Identity Center. The identity source defines where you administer and authenticate identities. IAM provides these features:
+ Active Directory users and user groups are synchronized between your identity source and IAM Identity Center.
+ AWS permission sets are defined by job roles, such as infrastructure administrator or security operations.
+ User groups from the identity source are mapped to the defined permissions.
+ You must require multi-factor authentication (MFA) for all root, IAM, and IAM Identity Center users.

You can also use an external identity provider as your identity source to manage access to your AWS accounts, resources, and cloud applications. During SAML-based authentication, users and groups are synchronized from your external identity provider by using System for Cross-domain Identity Management (SCIM) in IAM Identity Center. Users can complete this federation by using the IAM Identity Center portal. The following diagram illustrates how identify federation works.

![Setting up authentication in a landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/images/guide-img/156d118c-ed00-4c5b-9a02-63c2673a3342/images/acebedce-2258-4b5f-af09-a1c7c0023ac1.png)

Direct access to AWS accounts must be limited only through the [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) and [break glass identities](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/break-glass-access.html) (IAM roles or users that can access the accounts if the IAM Identity Center federation is broken or you are accidentally locked out of the environment).

## Break glass access
<a name="break-glass"></a>

[Break glass access](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/break-glass-access.html) refers to a quick means for a person who doesn't have access privileges to certain AWS accounts to gain access in exceptional circumstances, by using an approved process. The management account in AWS Organizations is used to provide break glass access to AWS accounts within the organization.

AWS discourages the use and creation of IAM users. However, break glass users are an exception. These users assume roles in the member accounts in your organization through trust policies. A break glass role that only the break glass users from the management account can assume is deployed to all the accounts in the organization. When you set up these roles in your organization, make sure that they can be used in emergency situations, such as the failure of the organization's identity provider, security incidents, or unavailability of key personnel, to provide temporary, elevated access beyond regular permissions to perform tasks such as updating guardrails, troubleshooting issues with automation tooling, or remediating security and operational issues that might occur. For more information, see [Set up emergency access to the AWS Management Console](https://docs.aws.amazon.com/singlesignon/latest/userguide/emergency-access.html) in the IAM Identity Center documentation.

**Warning**
  IAM users have long-term credentials, which present a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed.

## Roles and responsibilities
<a name="roles-responsibilities"></a>

Here's the approach for granting the appropriate level of access to new accounts in your landing zone:
+ New groups are created in your IdP according to the required job function. For example, an `AWS-Management-BillingAdmin` group could modify billing information, modify payment methods, download invoices, and read from [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) in the management account, but wouldn't be able to access other accounts.
+ The groups created in the identity source are visible in IAM Identity Center after federation is complete.
+ You can define new [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) in IAM Identity Center. A permission set defines the level of access that users and groups have to an AWS account. They are stored in IAM Identity Center and can be provisioned to one or more AWS accounts. For example, you could create a `BillingAdmin` permission set for the `AWS-Management-BillingAdmin` group.
**Note**
IAM Identity Center provides predefined permission sets such as `AWSReadOnlyAccess` and `AWSAdministratorAccess`.
+ IAM Identity Center provides AWS managed policies for job functions through an IAM policy that provides the appropriate level of access to AWS services. You can attach these managed policies to permission sets in IAM Identity Center. For example, you can attach the `Billing` managed policy to the `BillingAdmin` permission set. You can also create custom policies, if required.
+ In IAM Identity Center, you associate accounts with an identity source group and permission set. For example, you can associate the management account with the `AWS-Management-BillingAdmin` group and `BillingAdmin` permission set.

The following table lists the AWS managed policies for job functions that are available in IAM Identity Center. You can use these as a starting point for defining permission sets. For more information, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the IAM documentation.

|
|
| AWS managed policy name | Description of job function |
| --- |--- |
| `AdministratorAccess` | Provides full access to AWS services and resources. |
| `Billing` | Grants permissions for billing and cost management. This includes viewing account usage and viewing or modifying budgets and payment methods. |
| `DataScientist` | Grants permissions to AWS data analytics services. |
| `DatabaseAdministrator` | Grants full access permissions to the AWS services and actions required to set up and configure AWS database services. |
| `NetworkAdministrator` | Grants full access permissions to the AWS services and actions required to set up and configure AWS network resources. |
| `PowerUserAccess` | Provides full access to AWS services and resources for application developers, but doesn't allow management of users and groups. |
| `SecurityAudit` | Grants read access to the security configuration metadata. This is useful for software that audits the configuration of an AWS account. |
| `SupportUser` | Grants permissions to troubleshoot and resolve issues in an AWS account. This policy also enables the user to contact AWS Support. |
| `SystemAdministrator` | Grants full access permissions to the resources required for application and development operations. |
| `ViewOnlyAccess` | Grants permissions to view resources and basic metadata across all AWS services. |

The following table describes the additional permission sets that you can set up in IAM Identity Center, along with the associated accounts.

**Important**
Make sure that you choose and customize your permission sets according to your landing zone requirements.

|
|
| Permission set created in IAM Identity Center | AWS managed policies for job functions | Active Directory group | AWS account associated with the Active Directory group |
| --- |--- |--- |--- |
| `Administrator` | `AdministratorAccess` | `AWS-Management-Administrator` | Management |
| `AWS-Audit-Administrator` | Audit |
| `AWS-LogArchive-Administrator` | Log Archive |
| `AWS-SharedServices-Administrator` | Shared Services |
| `AWS-Networking-Administrator` | Networking |
| `AWS-Prod-Administrator` | Production |
| `AWS-NonProd-Administrator` | Non-production |
| `BillingAdmin` | `Billing` | `AWS-Management-BillingAdmin` | Management |
| `SecurityAuditor` | `SecurityAudit` | `AWS-Global-SecurityAuditor` | All accounts |
| `ReadOnly` | `ViewOnlyAccess` | `AWS-Core-ReadOnly` | Audit, Log Archive |
| `AWS-Infrastructure-ReadOnly` | Shared Services, Networking |
| `AWS-Infrastructure-ReadOnly-NonProd` | Non-production |
| `NetworkPowerUser` | `NetworkAdministrator` | `AWS-Infrastructure-NetworkPowerUser` | Networking |
| `Support` | `SupportUser` | `AWS-Global-SupportUser` | Log Archive, Shared Services, Networking, Non-production |
