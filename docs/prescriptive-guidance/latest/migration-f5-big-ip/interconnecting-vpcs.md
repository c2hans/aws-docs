---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/interconnecting-vpcs.html
---

# Interconnecting your VPCs
<a name="interconnecting-vpcs"></a>

The following tables show the key considerations when you are interconnecting your VPCs.

|
|
| **Security VPC with VPC peering** | **Security VPC with AWS Transit Gateway** | **Security VPC with VPN interconnect** |
| --- |--- |--- |
| **Advantages** | **Disadvantages** | **Advantages** | **Disadvantages** | **Advantages** | **Disadvantages** |
| + Easy and quick to set up<br />+ Simple routing<br />+ High redundancy<br />+ High bandwidth | + Only supports traffic from VPC-assigned CIDR ranges<br />+ Cannot insert security inspection between VPCs<br />+ Complex to manage at scale (all are point-to-point) | + Easy to set up<br />+ Flexible routing without SNAT<br />+ High redundancy<br />+ High bandwidth<br />+ Easy to manage at scale | + Routing is more complex (VPC route tables and AWS Transit Gateway route tables)<br />+ Complex topology to insert security inspection between VPCs | + Flexible routing without SNAT<br />+ Easy insertion of security inspection between VPCs | + Low bandwidth<br />+ Complex vendor-specific dependent failover<br />+ Complex to manage at scale (all are point-to-point) |

|
|
| Client (sends SYN) | AWS Transit Gateway | VPC peering | VPN between VPCs | Solution overview and possible concerns |
| --- |--- |--- |--- |--- |
| Internet or AWS Direct Connect to service in a single VPC with a public or private subnet. | N/A | N/A | N/A | Traffic traverses internet gateway, or virtual gateway - does not need to cross more than the VPC boundary. VPC acts as designed stub networks. Traffic ingresses from on premises to the AWS Cloud (AWS Direct Connect, VPN). |
| Internet or AWS Direct Connect in a VPC with clients in other VPCs (for example, pool members in another VPC), no SNAT. | Yes | No | Yes | AWS Transit Gateway or VPNs allow the traffic to bypass the VPC peering filter that only VPC-assigned CIDRs can pass.<br />VPN solutions will be constrained. No equal-cost multi-path routing (ECMP) (only a single route) and no bandwidth (about 1.2 GB-seconds per tunnel, in general only one tunnel). |
| Internet or AWS Direct Connect to a service in a VPC with customers in other VPCs (for example, pool members in another VPC), with SNAT. | Yes (but not required) | Yes | Yes (but not required) | Since the interconnection between the VPCs sees traffic from VPC-assigned CIDRs, any will work.<br />VPN solutions will be constrained. No ECMP (only a single route) and no bandwidth (about 1.2 GB-seconds per tunnel, in general only one tunnel). |
| Inside of VPC to service in same VPC. | N/A | N/A | N/A | All traffic constrained to a single VPC. Interconnection is not required. |
| Inside of one VPC to a service VPC. Service is in the destination VPC CIDR. | Yes (but not required) | Yes | Yes (but not required) | Since the interconnection between the VPCs sees traffic from VPC-assigned CIDRs, any will work. |
| Inside of one VPC to a service VPC. Service is outside the VPC CIDR range. | Yes | No | Yes | Since the interconnection between the VPCs sees traffic from VPC-assigned CIDRs, any will work.<br />VPN solutions will be constrained. No ECMP (only a single route) and no bandwidth (about 1.2 GB-seconds per tunnel, in general only one tunnel). |
| Inside of a single VPC to an internet service. | N/A | N/A | N/A | Traffic is from a VPC-assigned CIDR, if Elastic IP, NAT, or route table constructs are inline then traffic will flow. |
| Inside of a VPC to an internet service, routing out through a security or inspection VPC. | Yes | No | Yes | Since the interconnection between the VPCs sees traffic from outside a VPC-assigned CIDR range, VPC peering cannot be used.<br />VPN solutions will be constrained. No ECMP (only a single route) and no bandwidth (about 1.2 GB-seconds per tunnel, in general only one tunnel). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
