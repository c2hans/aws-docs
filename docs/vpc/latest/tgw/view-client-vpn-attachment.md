---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/view-client-vpn-attachment.html
---

# View a Client VPN attachment in AWS Transit Gateway
<a name="view-client-vpn-attachment"></a>

**To view your Client VPN attachments using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit gateways**.

1. Choose **Transit gateway attachments**.

1. In the **Resource type** column, look for **Client VPN**.

1. Choose an attachment to view its details.

**To view your Client VPN attachments using the AWS CLI**
Use the [describe-transit-gateway-attachments](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-attachments.html) command with a filter for resource type `client-vpn`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
