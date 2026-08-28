---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-free-tier.html
---

# Amazon Aurora on the AWS Free Tier
<a name="aurora-free-tier"></a>

Aurora PostgreSQL is also available on the [AWS Free Tier](https://aws.amazon.com/rds/free/) through the [Create with express configuration](CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.md). In addition to the express configuration limitations, the following restrictions apply when using Aurora PostgreSQL with the AWS Free Tier:
+ Only clusters created with express configuration are supported (full configuration is not available)
+ Up to 4 Aurora Capacity Units (ACUs) per cluster
+ Up to 1 GB storage per cluster
+ Maximum 2 clusters and 2 instances per account
+ Aurora Global Database and Zero-ETL integrations are not supported

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
