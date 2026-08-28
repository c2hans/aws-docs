---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/dimensions.html
---

# Amazon CloudWatch dimensions for Amazon RDS
<a name="dimensions"></a>

You can filter Amazon RDS metrics data by using any dimension in the following table.

|  Dimension  |  Filters the requested data for . . .  |
| --- | --- |
|  DBInstanceIdentifier  | A specific DB instance. |
|  DatabaseClass  | All instances in a database class. For example, you can aggregate metrics for all instances that belong to the database class `db.r5.large`. |
|  EngineName  | The identified engine name only. For example, you can aggregate metrics for all instances that have the engine name `postgres`. |
|  SourceRegion  | The specified Region only. For example, you can aggregate metrics for all DB instances in the `us-east-1` Region. |
|  DbInstanceIdentifier, VolumeName  | The metrics per-volume for a single instance.<br />RDS captures metrics for multiple storage volumes. |

**Note**
If you are using additional storage volumes, you can see aggregate storage metrics under the `DBInstanceIdentifier` dimension. To see per-volume storage metrics, use the `DbInstanceIdentifier, VolumeName` dimensions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
