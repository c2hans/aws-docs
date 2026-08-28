---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/automatic-assignment.html
---

# Configure automatic public IP addresses for WorkSpaces Personal
<a name="automatic-assignment"></a>

After you enable automatic assignment of public IP addresses, each WorkSpace that you launch is assigned a public IP address from the Amazon-provided pool of public addresses. A WorkSpace in a public subnet can access the internet through the internet gateway if it has a public IP address. WorkSpaces that already exist before you enable automatic assignment do not receive public addresses until you rebuild them.

Note that you do not need to enable automatic assignment of public addresses if your WorkSpaces are in private subnets and you configured a NAT gateway for the virtual private cloud (VPC), or if your WorkSpaces are in public subnets and you assigned them Elastic IP addresses. For more information, see [Configure a VPC for WorkSpaces Personal](amazon-workspaces-vpc.md).

**Warning**
If you associate an Elastic IP address that you own to a WorkSpace, and then you later disassociate that Elastic IP address from the WorkSpace, the WorkSpace loses its public IP address, and it doesn't automatically get a new one from the Amazon-provided pool. To associate a new public IP address from the Amazon-provided pool with the WorkSpace, you must [rebuild the WorkSpace](rebuild-workspace.md). If you don't want to rebuild the WorkSpace, you must associate another Elastic IP address that you own to the WorkSpace.

**To configure Elastic IP addresses**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **Directories**.

1. Select the directory for your WorkSpaces.

1. Choose **Actions**, **Update Details**.

1. Expand **Access to Internet** and select **Enable** or **Disable**.

1. Choose **Update**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
