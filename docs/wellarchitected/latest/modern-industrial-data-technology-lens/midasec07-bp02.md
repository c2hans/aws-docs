---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec07-bp02.html
---

# MIDASEC07-BP02 Implement SIEM systems
<a name="midasec07-bp02"></a>

 Aggregate and analyze logs from industrial and cloud systems using a security information and event management (SIEM) system to help detect and respond to threats efficiently.

 **Desired outcome:** Centralized visibility across hybrid environments enables faster detection of coordinated threats or unusual activities.

 **Benefits of establishing this best practice:** Improves threat correlation, reduces alert fatigue, and strengthens compliance with audit trails.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-27"></a>

 Use Amazon Security Lake or integrate with third-party SIEM tools such as Splunk or IBM QRadar for advanced analytics and incident workflows.

### Implementation steps
<a name="implementation-steps-28"></a>
+  Set up Amazon Security Lake to collect and normalize logs from AWS and industrial sources.
+  Integrate with a SIEM system for event correlation and alerting.
+  Define detection rules and dashboards tailored to OT and ICS environments.
+  Automate incident response workflows with runbooks or SOAR integrations.

## Resources
<a name="resources-28"></a>
+  [Amazon Security Lake](https://aws.amazon.com/security-lake/)
+  [AWS SIEM Partners ](https://aws.amazon.com/partners/siem/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
