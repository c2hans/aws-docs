---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/cloudwatch-alarms.html
---

# Amazon CloudWatch Alarms
<a name="cloudwatch-alarms"></a>

You can set up alarms using [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) based on the metrics collected by Amazon CloudWatch metrics. The alarm can then send a notification to Amazon SNS topic, or initiate Auto Scaling actions. An alarm requires period (length of the time to evaluate a metric), evaluation period (number of the most recent data points), and datapoints to alarm (number of data points within the evaluation period).
