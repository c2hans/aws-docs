---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_workload_health_collect_analyze_workload_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS08-BP03 Collect and analyze workload metrics
<a name="ops_workload_health_collect_analyze_workload_metrics"></a>

 Perform regular proactive reviews of metrics to identify trends and determine where appropriate responses are needed.

 You should aggregate log data from your application, workload components, services, and API calls to a service such as CloudWatch Logs. Generate metrics from observations of necessary log content to enable insight into the performance of operations activities.

 On AWS, you can analyze workload metrics and identify operational issues using the machine learning capabilities of [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html). AWS DevOps Guru provides notification of operational issues with [targeted and proactive](https://docs.aws.amazon.com/devops-guru/latest/userguide/view-insights.html) recommendations to resolve issues and maintain application health.

 In the AWS Shared Responsibility Model, portions of monitoring are delivered to you through the [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/). This dashboard provides alerts and remediation guidance when AWS is experiencing events that might affect you. Customers with Business and Enterprise Support subscriptions also get access to the [AWS Health API](https://docs.aws.amazon.com/health/latest/ug/getting-started-api.html), enabling integration to their event management systems.

 On AWS, you can [export your log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) or [send logs directly](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Sending-Logs-Directly-To-S3.html) to [Amazon S3](https://aws.amazon.com/s3/) for long-term storage. Using [AWS Glue](https://aws.amazon.com/glue/), you can discover and prepare your log data in Amazon S3 for analytics, storing associated metadata in the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html). [Amazon Athena](https://aws.amazon.com/athena/), through its native integration with AWS Glue, can then be used to analyze your log data, querying it using standard SQL. Using a business intelligence tool like [Quick](https://aws.amazon.com/quicksight/) you can visualize, explore, and analyze your data.

 An alternative [solution](https://aws.amazon.com/solutions/centralized-logging/) would be to use the [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/) and [OpenSearch Dashboards](https://aws.amazon.com/elasticsearch-service/the-elk-stack/kibana/) to collect, analyze, and display logs on AWS across multiple accounts and AWS Regions.

 **Common anti-patterns:**
+  You are asked by the network design team for current network bandwidth utilization rates. You provide the current metrics, network utilization is at 35%. They reduce circuit capacity as a cost savings measure causing widespread connectivity issues as your point-in-time measurement did not reflect the trend in utilization rates.
+  Your router has failed. It has been logging non-critical memory errors with greater and greater frequency up until its complete failure. You did not detect this trend and as a result did not replace the faulty memory before the router caused a service interruption.

 **Benefits of establishing this best practice:** By collecting and analyzing your workload metrics you gain understanding of the health of your workload and can gain insight to trends that may have an impact on your workload or the achievement of your business outcomes.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Collect and analyze workload metrics: Perform regular proactive reviews of metrics to identify trends and determine where appropriate responses are needed.
  +  [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
  +  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
  +  [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon Athena](https://aws.amazon.com/athena/)
+  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
+  [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html)
+  [AWS Glue](https://aws.amazon.com/glue/)
+  [AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html)
+  [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/)
+  [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/personal-health-dashboard/)
+  [Quick](https://aws.amazon.com/quicksight/)
+  [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
+  [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
