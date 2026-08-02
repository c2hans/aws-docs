---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-logs.html
---

# Application logs
<a name="application-logs"></a>

Centralized Logging with OpenSearch supports ingesting application logs from the following log sources:
+  [Instance Group](instance-group.md): the solution automatically installs a log agent (Fluent Bit 1.9), collects application logs on EC2 instances and then sends logs into Amazon OpenSearch Service.
+  [Amazon EKS cluster](amazon-eks-cluster.md): the solution generates all-in-one configuration file for customers to deploy the log agent (Fluent Bit 1.9) as a DaemonSet or Sidecar. After the log agent is deployed, the solution starts collecting pod logs and sends them to Amazon OpenSearch Service.
+  [Amazon S3](amazon-s3.md): the solution either ingests logs in the specified Amazon S3 location continuously or performs one-time ingestion. You can also filter logs based on Amazon S3 prefix or parse logs with custom Log Config.
+  [Syslog](syslog.md): the solution collects syslog logs through UDP or TCP protocol.

After creating a log analytics pipeline, you can add more log sources to the log analytics pipeline. For more information, see [add a new log source](log-sources.md#add-a-new-log-source).
+ Important If you are using Centralized Logging with OpenSearch to create an application log pipeline for the first time, you are recommended to learn the [concepts](solution-overview.md#concepts) and supported log formats and log sources.
