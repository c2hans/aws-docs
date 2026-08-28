---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/ug/delete-target-group.html
---

# Delete a VPC Lattice target group
<a name="delete-target-group"></a>

You can delete a target group if it is not referenced by the forward actions of any listener rules. Deleting a target group does not affect the targets registered with the target group. If you no longer need a registered EC2 instance, you can stop or terminate it.

**To delete a target group using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Target groups**.

1. Select the check box for the target group and then choose **Actions**, **Delete**.

1. When prompted for confirmation, enter **confirm** and then choose **Delete**.

**To delete a target group using the AWS CLI**
Use the [delete-target-group](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/delete-target-group.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
