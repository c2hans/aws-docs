---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_LoadBalancer.html
---

# LoadBalancer
<a name="API_LoadBalancer"></a>

Information about a load balancer.

## Contents
<a name="API_LoadBalancer_Contents"></a>

 ** AvailabilityZones.member.N **
The subnets for the load balancer.
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects
Required: No

 ** CanonicalHostedZoneId **
The ID of the Amazon Route 53 hosted zone associated with the load balancer.
Type: String
Required: No

 ** CreatedTime **
The date and time the load balancer was created.
Type: Timestamp
Required: No

 ** CustomerOwnedIpv4Pool **
[Application Load Balancers on Outposts] The ID of the customer-owned address pool.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(ipv4pool-coip-)[a-zA-Z0-9]+$`
Required: No

 ** DNSName **
The public DNS name of the load balancer.
Type: String
Required: No

 ** EnablePrefixForIpv6SourceNat **
[Network Load Balancers with UDP listeners] Indicates whether to use an IPv6 prefix from each subnet for source NAT. The IP address type must be `dualstack`. The default value is `off`.
Type: String
Valid Values: `on | off`
Required: No

 ** EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic **
Indicates whether to evaluate inbound security group rules for traffic sent to a Network Load Balancer through AWS PrivateLink.
Type: String
Required: No

 ** IpAddressType **
The type of IP addresses used for public or private connections by the subnets attached to your load balancer.
[Application Load Balancers] The possible values are `ipv4` (IPv4 addresses), `dualstack` (IPv4 and IPv6 addresses), and `dualstack-without-public-ipv4` (public IPv6 addresses and private IPv4 and IPv6 addresses).
[Network Load Balancers and Gateway Load Balancers] The possible values are `ipv4` (IPv4 addresses) and `dualstack` (IPv4 and IPv6 addresses).
Type: String
Valid Values: `ipv4 | dualstack | dualstack-without-public-ipv4`
Required: No

 ** IpamPools **
[Application Load Balancers] The IPAM pool in use by the load balancer, if configured.
Type: [IpamPools](API_IpamPools.md) object
Required: No

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: No

 ** LoadBalancerName **
The name of the load balancer.
Type: String
Required: No

 ** Scheme **
The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.
The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.
Type: String
Valid Values: `internet-facing | internal`
Required: No

 ** SecurityGroups.member.N **
The IDs of the security groups for the load balancer.
Type: Array of strings
Required: No

 ** State **
The state of the load balancer.
Type: [LoadBalancerState](API_LoadBalancerState.md) object
Required: No

 ** Type **
The type of load balancer.
Type: String
Valid Values: `application | network | gateway`
Required: No

 ** VpcId **
The ID of the VPC for the load balancer.
Type: String
Required: No

## See Also
<a name="API_LoadBalancer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/LoadBalancer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/LoadBalancer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/LoadBalancer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
