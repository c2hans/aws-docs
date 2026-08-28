---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target-disassociate.html
---

# Disassociate a target network from an AWS Client VPN endpoint
<a name="cvpn-working-target-disassociate"></a>

When you disassociate a target network, any routes that were manually added to the Client VPN endpoint's route table are deleted, as well as the route that was automatically created when the target network association was made (the local route of the VPC). If you disassociate all target networks from a Client VPN endpoint, clients can no longer establish a VPN connection.

**To disassociate a target network from a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint with which the target network is associated and choose **Target network associations**.

1. Select the target network to disassociate, choose **Disassociate**, and then choose **Disassociate target network**.

**To disassociate a target network from a Client VPN endpoint (AWS CLI)**
Use the [disassociate-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/disassociate-client-vpn-target-network.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
