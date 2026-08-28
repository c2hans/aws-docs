---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver-subnet-compatibility.html
---

# Subnet compatibility for Resolver endpoints
<a name="best-practices-resolver-subnet-compatibility"></a>

We recommend using [VPC Resolver on AWS Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html) to create endpoints on AWS Outposts Racks.

**Important**
Outposts subnets with [Local Network Interface (LNI)](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) enabled are not compatible with VPC Resolver endpoints. If you enable LNI on a subnet that contains VPC Resolver endpoint elastic network interfaces (ENIs), those ENIs stop functioning.

To avoid this issue:
+ Before creating a Resolver endpoint, verify that the target subnets don't have LNI enabled.
+ Don't enable LNI on subnets that already contain Resolver endpoint ENIs.
+ If you need both LNI and Resolver endpoints, use separate subnets for each.

For more information about LNI, see [Local network interfaces](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) in the *AWS Outposts User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
