---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp02.html
---

# RAIBR03-BP02 Identify the severity of each potential harm
<a name="raibr03-bp02"></a>

 Risk severity estimates the magnitude of the negative on affected stakeholder groups if it were to occur. Severity also considers the reversibility of harm, recognizing that some types of harm may be permanent or difficult to remedy.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-21"></a>

1.  Create standardized severity scale with clear impact levels. For example, establish a range from *low* (minimal, reversible impact) to *extreme* (substantial, long-lasting impact). Include specific criteria for each level to enable consistent evaluation.

1.  Evaluate harm severity considering multiple factors. As an example, in medical AI systems, incorrect diagnoses might have *major* severity due to potential health impacts and difficulty in reversing treatment decisions. Consider immediate effects, long-term consequences and reversibility.

1.  Document severity assessments with supporting evidence. For example, consider financial AI where incorrect investment advice might have a moderate or major severity estimate for impacted users, depending on the context. Include analysis of varying stakeholder impacts.

## Resources
<a name="resources-20"></a>

 **Related documents:**
+  [Learn how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)
+  [NIST Risk Management Framework](https://csrc.nist.gov/projects/risk-management/about-rmf)
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.5.2 AI system impact assessment process

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
