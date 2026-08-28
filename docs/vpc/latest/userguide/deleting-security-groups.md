---
source_url: https://docs.aws.amazon.com/vpc/latest/userguide/deleting-security-groups.html
---

# Delete a security group
<a name="deleting-security-groups"></a>

When you are finished with a security group that you created, you can delete it.

**Requirements**
+ The security group can't be associated with any resources.
+ The security group can't be referenced by a rule in another security group.
+ The security group can't be the default security group for a VPC.

**To delete a security group using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Select the security group and choose **Actions**, **Delete security groups**.

1. If you selected more than one security group, you are prompted for confirmation. If some of the security groups can't be deleted, we display the status of each security group, which indicates whether it will be deleted. To confirm deletion, enter **Delete**.

1. Choose **Delete**.

**To delete a security group using the AWS CLI**
Use the [delete-security-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-security-group.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
