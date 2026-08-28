---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/larger-failure-modes.html
---

# Larger failure modes
<a name="larger-failure-modes"></a>

 To design HA architectures to mitigate larger failure modes like rack, data center, Availability Zone (AZ), or Region failures, you should deploy multiple Outposts with sufficient infrastructure capacity in separate data centers with independent power and WAN connectivity. You anchor the Outposts to different Availability Zones (AZs) within an AWS Region or across multiple Regions. You should also provision resilient and sufficient site-to-site connectivity between the locations to support synchronous or asynchronous data replication and workload traffic redirection. Depending on your application architecture, you can use globally available [Amazon Route 53](https://aws.amazon.com/route53/) DNS and [Amazon Route 53 on Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver.html) to direct traffic to the desired location, and automate traffic redirection to surviving locations in the event of large-scale failures.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
