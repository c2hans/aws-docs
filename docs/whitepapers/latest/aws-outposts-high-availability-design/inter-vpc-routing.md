---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/inter-vpc-routing.html
---

# Outposts Rack Inter-VPC routing
<a name="inter-vpc-routing"></a>

Resources on two separate Outposts deployed in different VPCs can communicate each other across the customer network. Deploying this architecture enable you to route traffic Outposts-to-Outposts by your local on-premises and WAN networks adding routes towards the counterpart Outposts/VPC subnets.

![Diagram showing network paths for multiple VPC with multiple logical Outposts](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-50-multiple-vpc-multiple-outposts-networking-path.png)

Recommended practices for protecting against larger failure modes:
+ Deploy multiple Outposts anchored to multiple AZs and Regions.
+ Use separate VPCs for each Outpost in a multi-Outpost deployment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
