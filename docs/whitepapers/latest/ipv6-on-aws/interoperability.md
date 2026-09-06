---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/interoperability.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Interoperability
<a name="interoperability"></a>

 Although operating in dual-stack mode solves a lot of the problems with IPv4 and IPv6 interoperability, it creates management overhead. For example, security becomes harder because you have to manage two sets of security rules, one for each network stack. Routing and troubleshooting become harder, and you have to maintain additional records to existing DNS names.

 You may be able to avoid making the entire network dual-stack by focusing on implementing dual-stack at your border via load balancers. Existing segments of your network can continue to operate as IPv4 in most cases, and new segments are built with IPv6. Focus on implementing and operating interoperability layer where AWS services such as dual-stack VPC and load balancers, to help you solve interoperability challenges.

 The adoption of IPv6-only subnets in dual-stack VPCs enables you to expand and grow your network beyond the limited capabilities of the IPv4 space, and interoperability is ensured by the cloud-native Amazon VPC NAT Gateway with NAT64 and DNS64 integration.
