---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/archive-unpartitioned-tables.html
---

# Archiving data from unpartitioned tables
<a name="archive-unpartitioned-tables"></a>

In database tables where partitioning is not possible, you can use the Percona Toolkit [pt-archiver](https://docs.percona.com/percona-toolkit/pt-archiver.html) tool to archive your table's data into another table in your MySQL database.

The pt-archiver tool is used to archive the records from large tables to other tables or files. It's a read/write tool, which means it deletes data from the source table after archiving it, so you don't have to manage source data deletion separately. The main purpose of this script is to archive old data from the table without impacting the existing online transaction processing (OLTP) query load (see Appendix I) and insert the data into another table on the same or a different server.

You can download the [Percona Toolkit](https://www.percona.com/downloads/percona-toolkit/2.2.14/) and [install](https://docs.percona.com/percona-toolkit/installation.html) it on your local machine or on the Amazon Elastic Compute Cloud (Amazon EC2) instance from where you are connecting to the database. To run the pt-archiver tool, use the following syntax.

```
pt-archiver --source h=<HOST>,D=<DATABASE>,t=<TABLE>,u=<USER>,p=<PASSWORD> --dest h=<HOST>,D=<DATABASE>,t=<TABLE> --where ""1=1"" --statistics
```

Replace the `HOST`, `DATABASE`, `TABLE`, and `USER` with your source and destination database details and credentials.

You can also use [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html) to create and schedule this job for your tables.

When you use the pt-archiver tool to archive your table's data, consider the following:
+ Having a primary key on the source table will improve the performance of this tool. If the table doesn't have a primary key, you can [create an index on a unique column](https://dev.mysql.com/doc/refman/8.0/en/create-index.html#create-index-unique), which will help pt-archiver to go through all the rows of the table and archive them.
+ By default, pt-archiver deletes the data after archiving the table. Before you run it on the production server, be sure to test your archiving jobs with `--dry-run`. Alternatively, you can use the `--no-delete` option.
+ The pt-archiver tool adjusts its rate of archiving based on the load on your system (see Appendix II). With higher loads, you can expect slower archiving performance.

After you run pt-archiver, your archived data should be in the corresponding table in the archive schema. From there, you can move it to Amazon S3.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
