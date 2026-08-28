---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/delete-verified-access-group.html
---

# Delete a Verified Access group
<a name="delete-verified-access-group"></a>

When you are finished with a Verified Access group, you can delete it. You can't delete a group if there are associated Verified Access endpoints.

**To delete a Verified Access group using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access groups**.

1. Select the group.

1. Choose **Actions**, **Delete Verified Access group**.

1. When prompted for confirmation, enter **delete**, and then choose **Delete**.

**To delete a Verified Access group using the AWS CLI**
Use the [delete-verified-access-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-verified-access-group.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
