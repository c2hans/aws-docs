---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.limitations.html
---

# Limitations for the Amazon RDS Data API
<a name="data-api.limitations"></a>

RDS Data API has the following limitations:
+ You can only execute Data API queries on writer instances in a DB cluster. However, writer instances can accept both write and read queries.
+ With Aurora global databases, you can enable Data API on both the primary and secondary DB clusters. However, a secondary cluster doesn't have a writer instance until it's promoted to be the primary. Data API requires access to the writer instance for query processing, even for read queries. As a result, read and write queries sent to the secondary cluster fail while it lacks a writer instance. Once a secondary cluster is promoted and has a writer instance available, Data API queries on that DB instance succeed.
+ Data API isn't supported on T DB instance classes.
+ For Aurora PostgreSQL version 14 and higher databases, Data API only supports `scram-sha-256` for password encryption.
+ The response size limit is 1 MiB. If the call returns more than 1 MiB of response data, the call is terminated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
