---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.oracle2rds.replication.html
---

# Migrate Oracle database with AWS DMS ongoing replication
<a name="chap-manageddatabases.oracle2rds.replication"></a>

After you complete the full load, make sure that you perform ongoing replication using AWS DMS to keep the source and target databases in sync. To configure the ongoing replication task, sign in to the AWS Management Console and follow these steps.

1. Choose **Database Migration Service**, and then choose **Database migration tasks**.

1. Choose **Create task**.

1. For **Migration type**, choose **Replicate data changes only**.

1. For **CDC start mode for source transactions**, choose **Enable custom CDC start mode**.

1. For **Custom CDC start point**, choose **Specify a log sequence number** and enter the SCN that you captured before starting the full load.

For more information, see [Continuous replication tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html) and [Migrate from Oracle to Amazon RDS](https://aws.amazon.com/getting-started/hands-on/move-to-managed/migrate-oracle-to-amazon-rds/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
