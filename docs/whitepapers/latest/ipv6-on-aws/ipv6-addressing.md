---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/ipv6-addressing.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# IPv6 addressing
<a name="ipv6-addressing"></a>

 The IPv6 address space is organized by using format prefixes, that logically divide it in the form of a tree so that a route from one network to another can easily be found.

 The main categories of IPv6 addresses are:
+  Aggregatable global unicast addresses (GUA) — `2000::/3`
+  Unique-local unicast addresses (ULA) — `FC00::/7`
+  Link-local unicast addresses — `FE80::/10`
+  Multicast addresses — `FF00::/8`

 Note that the rest of the IPv6 addresses are reserved by the IETF (Internet Engineering Task Force) and may be used for new technologies or to augment these space allocations in the future.
