---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/connect.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connect
<a name="connect"></a>

 There are three primary methods for connecting to AWS with Direct Connect:
+  Physical cross-connect
+  Carrier interconnection
+  Data center interconnection

## Physical cross-connect
<a name="physical-cross-connect"></a>

 First, we’ll discuss using a physical cross-connect to establish a network connection from your premises to an AWS Region. This topology utilizes a partner in the AWS Direct Connect Partner Program to establish network circuits between an AWS Direct Connect point-of-presence (POP) and your data center, office, or colocation environment.

![Reference architecture for a physical cross-connect to Direct Connect.](http://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/images/physical-cross-connect.png)

 As indicated by the numbers on the diagram:

1.  **Connections** — Create a *connection* in an AWS Direct Connect Point of Presence (POP) to establish a network connection from your premises to an [AWS Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).

1.  **AWS Direct Connect location (DX POP)** — Work with a partner in the [AWS Direct Connect Partner Program](https://aws.amazon.com/directconnect/partners/?partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc&awsf.partner-solutions-filter-location=*all) to help you establish network circuits between an AWS Direct Connect POP and your data center, office, or colocation environment. The Partner can also help provide collocation space within the same facility as the POP location.
+  **Port speed** — The possible values are one Gbps, 10 Gbps, and 100 Gbps. You cannot change the port speed after you create the connection request. To change the port speed, you must create and configure a new connection.

### Customer router requirements
<a name="customer-router-requirements"></a>

 The interface must use single-mode fiber with a 1000BASE-LX (1310 nm) transceiver for 1 gigabit ethernet, a 10GBASE-LR (1310 nm) transceiver for 10 gigabits, or a 100GBASE-LR4 for 100 gigabit ethernet. Auto-negotiation for a port must be disabled for a connection with a port speed of more than one Gbps. However, depending on the AWS Direct Connect endpoint serving your connection, auto-negotiation might need to be enabled or disabled for one Gbps connections.

## Carrier interconnection
<a name="carrier-interconnection"></a>

 Next, we’ll discuss using carrier interconnection to establish a network connection from your premises to an AWS Region. This topology uses existing WAN services, such as Multiprotocol Label Switching, or MPLS, to provide the connection between your data center, office, or colocation environment to AWS.

![Reference architecture for carrier interconnection to Direct Connect.](http://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/images/carrier-interconnection.png)

 As indicated by the numbers on the diagram:

1.  **Connections** — Create a connection with an independent service provider (carrier) to establish a network connection from your premises to an AWS Region. In this case, the carrier will provide a virtual network connection (VLAN) to AWS using the existing WAN service (such as Multiprotocol Label Switching, or MPLS). Customers choosing this method of connection will usually already have a carrier service that has the option for virtual onramp service to AWS.

    Examples of carriers that can provide this service are:
   +  AT&T with Netbond
   +  Verizon with Software Defined Interconnect
   +  CenturyLink with Cloud Connect

1.  **Port speed** — You will subscribe to a port speed from the carrier. Although AWS Direct Connect is fixed at 1 Gbps, 10 Gbps, or 100 Gbps, carriers can provide a variety of different speeds over the existing WAN connection.

## Data center interconnection
<a name="data-center-interconnection"></a>

 Finally, we’ll discuss using a data center interconnection to establish a network connection from your premises to an AWS Region. This topology utilizes a physical connection in a data center to a private network and virtual network connection, or VLAN, to AWS.

![Reference architecture for data center interconnection to Direct Connect.](http://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/images/data-center-interconnection.png)

 As indicated by the numbers on the diagram:

1.  **Connections** — Create a connection with an independent service provider (data center) to establish a network connection from your premises to an AWS Region. In this case, the data center will provide a physical connection to their private network and a virtual network connection (VLAN) to AWS. Customers choosing this method of connection generally will already have a presence in a data center that provides private onramp service to AWS.

    Examples of data centers that can provide this service are:
   +  Equinix with Equinix Cloud Exchange
   +  Switch with Switch Cloud Platform

1.  **Port speed** — You will subscribe to a port speed from the data center. Although AWS Direct Connect is fixed at 1 Gbps, 10 Gbps, or 100 Gbps, data centers can provide a variety of different speeds over their private network connections.
