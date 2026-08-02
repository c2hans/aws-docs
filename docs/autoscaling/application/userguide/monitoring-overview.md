---
source_url: https://docs.aws.amazon.com/autoscaling/application/userguide/monitoring-overview.html
---

# Monitoring Application Auto Scaling
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of Application Auto Scaling and your other AWS solutions. You should collect monitoring data from all parts of your AWS solution so that you can more easily debug a multi-point failure if one occurs. AWS provides monitoring tools to watch Application Auto Scaling, report when something is wrong, and take automatic actions when appropriate.

You can use the following features to help you manage your AWS resources:

**AWS CloudTrail**
With AWS CloudTrail, you can track the calls made to the Application Auto Scaling API by or on behalf of your AWS account. CloudTrail stores the information in log files in the Amazon S3 bucket that you specify. You can identify which users and accounts called Application Auto Scaling, the source IP address from which the calls were made, and when the calls occurred. For more information, see [Log Application Auto Scaling API calls using AWS CloudTrail](logging-using-cloudtrail.md).
For information about other AWS services that can help you log and collect data about your workloads, see the [Logging and monitoring guide for application owners](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/introduction.html) guide in the *AWS Prescriptive Guidance*.

**Amazon CloudWatch**
Amazon CloudWatch helps you analyze logs and, in real time, monitor the metrics of your AWS resources and hosted applications. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track resource utilization and notify you when utilization is very high or when the metric's alarm has gone into the `INSUFFICIENT_DATA` state. For more information, see [Monitor usage of scalable resources using CloudWatch](monitoring-cloudwatch.md).
CloudWatch also tracks AWS API usage metrics for Application Auto Scaling. You can use these metrics to configure alarms that alert you when your API call volume violates a threshold that you define. For more information, see [AWS usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AWS-API-Usage-Metrics.html) in the *Amazon CloudWatch User Guide*.

**Amazon EventBridge**
Amazon EventBridge is a serverless event bus service that makes it easy to connect your applications with data from a variety of sources. EventBridge delivers a stream of real-time data from your own applications, Software-as-a-Service (SaaS) applications, and AWS services and routes that data to targets such as Lambda. This lets you monitor events that happen in services, and build event-driven architectures. For more information, see [Monitor Application Auto Scaling events using Amazon EventBridge](monitoring-eventbridge.md).

**AWS Health Dashboard**
The Health Dashboard (PHD) displays information, and also provides notifications that are invoked by changes in the health of AWS resources. The information is presented in two ways: on a dashboard that shows recent and upcoming events organized by category, and in a full event log that shows all events from the past 90 days. For more information, see [Getting started with your Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-health-dashboard.html).
