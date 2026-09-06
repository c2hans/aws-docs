---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/robust-network-design-control-tower/configure-vpcs.html
---

# Configuring the VPCs
<a name="configure-vpcs"></a>

A VPC is a logically isolated network in AWS that resembles a traditional data center network. A robust network usually includes three different VPCs in the network account:
+ Firewall VPC
+ Inbound VPC
+ Outbound VPC

Each of these VPCs is designated for specific purpose. Applications and other services should not be deployed in these VPCs except for those that are described in this guide.

When you create these VPCs, choose the **VPC only** option. Then, choose the **IPAM-allocated IPv4 CIDR block** option, select the relevant IPAM pool, and enter the appropriate netmask.

## Firewall VPC
<a name="firewall-vpc"></a>

The firewall VPC is dedicated for creating and configuring a firewall by using AWS Network Firewall. In the firewall VPC, create six private subnets:
+ Three subnets dedicated for transit gateway attachment
+ Three subnets dedicated for the firewall

## Inbound VPC
<a name="inbound-vpc"></a>

When configuring the network account, consider the traffic that comes to your services that are hosted on AWS. In the inbound VPC, you host an Application Load Balancer. You also configure the organization's standard AWS WAF firewall and other security-related services to help prevent malicious activities that could compromise security. In the inbound VPC, create six subnets:
+ Three public subnets for hosting the Application Load Balancer
+ Three transit gateway attachment subnets in which you will configure routing to the firewall for any other network CIDR blocks apart from the inbound VPC's CIDR block

## Outbound VPC
<a name="outbound-vpc"></a>

The outbound VPC controls the traffic that goes out from the network account. In the outbound VPC, create the following nine subnets:
+ Three public subnets in three different Availability Zones, with a NAT gateway in each subnet.
+ Three private subnets in the three Availability Zones, each containing a route table configured with `0.0.0.0/0` route to the ID of the NAT gateway ID that is created in the respective public subnet. Attach transit gateways to the private subnets.

Associate any private hosted zones with outbound VPC.

## VPC Flow Logs
<a name="vpc-flow-logs"></a>

To record all requests to network interfaces for future analysis, configure VPC Flow Logs. For more information, see the [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) and the [Configure VPC Flow Logs for centralization across AWS accounts](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-vpc-flow-logs-for-centralization-across-aws-accounts.html) pattern.
