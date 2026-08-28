---
source_url: https://docs.aws.amazon.com/controltower/latest/controlreference/control-considerations.html
---

# Considerations for controls and OUs
<a name="control-considerations"></a>

When working with controls and OUs, consider the following properties:

**Controls, landing zones, and OUs**
+ Mandatory controls are no longer enabled by default. Optional controls are applied at the discretion of administrators.
+ Controls can now be enabled on any OU within a customer's AWS Organization once they enable AWS Control Tower.
+ Regarding nested OUs, preventive controls enabled on any OUs higher in the tree will apply all OUs in the tree.
+ Detective controls can be applied to an OU that has either the ConfigBaseline enabled or the AWSControlTowerBaseline.
+ Hook controls can now be deployed into any OU. The hook will deploy the AWSServiceRoleForControlTower Service Linked Role (SLR), into the account and activate the opt-in regions.

For more information about how controls are applied to nested OUs, in AWS Control Tower, see [Nested Ous and controls](https://docs.aws.amazon.com/controltower/latest/userguide/nested-ous.html#nested-ous-and-controls).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
