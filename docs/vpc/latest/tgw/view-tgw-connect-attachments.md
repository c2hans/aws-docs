---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/view-tgw-connect-attachments.html
---

# View Connect attachments and Connect peers in AWS Transit Gateway
<a name="view-tgw-connect-attachments"></a>

View your Connect attachments and Connect peers.

**To view your Connect attachments and Connect peers using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Select the Connect attachment.

1. To view the Connect peers for the attachment, choose the **Connect Peers** tab.

**To view your Connect attachments and Connect peers using the AWS CLI**
Use the [describe-transit-gateway-connects](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-connects.html) and [describe-transit-gateway-connect-peers](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-connect-peers.html) commands.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
