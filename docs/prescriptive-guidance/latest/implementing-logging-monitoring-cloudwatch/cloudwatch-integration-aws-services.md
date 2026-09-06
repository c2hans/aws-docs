---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-integration-aws-services.html
---

# CloudWatch integration with AWS services
<a name="cloudwatch-integration-aws-services"></a>

AWS provides many services that include additional configuration options for logging and metrics. These services often enable you to configure CloudWatch Logs for log output and CloudWatch metrics for metrics output. The underlying infrastructure used to provide these services is managed by AWS and is inaccessible, but you can use the logging and metric options for your provisioned services to gain further insights and troubleshoot issues. For example, you can publish [VPC flow logs to CloudWatch](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html), or you can also [configure Amazon Relational Database Service (Amazon RDS) instances to publish logs to CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/publishing_cloudwatchlogs.html).

Most AWS services log their API calls with [integration to AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html). CloudTrail also [supports integration with CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html) and this means that you can search and analyze activity in AWS services. You can also use Amazon EventBridge to create and configure automation and notifications with event rules for specific actions performed in AWS services. Certain services [integrate directly](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html) with EventBridge. You can also [create events delivered through CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html#events-for-services-not-listed).
