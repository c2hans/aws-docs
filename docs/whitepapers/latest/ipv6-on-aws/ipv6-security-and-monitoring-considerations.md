---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/ipv6-security-and-monitoring-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# IPv6 security and monitoring considerations
<a name="ipv6-security-and-monitoring-considerations"></a>

## Network-level access control
<a name="network-level-access-control"></a>

 Amazon VPCs feature two network access control mechanisms, and these exist irrespectively of which version of the IP protocol is used (IPv4 or IPv6):
+  Security groups (SGs) at the elastic network interface level
+  Network access control lists (network ACLs) at the subnet level

 **Security groups** — A security group acts as a stateful virtual firewall for your instance to control inbound and outbound traffic. Each elastic network interface must have at least one security group associated with it. As security groups default to deny all inbound flows, additional IPv6 inbound rules need to be created when operating IPv6. For example, a web server security group that currently permits `0.0.0.0/0` on port 80 doesn’t permit IPv6 traffic. For example, if you wanted to allow all IPv6 traffic you would need an additional rule allowing traffic from `::/0`.

 **Network access control lists** — Network ACLs differ from security groups in several ways:
+  They are applied to VPC subnet instead of individual elastic network interface
+  They are stateless
+  They can have explicit `DENY` added to them
+  They default to `ALLOW ANY` for both inbound and outbound connectivity

 As a result of the last point, you don’t need to update default network ACLs to enable IPv6 connectivity explicitly.

## VPC Flow Logs
<a name="vpc-flow-logs"></a>

 VPC Flow Logs is a feature that enables you to capture information about the IPv6 traffic going to and from network interfaces in your VPC. VPC Flow Logs for IPv6 traffic works the same as IPv4 where you can create flow logs at the VPC level, the subnet level, or the network interface level. If you create VPC Flow Logs at a VPC or subnet level, every network interface in that VPC or subnet is monitored.

 The flow log records can use the *default format* or the *custom format*. With a custom format, you specify which fields are included in the IPv6 flow log records and in which order.

 Following is an example of a flow log record for IPv6 traffic using the default format. This is an example, of a default format capture for an ICMP ping traffic from `2406:da1c:491:7402:60ee:a99b:749c:c248` to `2406:da1c:491:7402:4427:239a:8656:4f3a` that was permitted.

**Table — VPC Flow Logs default format**

|  Field |  Example |
| --- | --- |
|  version  |  2  |
|  account-id  |  944045752502  |
|  interface-id  |  eni-0237699701b6463ba  |
|  srcaddr  |  2406:da1c:491:7402:60ee:a99b:749c:c248  |
|  dstaddr  |  2406:da1c:491:7402:4427:239a:8656:4f3a  |
|  srcport  |  0  |
|  dstport  |  0  |
|  protocol  |  58  |
|  packets  |  6  |
|  bytes  |  624  |
|  start  |  1621949678  |
|  end  |  1621949738  |
|  action  |  ACCEPT  |
|  log-status  |  OK  |

Note that if a network interface has multiple IPv6 addresses and traffic is sent to a secondary private IPv6 address, the VPC flow log displays the primary private IPv6 address if you simply use the default format `dstaddr` field.

 To capture the original destination IPv6 address, you can use a custom format flow log with the `pkt-dstaddr` field. It applies the same for `pkt-srcaddr` field. For other flow log considerations, refer to [Flow log limitations](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-logs-limitations).

 Flow log data can be published to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html) or [Amazon Simple Storage Service](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html) (Amazon S3).

### VPC Traffic Mirroring
<a name="vpc-traffic-mirroring"></a>

 VPC Traffic Mirroring is a complementary feature to flow logs that copies entire packets, including their payload of network traffic from a specified elastic network interface of an Amazon EC2 instance. Traffic Mirroring copies inbound and outbound IPv4 and IPv6 traffic from the network interfaces that are attached to your Amazon EC2 instances. You can send the mirrored traffic to the network interface of another EC2 instance, or a Network Load Balancer that has a UDP listener (listening on UDP port 4789 - `VXLAN`).

 The mirrored traffic is sent to the traffic mirror target by means of the source VPC IPv4 route table. Note that all mirrored traffic is encapsulated in an IPv4 packet. Traffic Mirroring mirrors both your IPv4 and IPv6 traffic. No special configuration is necessary to enable Traffic Mirroring for your IPv6 traffic, whether the traffic mirror source and the target are in the same VPC, or in a different VPC connected via VPC peering or a Transit Gateway (as long as the traffic mirror source can route to the traffic mirror target by IPv4).

## AWS Web Application Firewall
<a name="aws-web-application-firewall"></a>

 [AWS Web Application Firewall](https://aws.amazon.com/waf/) (AWS WAF) lets you monitor the HTTP(S) requests that are forwarded to an Amazon CloudFront distribution, an Amazon API Gateway REST API, an Application Load Balancer, or an AWS AppSync GraphQL API. With AWS WAF, the services that are associated with the protected resources can respond either with the requested content or with HTTP 403 status code based on conditions that are specified, such as the IP addresses (either IPv4 or IPv6) that the request originate from.

### Web ACL
<a name="web-acl"></a>

 You use the rules in a web ACL to block or allow web requests based on criteria which includes IP addresses or address ranges (either IPv4 or IPv6 addresses as specified in the IP set) that requests originate from. The IP set match statement inspects the IP address of a web request against a set of IP addresses and address ranges. Use this to allow or block web requests based on the IP addresses (either IPv4 or IPv6) that the requests originate from. AWS WAF IP sets supports all IPv4 and IPv6 CIDR ranges except for `0.0.0.0/0` and ::`/0`.

## AWS Shield
<a name="aws-shield"></a>

 [AWS Shield Standard and AWS Shield Advanced](https://aws.amazon.com/shield/features/) provides protection against DDoS attacks. A DDoS attack can prevent legitimate users from accessing a service and can cause the system to crash due to the overwhelming traffic volume. All of the AWS Shield detection and mitigations work with IPv4 and IPv6 without any impact to performance, scalability, or availability of the service.

## AWS Network Firewall
<a name="aws-network-firewall"></a>

[AWS Network Firewall](https://aws.amazon.com/network-firewall/) is a stateful, managed, network firewall and intrusion detection and prevention service for [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC). With this capability, you can enable AWS Network Firewall endpoints to filter both IPv4 and IPv6 traffic in dual stack subnets. So, you can filter IPv4 and IPv6 traffic flows to and from the public internet, on-premises network, or any endpoint in your Amazon VPC.

## AWS Systems Manager
<a name="aws-systems-manager"></a>

 Resources managed by [AWS Systems Manager](https://aws.amazon.com/systems-manager/) must have IPv4 connectivity to Systems Manager’s endpoints. For example, to connect to an EC2 instance using Systems Manager Session Manager, the instance must be running dual-stack and must have an IPv4 connectivity to the internet or AWS PrivateLink VPC endpoint. Similarly, on-premises resources must also be in dual-stack network mode.
