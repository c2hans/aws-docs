---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.gd.html
---

# Monitoring Aurora PostgreSQL Limitless Database with Amazon GuardDuty RDS Protection
<a name="limitless-monitoring.gd"></a>

Amazon GuardDuty is a threat detection service that helps protect your accounts, containers, workloads, and the data within your AWS environment. Using machine learning (ML) models, and anomaly and threat detection capabilities, GuardDuty continuously monitors different log sources and runtime activity to identify and prioritize potential security risks and malicious activities in your environment.

GuardDuty RDS Protection analyzes and profiles login events for potential access threats to your Amazon Aurora databases. When you turn on RDS Protection, GuardDuty consumes RDS login events from your Aurora databases. RDS Protection monitors these events and profiles them for potential insider threats or external actors.

For more information about GuardDuty RDS Protection in Aurora, see [Monitoring threats with Amazon GuardDuty RDS Protectionfor Amazon Aurora](guard-duty-rds-protection.md).

For more information about enabling GuardDuty RDS Protection, see [GuardDuty RDS Protection](https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html) in the *Amazon GuardDuty User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
