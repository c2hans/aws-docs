---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/alerting.html
---

# Alerting
<a name="alerting"></a>

Alerts are one of the most important information sources when it comes to the security, availability, performance, and reliability of your IT infrastructure and IT services. They notify and inform your IT teams about ongoing security threats, outages, performance issues, or system failures.

The Information Technology Infrastructure Library (ITIL), specifically IT service management (ITSM) practices, set automated alerting at the focal point of *monitoring and event management *and* incident management *best practices.

Incident alerting is when monitoring tools generate alerts to notify your team and automated tools (for items that are automatically actionable) about changes, high-risk actions, or failures in the IT environment. IT alerts are the first line of defense against system outages or changes that can turn into major incidents. By automatically monitoring systems and generating alerts for outages and risky changes, IT teams can minimize downtime and reduce the high cost that comes with it.

As best practices, the AWS Well-Architected Framework prescribes that you [use monitoring to generate alarm-based notifications](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf_monitor_instances_post_launch_generate_alarms.html), and [monitor and alarm proactively](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf_monitor_instances_post_launch_proactive.html). Use CloudWatch or a third-party monitoring service to set alarms that indicate when metrics are outside of expected boundaries.

The purpose of alert management is to establish efficient, standardized procedures for handling IT-related events and incidents through logging, classification, action definition and implementation, closure, and post-incident review activities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
