---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ipv6-on-aws/supporting-amazon-vpc-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Supporting Amazon VPC services
<a name="supporting-amazon-vpc-services"></a>

 AWS exposes a set of supporting services within customer VPCs at well-known/reserved addresses. These services are traditionally exposed from the IPv4 link-local address range (`169.254.0.0/16`). For [AWS Nitro System](https://aws.amazon.com/ec2/nitro/) instances, AWS also provides these services using IPv6 ULAs.

## Instance Metadata Service (IMDS)
<a name="instance-metadata-service-imds"></a>

 The instance metadata is information about your instance. Instances can introspect this at runtime by querying the IMDS available to it at `169.254.169.254`. For Nitro-based instances with IPv6 addresses, AWS provides this service at the `fd00:ec2::254` IPv6 endpoint.

 For more details, refer to [Use IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html).

## Route 53 DNS resolver
<a name="route-53-dns-resolver"></a>

 Amazon VPC features a built-in DNS resolver which resides at `VPC_CIDR_BASE + 2` and `169.254.169.253`. IPv6 enabled Nitro instances can access the service via `fd00:ec2::253`. Additionally, for IPv6 to IPv4 backwards-compatibility and communication, you have the option of using the AWS-managed DNS64 services, together with NAT64. Amazon Route 53 Resolver and DNS in general are discussed at greater length in the [Designing DNS for IPv6](designing-an-ipv6-aws-cloud-network.md) section of this document.

## Network Time Protocol server
<a name="network-time-protocol-server"></a>

 Amazon VPC provides a Stratum-3 NTP server at `169.254.169.123`. Nitro-based IPv6 enabled instances can reach this server via `fd00:ec2::123`.

## IP-based naming and resource-based naming for Amazon EC2
<a name="ip-based-naming-and-resource-based-naming-for-amazon-ec2"></a>

 When you launch an EC2 instance with IP address-based naming (IPBN), the guest OS hostname is configured to use the private IPv4 address. The format for an instance in any AWS Region is `private-ipv4-address.region.compute.internal`

 For example: `ip-10-20-14-8.ec2.internal`

 Resource-based naming (RBN) is used automatically when you launch EC2 instances in IPv6-only subnets. RBN is not selected by default when you launch an instance in dual-stack subnets, but it is an option that you can select depending on the subnet settings. When you launch an EC2 instance with a resource-based hostname type, the guest OS hostname is configured to use the EC2 instance ID.

 The format for an instance in any AWS Region is: `ec2-instance-id.region.compute.internal`

 For example: `i-0123456789abcdef.us-west-2.compute.internal`

 DNS queries for both IP address-based naming (IPBN) and resource-based naming (RBN) DNS hostnames coexist to ensure backward compatibility and to allow you to migrate from IPBN to RBN. For private DNS hostnames based on IPBN, you cannot configure whether a DNS A record query for the instance is responded to or not. DNS A record queries are always responded to. In contrast, for private DNS hostnames based on RBN, you can configure whether DNS A and/or DNS AAAA queries for the instance are responded to or not.

 You can configure the response behavior when you launch an instance or modify a subnet, and you can make the RBN DNS query configuration changes when you launch an instance, create a subnet, or modify a subnet.

 For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
