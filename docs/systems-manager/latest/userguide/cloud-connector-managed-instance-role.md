---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/cloud-connector-managed-instance-role.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Managed instance role
<a name="cloud-connector-managed-instance-role"></a>

The managed instance role is the IAM role that SSM Agent assumes on each Azure virtual machine after it's installed and registered. The role grants the agent the permissions it needs to call the Systems Manager service from the VM. Unlike the other three roles, this is not created on your behalf. You select an existing role during the connector setup wizard, or let the wizard create the recommended role `AmazonEC2RunCommandRoleForManagedInstances` with the `AmazonSSMManagedInstanceCore` AWS managed policy attached.

For information about creating this role and the policies you can attach to it, see [Create the IAM service role required for Systems Manager in hybrid and multicloud environments](hybrid-multicloud-service-role.md). Cloud Connector activations use the same role pattern as hybrid activations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
