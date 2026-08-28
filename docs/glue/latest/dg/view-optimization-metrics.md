---
source_url: https://docs.aws.amazon.com/glue/latest/dg/view-optimization-metrics.html
---

# Viewing Amazon CloudWatch metrics
<a name="view-optimization-metrics"></a>

 After running the table optimizers successfully, the service creates Amazon CloudWatch metrics on the optimization job performance. You can go to the **CloudWatch Metrics** and choose **Metrics**, **All metrics**. You can to filter metrics by the specific namespace (for example AWS Glue), table name, or database name.

 For more information, see [View available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html) in the *Amazon CloudWatch User Guide*.

****Compaction****
+ Number of bytes compacted
+ Number of files compacted
+ Number of DPU allocated to job
+ Duration of job (Hours)

****Snapshot retention****
+ Number of data files deleted
+ Number of manifest files deleted
+ Number of Manifest lists deleted
+ Duration of job (Hours)

****Orphan file deletion****
+ Number of orphan files deleted
+ Duration of job (Hours)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
