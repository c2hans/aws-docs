---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/amazon-vpc-internet-access.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon VPC internet access
<a name="amazon-vpc-internet-access"></a>

## Internet reachable IPv6 resources
<a name="internet-reachable-ipv6-resources"></a>

 As previously stated, elastic network interfaces retain their IPv6 addresses throughout their lifetime. For IPv4, elastic network interfaces can have zero or more Elastic IP addresses associated with them. An Elastic IP address defines a static 1:1 NAT relationship between an elastic network interface’s IPv4 address and a public internet-routable address.

![This is a diagram that illustrates internet access for a VPC public subnet.](https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/internet-access-for-a-vpc-public-subnet.png)

 In IPv6, VPC addressing is already globally unique, and therefore Elastic IP addresses are not required. Amazon assigned IPv6 addresses are automatically publicly advertised whereas for BYOIP ranges this is optional. In either case, resources deployed only have IPv6 internet reachability if their subnet’s routing table contains IPv6 destinations (such as `::/0`) via either an internet gateway or outbound traffic-only internet gateway.

![This is a diagram that illustrates internet access from a VPC private subnet.](https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/images/internet-access-from-a-vpc-private-subnet.png)
