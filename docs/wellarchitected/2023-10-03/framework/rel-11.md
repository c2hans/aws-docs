---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/rel-11.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL 11. How do you design your workload to withstand component failures?
<a name="rel-11"></a>

Workloads with a requirement for high availability and low mean time to recovery (MTTR) must be architected for resiliency.

**Topics**
+ [REL11-BP01 Monitor all components of the workload to detect failures](rel_withstand_component_failures_monitoring_health.md)
+ [REL11-BP02 Fail over to healthy resources](rel_withstand_component_failures_failover2good.md)
+ [REL11-BP03 Automate healing on all layers](rel_withstand_component_failures_auto_healing_system.md)
+ [REL11-BP04 Rely on the data plane and not the control plane during recovery](rel_withstand_component_failures_avoid_control_plane.md)
+ [REL11-BP05 Use static stability to prevent bimodal behavior](rel_withstand_component_failures_static_stability.md)
+ [REL11-BP06 Send notifications when events impact availability](rel_withstand_component_failures_notifications_sent_system.md)
+ [REL11-BP07 Architect your product to meet availability targets and uptime service level agreements (SLAs)](rel_withstand_component_failures_service_level_agreements.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
