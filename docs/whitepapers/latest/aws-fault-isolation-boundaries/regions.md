---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/regions.html
---

# Regions
<a name="regions"></a>

 Each AWS Region consists of multiple independent and physically separate Availability Zones within a geographic area. All Regions currently have three or more Availability Zones. Regions themselves are isolated and independent from other Regions with a few exceptions noted later in this document [(refer to Global single-Region operations)](global-services.md#global-single-region-operations). This separation between Regions limits service failures, when they occur, to a single Region. Other Regions’ normal operations are unaffected in this case. Additionally, the resources and data that you create in one Region do not exist in any other Region unless you explicitly use a replication or copy feature offered by an AWS service or replicate the resource yourself.

![This image illustrates current and planned AWS Regions as of December 2022.](http://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/images/current-and-planned-aws-regions.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
