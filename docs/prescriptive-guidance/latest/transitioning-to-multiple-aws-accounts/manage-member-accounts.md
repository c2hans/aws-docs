---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/manage-member-accounts.html
---

# Manage member accounts
<a name="manage-member-accounts"></a>

In this section, you invite your preexisting account into the organization and you begin to create new accounts within your organization. An important part of this process is defining the criteria you use to determine whether you need to provision a new account.

This section consists of the following topics:

1. [Invite your preexisting account](#invite-account)

1. [Customize VPC settings in AWS Control Tower](#customize-vpc-settings)

1. [Define scoping criteria](#define-scoping-criteria)

## Invite your preexisting account
<a name="invite-account"></a>

Within AWS Organizations, you can invite your company's preexisting account into your new organization. Only the management account in the organization can invite other accounts to join. When the administrator of the invited account accepts, the account immediately joins the organization, and the organization's management account becomes responsible for all charges accrued by the new member account. For more information, see [Inviting an AWS account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) and [Accepting or declining an invitation from an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html#orgs_manage_accounts_accept-decline-invite) (AWS Organizations documentation).

|
|
| Note: You can invite an account to join an organization only if that account isn't a currently in another organization. If the account is a member of an existing organization, you must remove it from the organization. If the account is the management account for a different organization that was created in error, you must delete the organization. |
| --- |

|
|
| Important: If you need access to any historical cost or usage information from your preexisting account, you can use AWS Cost and Usage Report to export that information to an Amazon Simple Storage Service (Amazon S3) bucket. Do this prior to accepting the invitation to join the organization. When an account joins an organization, you lose access to this historical data for the account. For more information, see [Setting up an Amazon S3 bucket for Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-s3.html) (AWS Cost and Usage Report documentation). |
| --- |

### Best practices
<a name="best-practices.d78b1450-a2ed-5b35-a775-2e3948215b7d"></a>
+ We recommend that you add your preexisting account, which likely contains production workloads, to the **Workloads** > **Prod** organizational unit that you created in [Add organizational units](add-organizational-units.md).
+ By default, the organization's management account doesn't have administrative access over member accounts that are invited to the organization. If you want the management account to have administrative control, you must create the **OrganizationAccountAccessRole** IAM role in the member account and grant permission to the management account to assume the role. For more information, see [Creating the OrganizationAccountAccessRole in an invited member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_create-cross-account-role) (AWS Organizations documentation).
+ For the preexisting account that you invited to the organization, review [Best practices for member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/best-practices_member-acct.html) (AWS Organizations documentation) and confirm that the account adheres to these recommendations.

## Customize VPC settings in AWS Control Tower
<a name="customize-vpc-settings"></a>

We recommend that you provision new AWS accounts through the [Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) in AWS Control Tower. By using Account Factory, you can use the AWS Control Tower integration with Amazon EventBridge to provision resources in new AWS accounts as soon as the account is created.

When you set up a new AWS account, a [default virtual private cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html) is automatically provisioned. However, when you set up a new account through Account Factory, AWS Control Tower automatically provisions an additional VPC. For more information, see [Overview of AWS Control Tower and VPCs](https://docs.aws.amazon.com/controltower/latest/userguide/vpc-concepts.html) (AWS Control Tower documentation). This means that, by default, AWS Control Tower provisions two default VPCs in every new account.

It is common for companies to want more control over the VPCs within their accounts. Many prefer to use other services, such as AWS CloudFormation, Hashicorp Terraform, or Pulumi, to set up and manage their VPCs. You should customize the Account Factory settings to prevent creation of the additional VPC provisioned by AWS Control Tower. For instructions, see [Configure Amazon VPC settings](https://docs.aws.amazon.com/controltower/latest/userguide/configuring-account-factory-with-VPC-settings.html) (AWS Control Tower documentation), and apply the following settings:

1. Disable the **Internet-accessible subnet **option.

1. In **Maximum number of private subnets**, choose **0**.

1. In **Regions for VPC creation**, clear all Regions.

1. In **Availability Zones**, choose **3**.

### Best practices
<a name="best-practices.1befb685-4664-50b5-905d-68ec2db2d15f"></a>
+ Delete the default VPC that is automatically provisioned in every new account. This prevents users from launching public EC2 instances in the account without explicitly creating a dedicated VPC. For more information, see [Delete your default subnets and default VPC](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html#deleting-default-vpc) (Amazon Virtual Private Cloud documentation). You can also configure [AWS Control Tower Account Factory for Terraform](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) (AFT) to automatically delete the default VPC in newly created accounts.
+ Provision a new AWS account called **dev-nonprod** into the **Workloads** > **NonProd** organizational unit. Use this account for your development environment. For instructions, see [Provision Account Factory accounts with AWS Service Catalog](https://docs.aws.amazon.com/controltower/latest/userguide/provision-as-end-user.html) (AWS Control Tower documentation).

## Define scoping criteria
<a name="define-scoping-criteria"></a>

You need to select the criteria your company will use when deciding whether to provision a new AWS account. You might decide to provision accounts for each business unit, or you might decide to provision accounts based on environment, such as production, testing, or QA. Every company has their own requirements for how large or small their AWS accounts should be. Generally, you evaluate the following three factors when deciding how to size your accounts:
+ **Balancing service quotas** – *Service quotas* are the maximum values for the number of resources, actions, and items for each AWS service within an AWS account. If many workloads share the same account and one workload is consuming most or all of a service quota, that might negatively impact another workload in the same account. If so, you might need to separate those workloads into different accounts. For more information, see [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) (AWS General Reference documentation).
+ **Cost reporting** - Isolating workloads into separate accounts allows you to see costs at an account level in the cost and usage reports. When you use the same account for multiple workloads, you can use tags to help you manage and identify resources. For more information about tagging, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) (AWS General Reference documentation).
+ **Controlling access** - When workloads share an account, you need to consider how you will configure IAM policies to limit access to the account resources so that users don't have access to the workloads they don't need. As an alternative, you can use multiple accounts and [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) in IAM Identity Center to manage access into individual accounts.

### Best practices
<a name="best-practices.9ab0bc64-704a-5a00-bb97-bc9937b1e850"></a>
+ Adhere to the best practices in [AWS multi-account strategy for your AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html) (AWS Control Tower documentation).
+ Establish an effective tagging strategy that helps you identify and manage AWS resources. You can use tags to categorize resources by purpose, business unit, environment, or other criteria. For more information, see [Best practices for tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-best-practices) (AWS General Reference documentation).
+ Don't overload an account with too many workloads. If the demand of the workload exceeds a service quota, this can cause performance issues. You can separate the competing workloads into different AWS accounts or you can request a service quota increase. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) (Service Quotas documentation).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
