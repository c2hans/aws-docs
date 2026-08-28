---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-edns0.html
---

# How Amazon Route 53 uses EDNS0 to estimate the location of a user
<a name="routing-policy-edns0"></a>

To improve the accuracy of geolocation, geoproximity, IP-based, and latency routing, Amazon Route 53 supports the edns-client-subnet extension of EDNS0. (EDNS0 adds optional extensions to the DNS protocol.) Route 53 can use edns-client-subnet only when DNS resolvers support it:
+ When a browser or other viewer uses a DNS resolver that does not support edns-client-subnet, Route 53 uses the source IP address of the DNS resolver to guess where the user is and responds to geolocation queries with the DNS record for the resolver's location.
+ When a browser or other viewer uses a DNS resolver that does support edns-client-subnet, the DNS resolver sends Route 53 a shortened version of the user's IP address. Route 53 finds the location of the user from the shortened IP address instead of the resolver's source IP address; this usually gives a more accurate location. Route 53 then responds to geolocation queries with the DNS record for the user's location.
+ EDNS0 is not applicable to private hosted zones. For private hosted zones Route 53 uses data from the VPC Resolvers in the AWS Region that the private hosted zone is in to make geolocation and latency routing decisions.

For more information about edns-client-subnet, see the EDNS Client Subnet RFC, [Client Subnet in DNS Requests](https://www.rfc-editor.org/rfc/rfc7871).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
