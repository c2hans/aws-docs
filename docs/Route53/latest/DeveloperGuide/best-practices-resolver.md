---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html
---

# Best practices for VPC Resolver
<a name="best-practices-resolver"></a>

This section provides best practices for optimizing Route 53 VPC Resolver, covering the following topics:

1. **Avoiding Loop Configurations with Resolver Endpoints:**
   + Prevent routing loops by ensuring that the same VPC is not associated with both a Resolver rule and its inbound endpoint.
   + Utilize AWS RAM to share VPCs across accounts while maintaining proper routing configurations.

   For more information, see [Avoid loop configurations with Resolver endpoints](best-practices-resolver-endpoints.md)

1. **Scaling Resolver endpoints:**
   + Implement security group rules that permit traffic based on connection state to reduce connection tracking overhead
   + Follow recommended security group rules for inbound and outbound Resolver endpoints to maximize query throughput.
   + Monitor unique IP address and port combinations generating DNS traffic to avoid capacity limitations.

   For more information, see [Resolver endpoint scaling](best-practices-resolver-endpoint-scaling.md)

1. **High availability for Resolver endpoints:**
   + Create inbound endpoints with IP addresses in at least two Availability Zones for redundancy.
   + Provision additional network interfaces to ensure availability during maintenance or traffic surges

   For more information, see [High availability for Resolver endpoints](best-practices-resolver-endpoint-high-availability.md)

1. **Preventing DNS zone walking attacks:**
   + Be aware of potential DNS zone walking attacks, where attackers attempt to retrieve all content from DNSSEC-signed DNS zones.
   + If your endpoints experience throttling due to suspected zone walking, contact AWS Support for assistance.

   For more information, see [DNS zone walking](best-practices-resolver-zone-walking.md)

1. **Subnet compatibility for Resolver endpoints:**
   + We recommend using non-Outposts subnets for Resolver endpoints.
   + Outposts subnets with Local Network Interface (LNI) enabled are not compatible with VPC Resolver endpoints.
   + If you enable LNI on a subnet that contains VPC Resolver endpoint ENIs, those ENIs stop functioning.

   For more information, see [Subnet compatibility for Resolver endpoints](best-practices-resolver-subnet-compatibility.md)

 By following these best practices, you can optimize the performance, scalability, and security of your VPC Resolver deployments, ensuring reliable and efficient DNS resolution for your applications and resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
