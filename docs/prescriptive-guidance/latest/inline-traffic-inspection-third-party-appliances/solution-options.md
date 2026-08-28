---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/inline-traffic-inspection-third-party-appliances/solution-options.html
---

# Inline traffic inspection solution options
<a name="solution-options"></a>

The following three sections describe data flows for traffic inspection using third-party firewall appliances in an AWS environment with Gateway Load Balancer and Gateway Load Balancer endpoints:
+ [VPC-to-VPC traffic inspection](vpc-to-vpc-traffic-inspection.md)
+ [VPC-to-on-premises traffic inspection](on-premises-traffic-inspection.md)
+ [Outbound traffic inspection through a NAT gateway and internet gateway](outbound-inspection-through-a-nat-and-internet-gateway.md)

The following resources are used in the three options for this solution:
+ Dedicated spoke VPCs for hosting workloads or applications.
+ One VPC for hosting firewall appliances.
+ A dedicated subnet for the AWS Transit Gateway elastic network interface for each Availability Zone in the spoke and appliance VPCs.
+ Appliance mode turned on for the appliance VPC attachment.
+ Dedicated subnets for Gateway Load Balancer endpoints in each Availability Zone.
+ A transit gateway to interconnect the VPCs, in addition to providing on-premises connectivity through the Transit Gateway virtual interface and AWS Direct Connect gateway or with a VPN attachment for AWS Site-to-Site VPN.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
