---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-vpc-to-network-where-to-forward-queries.html
---

# How VPC Resolver determines where to forward DNS queries
<a name="resolver-overview-forward-vpc-to-network-where-to-forward-queries"></a>

When an application that runs on an EC2 instance in a VPC submits a DNS query, Route 53 VPC Resolver performs the following steps:

1. Resolver checks for domain names in rules.

   If the domain name in a query matches the domain name in a default forward rule, VPC Resolver forwards the query to the IP address that you specified when you created the outbound endpoint. The outbound endpoint then forwards the query to the IP addresses of resolvers on your network, which you specified when you created the rule.

   If the delegation record in response matches the delegation rule, then the Resolver delegate the authority to on-prem resolvers through the outbound endpoint associated with the delegation rule.

   For more information, see [How VPC Resolver determines whether the domain name in a query matches any rules](resolver-overview-forward-vpc-to-network-domain-name-matches.md).

1. Resolver endpoint forwards DNS queries based on the settings in the "." rule.

   If the domain name in a query doesn't match the domain name in any other rules, VPC Resolver forwards the query based on the settings in the autodefined "." (dot) rule. The dot rule applies to all domain names except some AWS internal domain names and record names in private hosted zones. This rule causes VPC Resolver to forward DNS queries to public name servers if the domain names in queries don't match any names in your custom forwarding rules. If you want to forward all queries to the DNS resolvers on your network, you can create a custom forwarding rule, specify "." for the domain name, specify **Forwarding** for **Type**, and specify the IP addresses of those resolvers.

1. VPC Resolver returns the response to the application that submitted the query.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
