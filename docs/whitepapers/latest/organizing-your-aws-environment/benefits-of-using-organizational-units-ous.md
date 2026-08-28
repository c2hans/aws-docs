---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-organizational-units-ous.html
---

# Benefits of using organizational units (OUs)
<a name="benefits-of-using-organizational-units-ous"></a>

The following benefits of using OUs helped shape [Recommended OUs and accounts](recommended-ous-and-accounts.md).

## Group similar accounts based on function
<a name="group-similar-accounts-based-on-function"></a>

 When you have multiple accounts that perform either similar or related functions, you can benefit from grouping these accounts into distinct top-level OUs. Prudent use of top-level OUs can help your teams better understand the overall structure of your AWS accounts.

 For example, these best practices recommend [a set of top-level OUs](recommended-ous-and-accounts.md) to help you organize different sets of related accounts. At a minimum, the top-level OUs are used to distinguish between overall functions of accounts.

## Apply common policies
<a name="apply-common-policies"></a>

 OUs provide a way for you to organize your accounts so that it's easier to apply common overarching policies to accounts that have similar needs. Policies in AWS Organizations enable you to apply additional types of management to the accounts in your organization.

 By attaching policies to OUs rather than to individual accounts, you can simplify management of policies across groups of similar accounts. As the number of accounts in your environment grows, simplifying policy management by attaching policies to OUs becomes more important.

 AWS Organizations supports use of authorization and management policies. For a complete list of policy types, refer to [Managing AWS Organizations policies.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html)

### Authorization policies
<a name="authorization-policies"></a>
+  **Service control policies (SCPs):** SCPs are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. SCPs are a means of implementing controls in your AWS organization. Your use of SCPs can help ensure that your accounts stay within your access control guidelines. For example, you can use SCPs to constrain the set of AWS services and actions allowed on resources.
  +  Use SCPs to restrict your AWS Organizations' IAM principals' access to services and resources, or the conditions under which IAM principals can make requests. Refer to SCP examples and guidance on when to use SCPs.
+  **Resource control policies (RCPs):** RCPs are another type of authorization policy that you can use to manage permissions in your organization. RCPs offer central control over the maximum available permissions for resources in your organization. RCPs help you to ensure resources in your accounts stay within your organization's access control guidelines.
  +  Use RCPs to restrict who can access your resources, and enforce requirements on how your resources can be accessed. For example, only trusted external accounts can access specific Amazon S3 buckets hosted in your organization. Refer to RCP examples and guidance on when to use RCPs.

 Although you can apply SCPs and RCPs to the root of your organization, you typically associate these policies with underlying OUs. For example, based on the nature of the workloads deployed in accounts within an OU, you might choose to restrict the set of AWS services and AWS Regions that are allowed to be used by accounts in the OU.

 The effective permissions are the logical intersection between what is allowed by the RCPs and SCPs, and what is allowed by the identity-based and resource-based policies.

**Note**
Authorization policies (SCPs and RCPs) don't affect users, roles, or resources in the management account. They affect only the member accounts in your organization. This also means that SCPs and RCPs apply to member accounts that are designated as delegated administrators for policy management.

### Management policies
<a name="management-policies"></a>

 You can also apply the following policies to your organization:
+  [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html): Tag policies can help you monitor and ensure compliance with your cloud resource tagging standards.
+  [AI services opt-out policies:](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) You can use artificial intelligence (AI) services opt-out policies to control data collection for AWS AI services for all of your organization's accounts.
+  [Backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html): Backup policies can help you centrally manage and apply backup plans to the AWS resources across your organization's accounts.
+  [Chatbot policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html): Chatbot policies can help you to control access to your organization's accounts from chat channels. You can use Chatbot policies to determine which permissions models, chat platforms and chat workspaces can be used to access the accounts.
+  [Declarative policies for EC2:](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) Declarative policies allow you to centrally declare and enforce your desired configuration for a given AWS service at scale across an organization. Once attached, the configuration is always maintained when the service adds new features or APIs.
  +  Use declarative policies to prevent non-compliant actions. For example, you can block internet access to Amazon VPC resources across your organization.

## Share common resources
<a name="share-common-resources"></a>

 OUs provide a means for you to organize your accounts so that it's easier for you to share centrally managed resources across similar accounts.

 AWS services have been introducing support for sharing their resources through [AWS Resource Access Manager](https://aws.amazon.com/ram/) (AWS RAM) and AWS Organizations. For example, with AWS RAM, you can use OUs as the basis for sharing centrally managed network resources such as [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) [subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html).

## Provision and manage common resources
<a name="provision-and-manage-common-resources"></a>

 Sometimes you need to deploy common, centrally managed resource configurations to groups of related accounts. In cases where resource sharing doesn't apply, you can use a variety of AWS services and third-party tools that work with OUs to automatically roll out and update your own custom resources.

 For example, you can use OUs as a basis for targeting automation to deploy and update your own sets of IAM roles and [customer managed IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) that help establish common baseline and/or workload-specific security controls to groups of related accounts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
