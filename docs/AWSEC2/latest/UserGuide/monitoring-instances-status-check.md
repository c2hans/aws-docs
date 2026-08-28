---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check.html
---

# Monitor the status of your Amazon EC2 instances
<a name="monitoring-instances-status-check"></a>

You can monitor the status of your instances by viewing status checks and scheduled events for your instances.

A status check gives you the information that results from automated checks performed by Amazon EC2. These automated checks detect whether specific issues are affecting your instances. The status check information, together with the data provided by Amazon CloudWatch, gives you detailed operational visibility into each of your instances.

You can also see the status of specific events that are scheduled for your instances. The status of events provides information about upcoming activities that are planned for your instances, such as rebooting or retirement. They also provide the scheduled start and end time of each event.

**Topics**
+ [Status checks for Amazon EC2 instances](monitoring-system-instance-status-check.md)
+ [Application status checks](application-status-checks.md)
+ [State change events for Amazon EC2 instances](monitoring-instance-state-changes.md)
+ [Scheduled events for Amazon EC2 instances](monitoring-instances-status-check_sched.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
