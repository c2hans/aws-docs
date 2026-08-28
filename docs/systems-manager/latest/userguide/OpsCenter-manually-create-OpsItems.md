---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Create OpsItems manually
<a name="OpsCenter-manually-create-OpsItems"></a>

When you find an operational issue, you can manually create an OpsItem from OpsCenter to manage and resolve the issue.

If you set up OpsCenter for cross-account administration, a Systems Manager delegated administrator or AWS Organizations management account can create OpsItems for member accounts. For more information, see [(Optional) Manually set up OpsCenter to centrally manage OpsItems across accounts](OpsCenter-getting-started-multiple-accounts.md).

You can create OpsItems by using the AWS Systems Manager console, the AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell.

**Topics**
+ [Creating OpsItems manually (console)](OpsCenter-creating-OpsItems-console.md)
+ [Creating OpsItems manually (AWS CLI)](OpsCenter-creating-OpsItems-CLI.md)
+ [Creating OpsItems manually (PowerShell)](OpsCenter-creating-OpsItems-Powershell.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
