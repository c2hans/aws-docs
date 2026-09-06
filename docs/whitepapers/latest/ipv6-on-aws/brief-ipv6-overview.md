---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/brief-ipv6-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Brief IPv6 overview
<a name="brief-ipv6-overview"></a>

 The Internet Layer of the TCP/IP model aligns with the Layer 3 (Network) of the Open Systems Interconnection model (OSI model) and is used for transmitting data between the two nodes communicating over the IP. The IPv4 addressing scheme, with a 32-bit address field, provides around 4,000,000,000 possible addresses, which cannot fulfill the task of addressing the rapidly increasing number of the hosts on the internet.

 IPv6 offers the following significant features:
+  A larger address space — 128-bit long addresses vs 32-bit long addresses in IPv4
+  A large block of globally unique and hierarchically assigned addresses, based on prefixes rather than address classes, to keep routing tables small and backbone routing efficient
+  A mechanism for the auto-configuration of network interfaces
+  Support for encapsulation of itself and other protocols
+  A class of service that distinguishes types of data
+  Improved multicast routing capabilities (in preference to broadcasting)
+  Built-in authentication and encryption
+  Methods to adopt IPv6 and maintain interoperability with IPv4

 IPv6 uses the term node for any system that runs IPv6; that is, a host or a router. An IPv6 host is a node that does not forward IPv6 packets that are not explicitly addressed to it. A router is a node that forwards IP packets not addressed to it. Some considerations regarding the main differences between IPv4 and IPv6 follow:
+  **Headers** — IPv6 uses two distinct types of headers:
  +  Main/regular IPv6 header
  +  IPv6 extension headers

   The main IPv6 header is equivalent to the basic IPv4 version, despite some field differences that are the result of lessons learned from operating IPv4. IPv6 has a fixed 40-byte header that allows for faster processing of IP datagram.
+  **Flow labeling** — Flow labeling is a new field used by a node to label packets of a flow. A flow label of ‘0’ (zero) is used to indicate that packets have not been labeled. Packet classifiers can use the flow label, source address, and destination address fields to identify to which flow the packet belongs. Packets are processed in a flow-specific way by the nodes that are able to do it in a stateless manner or that have been set up with a flow-specific state.
+  **Address assignment** — IPv6 address can be assigned statically, using DHCPv6 and through Stateless Address Auto-Config (SLAAC), which makes use of the Media Access Control (MAC) address of the network interface to derive an IPv6 address for the node.
+  **Error correction** — IPv6 does not support header checksum capability, as it considered redundant, being processed both at the lower layer protocol (Ethernet) and upper layer protocols (TCP/UDP).
+  **Neighbor Discovery Protocol** — IPv6 defines Internet Control Message Protocol v6 (ICMPv6) messages to take the place of IPv4's ARP and other network discovery functions. It provides many improvements over IPv4, which includes Neighbor Unreachability Detection (NUD), improving packet delivery in the presence of failing routers, links, or mobile nodes.
