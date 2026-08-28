---
source_url: https://docs.aws.amazon.com/datasync/latest/userguide/task-report-viewing.html
---

# Viewing your DataSync task reports
<a name="task-report-viewing"></a>

DataSync creates task reports for every task execution. When your execution completes, you can find the related task reports in your S3 bucket. Task reports are organized under prefixes that include the IDs of your tasks and their executions.

To help locate task reports in your S3 bucket, use these examples:
+ **Summary only task report** – `{{reports-prefix}}/Summary-Reports/{{task-id-folder}}/{{task-execution-id-folder}}`
+ **Standard task report** – `{{reports-prefix}}/Detailed-Reports/{{task-id-folder}}/{{task-execution-id-folder}}`

Because task reports are in JSON format, you have several options for viewing your reports:
+ View a report by using [Amazon S3 Select](https://docs.aws.amazon.com/AmazonS3/latest/userguide/selecting-content-from-objects.html).
+ Visualize reports by using AWS services such as AWS Glue, Amazon Athena, and Amazon Quick. For more information about visualizing your task reports, see the [AWS Storage Blog](https://aws.amazon.com/blogs/storage/derive-insights-from-aws-datasync-task-reports-using-aws-glue-amazon-athena-and-amazon-quicksight/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
