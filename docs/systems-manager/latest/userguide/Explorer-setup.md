---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-setup.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Getting started with Systems Manager Explorer and OpsCenter
<a name="Explorer-setup"></a>

AWS Systems Manager uses an integrated setup experience to help you get started with Systems Manager Explorer and Systems Manager OpsCenter. In this documentation, Explorer and OpsCenter Setup is called *Integrated Setup*. If you already set up OpsCenter, you still need to complete Integrated Setup to verify settings and options. If you haven't set up OpsCenter, then you can use Integrated Setup to get started with both tools.

**Note**
Integrated Setup is only available in the Systems Manager console. You can't set up Explorer or OpsCenter programmatically.

Integrated Setup performs the following tasks:
+ [Configures roles and permissions](Explorer-setup-permissions.md): Integrated Setup creates an AWS Identity and Access Management (IAM) role that allows Amazon EventBridge to automatically create OpsItems based on default rules. After setting up, you must configure user, group, or role permissions for OpsCenter, as described in this section.
+ [Allows default rules for OpsItem creation](Explorer-setup-default-rules.md): Integrated Setup creates default rules in EventBridge. These rules automatically create OpsItems in response to events. Examples of these events are: state change for an AWS resource, a change in security settings, or a service becoming unavailable.
+ Activates OpsData sources: Integrated Setup activates the following data sources that populate Explorer widgets.
  + Support Center (You must have either a Business or Enterprise Support plan to activate this source.)
  + AWS Compute Optimizer (You must have either a Business or Enterprise Support plan to activate this source.)
  + Systems Manager State Manager association compliance
  + AWS Config Compliance
  + Systems Manager OpsCenter
  + Systems Manager Patch Manager patch compliance
  + Amazon Elastic Compute Cloud (Amazon EC2)
  + Systems Manager Inventory
  + AWS Trusted Advisor (You must have either a Business or Enterprise Support plan to activate this source.)
  + AWS Security Hub CSPM

**Note**
You can change setup configurations at any time on the **Settings** page.

After you complete Integrated Setup, we recommend that you [Set up Explorer to display data from multiple Regions and accounts](Explorer-resource-data-sync.md). Explorer and OpsCenter automatically synchronize OpsData and OpsItems for the AWS account and AWS Region you used when you completed Integrated Setup. You can aggregate OpsData and OpsItems from other accounts and Regions by creating a resource data sync.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
