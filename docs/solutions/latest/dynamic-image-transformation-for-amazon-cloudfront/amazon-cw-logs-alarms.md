---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/amazon-cw-logs-alarms.html
---

# Amazon CloudWatch Logs and Alarms
<a name="amazon-cw-logs-alarms"></a>

This solution captures application and service logs by creating CloudWatch logs groups in your account. By default, logs are kept indefinitely and never expire. You can adjust the LogRetentionPeriod parameter for each log group, keeping the indefinite retention, or choosing a retention period between on day and 10 years based on your requirements.

CloudWatch alarms help you monitor the solution’s functional and security assumptions are being followed. Following CloudWatch metrics can be leveraged with API Gateway to monitor client/server errors.

 [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html#cloudwatch-logs-features)

 [Amazon API Gateway dimensions and metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html)

 [Creating CloudWatch alarms to monitor API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring_automated_manual.html#creating_alarms)
