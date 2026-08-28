---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/architectures.html
---

# AWS Network Firewall example architectures with routing
<a name="architectures"></a>

This section provides a high-level view of simple architectures that you can configure with AWS Network Firewall and shows example route table configurations for each. For additional information and examples, see [Deployment models for AWS Network Firewall](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/).

**Note**
For information about managing route tables for your VPC, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon Virtual Private Cloud User Guide*.

**Unsupported architectures**
The following lists architectures and traffic types that Network Firewall doesn't support:
+ VPC peering.
+ Inspection of AWS Global Accelerator traffic.
+ Inspection of AmazonProvidedDNS traffic for Amazon EC2.

**Topics**
+ [Simple single zone architecture with an internet gateway using AWS Network Firewall](arch-single-zone-igw.md)
+ [Multi zone architecture with an internet gateway using AWS Network Firewall](arch-two-zone-igw.md)
+ [Architecture with an internet gateway and a NAT gateway using AWS Network Firewall](arch-igw-ngw.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
