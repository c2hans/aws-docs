---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp04.html
---

# MIDASEC01-BP04 Automate monitoring and reporting with cloud-ready compliance tools
<a name="midasec01-bp04"></a>

 Automate the collection, evaluation, and reporting of compliance evidence using AWS Cloud tools. Tailor configurations to meet industry-specific regulatory requirements such as NIST, CMMC, or ISO and IEC standards for manufacturing.

 **Desired outcome:** Ongoing compliance posture monitoring and reduced manual effort in security and audit processes.

 **Benefits of establishing this best practice:** Improves audit readiness, reduces cost and error in manual compliance efforts, and verifies continuous governance.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-7"></a>

 Establish manufacturing compliance baselines by documenting the required controls for industrial systems and mapping them to technical implementations.

 Then, implement automated monitoring that evaluates industrial system configurations, tracks security control changes, and validates compliance with manufacturing standards.

 Use AWS Config, Security Hub CSPM, and Audit Manager, configured specifically for manufacturing environments, to continuously monitor both IT and OT systems while maintaining required compliance evidence.

### Implementation steps
<a name="implementation-steps-8"></a>
+  Enable AWS Config across all Regions and accounts.
+  Use AWS Security Hub CSPM to aggregate security findings.
+  Map controls in AWS Audit Manager to your industry framework.
+  Schedule automated compliance report generation and alerting.

## Resources
<a name="resources-8"></a>

 **Related documents:**
+  [ What Is AWS Config? ](https://docs.aws.amazon.com/config/latest/developerguide/what-is-aws-config.html)
+  [ What is AWS Security Hub? ](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
+  [ What is AWS Audit Manager? ](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
