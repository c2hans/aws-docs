---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html
---

# AWS managed policies for AWS Resource Explorer
<a name="security_iam_awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**General AWS managed policies that include Resource Explorer permissions**
+ [AdministratorAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AdministratorAccess) – Grants full access to AWS services and resources.
+ [ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ReadOnlyAccess) – Grants read-only access to AWS services and resources.
+ [ViewOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/job-function/ViewOnlyAccess) – Grants permissions to view resources and basic metadata for AWS services.
**Note**
The Resource Explorer `Get*` permissions included in the `ViewOnlyAccess` policy perform like `List` permissions although they return only a single value, because a Region can contain only one index and one default view.

**AWS managed policies for Resource Explorer**
+ [AWSResourceExplorerFullAccess](#security_iam_awsmanpol_AWSResourceExplorerFullAccess)
+ [AWSResourceExplorerReadOnlyAccess](#security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess)
+ [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy)

## AWS managed policy: AWSResourceExplorerFullAccess
<a name="security_iam_awsmanpol_AWSResourceExplorerFullAccess"></a>

You can assign the `AWSResourceExplorerFullAccess` policy to your IAM identities.

This policy grants permissions that allow full administrative control of the Resource Explorer service. You can perform all tasks involved in turning on and managing Resource Explorer in the AWS Regions in your account. With this policy, the Resource Explorer console shows information from other integrated AWS services and allows you to perform actions such as creating an application.

**Permissions details**

This policy includes permissions that allow all actions for Resource Explorer, including turning on and turning off Resource Explorer in AWS Regions, creating or deleting an aggregator index for the account, creating, updating, and deleting views, and searching. This policy also includes permissions that are not part of Resource Explorer:
+ `ec2:DescribeRegions` – allows Resource Explorer to access the details about the Regions in your account.
+ `ram:ListResources` – allows Resource Explorer to list the resource shares that resources are part of.
+ `ram:GetResourceShares` – allows Resource Explorer to identify details about the resource shares that you own or that are shared with you.
+ `iam:CreateServiceLinkedRole` (included in the [AWSResourceExplorerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.html) managed policy) – allows Resource Explorer to create the required service-linked role when you [turn on Resource Explorer by creating the first index](manage-service-turn-on-region.md#manage-service-turn-on-region-region).
+ `organizations:DescribeOrganization` – allows Resource Explorer to access information about your organization.

To see the latest version of this AWS managed policy, see `[AWSResourceExplorerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.html)` in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSResourceExplorerReadOnlyAccess
<a name="security_iam_awsmanpol_AWSResourceExplorerReadOnlyAccess"></a>

You can assign the `AWSResourceExplorerReadOnlyAccess` policy to your IAM identities.

This policy grants read-only permissions that allows users to discover their resources with basic search access, and access other integrated AWS services in the Resource Explorer console.

**Permissions details**

This policy includes permissions that allow users to perform the Resource Explorer `Get*`, `List*`, and `Search` operations to view information about Resource Explorer components and configuration settings, but doesn't allow users to change them. Users can also search. This policy also includes two permissions that are not part of Resource Explorer:
+ `ec2:DescribeRegions` – allows Resource Explorer to access the details about the Regions in your account.
+ `ram:ListResources` – allows Resource Explorer to list the resource shares that resources are part of.
+ `ram:GetResourceShares` – allows Resource Explorer to identify details about the resource shares that you own or that are shared with you.
+ `organizations:DescribeOrganization` – allows Resource Explorer to access information about your organization.

To see the latest version of this AWS managed policy, see `[AWSResourceExplorerReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerReadOnlyAccess.html)` in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSResourceExplorerServiceRolePolicy
<a name="security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy"></a>

You can't attach `AWSResourceExplorerServiceRolePolicy` to any IAM entities yourself. This policy can be attached only to a service-linked role that allows Resource Explorer to perform actions on your behalf. For more information, see [Using service-linked roles for Resource Explorer](security_iam_service-linked-roles.md).

This policy grants the permissions required for Resource Explorer to retrieve information about your resources. Resource Explorer populates the indexes it maintains in each AWS Region that you register.

To see the latest version of this AWS managed policy, [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerServiceRolePolicy.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: AWSResourceExplorerOrganizationsAccess
<a name="security_iam_awsmanpol_AWSResourceExplorerOrganizationsAccess"></a>

You can assign `AWSResourceExplorerOrganizationsAccess` to your IAM identities.

This policy grants administrative permissions to Resource Explorer and grants read-only permissions to other AWS services to support this access. The AWS Organizations administrator needs these permissions to set up and manage multi-account search in the console.

**Permissions details**

This policy includes permissions that allow administrators to set up multi-account search for the organization:
+ `ec2:DescribeRegions` – Allows Resource Explorer to access the details about the Regions in your account.
+ `ram:ListResources` – Allows Resource Explorer to list the resource shares that resources are part of.
+ `ram:GetResourceShares` – Allows Resource Explorer to identify details about the resource shares that you own or that are shared with you.
+ `organizations:ListAccounts` – Allows Resource Explorer to identify the accounts within an organization.
+ `organizations:ListRoots` – Allows Resource Explorer to identify the root accounts within an organization.
+ `organizations:ListOrganizationalUnitsForParent` – Allows Resource Explorer to identify the organizational units (OUs) in a parent organizational unit or root.
+ `organizations:ListAccountsForParent` – Allows Resource Explorer to identify the accounts in an organization that are contained by the specified target root or an OU.
+ `organizations:ListDelegatedAdministrators` – Allows Resource Explorer to identify the AWS accounts that are designated as delegated administrators in this organization.
+ `organizations:ListAWSServiceAccessForOrganization` – Allows Resource Explorer to identify a list of the AWS services that are enabled to integrate with your organization.
+ `organizations:DescribeOrganization` – Allows Resource Explorer to retrieve information about the organization that the user's account belongs to.
+ `organizations:EnableAWSServiceAccess` – Allows Resource Explorer to enable the integration of an AWS service (the service that is specified by `ServicePrincipal`) with AWS Organizations.
+ `organizations:DisableAWSServiceAccess` – Allows Resource Explorer to disable the integration of an AWS service (the service that is specified by ServicePrincipal) with AWS Organizations.
+ `organizations:RegisterDelegatedAdministrator` – Allows Resource Explorer to enable the specified member account to administer the organization's features of the specified AWS service.
+ `organizations:DeregisterDelegatedAdministrator` – Allows Resource Explorer to remove the specified member AWS account as a delegated administrator for the specified AWS service.
+ `iam:GetRole` – Allows Resource Explorer to retrieve information about the specified role, including the role's path, GUID, ARN, and the role's trust policy that grants permission to assume the role.
+ `iam:CreateServiceLinkedRole` (included in the [AWSResourceExplorerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerFullAccess.html) managed policy) – Allows Resource Explorer to create the required service-linked role when you [turn on Resource Explorer by creating the first index](manage-service-turn-on-region.md#manage-service-turn-on-region-region).

To see the latest version of this AWS managed policy, see `[AWSResourceExplorerOrganizationsAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerServiceRolePolicy.html)` in the *AWS Managed Policy Reference Guide*.

## Resource Explorer updates to AWS managed policies
<a name="security_iam_awsmanpol_updates"></a>

View details about updates to AWS managed policies for Resource Explorer since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Resource Explorer Document history](doc-history.md) page.

| Change | Description | Date |
| --- | --- | --- |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | June 23, 2026 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | February 04, 2026 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | December 16, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | November 17, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | October 13, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | September 24, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | September 15, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions for AWS policy best practices | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were removed for resource types that are not currently supported by Resource Explorer. For the latest version of this policy, see [https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerServiceRolePolicy.html](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*. <br />The following permissions were removed for unsupported resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | September 5, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | August 4, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to allow Resource Explorer to manage indexes and views  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). The following permissions were added that allow Resource Explorer to create, manage, and delete indexes and views: [See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | July 23, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer modified the permissions in the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy). Permissions were added that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | May 7, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types  | Resource Explorer added permissions to the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | March 21, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types | Resource Explorer added permissions to the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | January 6, 2025 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types | Resource Explorer added permissions to the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | November 21, 2024 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) - Updated policy permissions to view additional resource types | Resource Explorer added permissions to the service-linked role policy [`AWSResourceExplorerServiceRolePolicy`](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) that allows Resource Explorer to view additional resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | December 12, 2023 |
| New managed policy | Resource Explorer added the following AWS managed policy:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | November 14, 2023 |
| Updated managed policies | Resource Explorer updated the following AWS managed policies to support multi-account search:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | November 14, 2023 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) – Updated policy to support multi-account search with Organizations | Resource Explorer added permissions to the service-linked role policy `[AWSResourceExplorerServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSResourceExplorerServiceRolePolicy)` that allows the Resource Explorer to support multi-account search with Organizations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | November 14, 2023 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) – Updated policy to support additional resource types | Resource Explorer added permissions to the service-linked role policy `[AWSResourceExplorerServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSResourceExplorerServiceRolePolicy)` that allows the service to index the following resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | October 17, 2023 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) – Updated policy to support additional resource types | Resource Explorer added permissions to the service-linked role policy `[AWSResourceExplorerServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSResourceExplorerServiceRolePolicy)` that allows the service to index the following resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | August 1, 2023 |
| [AWSResourceExplorerServiceRolePolicy](#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) – Updated policy to support additional resource types | Resource Explorer added permissions to the service-linked role policy `[AWSResourceExplorerServiceRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/aws-service-role/AWSResourceExplorerServiceRolePolicy)` that allows the service to index the following resource types:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | March 7, 2023 |
| New managed policies | Resource Explorer added the following AWS managed policies:[See the AWS documentation website for more details](http://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html) | November 7, 2022 |
| Resource Explorer started tracking changes | Resource Explorer started tracking changes for its AWS managed policies. | November 7, 2022 |
