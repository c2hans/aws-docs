---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp05.html
---

# HNSEC04-BP05 Allow only authorized personnel access to on-premises infrastructure
<a name="hnsec04-bp05"></a>

 Ensure that only authorized personnel have physical access to your on-premises networking infrastructure, such as data centers, server rooms, and network equipment. Implement strict access controls, logging, and monitoring to protect against unauthorized entry and physical tampering.

 **Desired outcome:** Prevent unauthorized physical access and tampering with critical hybrid network resources, supporting a robust security posture across both cloud and on-premises environments.

 **Level of risk exposed if this best practice is not established:** High

 **Benefits of establishing this best practice:**
+  Reduces risk of physical compromise or sabotage of network infrastructure
+  Supports regulatory compliance and audit requirements
+  Deters insider threats and unauthorized activity
+  Complement logical cloud security controls with physical safeguards

## Implementation guidance
<a name="implementation-guidance-21"></a>
+  Implement access control systems (for example, keycards and biometrics) for data center and server room entry.
+  Maintain visitor logs and conduct background checks for authorized personnel.
+  Use surveillance cameras and alarms to monitor critical physical locations.
+  Conduct regular audits and reviews of physical access records.
+  Establish clear procedures for visitor access and equipment removal or servicing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
