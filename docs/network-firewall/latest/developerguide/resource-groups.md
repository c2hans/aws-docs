---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/resource-groups.html
---

# Using tag-based resource groups in Network Firewall
<a name="resource-groups"></a>

Use *tag-based resource groups* to ensure that your rules stay in sync as your AWS resources change. A tag-based resource group is a collection of AWS resources, grouped by tags, that you can reference in an Network Firewall stateful rule group. A tag is a label that you assign to an AWS resource. As you add, delete, and modify your resources belonging to the resource group, Network Firewall automatically updates your rules with the IPs of the resources in the resource group. For information about referencing resource groups in rule groups, see [IP set references in Suricata compatible AWS Network Firewall rule groups](rule-groups-ip-set-references.md).

**Topics**
+ [Settings for the resource groups that you use in AWS Network Firewall](resource-group-settings.md)
+ [Creating a resource group in AWS Network Firewall](resource-group-creating.md)
+ [Updating a resource group in AWS Network Firewall](resource-group-updating.md)
+ [Deleting a resource group in AWS Network Firewall](resource-group-deleting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
