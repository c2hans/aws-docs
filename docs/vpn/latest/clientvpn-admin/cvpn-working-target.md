---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target.html
---

# AWS Client VPN target networks
<a name="cvpn-working-target"></a>

A target network is a subnet in a VPC. An AWS Client VPN endpoint must have at least one target network to enable clients to connect to it and establish a VPN connection.

For more information about the kinds of access that you can configure (such as enabling your clients to access the internet), see [Scenarios and examples for Client VPN](how-it-works.md#scenario).

## Client VPN target network requirements
<a name="cvpn-create-target-reqs"></a>

When creating a target network, the following rules apply:
+ The subnet must have a CIDR block with at least a /27 bitmask, for example 10.0.0.0/27. The subnet must also have at least 20 available IP addresses at all times.
+ The subnet's CIDR block cannot overlap with the client CIDR range of the Client VPN endpoint.
+ If you associate more than one subnet with a Client VPN endpoint, each subnet must be in a different Availability Zone. We recommend that you associate at least two subnets to provide Availability Zone redundancy.
+ If you specified a VPC when you created the Client VPN endpoint, the subnet must be in the same VPC. If you haven't yet associated a VPC with the Client VPN endpoint, you can choose any subnet in any VPC.

  All further subnet associations must be from the same VPC. To associate a subnet from a different VPC, you must first modify the Client VPN endpoint and change the VPC that's associated with it. For more information, see [Modify an AWS Client VPN endpoint](cvpn-working-endpoint-modify.md).

When you associate a subnet with a Client VPN endpoint, we automatically add the local route of the VPC in which the associated subnet is provisioned to the Client VPN endpoint's route table.

**Note**
After your target networks are associated, when you add or remove additional CIDRs to your attached VPC, you must perform one of the following operations to update the local route for your Client VPN endpoint route table:
Disassociate your Client VPN endpoint from the target network, and then associate the Client VPN endpoint to the target network.
Manually add the route to, or remove the route from the Client VPN endpoint route table.

After you associate the first subnet with the Client VPN endpoint, the Client VPN endpoint's status changes from `pending-associate` to `available` and clients are able to establish a VPN connection.

**Topics**
+ [Requirements for creating a target network](#cvpn-create-target-reqs)
+ [Associate a target network with an endpoint](cvpn-working-target-associate.md)
+ [Apply a security group to a target network](cvpn-working-target-apply.md)
+ [View target networks](cvpn-working-target-view.md)
+ [Disassociate a target network from an endpoint](cvpn-working-target-disassociate.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
