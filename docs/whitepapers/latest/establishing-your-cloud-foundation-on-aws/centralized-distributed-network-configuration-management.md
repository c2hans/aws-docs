---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/centralized-distributed-network-configuration-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Centralized or distributed network configuration and management
<a name="centralized-distributed-network-configuration-management"></a>

 As you build your network, you need to decide between distributed and centralized networking components for your organization. When starting distributed networks or Full Mesh routing solutions with smaller networks, on-premises sites, and cloud providers network may help reduce complicated point to point communication. However, as the network grows, and the number of nodes increases, the number of connections between the nodes increases the complexity for the network management introducing scalability challenges. Hub and spoke network topologies offer a different set of advantages over point to point communication links. Centralized networks (hub and spoke networks) allow you to inspect all your traffic in one point, controlling ingress and egress traffic from your environment, and simplify the management of the connections. Hub and spoke networks offer larger scalability over new links, and they offer centralized control over spoke sites. With these kinds of tools, you can centrally control access to public and private networks, restrict users access to resources over LAN and WIFI networks, control the addition and deletion of routing components, and simplify the modification of the logical divisions within your network (VLAN, VRFs, and so on).
