---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.parallel.html
---

# Export performance in Aurora MySQL
<a name="aurora-export-snapshot.parallel"></a>

Aurora MySQL version 2 and version 3 DB cluster snapshots use an advanced export mechanism to improve performance and reduce export time. The mechanism includes optimizations such as multiple export threads and Aurora MySQL parallel query to take advantage of the Aurora shared storage architecture. The optimizations are applied adaptively, depending on the data set size and structure.

You don't need to turn on parallel query to use the faster export process, but the process does have the same limitations as parallel query. In addition, some data values aren't supported, such as dates where the day of the month is `0` or the year is `0000`. For more information, see [Parallel query for Amazon Aurora MySQL](aurora-mysql-parallel-query.md).

When performance optimizations are applied, you might also see much larger (\~200 GB) Parquet files for Aurora MySQL version 2 and 3 exports.

If the faster export process can't be used, for example because of incompatible data types or values, Aurora automatically switches to a single-threaded export mode without parallel query. Depending on which process is used, and the amount of data to be exported, export performance can vary.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
