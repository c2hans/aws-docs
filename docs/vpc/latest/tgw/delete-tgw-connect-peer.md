---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/delete-tgw-connect-peer.html
---

# Delete a Connect peer in AWS Transit Gateway
<a name="delete-tgw-connect-peer"></a>

If you no longer need a Connect peer, you can delete it.

**To delete a Connect peer using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the Connect attachment.

1. In the **Connect Peers** tab, select the Connect peer and choose **Actions**, **Delete connect peer**.

**To delete a Connect peer using the AWS CLI**
Use the [delete-transit-gateway-connect-peer](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-connect-peer.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
