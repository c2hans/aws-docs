---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/scope-bgp-communities.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Scope BGP communities
<a name="scope-bgp-communities"></a>

 You can apply BGP community tags on the public prefixes that you advertise to Amazon to indicate how far to propagate your prefixes in the Amazon network for:
+  The local AWS Region only,
+  All Regions within a continent, or
+  All AWS Regions.

 You can use the following BGP communities for your prefixes:
+  7224:9100—Region (local AWS Region)
+  7224:9200—Continental (all AWS Regions for a continent)
  +  North America
  +  Asia Pacific
  +  Europe, the Middle East, and Africa
+  7224:9300—Global (all public AWS Regions)

**Note**
 If you do not apply any community tags, prefixes are advertised to all public AWS Regions (globally) by default.

 The communities 7224:1—7224:65535 are reserved by AWS Direct Connect.

 AWS Direct Connect applies the following BGP communities to its advertised routes:
+  7224:8100—Routes that originate from the same AWS Region in which the AWS Direct Connect point of presence is associated
+  7224:8200—Routes that originate from the same continent with which the AWS Direct Connect point of presence is associated
+  No tag—Global (all public AWS Regions)

 Communities that are not supported for an AWS Direct Connect public connection are removed.

**Note**
 If you do not apply any community tags, all AWS public IP addresses will be advertised into the customer network. Apply tags to limit the exposure into your network.

![Reference diagram of advertising BGP Community Tags using Direct Connect.](http://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/images/bgp-community-tags.png)

1.  **Customer-advertised IP prefixes** – Public prefixes advertised to Amazon network

1.  **AWS-advertised public addresses** – AWS public service IP addresses advertised over BGP

 When you're using AWS Direct Connect to access public AWS services, you must specify the public IPv4 prefixes or IPv6 prefixes (where applicable) to advertise over BGP.

 The following inbound routing policies apply:
+  You must own the public prefixes, and they must be registered as such in the appropriate Regional internet registry.
+  Traffic must be destined to Amazon public prefixes. Transitive routing between connections is not supported.
+  AWS Direct Connect performs inbound packet filtering to validate that the source of the traffic originated from your advertised prefix.

 The following outbound routing policies apply:
+  `AS_PATH` and [longest prefix match](https://en.wikipedia.org/wiki/Longest_prefix_match) is used to determine the routing path, and AWS Direct Connect is the preferred path for traffic sourced from Amazon.
+  AWS Direct Connect advertises all local and remote AWS Region prefixes where available, and includes on-net prefixes from other AWS non-Region points of presence (POP) where available: for example, [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and [Amazon Route 53](https://aws.amazon.com/route53/).
+  AWS Direct Connect advertises prefixes with a minimum path length of three.
+  AWS Direct Connect advertises all public prefixes with the well-known `NO_EXPORT` BGP community.
+  If you have multiple AWS Direct Connect connections, you can adjust the load sharing of inbound traffic by advertising prefixes with similar path attributes.
+  The prefixes advertised by AWS Direct Connect must not be advertised beyond the network boundaries of your connection. For example, these prefixes must not be included in any public internet routing table.
+  AWS Direct Connect keeps prefixes advertised by customers within the Amazon network. AWS does not re-advertise customer prefixes learned from a public virtual interface (VIF) to any of the following:
  +  Other AWS Direct Connect customers
  +  Networks that peer with the AWS Global Network
  +  Amazon's transit providers

![Reference diagram of public VIF routing of Amazon Connect traffic using Direct Connect.](http://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/images/public-vif-routing.png)

 As indicated by the number on the diagram:

1.  **Connections** – Direct Connect routing of Amazon Connect traffic
