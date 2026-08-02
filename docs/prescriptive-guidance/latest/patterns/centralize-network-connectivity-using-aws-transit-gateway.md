---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-network-connectivity-using-aws-transit-gateway.html
---

# Centralize network connectivity using AWS Transit Gateway
<a name="centralize-network-connectivity-using-aws-transit-gateway"></a>

*Mydhili Palagummi and Nikhil Marrapu, Amazon Web Services*

## Summary
<a name="centralize-network-connectivity-using-aws-transit-gateway-summary"></a>

This pattern describes the simplest configuration in which AWS Transit Gateway can be used to connect an on-premises network to virtual private clouds (VPCs) in multiple AWS accounts within an AWS Region. Using this setup, you can establish a hybrid network that connects multiple VPC networks in a Region and an on-premises network. This is accomplished by using a transit gateway and a virtual private network (VPN) connection to the on-premises network.

## Prerequisites and limitations
<a name="centralize-network-connectivity-using-aws-transit-gateway-prereqs"></a>

**Prerequisites **
+ An account for hosting network services, managed as a member account of an organization in AWS Organizations
+ VPCs in multiple AWS accounts, without overlapping Classless Inter-Domain Routing (CIDR) blocks

**Limitations **

This pattern does not support the isolation of traffic between certain VPCs or the on-premises network. All the networks attached to the transit gateway will be able to reach each other. To isolate traffic, you need to use custom route tables on the transit gateway. This pattern only connects the VPCs and on-premises network by using a single default transit gateway route table, which is the simplest configuration.

## Architecture
<a name="centralize-network-connectivity-using-aws-transit-gateway-architecture"></a>

**Target technology stack  **
+ AWS Transit Gateway
+ AWS Site-to-Site VPN
+ VPC
+ AWS Resource Access Manager (AWS RAM)

**Target architecture **

![AWS Transit Gateway connects on-premises network to VPCs in multiple AWS accounts within a Region.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e23f5faf-e75e-42a3-80e3-142516a2db4e/images/1ecf7e04-bbf8-4304-88c8-6aceb7271d1e.jpeg)

## Tools
<a name="centralize-network-connectivity-using-aws-transit-gateway-tools"></a>

**AWS services**
+ [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you securely share your resources across your AWS accounts, organizational units, or your entire organization from AWS Organizations.
+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is a central hub that connects virtual private clouds (VPCs) and on-premises networks.

## Epics
<a name="centralize-network-connectivity-using-aws-transit-gateway-epics"></a>

### Create a transit gateway in the network services account
<a name="create-a-transit-gateway-in-the-network-services-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a transit gateway. | In the AWS account where you want to host network services, create a transit gateway in the target AWS Region. For instructions, see [Create a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#create-tgw). Note the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-network-connectivity-using-aws-transit-gateway.html) | Network administrator |

### Connect the transit gateway to your on-premises network
<a name="connect-the-transit-gateway-to-your-on-premises-network"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a customer gateway device for the VPN connection. | The customer gateway device is attached on the on-premises side of the Site-to-Site VPN connection between the transit gateway and your on-premises network. For more information, see [Your customer gateway device](https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html) in the AWS Site-to-Site VPN documentation. Identify or launch a supported on-premises customer device and note its public IP address. VPN configuration is completed later in this epic.  | Network administrator |
| In the network services account, create a VPN attachment to the transit gateway. | To set up a connection, create a VPN attachment for the transit gateway. For instructions, see [Transit gateway VPN attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html). | Network administrator |
| Configure the VPN on the customer gateway device in your on-premises network.  | Download the configuration file for the Site-to-Site VPN connection associated with the transit gateway and configure VPN settings on the customer gateway device. For instructions, see [Download the configuration file](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-download-config). | Network administrator |

### Share the transit gateway in the network services account to other AWS accounts or your organization
<a name="share-the-transit-gateway-in-the-network-services-account-to-other-aws-accounts-or-your-organization"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| In the AWS Organizations management account, turn on sharing. | To share the transit gateway with your organization or with certain organizational units, turn on sharing in AWS Organizations. Otherwise, you would need to share the transit gateway for each account individually. For instructions, see [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs). | AWS systems administrator |
| Create the transit gateway resource share in the network services account. | To allow VPCs in other AWS accounts within your organization to connect to the transit gateway, in the network services account, use the AWS RAM console to share the transit gateway resource. For instructions, see [Create a resource share](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-create). | AWS systems administrator |

### Connect VPCs to the transit gateway
<a name="connect-vpcs-to-the-transit-gateway"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create VPC attachments in individual accounts.  | In the accounts to which the transit gateway has been shared, create transit gateway VPC attachments. For instructions, see [Create a transit gateway attachment to a VPC](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#create-vpc-attachment). | Network administrator |
| Accept the VPC attachment requests. | In the network services account, accept the transit gateway VPC attachment requests. For instructions, see [Accept a shared attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#tgw-accept-shared-attachment). | Network administrator |

### Configure routing
<a name="configure-routing"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure routes in individual account VPCs. | In each individual account VPC, add routes to the on-premises network and to other VPC networks, using the transit gateway as the target. For instructions, see [Add and remove routes from a route table](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithRouteTables.html#AddRemoveRoutes). | Network administrator |
| Configure routes in the transit gateway route table. | Routes from VPCs and the VPN connection should be propagated and should appear in the transit gateway default route table. If needed, create any static routes (one example is static routes for the static VPN connection) in the transit gateway default route table. For instructions, see [Create a static route](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#tgw-create-static-route). | Network administrator |
| Add security group and network access control list (ACL) rules. | For the EC2 instances and other resources in the VPC, ensure that the security group rules and the network ACL rules allow traffic between VPCs as well as the on-premises network. For instructions, see [Control traffic to resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#AddRemoveRules) and [Add and delete rules from an ACL](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#Rules). | Network administrator |

### Test connectivity
<a name="test-connectivity"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test connectivity between VPCs. | Ensure that network ACL and security groups allow Internet Control Message Protocol (ICMP) traffic, and then ping from instances in a VPC to another VPC that is also connected to the transit gateway. | Network administrator |
| Test connectivity between VPCs and the on-premises network. | Ensure that network ACL rules, security group rules, and any firewalls allow ICMP traffic, and then ping between the on-premises network and the EC2 instances in the VPCs. Network communication must be initiated from the on-premises network first to bring the VPN connection to `UP` status. | Network administrator |

## Related resources
<a name="centralize-network-connectivity-using-aws-transit-gateway-resources"></a>
+ [Building a scalable and secure multi VPC AWS Network Infrastructure](https://d1.awsstatic.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure.pdf) (AWS whitepaper)
+ [Working with shared resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with.html) (AWS RAM documentation)
+ [Working with transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-transit-gateways.html) (AWS Transit Gateway documentation)
