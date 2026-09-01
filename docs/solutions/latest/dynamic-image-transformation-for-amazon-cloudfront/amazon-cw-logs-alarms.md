---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/amazon-cw-logs-alarms.html
---

# Amazon CloudWatch Logs and Alarms
<a name="amazon-cw-logs-alarms"></a>

This solution captures application and service logs by creating CloudWatch log groups in your account. Log retention depends on the deployment architecture:
+  **Lambda architecture**: You control retention with the `LogRetentionPeriod` parameter. By default, logs are kept indefinitely and never expire. You can instead select any of the following retention periods, in days, which map to the CloudWatch `RetentionInDays` values: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, or 3653.
+  **ECS architecture**: Log retention is fixed at 10 years (3653 days) and is not configurable.

CloudWatch alarms help you monitor the solution’s functional and security assumptions are being followed. Following CloudWatch metrics can be leveraged with API Gateway to monitor client/server errors.

 [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html#cloudwatch-logs-features)

 [Amazon API Gateway dimensions and metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html)

 [Creating CloudWatch alarms to monitor API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring_automated_manual.html#creating_alarms)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
