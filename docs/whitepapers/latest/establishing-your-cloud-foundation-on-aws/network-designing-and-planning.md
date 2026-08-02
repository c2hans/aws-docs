---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/network-designing-and-planning.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Network designing and planning
<a name="network-designing-and-planning"></a>

Your workloads use IP addresses to communicate with each other, within your cloud environment, or in hybrid environments with resources outside your cloud environment. IP address management is an essential component for you to manage your network when you plan the different stages to deploy and operate your workloads. Without considering how your IP address space will be allocated, you run the risk of overlapping CIDRs and IP address exhaustion which can lead to network or service outages. Having a plan on where CIDR space will be allocated to will help you build your foundational environment to include support routing rules and route optimization.

## CIDRs
<a name="cidrs"></a>

In traditional on-premises networking you assign Classless Inter Domain Routing (CIDR) ranges to your LAN for private communication. Similarly, when creating networks in your cloud environment you also need to assign non-overlapping CIDR ranges to your network. Non-overlapping IP spaces allow you to build optimal routing that helps enhance your network performance and avoids intermittent connectivity issues and communication failures. There are cases were overlapping IP ranges cannot be avoided and it is important to design network routes or translation devices to ensure the communication between these networks performs as expected. When planning your network CIDR range, we recommend that you leverage a contiguous CIDR range for geographic regions, locations, or even services. By grouping your CIDRs you can classify or categorize them to help administrators easily identify and appropriately create routes.

## IP address utilization
<a name="ip-address-utilization"></a>

An important aspect of planning and designing your network is to ensure the risk of IP address exhaustion is mitigated. IP exhaustion happens when the number of IP addresses you need in a given network is greater than the IP addresses available. This is a big risk in the cloud environments due to the elasticity the cloud provides. As your workloads scale up and down, they consume more IP addresses in the given network. If there are no IPs available in your network, scaling will fail and you are at risk of having service impairment. When planning, you need to ensure that the IP range is large enough to accommodate networking and non-networking resources in your cloud environment. Addressing the size of the CIDR for current and future uses should be considered in planning.

## Virtual networks
<a name="virtual-networks"></a>

Virtual networks allow you to isolate resources from one another based on your operational requirements. Leveraging virtual networks enables your team to define a strict network boundary between resources, which can ensure network isolation and mitigate risk of resources in one virtual network from access resources in another virtual network. For example, developers can have separate networks to create and develop resources isolated from production workloads. Issues or risky activity developers are taking within one virtual network will not impact network resources within another virtual network. At this stage, you should gauge short- and long-term projects that might affect network topologies such as merging of organizations, large data center migrations, and adoption of new vendors or technologies. Network admins and leadership should be ready to define virtual networks and restructure sub-networks and routing, and switching and physical layer networking modifications to establish communication across their network.

## IPv4 and IPv6
<a name="ipv4-ipv6"></a>

Ever decreasing IPv4 space has posed challenges to IT and networking departments worldwide. The development of IPv6 is one of the most important advancement in networking technology. It not only solves the impending problem of IPv4 exhaustion, it simplifies routing, and provides an almost infinite pool of addresses which makes mobile networks and Internet of Things (IoT) devices easy to deploy and configure. IPv4 networks come with the challenges and complexities associated with planning a private network's IP schema. With the limited IPv4 space, a key design consideration is to decide how much space to allocate to a given application based on its requirements. Using IPv4 spaces often leads to the following design constraints:

1. Network architectures are designed too small, which requires you to expand the size of the network by adding new CIDR blocks to the network.

1. Network architectures are designed too large, which requires customers to accept overlapping IP, causing connectivity issues, and impacting the performance of the network.

IPv6 uses 128 bits instead of the IPv4 32 bits, which essentially eliminates any size considerations, allowing you to create unique IP addresses, to almost eliminate the overlapping concerns.

## Network configuration and management
<a name="network-configuration-management"></a>

The network is the backbone of any IT infrastructure. Whether its post deployment operational issues or troubleshooting, you often need to make changes to individual components in the network, resulting in changes to the overall topology. These changes include modifications of route tables, allocation of new private and public IP addresses, and troubleshooting (connectivity, packet loss, throughput, bandwidth consumption, or latency issues) within and outside each team’s resources and your organization. A robust network architecture reduces the needs to make major changes to your network topology when any of these scenarios are encountered.
