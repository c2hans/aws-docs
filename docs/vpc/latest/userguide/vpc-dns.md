---
source_url: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html
---

# DNS attributes for your VPC
<a name="vpc-dns"></a>

Domain Name System (DNS) is a standard by which names used on the internet are resolved to their corresponding IP addresses. A DNS hostname is a name that uniquely and absolutely names a computer; it's composed of a host name and a domain name. DNS servers resolve DNS hostnames to their corresponding IP addresses.

Public IPv4 addresses enable communication over the internet, while private IPv4 addresses enable communication within the network of the instance. For more information, see [IP addressing for your VPCs and subnets](vpc-ip-addressing.md).

Amazon provides a DNS server ([the Amazon Route 53 Resolver](AmazonDNS-concepts.md#AmazonDNS)) for your VPC. To use your own DNS server instead, create a new set of DHCP options for your VPC. For more information, see [DHCP option sets in Amazon VPC](VPC_DHCP_Options.md).

**Topics**
+ [Understanding Amazon DNS](AmazonDNS-concepts.md)
+ [View DNS hostnames for your EC2 instance](vpc-dns-viewing.md)
+ [View and update DNS attributes for your VPC](vpc-dns-updating.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
