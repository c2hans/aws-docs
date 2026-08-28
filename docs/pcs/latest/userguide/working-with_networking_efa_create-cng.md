---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_networking_efa_create-cng.html
---

# Create or update compute node groups for EFA
<a name="working-with_networking_efa_create-cng"></a>

Your AWS PCS compute node groups must contain instances that have the same number of vCPUs, processor architecture, and EFA support. Configure the compute node group to use the AMI with the EFA software installed on it, and to use the launch template that configures EFA-enabled network interfaces.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
