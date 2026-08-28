---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/delete-verified-access-instance.html
---

# Delete a Verified Access instance
<a name="delete-verified-access-instance"></a>

When you are finished with a Verified Access instance, you can delete it. Before you can delete an instance, you must remove any associated trust providers or Verified Access groups.

**To delete a Verified Access instance using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access instances**.

1. Select the Verified Access instance.

1. Choose **Actions**, **Delete Verified Access instance**.

1. When prompted for confirmation, enter **delete**, and then choose **Delete**.

**To delete a Verified Access instance using the AWS CLI**
Use the [delete-verified-access-instance](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-verified-access-instance.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
