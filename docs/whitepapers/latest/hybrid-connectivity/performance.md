---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/performance.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Performance
<a name="performance"></a>

## Definition
<a name="definition-perf"></a>

 There are multiple factors which influence network performance, such as latency, packet loss, jitter, and bandwidth. Depending on application requirements, the importance of each of these factors can vary.

## Key questions
<a name="key-questions-perf"></a>

 Based on your application requirements, you need to identify and prioritize the network performance factors that impact your application behavior and user experience.

### Bandwidth
<a name="bandwidth"></a>

 *Bandwidth* refers to the data transfer rate of a connection, and is usually measured in bits per second (bps). Megabits per second (Mbps) and gigabits per second (Gbps) are common scaling, and are base 10 (1,000,000 bits per second = 1 Mbps) as opposed to base 2 (2^10) seen elsewhere.

 When evaluating the bandwidth needs of applications, keep in mind that the bandwidth requirements can change over time. Initial deployment into the cloud, normal operations, new workloads, and failover scenarios can all have different bandwidth requirements.

 Applications can have their own bandwidth considerations. Some applications might require deterministic performance over a high-bandwidth connection, while others can require both deterministic performance and high bandwidth. An application may need special configuration to use multiple traffic flows (sometimes referred to as streams or sockets) in parallel if it is hitting per traffic flow bandwidth limits, allowing it to use more of the connection’s bandwidth. VPNs can limit throughput because of tunneling overheads, lower MTU limits, or hardware bandwidth limitations.

### Latency
<a name="latency"></a>

*Latency* is the time needed for a packet to go from source to destination over a network connection, and is usually measured in milliseconds (ms), with low latency requirements sometimes expressed in microseconds (μs). Latency is a function of the speed of light, hence latency increases with distance.

 Application latency requirements can take different forms. A highly interactive application, such as a virtual desktop, can have a latency target measured from when a user performs an input until the user sees the virtual desktop react to that input. Voice over IP (VoIP) applications can have similar requirements. A second type of workload to consider are ones that are highly transactional, needing a response from the server before they can continue. Databases or other forms of key/value stores can be highly impacted by increased network latency.

### Jitter
<a name="jitter"></a>

*Jitter* measures how consistent the network latency is, and, like latency, is usually measured in milliseconds (ms).

 Application jitter requirements are typically found in real time streaming applications, including video and voice delivery. These applications tend to require their data flow to be at a consistent rate and delay, with small buffers to correct for small amounts of jitter.

### Packet loss
<a name="packet-loss"></a>

*Packet loss* is the measurement of what percentage of network traffic is not delivered. All networks have some degree of packet loss at times due to high traffic bursts, capacity reductions, network equipment failures, and other reasons. Thus, applications must have some tolerance of packet loss, however, how much they can tolerate can vary from application to application.

 Applications that use TCP to transport their traffic have the ability to correct for packet loss via retransmission. Applications that use UDP or their own protocols on top of IP need to implement their own means of handling packet loss, and may be highly sensitive to it. A voice over IP application may simply insert silence into the part of the call that had the packet loss, as opposed to attempting a retransmit. Some VPN solutions include their own mechanisms for recovering from packet loss on the network they are using to carry traffic.

## Capabilities to consider
<a name="capabilities-to-consider-perf"></a>

 When predictable latency and throughput are required, AWS Direct Connect is the recommended choice, as it provides deterministic performance. Bandwidth can be selected based on throughput requirements. AWS recommends using AWS Direct Connect when you require a more consistent network experience than internet-based connections can provide. Private VIFs and Transit VIFs support jumbo frames, which can reduce the number of packets through the network and can improve throughput due to reduced overhead. AWS Direct Connect [SiteLink](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-direct-connect-sitelink/) allows using the AWS backbone to provide connectivity between your locations and can be enabled on demand. Bandwidth used for SiteLink should be taken into account for your Direct Connect bandwidth selection.

 Using a VPN over AWS Direct Connect adds encryption. However, it reduces the MTU size which might reduce throughput. AWS managed Site-to-Site (S2S) VPN capabilities can be found in the [AWS Site-to-Site VPN documentation](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html). Many Direct Connection locations support MACsec if encryption over your connection is the primary encryption requirement. MACsec does not have the same MTU or potential throughput considerations of Site-to-Site VPN connections. AWS Transit Gateway allows customers to horizontally scale the number of VPN connections and raise throughput accordingly with Equal-cost multi-path routing (ECMP). AWS’s managed Site-to-Site VPN supports using Direct Connect transit VIFs for private connectivity – see the [Private IP VPN with AWS Direct Connect](https://docs.aws.amazon.com/vpn/latest/s2svpn/private-ip-dx.html) for details.

 Another option is to use an AWS managed Site-to-Site VPN over the internet. It can be an attractive option due to low cost and is widely available. However, keep in mind that performance over the internet is best effort. Internet weather events, congestion, and increased latency periods can be unpredictable. AWS offers a solution with [AWS Accelerated S2S VPN](https://aws.amazon.com/blogs/architecture/improve-vpn-network-performance-of-aws-hybrid-cloud-with-global-accelerator/), which can mitigate some of the downsides of using an internet path. Accelerated S2S VPN uses AWS Global Accelerator, which allows VPN traffic to enter the AWS network as early and as close as possible to the customer gateway device. This optimizes the network path, using the congestion-free AWS global network, to route traffic to the endpoint that provides the best performance. You can use accelerated VPN connections to avoid network disruptions that can occur when traffic is routed over the public internet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
