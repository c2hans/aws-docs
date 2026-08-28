---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-modifying.html
---

# Modify a transit gateway in AWS Transit Gateway
<a name="tgw-modifying"></a>

You can modify the configuration options for a transit gateway. When you modify a transit gateway, any existing transit gateway attachments don't experience any service interruptions.

You cannot modify a transit gateway that has been shared with you.

You cannot remove a CIDR block for the transit gateway if any of the IP addresses are currently used for a [Connect peer](tgw-connect.md).

**Note**
Transit gateways that have Encryption Support enabled can be attached to VPCs with Encryption Controls in monitor or Enforce mode, or to VPCs that don’t have Encryption Controls enabled. VPCs that have Encryption Controls in Enforce mode can ONLY be attached to Transit Gateways that have Encryption Support enabled.
For more detailed information, see [Encryption Support for AWS Transit Gateway](tgw-encryption-support.md).

**To modify a transit gateway**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateways**.

1. Choose the transit gateway to modify.

1. Choose **Actions**, **Modify transit gateway**.

1. Modify the options as needed, and choose **Modify transit gateway**.

**To modify your transit gateway using the AWS CLI**
Use the [modify-transit-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-transit-gateway.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
