---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/rel_planning_network_topology_non_overlap_ip.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL02-BP05 Enforce non-overlapping private IP address ranges in all private address spaces where they are connected
<a name="rel_planning_network_topology_non_overlap_ip"></a>

 The IP address ranges of each of your VPCs must not overlap when peered or connected via VPN. You must similarly avoid IP address conflicts between a VPC and on-premises environments or with other cloud providers that you use. You must also have a way to allocate private IP address ranges when needed.

 An IP address management (IPAM) system can help with this. Several IPAMs are available from the AWS Marketplace.

 **Common anti-patterns:**
+  Using the same IP range in your VPC as you have on premises or in your corporate network.
+  Not tracking IP ranges of VPCs used to deploy your workloads.

 **Benefits of establishing this best practice:** Active planning of your network will ensure that you do not have multiple occurrences of the same IP address in interconnected networks. This prevents routing problems from occurring in parts of the workload that are using the different applications.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Monitor and manage your CIDR use. Evaluate your potential usage on AWS, add CIDR ranges to existing VPCs, and create VPCs to allow planned growth in usage.
  +  Capture current CIDR consumption (for example, VPCs, subnets)
    +  Use service API operations to collect current CIDR consumption.
  +  Capture your current subnet usage.
    +  Use service API operations to collect subnets per VPC in each Region.
      +  [DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)
    +  Record the current usage.
    +  Determine if you created any overlapping IP ranges.
    +  Calculate the spare capacity.
    +  Identify overlapping IP ranges. You can either migrate to a new range of addresses or use Network and Port Translation (NAT) appliances from AWS Marketplace if you need to connect the overlapping ranges.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help plan your networking](https://aws.amazon.com/partners/find/results/?keyword=network)
+  [AWS Marketplace for Network Infrastructure](https://aws.amazon.com/marketplace/b/2649366011)
+  [Amazon Virtual Private Cloud Connectivity Options Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html)
+  [Multiple data center HA network connectivity](https://aws.amazon.com/answers/networking/aws-multiple-data-center-ha-network-connectivity/)
+  [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+  [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)

 **Related videos:**
+  [AWS re:Invent 2018: Advanced VPC Design and New Capabilities for Amazon VPC (NET303)](https://youtu.be/fnxXNZdf6ew)
+  [AWS re:Invent 2019: AWS Transit Gateway reference architectures for many VPCs (NET406-R1)](https://youtu.be/9Nikqn_02Oc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
