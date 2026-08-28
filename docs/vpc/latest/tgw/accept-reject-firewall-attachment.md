---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/accept-reject-firewall-attachment.html
---

# Accept or reject an AWS Transit Gateway network function attachment
<a name="accept-reject-firewall-attachment"></a>

You can use either the Amazon VPC console or the AWS Network Firewall CLI or API to accept or reject a transit gateway network function attachment, including Network Firewall attachments. If you are the owner of a transit gateway and someone has created a firewall attachment to your transit gateway from another account, you need to accept or reject the attachment request.

To accept or reject a network function attachment using the Network Firewall CLI, see the `AcceptNetworkFirewallTransitGatewayAttachment` or `RejectNetworkFirewallTransitGatewayAttachment` APIs in the [*AWS Network Firewall API Reference*](https://docs.aws.amazon.com/network-firewall/latest/APIReference/Welcome.html).

## Accept or reject a network function attachment using the console
<a name="create-firewall-attachment-console"></a>

Use the Amazon VPC console to accept or reject a transit gateway network function attachment.

**To accept or reject a network function attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateways**.

1. Choose **Transit gateway attachments**.

1. Select the attachment with a state of **Pending acceptance** and a type of **Network function**.

1. Choose **Actions**, and then choose either **Accept attachment** or **Reject attachment**.

1. In the confirmation dialog box, choose **Accept** or **Reject**.

If you accept the attachment, it becomes active and the firewall can inspect traffic. If you reject the attachment, it enters a rejected state and will eventually be deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
