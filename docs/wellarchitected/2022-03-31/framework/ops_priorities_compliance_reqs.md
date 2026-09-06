---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_priorities_compliance_reqs.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS01-BP04 Evaluate compliance requirements
<a name="ops_priorities_compliance_reqs"></a>

 Evaluate external factors, such as regulatory compliance requirements and industry standards, to ensure that you are aware of guidelines or obligations that might mandate or emphasize specific focus. If no compliance requirements are identified, ensure that you apply due diligence to this determination.

 **Common anti-patterns:**
+  You are being audited and are asked to provide proof of compliance with industry regulations. You have no idea if you are compliant because you have never evaluated what your compliance requirements are.
+  Your administrative account has been compromised resulting in the download of customer data and damaged to customer trust. Your industry best practices require the use of MFA to secure administrative accounts. You did not secure your administrative account with MFA and subject to litigation by your customers.

 **Benefits of establishing this best practice:** Evaluating and understanding the compliance requirements that apply to your workload will inform how you prioritize your efforts to deliver business value.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Understand compliance requirements: Evaluate external factors, such as regulatory compliance requirements and industry standards, to ensure that you are aware of guidelines or obligations that might mandate or emphasize specific focus. If no compliance requirements are identified, ensure that due diligence was applied to the determination.
  +  Understand regulatory compliance requirements: Identify regulatory compliance requirements that you are legally obligated to satisfy. Use these requirements to focus your efforts. Examples include obligations from privacy and data protection acts.
    +  [AWS Compliance](https://aws.amazon.com/compliance/)
    +  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
    +  [AWS Compliance Latest News](https://aws.amazon.com/compliance/compliance-latest-news/)
  +  Understand industry standards and best practices: Identify industry standards and best practice requirements that apply to your workload, such as the Payment Card Industry Data Security Standard (PCI DSS). Use these requirements to focus your efforts.
    +  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
  +  Understand internal compliance requirements: Identify compliance requirements and best practices that are established by your organization. Use these requirements to focus your efforts. Examples include information security policies and data classification standards.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Cloud Compliance](https://aws.amazon.com/compliance/)
+  [AWS Compliance](https://aws.amazon.com/compliance/)
+  [AWS Compliance Latest News](https://aws.amazon.com/compliance/compliance-latest-news/)
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
