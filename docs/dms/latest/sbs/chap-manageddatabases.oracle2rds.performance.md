---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.oracle2rds.performance.html
---

# Full load Oracle database migration options performance comparison
<a name="chap-manageddatabases.oracle2rds.performance"></a>

We analyzed the Oracle Export/Import, Oracle Data Pump, database link, and SQL\*Loader tools for their performance in a full load migration. We populated the `sporting_event_ticket` table with 10 GB of data to use as a test environment.

We expect the similar trend for larger data sets too. We didn’t include Oracle materialized views or SQL Developer database copy because those tools aren’t recommended for data sets larger than 1 GB.

![Performance comparison of Oracle Export/Import](http://docs.aws.amazon.com/dms/latest/sbs/images/oracle2rds-performance-comparison.png)

+ 18:08 minutes is the total elapsed time for Oracle Data Pump. This time includes:
  + 3:07 minutes to unload data and metadata using `expdp`.
  + 2:00 minutes to upload the data dump to Amazon S3 from Amazon EC2.
  + 3:01 minutes to download the data dump to Amazon RDS instance.
  + 7:00 Minutes to load data and metadata into Amazon RDS using `impdp`.
+ 22 minutes is the total elapsed time for Oracle SQL\*Loader. This time includes:
  + 15 minutes to unload data.
  + 7 minutes to load data into the target using `direct=y`.
+ 29 minutes is the total elapsed time for database link.
+ 52 minutes is the total elapsed time for Oracle Export/Import. This time includes:
  + 14 minutes to unload data using `exp`.
  + 38 minutes to load data using `imp`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
