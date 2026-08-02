---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/monitor-the-solution.html
---

# Monitor the solution
<a name="monitor-the-solution"></a>

This solution defines several CloudWatch alarms to monitor its health and performance. Each alarm has a fixed threshold or an anomaly-based threshold that causes state to transit between `OK` and `ALARM`. Review the full list of alarms with details in the [Amazon CloudWatch Alarms](traffic-monitoring.md#amazon-cloudwatch-alarms) section. You can view the alarms in the Amazon CloudWatch console and configure alarm notifications as needed after stack deployment. For general information about CloudWatch alarms and alarm actions, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

All compute resources in this solution send log information to CloudWatch Logs. These logs are available in CloudWatch for querying and searching in real time. This solution uses CloudTrail to track S3 and Lambda API activities with [data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html). The CloudTrail log files are stored in an S3 bucket, and the event history can be viewed in CloudTrail.

 [CloudFront access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) are configured to create log files containing information about user requests initiated to the solution’s CloudFront distribution. To analyze the access logs in Amazon Athena, see [Querying Amazon CloudFront logs](https://docs.aws.amazon.com/athena/latest/ug/cloudfront-logs.html) in the *Amazon Athena User Guide*.

Prebid Server tasks running in the ECS cluster output the runtime logs into the mounted Amazon Elastic File System which is shared across containers, and store the log data long-term in S3. For more information about Prebid Server logs, see the [Logging](logging.md) section.

You can monitor how the ECS resources in this solution are performing using the cluster and service metrics that are available in the Amazon ECS console. To view these metrics, follow the steps in [Viewing Amazon ECS metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/viewing_cloudwatch_metrics.html) in the *Amazon ECS Developer Guide*.

This solution associates a web ACL with the CloudFront distribution to prevent DDoS attacks against the Prebid Server cluster. Users can access near real-time summaries of the traffic that the web ACL evaluates in the web ACL’s **Traffic overview** tab on the AWS WAF console. For details, see [Web ACL traffic overview dashboards](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-dashboards.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
