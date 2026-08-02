---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/rel_planning_network_topology_ip_subnet_allocation.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL02-BP03 Ensure IP subnet allocation accounts for expansion and availability
<a name="rel_planning_network_topology_ip_subnet_allocation"></a>

 Amazon VPC IP address ranges must be large enough to accommodate workload requirements, including factoring in future expansion and allocation of IP addresses to subnets across Availability Zones. This includes load balancers, EC2 instances, and container-based applications.

 When you plan your network topology, the first step is to define the IP address space itself. Private IP address ranges (following RFC 1918 guidelines) should be allocated for each VPC. Accommodate the following requirements as part of this process:
+  Allow IP address space for more than one VPC per Region.
+  Within a VPC, allow space for multiple subnets so that you can cover multiple Availability Zones.
+  Always leave unused CIDR block space within a VPC for future expansion.
+  Ensure that there is IP address space to meet the needs of any transient fleets of EC2 instances that you might use, such as Spot Fleets for machine learning, Amazon EMR clusters, or Amazon Redshift clusters.
+  Note that the first four IP addresses and the last IP address in each subnet CIDR block are reserved and not available for your use.
+  You should plan on deploying large VPC CIDR blocks. Note that the initial VPC CIDR block allocated to your VPC cannot be changed or deleted, but you can add additional non-overlapping CIDR blocks to the VPC. Subnet IPv4 CIDRs cannot be changed, however IPv6 CIDRs can. Keep in mind that deploying the largest VPC possible (/16) results in over 65,000 IP addresses. In the base 10.x.x.x IP address space alone, you could provision 255 such VPCs. You should therefore err on the side of being too large rather than too small to make it easier to manage your VPCs.

 **Common anti-patterns:**
+  Creating small VPCs.
+  Creating small subnets and then having to add subnets to configurations as you grow.
+  Incorrectly estimating how many IP addresses a elastic load balancer can use.
+  Deploying many high traffic load balancers into the same subnets.

 **Benefits of establishing this best practice:** This ensures that you can accommodate the growth of your workloads and continue to provide availability as you scale up.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Plan your network to accommodate for growth, regulatory compliance, and integration with others. Growth can be underestimated, regulatory compliance can change, and acquisitions or private network connections can be difficult to implement without proper planning.
  +  Select relevant AWS accounts and Regions based on your service requirements, latency, regulatory, and disaster recovery (DR) requirements.
  +  Identify your needs for regional VPC deployments.
  +  Identify the size of the VPCs.
    +  Determine if you are going to deploy multi-VPC connectivity.
      +  [What Is a Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
      +  [Single Region Multi-VPC Connectivity](https://aws.amazon.com/answers/networking/aws-single-region-multi-vpc-connectivity/)
    +  Determine if you need segregated networking for regulatory requirements.
    +  Make VPCs as large as possible. The initial VPC CIDR block allocated to your VPC cannot be changed or deleted, but you can add additional non-overlapping CIDR blocks to the VPC. This however may fragment your address ranges.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help plan your networking](https://aws.amazon.com/partners/find/results/?keyword=network)
+  [AWS Marketplace for Network Infrastructure](https://aws.amazon.com/marketplace/b/2649366011)
+  [Amazon Virtual Private Cloud Connectivity Options Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html)
+  [Multiple data center HA network connectivity](https://aws.amazon.com/answers/networking/aws-multiple-data-center-ha-network-connectivity/)
+  [Single Region Multi-VPC Connectivity](https://aws.amazon.com/answers/networking/aws-single-region-multi-vpc-connectivity/)
+  [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

 **Related videos:**
+  [AWS re:Invent 2018: Advanced VPC Design and New Capabilities for Amazon VPC (NET303)](https://youtu.be/fnxXNZdf6ew)
+  [AWS re:Invent 2019: AWS Transit Gateway reference architectures for many VPCs (NET406-R1)](https://youtu.be/9Nikqn_02Oc)
