---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel-13.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL 13  How do you plan for disaster recovery (DR)?
<a name="rel-13"></a>

Having backups and redundant workload components in place is the start of your DR strategy. [RTO and RPO are your objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html) for restoration of your workload. Set these based on business needs. Implement a strategy to meet these objectives, considering locations and function of workload resources and data. The probability of disruption and cost of recovery are also key factors that help to inform the business value of providing disaster recovery for a workload.

**Topics**
+ [REL13-BP01 Define recovery objectives for downtime and data loss](rel_planning_for_recovery_objective_defined_recovery.md)
+ [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel_planning_for_recovery_disaster_recovery.md)
+ [REL13-BP03 Test disaster recovery implementation to validate the implementation](rel_planning_for_recovery_dr_tested.md)
+ [REL13-BP04 Manage configuration drift at the DR site or Region](rel_planning_for_recovery_config_drift.md)
+ [REL13-BP05 Automate recovery](rel_planning_for_recovery_auto_recovery.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
