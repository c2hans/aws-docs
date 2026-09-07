---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-search-analysis.html
---

# Searching and analyzing logs in CloudWatch
<a name="cloudwatch-search-analysis"></a>

After your logs and metrics are captured into a consistent format and location, you can search and analyze them to help improve operational efficiency, in addition to identifying and troubleshooting issues. We recommend that you capture your logs in a well-formed format (for example, JSON) to make it easier to search and analyze your logs. Most workloads use a collection of AWS resources such as network, compute, storage, and databases. Where possible, you should collectively analyze the metrics and logs from these resources and correlate them in order to effectively monitor and manage all of your AWS workloads.

CloudWatch provides several features to help analyze logs and metrics, such as [CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) to collectively define and monitor metrics and logs for an application across different AWS resources, [CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) to surface anomalies for your metrics, and [CloudWatch Log Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to interactively search and analyze your log data in CloudWatch Logs.

## Collectively monitor and analyze applications with CloudWatch Application Insights
<a name="monitor-application-insights-cloudwatch"></a>

Application owners can use Amazon CloudWatch Application Insights to set up automatic monitoring and analysis for workloads. This can be configured in addition to standard systems-level monitoring configured for all workloads in an account. Setting up monitoring through CloudWatch Application Insights can also help application teams proactively align to operations and reduce mean time to recovery (MTTR). CloudWatch Application Insights can help reduce the effort required to establish application-level logging and monitoring. It also provides a component-based framework that assists teams in dividing logging and monitoring responsibilities.

CloudWatch Application Insights uses resource groups to identify the resources that should be collectively monitored as an application. The supported resources in the resource group become individually defined components of your CloudWatch Application Insights application. Each component of your CloudWatch Application Insights application has its own logs, metrics, and alarms.

For logs, you define the log pattern set that should be used for the component and within your CloudWatch Application Insights application. A log pattern set is a collection of log patterns to search for based on regular expressions, along with a low, medium, or high severity for when the pattern is detected. For metrics, you choose the metrics to monitor for each component from a list of service-specific and supported metrics. For alarms, CloudWatch Application Insights automatically creates and configures standard or anomaly detection alarms for the metrics being monitored. CloudWatch Application Insights has automatic configurations for metrics and log capture for the technologies outlined in the [Logs and metrics supported by CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-logs-and-metrics.html) in the CloudWatch documentation. The following diagram shows the relationships between CloudWatch Application Insights components and their logging and monitoring configurations. Each component has defined its own logs and metrics to monitor using CloudWatch logs and metrics.

![Process flow between AWS Resource Group, log groups, existing alarms, and new AutoConfigured alarms.](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/images/guide-img/b9e7cf06-b902-4bab-ad2d-f312917302bd/images/86763c83-20f9-491e-9568-0d7b4b1ce46b.png)

EC2 instances monitored by CloudWatch Application Insights require Systems Manager and CloudWatch agents and permissions. For more information about this, see [Prerequisites to configure an application with CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-prereqs.html) in the CloudWatch documentation. CloudWatch Application Insights uses Systems Manager to install and update the CloudWatch agent. The metrics and logs configured in CloudWatch Application Insights create a CloudWatch agent configuration file that is stored in a Systems Manager parameter with the `AmazonCloudWatch-ApplicationInsights-SSMParameter` prefix for each CloudWatch Application Insights component. This results in a separate CloudWatch agent configuration file being added to the CloudWatch agent configuration directory on the EC2 instance. A Systems Manager command is run to append this configuration to the active configuration on the EC2 instance. Using CloudWatch Application Insights doesn't impact existing CloudWatch agent configuration settings. You can use CloudWatch Application Insights in addition to your own system and application-level CloudWatch agent configurations. However, you should ensure that the configurations don't overlap.

## Performing log analysis with CloudWatch Logs Insights
<a name="log-analysis-cloudwatch-insights"></a>

CloudWatch Logs Insights makes it easy to search multiple log groups by using a simple query language. If your application logs are structured in JSON format, CloudWatch Logs Insights automatically discovers the JSON fields across your log streams in multiple log groups. You can use CloudWatch Logs Insights to analyze your application and system logs, which saves your queries for future use. The query syntax for CloudWatch Logs Insights supports functions such as aggregation with functions, for example, sum(), avg(), count(), min(), and max(), that can be helpful for troubleshooting your applications or performance analysis.

If you use the embedded metric format to create CloudWatch metrics, you can query your embedded metric format logs to generate one-time metrics by using the supported aggregation functions. This helps reduce your CloudWatch monitoring costs by capturing data points necessary to generate specific metrics on an as-needed basis, instead of actively capturing them as custom metrics. This is especially effective for dimensions with high cardinality that would result in a large number of metrics. CloudWatch Container Insights also takes this approach and captures detailed performance data but only generates CloudWatch metrics for a subset of this data.

For example, the following embedded metric entry only generates a limited set of CloudWatch metrics from the metric data that is captured in the embedded metric format statement:

```
{
 "AutoScalingGroupName": "eks-e0bab7f4-fa6c-64ba-dbd9-094aee6cf9ba",
 "CloudWatchMetrics": [
 {
 "Metrics": [
 {
 "Unit": "Count",
 "Name": "pod_number_of_container_restarts"
 }
 ],
 "Dimensions": [
 [
 "PodName",
 "Namespace",
 "ClusterName"
 ]
 ],
 "Namespace": "ContainerInsights"
 }
 ],
 "ClusterName": "eksdemo",
 "InstanceId": "i-03b21a16b854aa4ca",
 "InstanceType": "t3.medium",
 "Namespace": "amazon-cloudwatch",
 "NodeName": "ip-172-31-10-211.ec2.internal",
 "PodName": "cloudwatch-agent",
 "Sources": [
 "cadvisor",
 "pod",
 "calculated"
 ],
 "Timestamp": "1605111338968",
 "Type": "Pod",
 "Version": "0",
 "pod_cpu_limit": 200,
 "pod_cpu_request": 200,
 "pod_cpu_reserved_capacity": 10,
 "pod_cpu_usage_system": 3.268605094109382,
 "pod_cpu_usage_total": 8.899539221131045,
 "pod_cpu_usage_user": 4.160042847048305,
 "pod_cpu_utilization": 0.44497696105655227,
 "pod_cpu_utilization_over_pod_limit": 4.4497696105655224,
 "pod_memory_cache": 4096,
 "pod_memory_failcnt": 0,
 "pod_memory_hierarchical_pgfault": 0,
 "pod_memory_hierarchical_pgmajfault": 0,
 "pod_memory_limit": 209715200,
 "pod_memory_mapped_file": 0,
 "pod_memory_max_usage": 43024384,
 "pod_memory_pgfault": 0,
 "pod_memory_pgmajfault": 0,
 "pod_memory_request": 209715200,
 "pod_memory_reserved_capacity": 5.148439982463127,
 "pod_memory_rss": 38481920,
 "pod_memory_swap": 0,
 "pod_memory_usage": 42803200,
 "pod_memory_utilization": 0.6172094650851303,
 "pod_memory_utilization_over_pod_limit": 11.98828125,
 "pod_memory_working_set": 25141248,
 "pod_network_rx_bytes": 3566.4174629544723,
 "pod_network_rx_dropped": 0,
 "pod_network_rx_errors": 0,
 "pod_network_rx_packets": 3.3495665260575094,
 "pod_network_total_bytes": 4283.442421354973,
 "pod_network_tx_bytes": 717.0249584005006,
 "pod_network_tx_dropped": 0,
 "pod_network_tx_errors": 0,
 "pod_network_tx_packets": 2.6964010534762948,
 "pod_number_of_container_restarts": 0,
 "pod_number_of_containers": 1,
 "pod_number_of_running_containers": 1,
 "pod_status": "Running"
}
```

However, you can query the captured metrics to gain further insights. For example, you can run the following query to see the latest 20 pods with memory page faults:

```
fields @timestamp, @message
| filter (pod_memory_pgfault > 0)
| sort @timestamp desc
| limit 20
```

## Performing log analysis with Amazon OpenSearch Service
<a name="log-analysis-amazon-es"></a>

CloudWatch integrates with [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) by enabling you to stream log data from CloudWatch log groups to an Amazon OpenSearch Service cluster of your choice with a [subscription filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_ES_Stream.html). You can use CloudWatch for primary log and metrics capture and analysis, and then augment it with Amazon OpenSearch Service for the following use cases:
+ **Fine-grained data access control** – Amazon OpenSearch Service enables you to limit access to data down to the field level and helps anonymize data in fields based on user permissions. This is useful if you want support troubleshooting without exposing sensitive data.
+ **Aggregate and search logs across multiple accounts, Regions, and infrastructure** – You can stream your logs from multiple accounts and Regions into a common Amazon OpenSearch Service cluster. Your centralized operations teams can analyze trends, issues, and perform analytics across accounts and Regions. Streaming CloudWatch logs to Amazon OpenSearch Service also helps you search and analyze a multi-Region application in a central location.
+ **Ship and enrich logs directly to Amazon OpenSearch Service by using ElasticSearch agents** – Your application and technology stack components can use OSs that are not supported by the CloudWatch agent. You might also want to enrich and transform log data before it is shipped to your logging solution. Amazon OpenSearch Service supports standard Elasticsearch clients such as the [Elastic Beats family data shippers](https://www.elastic.co/beats/) and [Logstash](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-logstash.html) that support log enrichment and transformation before sending the log data to Amazon OpenSearch Service.
+ **Existing operations management solution uses an **[**ElasticSearch, Logstash, Kibana**](https://www.elastic.co/elastic-stack?ultron=B-Stack-Trials-AMER-US-W-Exact&gambit=Elasticsearch-ELK&blade=adwords-s&hulk=cpc&Device=c&thor=elk%20elasticsearch%20logstash%20kibana&gclid=EAIaIQobChMI3raE5vWK8AIVTT6tBh2idgBbEAAYASAAEgKsoPD_BwE)

** (ELK) Stack for logging and monitoring** – You might already have a significant investment in Amazon OpenSearch Service or open-source Elasticsearch with many workloads already configured. You might also have operational dashboards that have been created in [Kibana](https://www.elastic.co/kibana) that you want to continue to use.

If you don't plan to use CloudWatch logs, you can use Amazon OpenSearch Service supported agents, log drivers, and libraries (for example, Fluent Bit, Fluentd, [logstash](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-logstash.html), and the [Open Distro for ElasticSearch API](https://opendistro.github.io/for-elasticsearch-docs/docs/elasticsearch/popular-api/)

) to ship your logs directly to Amazon OpenSearch Service and bypass CloudWatch. However, you should also implement a solution to capture logs generated by AWS services. CloudWatch Logs is the primary log capture solution for many AWS services and multiple services automatically create new log groups in CloudWatch. For example, Lambda creates a new log group for every Lambda function. You can set up a subscription filter for a log group to stream its logs to Amazon OpenSearch Service. You can manually configure a subscription filter for each individual log group that you want to stream to Amazon OpenSearch Service. Alternatively, you can deploy a solution that automatically subscribes new log groups to ElasticSearch clusters. You can stream logs to an ElasticSearch cluster in the same account or a centralized account. Streaming logs to an ElasticSearch cluster in the same account helps workload owners to better analyze and support their workloads.

You should consider setting up an ElasticSearch cluster in a centralized or shared account for aggregating logs across your accounts, Regions, and applications. For example, AWS Control Tower sets up a Log Archive account that is used for centralized logging. When a new account is created in AWS Control Tower, its AWS CloudTrail and AWS Config logs are delivered to an S3 bucket in this centralized account. The logging instrumented by AWS Control Tower is for configuration, change, and audit logging.

To establish a centralized application log analysis solution with Amazon OpenSearch Service, you can deploy one or more centralized Amazon OpenSearch Service clusters to your centralized logging account and configure log groups in your other accounts to stream logs to the centralized Amazon OpenSearch Service clusters.

You can create separate Amazon OpenSearch Service clusters to handle different applications or layers of your cloud architecture that might be distributed across your accounts. Using separate Amazon OpenSearch Service clusters helps you reduce your security and availability risk and having a common Amazon OpenSearch Service cluster can make it easier to search and relate data within the same cluster.
