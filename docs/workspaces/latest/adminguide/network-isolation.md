---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/network-isolation.html
---

# Network isolation
<a name="network-isolation"></a>

A virtual private cloud (VPC) is a virtual network in your own logically isolated area in the AWS Cloud. You can deploy your WorkSpaces in a private subnet in your VPC. For more information, see [Configure a VPC for WorkSpaces Personal](amazon-workspaces-vpc.md).

To allow traffic only from specific address ranges (for example, from your corporate network), update the security group for your VPC or use an [IP access control group](amazon-workspaces-ip-access-control-groups.md).

You can restrict WorkSpace access to trusted devices with valid certificates. For more information, see [Restrict access to trusted devices for WorkSpaces Personal](trusted-devices.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
