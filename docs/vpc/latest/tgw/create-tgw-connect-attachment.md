---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw-connect-attachment.html
---

# Create a Connect attachment in AWS Transit Gateway
<a name="create-tgw-connect-attachment"></a>

To create a Connect attachment, you must specify an existing attachment as the transport attachment. You can specify a VPC attachment or a Direct Connect attachment as the transport attachment.

**To create a Connect attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateway attachments**.

1. Choose **Create transit gateway attachment**.

1. (Optional) For **Name tag**, specify a name tag for the attachment.

1. For **Transit gateway ID**, choose the transit gateway for the attachment.

1. For **Attachment type**, choose **Connect**.

1. For **Transport attachment ID**, choose the ID of an existing attachment (the transport attachment).

1. Choose **Create transit gateway attachment**.

**To create a Connect attachment using the AWS CLI**
Use the [create-transit-gateway-connect](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-connect.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
