---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-incident-response.html
---

# 8. Incident response and business continuity for agentic AI systems on AWS
<a name="best-practices-incident-response"></a>

Like most existing enterprise technologies, a [business continuity plan](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html) is vital to manage organizational risk. Agentic AI systems require the same level of planning and care as traditional technology systems. However, as these systems begin to take on human-like activities, an additional risk might emerge where human operators are no longer adequately skilled to handle the workloads of agentic AI systems in a failure scenario.

**This section contains the following best practices:**
+ [8.1 Implement comprehensive operational observability (AI-specific)](#best-practices-8-operational-observability)
+ [8.2 Establish emergency shutdown capabilities for high-risk scenarios (General)](#best-practices-8-emergency-shutdown)
+ [8.3 Maintain business continuity plans for critical operations (General)](#best-practices-8-continuity-plans)
+ [8.4 Implement recovery methods within acceptable timeframes (General)](#best-practices-8-recovery-methods)

## 8.1 Implement comprehensive operational observability (AI-specific)
<a name="best-practices-8-operational-observability"></a>

Deploy observability capabilities that determine whether systems are operating outside acceptable bounds. This enables early detection of security incidents or system malfunctions. Monitor for unacceptable scenarios, including the generation of harmful or offensive content, system outcomes that demonstrate bias or unintended preferences, decreased user satisfaction, unexpected system interaction or usage patterns, privacy violations, and regulatory compliance breaches. Where real-time detective or preventative measures are not feasible, post-operation detective controls can be a suitable alternative. This might involve regular scanning of collated logs with the aim to identify anomalous activity, such as a sudden increase in a particular activity or a slow shift to the baseline.

## 8.2 Establish emergency shutdown capabilities for high-risk scenarios (General)
<a name="best-practices-8-emergency-shutdown"></a>

Implement immediate system shutdown capabilities, including an emergency response process that can roll back to stable versions, disable functionality, or move to safe mode when security threats are detected. Document business processes to shut down any system that is deemed high risk to the organization, and provide clear procedures for emergency response situations.

## 8.3 Maintain business continuity plans for critical operations (General)
<a name="best-practices-8-continuity-plans"></a>

Establish acceptable business continuity plans to support critical business operations while agentic AI systems are offline. This ensures that business functions can continue during security incidents. If you are building business-critical processes with AI, make sure that you establish safe fallback systems and staff to maintain essential operations.

## 8.4 Implement recovery methods within acceptable timeframes (General)
<a name="best-practices-8-recovery-methods"></a>

The AWS Well-Architected Framework recommends that you [automate recovery](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_auto_recovery.html) and that you [define recovery objectives for downtime and data loss](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_planning_for_recovery_objective_defined_recovery.html). Deploy recovery methods that allow for remediation of degraded systems within business-acceptable timeframes, and balance security responses with operational requirements.
