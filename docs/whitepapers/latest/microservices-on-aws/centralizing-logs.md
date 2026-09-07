---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/centralizing-logs.html
---

# Centralizing logs
<a name="centralizing-logs"></a>

 Logging is key to pinpoint and resolve issues. With microservices, you can release more frequently and experiment with new features. AWS provides services like Amazon S3, CloudWatch Logs, and Amazon OpenSearch Service to centralize log files. Amazon EC2 uses a daemon for sending logs to CloudWatch, while Lambda and Amazon ECS natively send their log output there. For Amazon EKS, either [Fluent Bit or Fluentd can be used](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-logs.html) to forward logs to CloudWatch for reporting using OpenSearch and Kibana. However, due to the smaller footprint and [performance advantages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-logs.html), Fluent Bit is recommended over Fluentd.

 Figure 12 illustrates how logs from various AWS services are directed to Amazon S3 and CloudWatch. These centralized logs can be further analyzed using Amazon OpenSearch Service, inclusive of Kibana for data visualization. Also, Amazon Athena can be employed for ad hoc queries against the logs stored in Amazon S3.

![Diagram showing logging capabilities of AWS services](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/logging-capabilities.png)
