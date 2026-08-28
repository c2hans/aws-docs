---
source_url: https://docs.aws.amazon.com/neptune/latest/userguide/cw-dimensions.html
---

# Neptune CloudWatch Dimensions
<a name="cw-dimensions"></a>

The metrics for Amazon Neptune are qualified by the values for the account, graph name, or operation. You can use the Amazon CloudWatch console to retrieve Neptune data along with any of the dimensions in the following table.

| Dimension | Description |
| --- | --- |
| DBInstanceIdentifier | Filters the data you request for a specific database instance within a cluster. |
| DBClusterIdentifier | Filters the data you request for a specific Neptune DB cluster. |
| DBClusterIdentifier, EngineName | Filters the data by the cluster. The engine name for all Neptune instances is neptune. |
| DBClusterIdentifier, Role | Filters the data you request for a specific Neptune DB cluster, aggregating the metric by instance role (WRITER/READER). For example, you can aggregate metrics for all READER instances that belong to a cluster. |
| DBClusterIdentifier, SourceRegion | Filters the data by the primary cluster in a global database primary region. |
| DatabaseClass | Filters the data you request for all instances in a database class. For example, you can aggregate metrics for all instances that belong to the database class db.r4.large |
| EngineName | The engine name for all Neptune instances is neptune. |
| GlobalDbDBClusterIdentifier, SecondaryRegion | Filters the data by the secondary cluster of a specified global database in a secondary region. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
