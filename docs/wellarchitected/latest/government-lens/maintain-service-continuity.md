---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/maintain-service-continuity.html
---

# Maintain service continuity
<a name="maintain-service-continuity"></a>

 Particular government services must not have unexpected downtime due to the risk of immediate dangers to the quality of life for citizens, for example, emergency services, social welfare payments, policing systems, and healthcare services. Resilient architectures are key to support this design principle, and the people responsible for service delivery must take a risk-based approach to architectural decisions to support critical government services. Make deliberate use of the [AWS Well-Architected Framework Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) to inform your decision making.

 **Questions to ask:**
+  How will your system or service handle an attack or disruption? What backup options exist for users?
+  How will a disruption to service be detected and escalated proportionately to the risk and impact of the service?

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
