---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.html
---

# AWS services for logging and monitoring
<a name="aws-services-logging-monitoring"></a>

This guide focuses on logging and monitoring applications deployed in the AWS Cloud. You can use AWS services to implement your logging and monitoring plan, or you can use them to augment your current solutions. For example, if you are troubleshooting an issue with your application, you might:
+ Triage the application logs with the VPC Flow Logs feature in Amazon Virtual Private Cloud (Amazon VPC) and view the network traffic that corresponds to the issue.
+ Use AWS CloudTrail to view the API calls that correspond to the issue event times.
+ Review the logs in Amazon CloudWatch Logs to check for CPU spikes that correspond to the issue event times.

You can deploy the following AWS services and features for logging and monitoring your application:
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account by recording the actions taken by a user, role, or an AWS service. For more information about using this service to log or monitor events for your application, see [AWS CloudTrail](cloudtrail.md) in this guide.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you analyze logs and, in real time, monitor the metrics of your AWS resources and hosted applications. You can also use the ServiceLens feature to monitor the health of your application or use the Synthetics feature to create canaries that monitor your endpoints and APIs. For more information about using this service to monitor your application, see [Amazon CloudWatch](cloudwatch.md) in this guide.
+ [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) helps you centralize the logs from all your systems, applications, and AWS services so you can monitor them and archive them securely. For more information about using this service to log events for your application, see [Amazon CloudWatch Logs](cloudwatch-logs.md) in this guide.
+ The [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) feature of Amazon Virtual Private Cloud (Amazon VPC) captures information about the IP traffic going to and from network interfaces in your VPC. For more information about using this service to log events for your application, see [VPC Flow Logs](vpc-flow-logs.md) in this guide.
+ [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) collects data about requests that your application serves, and it helps you view, filter, and gain insights into that data to identify issues and opportunities for optimization. For more information about using this service to monitor your application, see [AWS X-Ray](x-ray.md) in this guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
