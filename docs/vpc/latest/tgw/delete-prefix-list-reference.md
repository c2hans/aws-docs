---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/delete-prefix-list-reference.html
---

# Delete a prefix list reference in AWS Transit Gateway
<a name="delete-prefix-list-reference"></a>

If you no longer need a prefix list reference, you can delete it from your transit gateway route table. Deleting the reference does not delete the prefix list.

**To delete a prefix list reference using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the transit gateway route table.

1. Choose the prefix list reference, and choose **Delete references**.

1. Choose **Delete references**.

**To modify a prefix list reference using the AWS CLI**
Use the [delete-transit-gateway-prefix-list-reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-prefix-list-reference.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
