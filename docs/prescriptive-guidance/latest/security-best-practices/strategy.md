---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/strategy.html
---

# Step 1. Implement a backup strategy
<a name="strategy"></a>

A comprehensive backup strategy is an essential part of an organization's data protection plan to withstand, recover from, and reduce any impact that might be sustained because of a security event. Create an extensive backup strategy that defines which data must be backed up, how often data must be backed up, and how backup and recovery tasks will be monitored.

When you develop a comprehensive strategy for backing up and restoring data, first identify interruptions that might occur, and their potential business impact.

Your objective is to build a recovery strategy that brings your workload back up or avoids downtime within the acceptable [recovery objectives](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html#recovery-objectives-rto-and-rpo), Recovery Time Objective (RTO) and Recovery Point Objective (RPO). RTO is the acceptable delay between the interruption of service and restoration of service. RPO is the acceptable amount of time since the last data recovery point. Consider a granular backup strategy that includes all of the following:
+ Continuous backup cadence
+ Point-in-Time Recovery (PITR)
+ File-level recovery
+ Application data–level recovery
+ Volume-level recovery
+ Instance-level recovery

## Ransomware
<a name="ransomware.952a1367-c70e-513b-9d16-179156f9ec40"></a>

A well-designed backup strategy should include actions that can protect and recover your resources from [ransomware](https://aws.amazon.com/blogs/security/ransomware-mitigation-top-5-protections-and-recovery-preparation-actions/), with detailed recovery requirements for your applications and their data dependencies. For example, while you establish preventive and detective controls to mitigate the risk of ransomware, make sure that you also design the appropriate level of granularity for cross-AWS Region or cross-account copy and restore patterns, to ensure that administrators do not restore corrupt backup data after the security event.

## Retention requirements
<a name="retention-requirements.74493df6-7fc3-5777-9bf0-7e563e9a1b4f"></a>

In some industries, when developing a backup strategy, you must also consider the regulations for data retention requirements. Make sure that your backup strategy is designed with retention requirements that are sufficient to meet your regulatory needs for each data classification level and resource type.

## Compliance
<a name="compliance.3669139b-14f5-5d77-a879-a85434a165c3"></a>

Consult your security compliance teams to validate whether your backup resources and operations should be included in or segmented from the scope of your compliance programs. Including backup and recovery as a critical part of your security program will help you understand where data is across your environment and appropriately define compliance scope.

For architectural best practices for designing and operating reliable, secure, efficient, and cost-effective workloads in the cloud, see [Backup and recovery approaches using AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/welcome.html) and [ Reliability Pillar – AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
