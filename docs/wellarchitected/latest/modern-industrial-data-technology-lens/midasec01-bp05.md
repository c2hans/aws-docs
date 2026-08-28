---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp05.html
---

# MIDASEC01-BP05 Implement incident response playbooks
<a name="midasec01-bp05"></a>

 Develop and test incident response playbooks for common OT/IT scenarios such as device compromise, unauthorized access, and data exfiltration. Verify your cross-functional coordination and readiness to minimize downtime and safety risks.

 **Desired outcome:** Manufacturing organizations respond to incidents swiftly with predefined procedures, minimizing production disruption.

 **Benefits of establishing this best practice:** Improves MTTD and MTTR, reduces risk of safety events, and improves regulatory and audit outcomes.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-8"></a>

 Use AWS Systems Manager, AWS Lambda, and Amazon EventBridge to automate containment and response. Simulate scenarios to validate readiness.

### Implementation steps
<a name="implementation-steps-9"></a>
+  Identify critical incident types and build corresponding playbooks.
+  Use AWS Systems Manager Automation to orchestrate predefined remediation.
+  Run chaos experiments using AWS Fault Injection Service to test response efficacy.
+  Train IT and OT teams on roles and escalation procedures.

## Resources
<a name="resources-9"></a>

 **Related documents:**
+  [AWS Systems Manager Automation ](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/)
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
