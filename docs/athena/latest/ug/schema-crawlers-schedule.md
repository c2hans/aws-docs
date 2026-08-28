---
source_url: https://docs.aws.amazon.com/athena/latest/ug/schema-crawlers-schedule.html
---

# Schedule a crawler to keep the AWS Glue Data Catalog and Amazon S3 in sync
<a name="schema-crawlers-schedule"></a>

AWS Glue crawlers can be set up to run on a schedule or on demand. For more information, see [Time-based schedules for jobs and crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html) in the *AWS Glue Developer Guide*.

If you have data that arrives for a partitioned table at a fixed time, you can set up an AWS Glue crawler to run on schedule to detect and update table partitions. This can eliminate the need to run a potentially long and expensive `MSCK REPAIR` command or manually run an `ALTER TABLE ADD PARTITION` command. For more information, see [Table partitions](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html#tables-partition) in the *AWS Glue Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
