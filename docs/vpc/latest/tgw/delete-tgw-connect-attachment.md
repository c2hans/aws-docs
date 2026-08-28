---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/delete-tgw-connect-attachment.html
---

# Delete a Connect attachment in AWS Transit Gateway
<a name="delete-tgw-connect-attachment"></a>

If you no longer need a Connect attachment, you can delete it. You must first delete any Connect peers for the attachment.

**To delete a Connect attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the Connect attachment, and choose **Actions**, **Delete transit gateway attachment**.

1. Enter **delete** and choose **Delete**.

**To delete a Connect attachment using the AWS CLI**
Use the [delete-transit-gateway-connect](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-connect.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
