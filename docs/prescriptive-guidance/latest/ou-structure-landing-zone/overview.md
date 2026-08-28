---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/ou-structure-landing-zone/overview.html
---

# Overview
<a name="overview"></a>

We worked with a multinational pharmaceutical company to run proof-of-concept (PoC) activities on AWS to explore how they could migrate their applications from on premises to the AWS Cloud. As they started scaling and accelerating their migration workflow to include production workloads, it became clear that they needed a regulated and compliant AWS landing zone to support their goal. We used [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) to design and implement a new AWS landing zone.

An important aspect of a new AWS landing zone and its organization is the structure of its *organizational units* (OUs). An OU is a logical grouping of AWS accounts created by using [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). You can use OUs to organize AWS accounts into a hierarchy and apply management and governance controls consistently and more easily.

You can attach policy-based controls to an OU and to AWS accounts. Child OUs within an OU automatically inherit those controls. Therefore, OUs play a critical role in managing security and governance in AWS Organizations.

A *policy* is a JSON document that includes one or more statements that define the controls you want to apply to a group of AWS accounts. AWS Organizations currently supports four types of policies, also known as *service control policies* (SCPs). An SCP defines the AWS services and actions that are available for use in different AWS accounts. For example, you can use an SCP to require Amazon Elastic Compute Cloud (Amazon EC2) instance launches to use a specific instance type.

## Policy types
<a name="policy-types"></a>

SCP policy types include the following:
+ [Allow lists and deny lists](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html) are complementary strategies that you can use to apply SCPs to filter the permissions that are available to accounts.
+ [Tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) help you maintain consistent tags, including the preferred case treatment of tag keys and tag values across accounts.
+ [Backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html) configure backups for supported resource types, such as the time window of the backup and destination vaults for backups across AWS Regions.
+ [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) enable or disable the continuous improvement of AWS artificial intelligence (AI) services globally.

**Policy inheritance behavior: **When you attach a policy to a specific OU, the accounts that are directly under that OU or any child OU inherit the policy. When you attach a policy to a specific account, the policy affects only that account. You can overwrite inherited policies by introducing exception policies. Inheritance explicitly allows all permissions to flow down from the root (OU) to every AWS account in that OU and child OU, unless you explicitly deny a permission. To deny a permission, you create an additional policy and attach it to the appropriate OU or AWS account. For more information about policy inheritance and exceptions, see the [AWS Organizations documentation](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_auth.html#orgs_manage_policies_inheritance_auth_scps).

AWS Control Tower also provides its own set of detective and preventive controls (also called *guardrails*) by using the OU structure. AWS Control Tower preventive controls prevent actions by using the SCPs in AWS Organizations. Detective controls report on configurational drift against the control by using AWS Config. For more information about these controls, see the [AWS Control Tower documentation](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html).

You can also enable [AWS Security Hub](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-securityhub.html) to automate security best practice checks, aggregate security alerts into a single place and format, and understand overall security posture across all your AWS accounts.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
