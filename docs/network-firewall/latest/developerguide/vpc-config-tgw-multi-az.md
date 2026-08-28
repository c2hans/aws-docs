---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config-tgw-multi-az.html
---

# Transit gateway attachment configuration for AWS Network Firewall
<a name="vpc-config-tgw-multi-az"></a>

This section applies to the use of Network Firewall with a transit gateway in multiple Availability Zones where the firewall endpoints might reside in different Availability Zones than the subnets whose traffic they're filtering.

**Note**
To use this configuration, you must enable appliance mode on the transit gateway VPC attachment for any VPC where Network Firewall endpoints reside.

A Network Firewall endpoint is a stateful network appliance. Enabling appliance mode ensures that the transit gateway continues to use the same Availability Zone for the VPC attachment over the lifetime of a flow of traffic between source and destination.

For information about VPC transit gateways, see the guide [Amazon Virtual Private Cloud Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

For information about appliance mode and how to enable it in your attachments, see [Availability Zones](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html#tgw-az-overview) and [Example: Appliance in a shared services VPC](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-appliance-scenario.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
