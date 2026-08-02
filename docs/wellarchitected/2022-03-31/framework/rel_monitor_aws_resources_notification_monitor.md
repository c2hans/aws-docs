---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_monitor_aws_resources_notification_monitor.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL06-BP03 Send notifications (Real-time processing and alarming)
<a name="rel_monitor_aws_resources_notification_monitor"></a>

 Organizations that need to know, receive notifications when significant events occur.

 Alerts can be sent to Amazon Simple Notification Service (Amazon SNS) topics, and then pushed to any number of subscribers. For example, Amazon SNS can forward alerts to an email alias so that technical staff can respond.

 **Common anti-patterns:**
+  Configuring alarms at too low of threshold, causing too many notifications to be sent.
+  Not archiving alarms for future exploration.

 **Benefits of establishing this best practice:** Notifications on events (even those that can be responded to and automatically resolved) allow you to have a record of events and potentially address them in a different manner in the future.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Perform real-time processing and alarming. Organizations that need to know, receive notifications when significant events occur
  +  Amazon CloudWatch dashboards are customizable home pages in the CloudWatch console that you can use to monitor your resources in a single view, even those resources that are spread across different Regions.
    +  [Using Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
  +  Create an alarm when the metric surpasses a limit.
    +  [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [One Observability Workshop](https://observability.workshop.aws/)
+  [The Amazon Builders' Library: Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/)
+  [Using Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
+  [Using Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
+  [Using Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
