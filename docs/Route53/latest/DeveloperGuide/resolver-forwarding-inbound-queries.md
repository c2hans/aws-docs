---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html
---

# Forwarding inbound DNS queries to your VPCs
<a name="resolver-forwarding-inbound-queries"></a>

To forward DNS queries from your network to VPC Resolver, you create an inbound endpoint. An inbound endpoint specifies the IP addresses (from the range of IP addresses available to your VPC) that you want DNS resolvers on your network to forward DNS queries to. Those IP addresses aren't public IP addresses, so for each inbound endpoint, you need to connect your VPC to your network using either an Direct Connect connection or a VPN connection.

When implementing inbound delegation, you're delegating DNS authority for a subdomain from your on-premises DNS infrastructure to VPC Resolver. To properly configure this delegation, you must use the inbound endpoint's IP addresses as glue records (NS records) on your on-premises name server for the subdomain being delegated. For example, if you're delegating the subdomain "aws.example.com" to VPC Resolver through an inbound delegation endpoint with IP addresses 10.0.1.100 and 10.0.1.101, you would create NS records on your on-premises DNS server pointing "aws.example.com" to these IP addresses. This makes sure that DNS queries for the delegated subdomain are properly routed to the VPC Resolver through the inbound endpoint, allowing the VPC Resolver to respond with records from the associated private hosted zone.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
