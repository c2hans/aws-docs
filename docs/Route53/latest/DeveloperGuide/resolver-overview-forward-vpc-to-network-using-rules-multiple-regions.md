---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-overview-forward-vpc-to-network-using-rules-multiple-regions.html
---

# Using rules in multiple Regions
<a name="resolver-overview-forward-vpc-to-network-using-rules-multiple-regions"></a>

Route 53 VPC Resolver is a Regional service, so objects that you create in one AWS Region are available only in that Region. To use the same rule in more than one Region, you must create the rule in each Region.

The AWS account that created a rule can share the rule with other AWS accounts. For more information, see [Sharing Resolver rules with other AWS accounts and using shared rules](resolver-rules-managing.md#resolver-rules-managing-sharing).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
