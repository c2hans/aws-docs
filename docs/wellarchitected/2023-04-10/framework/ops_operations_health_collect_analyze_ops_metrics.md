---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_operations_health_collect_analyze_ops_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS09-BP03 Collect and analyze operations metrics
<a name="ops_operations_health_collect_analyze_ops_metrics"></a>

 Perform regular, proactive reviews of metrics to identify trends and determine where appropriate responses are needed.

 You should aggregate log data from the processing of your operations activities and operations API calls, into a service such as CloudWatch Logs. Generate metrics from observations of necessary log content to gain insight into the performance of operations activities.

 On AWS, you can [export your log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) or [send logs directly](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Sending-Logs-Directly-To-S3.html) to [Amazon S3](https://aws.amazon.com/s3/) for long-term storage. Using [AWS Glue](https://aws.amazon.com/glue/), you can discover and prepare your log data in Amazon S3 for analytics, storing associated metadata in the [AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html). [Amazon Athena](https://aws.amazon.com/athena/), through its native integration with AWS Glue, can then be used to analyze your log data, querying it using standard SQL. Using a business intelligence tool like [Quick](https://aws.amazon.com/quicksight/) you can visualize, explore, and analyze your data.

 **Common anti-patterns:**
+  Consistent delivery of new features is considered a key performance indicator. You have no method to measure how frequently deployments occur.
+  You log deployments, rolled back deployments, patches, and rolled back patches to track you operations activities, but no one reviews the metrics.
+  You have a recovery time objective to restore a lost database within fifteen minutes that was defined when the system was deployed and had no users. You now have ten thousand users and have been operating for two years. A recent restore took over two hours. This was not recorded and no one is aware.

 **Benefits of establishing this best practice:** By collecting and analyzing your operations metrics, you gain understanding of the health of your operations and can gain insight to trends that have may an impact on your operations or the achievement of your business outcomes.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Collect and analyze operations metrics: Perform regular proactive reviews of metrics to identify trends and determine where appropriate responses are needed.
  +  [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
  +  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
  +  [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon Athena](https://aws.amazon.com/athena/)
+  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
+  [Quick](https://aws.amazon.com/quicksight/)
+  [AWS Glue](https://aws.amazon.com/glue/)
+  [AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html)
+  [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
+  [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
