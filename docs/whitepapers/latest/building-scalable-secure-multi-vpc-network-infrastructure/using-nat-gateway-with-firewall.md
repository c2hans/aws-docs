---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/using-nat-gateway-with-firewall.html
---

# Using the NAT gateway with AWS Network Firewall for centralized IPv4 egress
<a name="using-nat-gateway-with-firewall"></a>

If you want to inspect and filter your outbound traffic, you can incorporate AWS Network Firewall with NAT gateway in your centralized egress architecture. AWS Network Firewall is a managed service that makes it easy to deploy essential network protections for all of your VPCs. It provides control and visibility to Layer 3-7 network traffic for your entire VPC. You can do URL/domain name, IP address, and content-based outbound traffic filtering to stop possible data loss, help meet compliance requirements, and block known malware communications. AWS Network Firewall supports thousands of rules that can filter out network traffic destined for known bad IP addresses or bad domain names. You can also use Suricata IPS rules as part of the AWS Network Firewall service by importing open-source rulesets or authoring your own Intrusion Prevention System (IPS) rules using Suricata rule syntax. AWS Network Firewall also allows you to import compatible rules sourced from AWS partners.

In the centralized egress architecture with inspection, the AWS Network Firewall endpoint is a default route table target in the transit gateway attachments subnet route table for the egress VPC. Traffic between spoke VPCs and the internet is inspected using AWS Network Firewall as shown in the following diagram.

![A diagram depicting centralized egress with AWS Network Firewall and NAT gateway (route table design)](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/centralized-egress-rt.png)

For centralized deployment model with Transit Gateway, AWS recommends deploying AWS Network Firewall endpoints in multiple Availability Zones. There should be one firewall endpoint in each Availability Zone the customer is running workloads in, as shown in the preceding diagram. As a best practice, the firewall subnet should not contain any other traffic because AWS Network Firewall is not able to inspect traffic from sources or destinations within a firewall subnet.

Similar to the previous setup, spoke VPC attachments are associated with Route Table 1 (RT1) and are propagated to Route Table 2 (RT2). A Blackhole route is explicitly added to disallow the two VPCs from communicating with each other.

Continue to use a default route in RT1 pointing all traffic to egress VPC. Transit Gateway will forward all traffic flows to one of the two availability zones in the egress VPC. Once traffic reaches one of Transit Gateway ENIs in the egress VPC, you hit a default route which will forward traffic to one of the AWS Network Firewall endpoints in their respective availability zone. AWS Network Firewall will then inspect traffic based on the rules you set before forwarding traffic to the NAT gateway using a default route.

This case doesn’t require Transit Gateway appliance mode, because you aren’t sending traffic between attachments.

**Note**
AWS Network Firewall does not perform network address translation for you, this function would be handled by the NAT gateway after traffic inspection through the AWS Network Firewall. Ingress routing is not required in this case as return traffic will be forwarded to the NATGW IPs by default.

Because you are using a Transit Gateway, here we can place the firewall prior to NAT gateway. In this model, the firewall can see the source IP behind the Transit Gateway.

If you were doing this in a single VPC, we can use the VPC routing enhancements that allow you to inspect traffic between subnets in the same VPC. For details, refer to the [Deployment models for AWS Network Firewall with VPC routing enhancements](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall-with-vpc-routing-enhancements/) blog post.

## Scalability
<a name="scalability-2"></a>

AWS Network Firewall can automatically scale firewall capacity up or down based on traffic load to maintain steady, predictable performance to minimize costs. AWS Network Firewall is designed to support tens of thousands of firewall rules and can scale up to 100 Gbps throughput per Availability Zone.

## Key considerations
<a name="key-considerations-1"></a>
+ Each firewall endpoint can handle about 100 Gbps of traffic, if you require higher burst or sustained throughput, contact [AWS support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html).
+ If you choose to create a NAT gateway in your AWS account along with Network Firewall, standard NAT gateway processing and per-hour usage [charges](https://aws.amazon.com/network-firewall/pricing/) are waived on a one-to-one basis with the processing per GB and usage hours charged for your firewall.
+ You can also consider distributed firewall endpoints through AWS Firewall Manager without a Transit Gateway.
+ Test firewall rules before moving them to production, similar to a network access control list, as order matters.
+ Advanced Suricata rules are required for deeper inspection. Network firewall supports encrypted traffic inspection for ingress as well as egress traffic.
+ The `HOME_NET` rule group variable defined the source IP range eligible for processing in the Stateful engine. Using a centralized approached, you must add all additional VPC CIDRs attached to the Transit Gateway to make them eligible for processing. Refer to the [Network Firewall documentation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-domain-names.html) for more details on the `HOME_NET` rule group variable.
+ Consider deploying Transit Gateway and egress VPC in a separate Network Services account to segregate access based on delegation of duties; for example, only network administrators can access the Network Services account.
+  To simplify deployment and management of AWS Network Firewall in this model, AWS Firewall Manager can be used. Firewall Manager allows you to centrally administer your different firewalls by automatically applying protection you create in the centralized location to multiple accounts. Firewall Manager supports both distributed and centralized deployment models for Network Firewall. To learn more, see the blog post [How to deploy AWS Network Firewall by using AWS Firewall Manager](https://aws.amazon.com/blogs/security/how-to-deploy-aws-network-firewall-by-using-aws-firewall-manager/).
