---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/acccept-tgw-attach.html
---

# Accept a shared attachment in AWS Transit Gateway
<a name="acccept-tgw-attach"></a>

If you didn't enable the **Auto accept shared attachments** functionality when you created your transit gateway, you must manually accept cross-account (shared) attachment using either the Amazon VPC Console or the AWS CLI.

**To manually accept a shared attachment**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the transit gateway attachment that's pending acceptance.

1. Choose **Actions**, **Accept transit gateway attachment**.

**To accept a shared attachment using the AWS CLI**
Use the [accept-transit-gateway-vpc-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/accept-transit-gateway-vpc-attachment.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
