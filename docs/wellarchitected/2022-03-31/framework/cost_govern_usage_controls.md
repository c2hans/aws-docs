---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/cost_govern_usage_controls.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# COST02-BP05 Implement cost controls
<a name="cost_govern_usage_controls"></a>

 Implement controls based on organization policies and defined groups and roles. These certify that costs are only incurred as defined by organization requirements: for example, control access to regions or resource types with AWS Identity and Access Management (IAM) policies.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

A common first step in implementing cost controls is to set up notifications when cost or usage events occur outside of the organization policies. This enables you to act quickly and verify if corrective action is required, without restricting or negatively impacting workloads or new activity. After you know the workload and environment limits, you can enforce governance. In AWS, notifications are conducted with AWS Budgets, which allows you to define a monthly budget for your AWS costs, usage, and commitment discounts (Savings Plans and Reserved Instances). You can create budgets at an aggregate cost level (for example, all costs), or at a more granular level where you include only specific dimensions such as linked accounts, services, tags, or Availability Zones.

As a second step, you can enforce governance policies in AWS through [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM), and [AWS Organizations Service Control Policies (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html). IAM allows you to securely manage access to AWS services and resources. Using IAM, you can control who can create and manage AWS resources, the type of resources that can be created, and where they can be created. This minimizes the creation of resources that are not required. Use the roles and groups created previously, and assign [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) to enforce the correct usage. SCP offers central control over the maximum available permissions for all accounts in your organization, ensuring that your accounts stay within your access control guidelines. SCPs are available only in an organization that has all features enabled, and you can configure the SCPs to either deny or allow actions for member accounts by default. Refer to the [Well-Architected Security Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) for more details on implementing access management.

Governance can also be implemented through management of Service Quotas. By ensuring Service Quotas are set with minimum overhead and accurately maintained, you can minimize resource creation outside of your organization’s requirements. To achieve this, you must understand how quickly your requirements can change, understand projects in progress (both creation and decommission of resources), and factor in how fast quota changes can be implemented. [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) can be used to increase your quotas when required.

**Implementation steps**
+ ** Implement notifications on spend:** Using your defined organization policies, create AWS budgets to provide notifications when spending is outside of your policies. Configure multiple cost budgets, one for each account, which notifies you about overall account spending. Then configure additional cost budgets within each account for smaller units within the account. These units vary depending on your account structure. Some common examples are AWS Regions, workloads (using tags), or AWS services. Ensure that you configure an email distribution list as the recipient for notifications, and not an individual's email account. You can configure an actual budget for when an amount is exceeded, or use a forecasted budget for notifying on forecasted usage.
+ ** Implement controls on usage: **Using your defined organization policies, implement IAM policies and roles to specify which actions users can perform and which actions they cannot perform. Multiple organizational policies may be included in an AWS policy. In the same way that you defined policies, start broadly and then apply more granular controls at each step. Service limits are also an effective control on usage. Implement the correct service limits on all your accounts.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)
+  [AWS multiple account billing strategy](https://aws.amazon.com/answers/account-management/aws-multi-account-billing-strategy/)
+  [Control access to AWS Regions using IAM policies](https://aws.amazon.com/blogs/security/easier-way-to-control-access-to-aws-regions-using-iam-policies/)

 **Related examples:**
+  [Well-Architected Labs: Cost and Usage Governance](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/100_2_Cost_and_Usage_Governance/README.html)
+  [Well-Architected Labs: Cost and Usage Governance](https://wellarchitectedlabs.com/Cost/Cost_Fundamentals/200_2_Cost_and_Usage_Governance/README.html)
