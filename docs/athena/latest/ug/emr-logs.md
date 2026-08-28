---
source_url: https://docs.aws.amazon.com/athena/latest/ug/emr-logs.html
---

# Query Amazon EMR logs
<a name="emr-logs"></a>

Amazon EMR and big data applications that run on Amazon EMR produce log files. Log files are written to the [primary node](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html), and you can also configure Amazon EMR to archive log files to Amazon S3 automatically. You can use Amazon Athena to query these logs to identify events and trends for applications and clusters. For more information about the types of log files in Amazon EMR and saving them to Amazon S3, see [View log files](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-manage-view-web-log-files.html) in the *Amazon EMR Management Guide*.

**Topics**
+ [Create and query a basic table based on Amazon EMR log files](emr-create-table.md)
+ [Create and query a partitioned table based on Amazon EMR logs](emr-create-table-partitioned.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
