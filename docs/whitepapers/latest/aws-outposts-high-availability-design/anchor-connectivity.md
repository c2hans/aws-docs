---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/anchor-connectivity.html
---

# Anchor connectivity
<a name="anchor-connectivity"></a>

 An [Outpost service link](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html) connects to either public or private anchors (not both) in a specific Availability Zone (AZ) in the Outpost’s parent Region. Outpost servers initiate outbound service link VPN connections from their service link IP addresses to the anchor points in the anchor AZ. These connections use UDP and TCP port 443. AWS is responsible for the availability of the anchor points in the Region.

 You must ensure the Outpost service link IP addresses can connect through your network to the anchor points in the anchor AZ. The service link IP addresses do not need to communicate with other hosts on your on-premises network.

 Public anchor points reside in the Region’s [public IP ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) (in the EC2 service CIDR blocks) and may be accessed via the internet or [AWS Direct Connect](https://aws.amazon.com/directconnect/) (DX) public virtual interfaces (VIFs). The use of public anchor points allows for more flexible path selection as service link traffic may be routed over any available path that can successfully reach the anchor points on the public internet.

 Private anchor points allow you to use your IP address ranges for anchor connectivity. Private anchor points are created in a [private subnet within a dedicated VPC](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html#private-connectivity) using customer-assigned IP addresses. The VPC is created in the AWS account that owns the Outpost resource and you are responsible for ensuring the VPC is available and properly configured. Use a Security Control Policy (SCP) in AWSOrigamiServiceGateway Organizations to prevent users from deleting that Virtual Private Cloud (VPC).Private anchor points must be accessed using [Direct Connect private VIFs](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-outposts-private-connectivity/).

 You should provision redundant network paths between the Outpost and the anchor points in the Region with connections terminating on separate devices in more than one location. Dynamic routing should be configured to automatically reroute traffic to alternate paths when connections or networking devices fail. You should provision sufficient network capacity to ensure that the failure of one WAN path does not overwhelm the remaining paths.

 The following diagram shows three Outposts with redundant network paths to their anchor AZs using AWS Direct Connect as well as public internet connectivity. Outpost A and Outpost B are anchored to different Availability Zones in the same Region. Outpost A connects to private anchor points in AZ 1 of region 1. Outpost B connects to public anchor points in AZ 2 of region 1. Outpost C connects to public anchors in AZ 1 of region 2.

![Diagram showing Highly available anchor connectivity with AWS Direct Connect and public internet access](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/highly-available-anchor-connectivity.png)

 Outpost A has three redundant network paths to reach its private anchor point. Two paths are available through redundant Direct Connect circuits at a single Direct Connect location. The third path is available through a Direct Connect circuit at a second Direct Connect location. This design keeps Outpost A’s service link traffic on private networks and provides path redundancy that allows for failure of any one of the Direct Connect circuits or failure of an entire Direct Connect location.

 Outpost B has four redundant network paths to reach its public anchor point. Three paths are available through public VIFs provisioned on the Direct Connect circuits and locations used by Outpost A. The fourth path is available through the customer WAN and the public internet. Outpost B’s service link traffic may be routed over any available path that can successfully reach the anchor points on the public internet. Using the Direct Connect paths may provide more consistent latency and higher bandwidth availability, while the public internet path may be used for Disaster Recovery (DR) or bandwidth augmentation scenarios.

 Outpost C has two redundant network paths to reach its public anchor point. Outpost C is deployed in a different data center than Outposts A and B. Outpost C’s data center does not have dedicated circuits connecting to the customer WAN. Instead, the data center has redundant internet connections provided by two different Internet Service Providers (ISPs). Outpost C’s service link traffic may be routed over either of the ISP networks to reach the anchor points on the public internet. This design allows flexibility to route service link traffic over any available public internet connection. However, the end-to-end path is dependent on public third-party networks where bandwidth availability and network latency fluctuate.

 The network path between an Outpost and its service link anchor points must meet the following bandwidth specification:
+ 500 Mbps - 1 Gbps of available bandwidth per Outpost rack (for example, 3 racks: 1.5 – 3 Gbps available bandwidth)

## Recommended practices for highly available anchor connectivity
<a name="recommended-practices-for-highly-available-anchor-connectivity"></a>
+  Provision redundant network paths between each Outpost and its anchor points in the Region.
+  Use Direct Connect (DX) paths to control latency and bandwidth availability.
+  Ensure that TCP and UDP port 443 are open (outbound) from the Outpost Service Link CIDR blocks to the [EC2 IP address ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the parent Region. Ensure the ports are open on all network paths.
+ Keep track of the Amazon EC2 IP address ranges on your firewall if you are using a subset of CIDR ranges for the Region.
+  Ensure each path meets the bandwidth availability and latency requirements.
+  Use dynamic routing to automate traffic redirection around network failures.
+  Test routing the service link traffic over each planned network path to ensure the path functions as expected.
