---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-endpoints.html
---

# Avoid loop configurations with Resolver endpoints
<a name="best-practices-resolver-endpoints"></a>

Don't associate the same VPC to a Resolver rule and its inbound endpoint (whether it's a direct target of the endpoint, or through an on-premises DNS server). When the outbound endpoint in a Resolver rule points to an inbound endpoint that shares a VPC with the rule, it can cause a loop where the query is continually passed between the inbound and outbound endpoints.

The forwarding rule can still be associated with other VPCs that are shared with other accounts by using AWS Resource Access Manager (AWS RAM). Private hosted zones associated with the hub, or a central VPC, still resolve from queries to inbound endpoints because a forwarding resolver rule does not change this resolution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
