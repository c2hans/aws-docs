---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/use-cases.html
---

# Use cases
<a name="use-cases"></a>

 **Network connectivity**

To meet your workloads' requirements, this solution helps you attach VPCs with Transit Gateway by tagging the VPCs and subnets across multiple accounts. Based on the VPC and subnet tags, the solution automatically updates the subnet’s associated route table with default routes to the transit gateway. It also creates association and enables propagation in the transit gateway route tables.

To connect your network across AWS Regions, this solution can create inter-Region transit gateway peering attachments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
