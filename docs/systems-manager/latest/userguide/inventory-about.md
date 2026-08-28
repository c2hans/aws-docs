---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-about.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Learn more about Systems Manager Inventory
<a name="inventory-about"></a>

When you configure AWS Systems Manager Inventory, you specify the type of metadata to collect, the managed nodes to collect from, and a schedule for metadata collection. These configurations are saved with your AWS account as an AWS Systems Manager State Manager association. An association is simply a configuration.

**Note**
Inventory only collects metadata. It doesn't collect any personal or proprietary data.

**Topics**
+ [Metadata collected by Inventory](inventory-schema.md)
+ [Working with file and Windows registry inventory](inventory-file-and-registry.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
