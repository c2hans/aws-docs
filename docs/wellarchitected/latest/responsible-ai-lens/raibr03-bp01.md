---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp01.html
---

# RAIBR03-BP01 Identify the likelihood of each potential harm
<a name="raibr03-bp01"></a>

 Establish a risk rating methodology that considers the likelihood of the event occurring. The risk likelihood indicates the probability of a harmful event occurring when the system is deployed for the use case.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-20"></a>

1.  Create a standardized likelihood scale with clear definitions. For example, establish ranges from *almost certain* (95%\+ probability) to *highly unlikely* (less than 5% probability). Include specific frequency ranges for each category to maintain consistent evaluation.

1.  Document likelihood assessments with supporting evidence. For example, consider a content moderation system where historical data shows harmful content detection failures occur in 15% of edge cases, placing this risk in the *unlikely* category. Include rationale for each assessment.

## Resources
<a name="resources-19"></a>

 **Related documents:**
+  [Learn how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)
+  [NIST Risk Management Framework](https://csrc.nist.gov/projects/risk-management/about-rmf)
+  [Responsible AI in the generative era](https://www.amazon.science/blog/responsible-ai-in-the-generative-era)
+  [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.5.2 AI system impact assessment process

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
