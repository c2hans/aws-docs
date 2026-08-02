---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/monitor-alert.html
---

# Step 7. Implement backup monitoring and alerting
<a name="monitor-alert"></a>

Backup jobs can fail. A failed job, such as backup, restore, or copy task, might impact on subsequent steps in a process. When the initial backup job fails, there's a high probability that other succeeding tasks will also fail. In such a scenario, you can best understand the course of events through monitoring and notification. Monitoring and alerting can provide organizational awareness for your backup jobs, which helps you respond to backup failures.

Activating and configuring notifications to [monitor AWS Backup jobs](https://aws.amazon.com/blogs/storage/configuring-notifications-to-monitor-aws-backup-jobs/) provides the following benefits:
+ Gives you awareness of your backup activities
+ Helps ensure that you meet critical service-level agreements (SLAs)
+ Enhances your business-as-usual monitoring
+ Helps you meet compliance obligations

You can implement backup monitoring for your workloads by integrating AWS Backup with other AWS services and ticketing systems to perform automated investigation and escalation flows. For example, you can do the following:
+ Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track metrics, create alarms, and view dashboards.
+ Use [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to monitor AWS Backup processes and events.
+ Use [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to monitor [AWS Backup API](https://docs.aws.amazon.com/aws-backup/latest/devguide/api-reference.html) calls with detailed information on the time, source IP, users, and accounts making those calls.
+ Use [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) to subscribe to AWS Backup related topics such as backup, restore, and copy events.

You can use AWS Backup Audit Manager to automatically generate evidence of your daily [backup audit reports](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-audit-reports.html) for each account and Region. You can also scale your backup monitoring across multiple accounts by using a set of automation templates and dashboards (known as the backup observer solution) to obtain aggregated daily cross-account multi-Region [AWS Backup reporting](https://aws.amazon.com/blogs/storage/obtain-aggregated-daily-cross-account-multi-region-aws-backup-reporting/).
