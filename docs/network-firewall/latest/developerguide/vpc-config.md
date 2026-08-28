---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/vpc-config.html
---

# Configuring your VPC and other components for AWS Network Firewall
<a name="vpc-config"></a>

This section describes the changes that you must make in your VPC configuration and other components to use AWS Network Firewall. For information about managing your Amazon Virtual Private Cloud VPC, see the [Amazon Virtual Private Cloud User Guide](https://docs.aws.amazon.com/vpc/latest/userguide).

For examples of architectures that are supported by Network Firewall, see [Architecture and routing examples](architectures.md).

**Unsupported architectures**
The following lists architectures and traffic types that Network Firewall doesn't support:
+ VPC peering.
+ Inspection of AWS Global Accelerator traffic.
+ Inspection of AmazonProvidedDNS traffic for Amazon EC2.

**Topics**
+ [VPC subnet configuration for AWS Network Firewall](vpc-config-subnets.md)
+ [VPC route table configuration for AWS Network Firewall](vpc-config-route-tables.md)
+ [Transit gateway attachment configuration for AWS Network Firewall](vpc-config-tgw-multi-az.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
