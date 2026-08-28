---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/rel-06.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL 6. How do you monitor workload resources?
<a name="rel-06"></a>

Logs and metrics are powerful tools to gain insight into the health of your workload. You can configure your workload to monitor logs and metrics and send notifications when thresholds are crossed or significant events occur. Monitoring allows your workload to recognize when low-performance thresholds are crossed or failures occur, so it can recover automatically in response.

**Topics**
+ [REL06-BP01 Monitor all components for the workload (Generation)](rel_monitor_aws_resources_monitor_resources.md)
+ [REL06-BP02 Define and calculate metrics (Aggregation)](rel_monitor_aws_resources_notification_aggregation.md)
+ [REL06-BP03 Send notifications (Real-time processing and alarming)](rel_monitor_aws_resources_notification_monitor.md)
+ [REL06-BP04 Automate responses (Real-time processing and alarming)](rel_monitor_aws_resources_automate_response_monitor.md)
+ [REL06-BP05 Analytics](rel_monitor_aws_resources_storage_analytics.md)
+ [REL06-BP06 Conduct reviews regularly](rel_monitor_aws_resources_review_monitoring.md)
+ [REL06-BP07 Monitor end-to-end tracing of requests through your system](rel_monitor_aws_resources_end_to_end.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
