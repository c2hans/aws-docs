---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec08-bp01.html
---

# MIDASEC08-BP01 Align security controls with industry standards
<a name="midasec08-bp01"></a>

 Implement security controls across industrial workloads, and map those controls to recognized industry standards such as NIST 800-82, ISO/IEC 27001, and IEC 62443.

 **Desired outcome:** Security implementations are auditable, and your organization improves its compliance with applicable industrial regulations.

 **Benefits of establishing this best practice:** Streamlines audit processes, standardizes your security practices, and demonstrates due diligence in regulated industries.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-28"></a>

 Use AWS Audit Manager and AWS Control Tower to align cloud configurations with industry-standard security frameworks.

### Implementation steps
<a name="implementation-steps-29"></a>
+  Identify regulatory and industry-specific frameworks applicable to your workloads.
+  Map AWS services and controls to required standards using AWS Audit Manager frameworks.
+  Continuously monitor control adherence using AWS Config and Security Hub CSPM.
+  Integrate compliance requirements into the CI/CD process for industrial apps.

## Resources
<a name="resources-29"></a>
+  [ What is AWS Audit Manager? ](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)
+  [ Security standards and controls reference ](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
